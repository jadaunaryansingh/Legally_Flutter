# Legally Backend - FastAPI + RAG-lite

Production-ready legal AI backend for Bharatiya Nyaya Sanhita, 2023 (BNS)

## 🏗️ Architecture

- **Framework**: FastAPI (Python)
- **AI**: Groq (llama-3.3-70b-versatile)
- **Retrieval**: RAG-lite (keyword-based search in bns_sections.json)
- **Deployment**: Vercel

## 🚀 Setup

### 1. Install Dependencies

```bash
cd backend
pip install -r requirements.txt
```

### 2. Configure Environment Variables

```bash
cp .env.example .env
```

Edit `.env` and add your Groq API key:
```
GROQ_API_KEY=your_actual_groq_api_key
```

Get your Groq API key from: https://console.groq.com/keys

### 3. Run Locally

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

API will be available at: `http://localhost:8000`

## 📡 API Endpoints

### Main Endpoints

#### 1. Ask Legal AI (Primary Endpoint for FlutterFlow)

```http
POST /api/ask
Content-Type: application/json

{
  "message": "What is the punishment for murder under BNS?"
}
```

**Response:**
```json
{
  "reply": "Under Section 103 of the Bharatiya Nyaya Sanhita, 2023..."
}
```

**FlutterFlow JSON Path:** `$.reply`

#### 2. Get All BNS Sections

```http
GET /api/sections?search=murder&limit=50&offset=0
```

**Response:**
```json
{
  "sections": [
    {
      "section": "103",
      "title": "Punishment for murder",
      "description": "Punishment for murder.",
      "punishment": "Punishment for murder",
      "category": "Murder & Homicide",
      "act": "Bharatiya Nyaya Sanhita, 2023 (BNS)"
    }
  ],
  "total": 1
}
```

#### 3. Get Specific Section

```http
GET /api/sections/103
```

#### 4. Get Categories

```http
GET /api/categories
```

#### 5. Get Metadata

```http
GET /api/metadata
```

## 🔒 Security

- ✅ CORS enabled for mobile apps
- ✅ API key stored in environment variables
- ✅ No sensitive data in codebase
- ✅ HTTPS enforced in production

## 🌐 Deploy to Vercel

### Prerequisites
- Vercel account
- Vercel CLI installed: `npm i -g vercel`

### Deployment Steps

1. **Login to Vercel**
   ```bash
   vercel login
   ```

2. **Deploy**
   ```bash
   cd backend
   vercel
   ```

3. **Add Environment Variable**
   ```bash
   vercel env add GROQ_API_KEY
   ```
   Enter your Groq API key when prompted.

4. **Deploy to Production**
   ```bash
   vercel --prod
   ```

5. **Your API URL**
   ```
   https://your-project.vercel.app
   ```

### Testing Deployment

```bash
curl https://your-project.vercel.app/
```

## 📱 FlutterFlow Integration

### API Configuration in FlutterFlow

1. **Add API Call**
   - Name: `askLegalAI`
   - Method: `POST`
   - URL: `https://your-backend.vercel.app/api/ask`

2. **Request Body** (JSON)
   ```json
   {
     "message": "[message]"
   }
   ```
   
3. **Variable: message**
   - Type: String
   - Source: Widget State Variable

4. **Response JSON Path**
   - Field: `reply`
   - Path: `$.reply`

## 🧪 Testing

### Test with cURL

```bash
# Test health
curl https://your-backend.vercel.app/

# Test ask endpoint
curl -X POST https://your-backend.vercel.app/api/ask \
  -H "Content-Type: application/json" \
  -d '{"message": "What is Section 103 BNS?"}'

# Test sections endpoint
curl "https://your-backend.vercel.app/api/sections?search=murder"

# Test specific section
curl https://your-backend.vercel.app/api/sections/103
```

### Test with Python

```python
import requests

# Ask AI
response = requests.post(
    "https://your-backend.vercel.app/api/ask",
    json={"message": "What is murder under BNS?"}
)
print(response.json()["reply"])
```

## 📊 Performance

- **Cold Start**: ~2-3 seconds (Vercel serverless)
- **Warm Response**: ~1-2 seconds
- **AI Generation**: ~2-4 seconds (depends on Groq)

## 🐛 Troubleshooting

### Error: "Groq API key not configured"
- Make sure `GROQ_API_KEY` is set in `.env` (local) or Vercel environment variables (production)

### Error: "No relevant BNS sections found"
- The search is keyword-based. Try different keywords related to your question.

### Error: "AI service timeout"
- Groq API might be slow. Try again or increase timeout in `main.py`

## 📝 Legal Framework

**IMPORTANT**: This API strictly uses:
- ✅ Bharatiya Nyaya Sanhita, 2023 (BNS)
- ❌ NOT Indian Penal Code (IPC)

The AI is instructed to cite only BNS sections.

## 🔄 Updates

To update BNS data:
1. Update `bns_sections.json` in root directory
2. Restart server (local) or redeploy (Vercel)

## 📄 License

MIT License - Use responsibly for educational purposes.
