# 📡 Legally - API Reference

Complete API documentation for the Legally backend server.

---

## 📋 Overview

**Base URL**: `https://your-backend.vercel.app`

**API Version**: 1.0.0

**Legal Framework**: Bharatiya Nyaya Sanhita, 2023 (BNS)

**Authentication**: None required (public API)

**Rate Limiting**: Handled by Vercel (serverless)

**Response Format**: JSON

---

## 🌐 Endpoints

### 1. Health Check

**GET** `/`

Check if API is online and get metadata.

#### Request

```http
GET / HTTP/1.1
Host: your-backend.vercel.app
```

#### Response

**Status**: `200 OK`

```json
{
  "status": "online",
  "api": "Legally - BNS Legal AI",
  "version": "1.0.0",
  "legal_framework": "Bharatiya Nyaya Sanhita, 2023",
  "total_sections": 384
}
```

#### Example

```bash
curl https://your-backend.vercel.app/
```

---

### 2. Ask Legal AI (Main Endpoint)

**POST** `/api/ask`

Send a legal question and receive AI-generated answer based on BNS.

#### Request

**Headers**:
```http
Content-Type: application/json
```

**Body**:
```json
{
  "message": "string (required, 3-500 characters)"
}
```

#### Response

**Status**: `200 OK`

```json
{
  "reply": "string (AI-generated response)"
}
```

**Error Status**: `400 Bad Request`, `500 Internal Server Error`, `504 Gateway Timeout`

```json
{
  "detail": "string (error message)"
}
```

#### Examples

**Request**:
```bash
curl -X POST https://your-backend.vercel.app/api/ask \
  -H "Content-Type: application/json" \
  -d '{"message": "What is the punishment for murder under BNS?"}'
```

**Response**:
```json
{
  "reply": "Under Section 103 of the Bharatiya Nyaya Sanhita, 2023, the punishment for murder is one of the following:\n\n1. **Death penalty** - in the rarest of rare cases\n2. **Life imprisonment** - in most cases\n3. **Fine** - may be imposed in addition to imprisonment\n\n**Section 103: Punishment for murder.**\n\nMurder is defined under Section 100 as culpable homicide with specific intentions...\n\n⚖️ LEGAL DISCLAIMER: This is AI-generated educational information based on BNS, 2023. It is NOT legal advice. Consult a qualified advocate for specific legal advice on your situation."
}
```

#### FlutterFlow Configuration

**API Call Name**: `askLegalAI`

**Method**: POST

**URL**: `https://your-backend.vercel.app/api/ask`

**Headers**:
```json
{
  "Content-Type": "application/json"
}
```

**Body**:
```json
{
  "message": "[messageVariable]"
}
```

**JSON Path for Response**:
- Field: `reply`
- Path: `$.reply`

---

### 3. Get All BNS Sections

**GET** `/api/sections`

Retrieve BNS sections with optional filtering and pagination.

#### Request

**Query Parameters** (all optional):

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `search` | string | - | Keyword search in title/description |
| `category` | string | - | Filter by category |
| `limit` | integer | 50 | Max results to return (1-384) |
| `offset` | integer | 0 | Number of results to skip |

#### Response

**Status**: `200 OK`

```json
{
  "sections": [
    {
      "section": "string",
      "title": "string",
      "description": "string",
      "punishment": "string | null",
      "category": "string",
      "act": "Bharatiya Nyaya Sanhita, 2023 (BNS)"
    }
  ],
  "total": integer
}
```

#### Examples

**Get first 10 sections**:
```bash
curl "https://your-backend.vercel.app/api/sections?limit=10&offset=0"
```

**Search for "murder"**:
```bash
curl "https://your-backend.vercel.app/api/sections?search=murder"
```

**Filter by category**:
```bash
curl "https://your-backend.vercel.app/api/sections?category=Murder%20%26%20Homicide"
```

**Combined example**:
```bash
curl "https://your-backend.vercel.app/api/sections?search=theft&limit=20"
```

**Response**:
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
    },
    {
      "section": "104",
      "title": "Punishment for murder by life-convict",
      "description": "Punishment for murder by life-convict.",
      "punishment": "Punishment for murder by life-convict",
      "category": "Murder & Homicide",
      "act": "Bharatiya Nyaya Sanhita, 2023 (BNS)"
    }
  ],
  "total": 2
}
```

#### FlutterFlow Configuration

**API Call Name**: `getAllSections`

**Method**: GET

**URL**: `https://your-backend.vercel.app/api/sections`

**Query Parameters**:
- `search`: [searchQueryVariable] (optional)
- `category`: [selectedCategoryVariable] (optional)
- `limit`: 50
- `offset`: 0

**JSON Path for Response**:
- Field: `sections`
- Path: `$.sections[*]`
- Type: List<JSON>

---

### 4. Get Section by ID

**GET** `/api/sections/{section_id}`

Retrieve a specific BNS section by its ID (1-384).

#### Request

**Path Parameters**:

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `section_id` | string | Yes | Section number (e.g., "103") |

#### Response

**Status**: `200 OK`

```json
{
  "section": "string",
  "title": "string",
  "description": "string",
  "punishment": "string | null",
  "category": "string",
  "act": "Bharatiya Nyaya Sanhita, 2023 (BNS)"
}
```

**Error Status**: `404 Not Found`

```json
{
  "detail": "Section {section_id} not found"
}
```

#### Examples

**Get Section 103 (Murder)**:
```bash
curl https://your-backend.vercel.app/api/sections/103
```

**Response**:
```json
{
  "section": "103",
  "title": "Punishment for murder",
  "description": "Punishment for murder.",
  "punishment": "Punishment for murder",
  "category": "Murder & Homicide",
  "act": "Bharatiya Nyaya Sanhita, 2023 (BNS)"
}
```

**Get Section 1**:
```bash
curl https://your-backend.vercel.app/api/sections/1
```

#### FlutterFlow Configuration

**API Call Name**: `getSectionById`

**Method**: GET

**URL**: `https://your-backend.vercel.app/api/sections/[sectionId]`

**Path Variables**:
- `sectionId`: [sectionIdVariable]

**JSON Path for Response**: (none needed, entire response is the section object)

---

### 5. Get Categories

**GET** `/api/categories`

Retrieve all unique categories in BNS.

#### Request

```http
GET /api/categories HTTP/1.1
Host: your-backend.vercel.app
```

#### Response

**Status**: `200 OK`

```json
{
  "categories": [
    "string",
    "string",
    ...
  ],
  "total": integer
}
```

#### Example

```bash
curl https://your-backend.vercel.app/api/categories
```

**Response**:
```json
{
  "categories": [
    "Assault & Violence",
    "Corruption",
    "Cyber Crimes",
    "General Provisions",
    "Miscellaneous",
    "Murder & Homicide",
    "Property Crimes",
    "Sexual Offenses",
    "Theft & Robbery"
  ],
  "total": 9
}
```

#### FlutterFlow Configuration

**API Call Name**: `getCategories`

**Method**: GET

**URL**: `https://your-backend.vercel.app/api/categories`

**JSON Path for Response**:
- Field: `categories`
- Path: `$.categories[*]`
- Type: List<String>

---

### 6. Get Metadata

**GET** `/api/metadata`

Get metadata about BNS Act.

#### Request

```http
GET /api/metadata HTTP/1.1
Host: your-backend.vercel.app
```

#### Response

**Status**: `200 OK`

```json
{
  "title": "string",
  "short_name": "string",
  "replaces": "string",
  "effective_date": "string",
  "total_sections": integer,
  "description": "string"
}
```

#### Example

```bash
curl https://your-backend.vercel.app/api/metadata
```

**Response**:
```json
{
  "title": "Bharatiya Nyaya Sanhita, 2023",
  "short_name": "BNS",
  "replaces": "Indian Penal Code, 1860 (IPC)",
  "effective_date": "July 1, 2024",
  "total_sections": 384,
  "description": "The Bharatiya Nyaya Sanhita (BNS) is the new criminal code of India that replaces the Indian Penal Code (IPC)"
}
```

---

## 🔒 Security

### API Key

**Not required** - The backend API is public.

**Groq API Key** - Stored securely in Vercel environment variables, never exposed to clients.

### CORS

**Allowed Origins**: All (`*`)

For production, configure specific origins in `main.py`:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://yourdomain.com"],  # Specific domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### Rate Limiting

Currently handled by Vercel's serverless limits.

To add rate limiting, use `slowapi`:

```python
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter

@app.post("/api/ask")
@limiter.limit("10/minute")
async def ask_legal_ai(request: AskRequest):
    ...
```

---

## ⚠️ Error Handling

### Error Response Format

All errors return JSON:

```json
{
  "detail": "string (error message)"
}
```

### HTTP Status Codes

| Code | Meaning | Description |
|------|---------|-------------|
| 200 | OK | Request successful |
| 400 | Bad Request | Invalid input (e.g., empty message) |
| 404 | Not Found | Resource not found (e.g., section ID) |
| 500 | Internal Server Error | Server error (e.g., Groq API failure) |
| 504 | Gateway Timeout | AI service timeout (>30 seconds) |

### Common Errors

**Empty Message**:
```json
{
  "detail": "Please provide a valid question"
}
```

**Section Not Found**:
```json
{
  "detail": "Section 999 not found"
}
```

**Groq API Key Missing**:
```json
{
  "detail": "Groq API key not configured"
}
```

**AI Service Timeout**:
```json
{
  "detail": "AI service timeout"
}
```

---

## 📊 Response Times

### Expected Latency

| Endpoint | Cold Start | Warm |
|----------|------------|------|
| `/` | 2-3s | <100ms |
| `/api/ask` | 3-5s | 2-4s |
| `/api/sections` | 2-3s | 100-500ms |
| `/api/sections/{id}` | 2-3s | <100ms |
| `/api/categories` | 2-3s | <100ms |
| `/api/metadata` | 2-3s | <100ms |

**Note**: `/api/ask` includes AI generation time (~2-4s) which cannot be reduced.

---

## 🧪 Testing

### Test with cURL

**Health Check**:
```bash
curl https://your-backend.vercel.app/
```

**Ask AI**:
```bash
curl -X POST https://your-backend.vercel.app/api/ask \
  -H "Content-Type: application/json" \
  -d '{"message": "What is Section 103 BNS?"}'
```

**Get Sections**:
```bash
curl "https://your-backend.vercel.app/api/sections?limit=5"
```

**Get Section by ID**:
```bash
curl https://your-backend.vercel.app/api/sections/103
```

**Get Categories**:
```bash
curl https://your-backend.vercel.app/api/categories
```

### Test with Python

```python
import requests

BASE_URL = "https://your-backend.vercel.app"

# Ask AI
response = requests.post(
    f"{BASE_URL}/api/ask",
    json={"message": "What is murder under BNS?"}
)
print(response.json()["reply"])

# Get sections
response = requests.get(f"{BASE_URL}/api/sections?search=theft")
sections = response.json()["sections"]
for section in sections:
    print(f"Section {section['section']}: {section['title']}")

# Get specific section
response = requests.get(f"{BASE_URL}/api/sections/103")
section = response.json()
print(section)
```

### Test with JavaScript

```javascript
// Ask AI
fetch('https://your-backend.vercel.app/api/ask', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ message: 'What is Section 103 BNS?' })
})
  .then(res => res.json())
  .then(data => console.log(data.reply));

// Get sections
fetch('https://your-backend.vercel.app/api/sections?limit=10')
  .then(res => res.json())
  .then(data => console.log(data.sections));

// Get section by ID
fetch('https://your-backend.vercel.app/api/sections/103')
  .then(res => res.json())
  .then(data => console.log(data));
```

---

## 📝 Best Practices

### For FlutterFlow Integration

1. **Store Base URL as constant**:
   ```dart
   const String API_BASE_URL = "https://your-backend.vercel.app";
   ```

2. **Handle loading states**:
   - Show loading indicator during API call
   - Disable send button while processing

3. **Error handling**:
   - Display user-friendly error messages
   - Implement retry logic for timeouts

4. **Caching**:
   - Cache sections list locally
   - Only refetch when needed
   - Cache categories (rarely change)

5. **Debouncing**:
   - Debounce search queries (500ms)
   - Prevent excessive API calls

### For Mobile App

**Timeouts**:
```dart
// Set appropriate timeout for AI calls
final response = await http.post(
  Uri.parse('$API_BASE_URL/api/ask'),
  headers: {'Content-Type': 'application/json'},
  body: jsonEncode({'message': message}),
).timeout(Duration(seconds: 30));
```

**Retry Logic**:
```dart
Future<String> askAIWithRetry(String message, {int maxRetries = 3}) async {
  for (int i = 0; i < maxRetries; i++) {
    try {
      final response = await askAI(message);
      return response;
    } catch (e) {
      if (i == maxRetries - 1) rethrow;
      await Future.delayed(Duration(seconds: 2 * (i + 1)));
    }
  }
  throw Exception('Failed after $maxRetries retries');
}
```

---

## 🔄 Versioning

**Current Version**: 1.0.0

**Version Format**: `MAJOR.MINOR.PATCH`

- **MAJOR**: Breaking changes
- **MINOR**: New features (backward compatible)
- **PATCH**: Bug fixes

**Future Versions**:
- `v1.1.0`: Add case law integration
- `v1.2.0`: Add multi-language support
- `v2.0.0`: Complete API redesign (if needed)

**Version Header** (future):
```http
API-Version: 1.0.0
```

---

## 📚 Additional Resources

### API Documentation

- **Interactive Docs**: `https://your-backend.vercel.app/docs` (FastAPI auto-generated)
- **OpenAPI Spec**: `https://your-backend.vercel.app/openapi.json`

### Support

- **Email**: support@yourcompany.com
- **GitHub**: Create issue in repository
- **Documentation**: See `backend/README.md`

### Legal Framework

- **BNS Full Text**: Available in `bns_sections.json`
- **Total Sections**: 384
- **Effective Date**: July 1, 2024
- **Replaces**: Indian Penal Code, 1860 (IPC)

---

## ✅ API Summary

| Endpoint | Method | Purpose | Response Time |
|----------|--------|---------|---------------|
| `/` | GET | Health check | <100ms |
| `/api/ask` | POST | Ask legal AI | 2-4s |
| `/api/sections` | GET | Get all sections | 100-500ms |
| `/api/sections/{id}` | GET | Get specific section | <100ms |
| `/api/categories` | GET | Get categories | <100ms |
| `/api/metadata` | GET | Get BNS metadata | <100ms |

**Total Endpoints**: 6

**Authentication**: None required

**Rate Limiting**: Vercel default

**Legal Framework**: BNS 2023 only

---

**END OF API REFERENCE**

Happy coding! 🚀
