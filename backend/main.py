"""
Legally - BNS Legal AI Backend
FastAPI server with RAG-lite for Bharatiya Nyaya Sanhita, 2023
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import json
import os
from typing import List, Dict, Optional
import httpx
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="Legally API",
    description="BNS Legal AI Backend using RAG-lite and Groq",
    version="1.0.0"
)

# CORS Configuration - Allow FlutterFlow and mobile apps
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your FlutterFlow domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load BNS JSON Database
BNS_DATABASE = {}
BNS_METADATA = {}

def load_bns_database():
    """Load BNS sections from JSON file"""
    global BNS_DATABASE, BNS_METADATA
    try:
        json_path = os.path.join(os.path.dirname(__file__), "..", "bns_sections.json")
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            BNS_METADATA = data.get("metadata", {})
            BNS_DATABASE = data.get("sections", {})
        print(f"✅ Loaded {len(BNS_DATABASE)} BNS sections")
    except Exception as e:
        print(f"❌ Error loading BNS database: {e}")
        raise

# Load database on startup
load_bns_database()

# Request/Response Models
class AskRequest(BaseModel):
    message: str

class AskResponse(BaseModel):
    reply: str

class Section(BaseModel):
    section: str
    title: str
    description: str
    punishment: Optional[str]
    category: str
    act: str

class SearchResponse(BaseModel):
    sections: List[Section]
    total: int

# Groq Configuration
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
GROQ_MODEL = "llama-3.3-70b-versatile"

if not GROQ_API_KEY:
    print("⚠️  WARNING: GROQ_API_KEY not set in environment variables")

# RAG-lite: Search BNS sections
def search_bns_sections(query: str, limit: int = 5) -> List[Dict]:
    """
    Simple keyword-based search in BNS sections
    Returns relevant sections based on query
    """
    query_lower = query.lower()
    results = []
    
    for section_id, section_data in BNS_DATABASE.items():
        score = 0
        title = section_data.get("title", "").lower()
        description = section_data.get("description", "").lower()
        category = section_data.get("category", "").lower()
        
        # Scoring based on keyword matches
        if query_lower in title:
            score += 10
        if query_lower in description:
            score += 5
        if query_lower in category:
            score += 3
        
        # Check for individual words
        query_words = query_lower.split()
        for word in query_words:
            if len(word) > 3:  # Skip small words
                if word in title:
                    score += 2
                if word in description:
                    score += 1
        
        if score > 0:
            results.append({
                "section": section_data,
                "score": score
            })
    
    # Sort by score and return top results
    results.sort(key=lambda x: x["score"], reverse=True)
    return [r["section"] for r in results[:limit]]

def format_sections_for_context(sections: List[Dict]) -> str:
    """Format BNS sections for AI context"""
    if not sections:
        return "No relevant BNS sections found."
    
    context = "### RELEVANT BNS SECTIONS:\n\n"
    for section in sections:
        context += f"""
**Section {section['section']}: {section['title']}**
Act: {section['act']}
Category: {section.get('category', 'N/A')}
Description: {section.get('description', 'N/A')}
Punishment: {section.get('punishment', 'N/A')}
---
"""
    return context

async def ask_groq(user_message: str, bns_context: str) -> str:
    """Send query to Groq AI with BNS context"""
    
    if not GROQ_API_KEY:
        raise HTTPException(status_code=500, detail="Groq API key not configured")
    
    system_prompt = f"""You are a specialized legal AI assistant for Indian criminal law, specifically for the Bharatiya Nyaya Sanhita, 2023 (BNS).

STRICT RULES:
1. You MUST ONLY cite and reference the Bharatiya Nyaya Sanhita, 2023 (BNS)
2. DO NOT mention or reference the Indian Penal Code (IPC) unless explicitly comparing
3. Always cite sections in this format: "Section [number], Bharatiya Nyaya Sanhita, 2023"
4. For each legal response, mention:
   - Relevant section numbers
   - Legal ingredients/elements of the offense
   - Punishment prescribed
   - Whether the offense is cognizable/non-cognizable (if applicable)
   - Whether the offense is bailable/non-bailable (if applicable)

5. Always end with this disclaimer:
   "⚖️ LEGAL DISCLAIMER: This is AI-generated educational information based on BNS, 2023. It is NOT legal advice. Consult a qualified advocate for specific legal advice on your situation."

6. Be clear, professional, and educational
7. If asked about a topic not covered in BNS, clearly state that

BNS METADATA:
- Title: {BNS_METADATA.get('title', 'Bharatiya Nyaya Sanhita, 2023')}
- Total Sections: {BNS_METADATA.get('total_sections', 384)}
- Effective Date: {BNS_METADATA.get('effective_date', 'July 1, 2024')}
- Replaces: {BNS_METADATA.get('replaces', 'Indian Penal Code, 1860')}
"""

    user_prompt = f"""{bns_context}

USER QUESTION:
{user_message}

Provide a comprehensive legal analysis based STRICTLY on the Bharatiya Nyaya Sanhita, 2023 sections provided above. If the relevant sections are not provided, state that more specific information is needed."""

    try:
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.post(
                GROQ_API_URL,
                headers={
                    "Authorization": f"Bearer {GROQ_API_KEY}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": GROQ_MODEL,
                    "messages": [
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_prompt}
                    ],
                    "temperature": 0.3,  # Lower temperature for more factual responses
                    "max_tokens": 1500,
                    "top_p": 0.9
                }
            )
            
            if response.status_code != 200:
                raise HTTPException(
                    status_code=response.status_code,
                    detail=f"Groq API error: {response.text}"
                )
            
            result = response.json()
            ai_reply = result["choices"][0]["message"]["content"]
            return ai_reply
            
    except httpx.TimeoutException:
        raise HTTPException(status_code=504, detail="AI service timeout")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"AI service error: {str(e)}")

# API Endpoints

@app.get("/", response_class=HTMLResponse)
async def root():
    """Serve the HTML testing interface"""
    html_path = os.path.join(os.path.dirname(__file__), "index.html")
    try:
        with open(html_path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return HTMLResponse(content="<h1>Legally API</h1><p>API is running but index.html not found</p>", status_code=200)

@app.get("/health")
async def health():
    """API health check"""
    return {
        "status": "online",
        "api": "Legally - BNS Legal AI",
        "version": "1.0.0",
        "legal_framework": "Bharatiya Nyaya Sanhita, 2023",
        "total_sections": len(BNS_DATABASE)
    }

@app.post("/api/ask", response_model=AskResponse)
async def ask_legal_ai(request: AskRequest):
    """
    Main endpoint for legal AI queries
    Uses RAG-lite to find relevant BNS sections and generates response
    """
    try:
        if not request.message or len(request.message.strip()) < 3:
            raise HTTPException(status_code=400, detail="Please provide a valid question")
        
        # Step 1: Search relevant BNS sections (RAG-lite)
        relevant_sections = search_bns_sections(request.message, limit=5)
        
        # Step 2: Format sections as context
        bns_context = format_sections_for_context(relevant_sections)
        
        # Step 3: Ask Groq AI with BNS context
        ai_reply = await ask_groq(request.message, bns_context)
        
        return AskResponse(reply=ai_reply)
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

@app.get("/api/sections", response_model=SearchResponse)
async def get_all_sections(
    search: Optional[str] = None,
    category: Optional[str] = None,
    limit: int = 50,
    offset: int = 0
):
    """
    Get BNS sections with optional filtering
    """
    try:
        sections_list = list(BNS_DATABASE.values())
        
        # Filter by search query
        if search:
            search_lower = search.lower()
            sections_list = [
                s for s in sections_list
                if search_lower in s.get("title", "").lower()
                or search_lower in s.get("description", "").lower()
                or search_lower in s.get("section", "")
            ]
        
        # Filter by category
        if category:
            sections_list = [
                s for s in sections_list
                if s.get("category", "").lower() == category.lower()
            ]
        
        total = len(sections_list)
        
        # Pagination
        sections_list = sections_list[offset:offset + limit]
        
        return SearchResponse(
            sections=[Section(**s) for s in sections_list],
            total=total
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching sections: {str(e)}")

@app.get("/api/sections/{section_id}", response_model=Section)
async def get_section_by_id(section_id: str):
    """Get specific BNS section by ID"""
    section = BNS_DATABASE.get(section_id)
    
    if not section:
        raise HTTPException(status_code=404, detail=f"Section {section_id} not found")
    
    return Section(**section)

@app.get("/api/categories")
async def get_categories():
    """Get all unique categories in BNS"""
    categories = set()
    for section in BNS_DATABASE.values():
        cat = section.get("category")
        if cat:
            categories.add(cat)
    
    return {
        "categories": sorted(list(categories)),
        "total": len(categories)
    }

@app.get("/api/metadata")
async def get_metadata():
    """Get BNS metadata"""
    return BNS_METADATA

# For local development
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
