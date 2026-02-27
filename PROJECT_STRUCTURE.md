# 📦 Legally - Project Structure

Complete file organization for the BNS Legal AI application.

---

## 📁 Directory Structure

```
LegallyFlutter/
│
├─ backend/                           # FastAPI Backend
│  ├─ main.py                         # Main FastAPI application
│  ├─ requirements.txt                # Python dependencies
│  ├─ .env.example                    # Environment variables template
│  ├─ .env                            # Actual env vars (DO NOT COMMIT)
│  ├─ .gitignore                      # Git ignore rules
│  ├─ vercel.json                     # Vercel deployment config
│  └─ README.md                       # Backend documentation
│
├─ bns_sections.json                  # BNS Database (384 sections)
│
├─ docs/                              # Documentation (you are here)
│  ├─ FLUTTERFLOW_BUILD_GUIDE.md      # Complete FlutterFlow guide
│  ├─ QUICK_START.md                  # 30-minute quick start
│  ├─ PROJECT_STRUCTURE.md            # This file
│  ├─ DEPLOYMENT.md                   # Deployment instructions
│  └─ API_REFERENCE.md                # API documentation
│
├─ flutterflow/                       # FlutterFlow project (after download)
│  └─ (standard Flutter structure)
│
├─ assets/                            # App assets
│  ├─ images/
│  │  ├─ logo.png                     # App logo
│  │  ├─ scales-of-justice.png        # Loading animation
│  │  └─ onboarding/                  # Onboarding images
│  ├─ icons/
│  │  └─ app_icon.png                 # App icon (1024x1024)
│  └─ fonts/
│     ├─ Playfair_Display/            # Heading font
│     └─ Inter/                       # Body font
│
├─ firebase/                          # Firebase configuration
│  ├─ google-services.json            # Android config (DO NOT COMMIT)
│  ├─ GoogleService-Info.plist        # iOS config (DO NOT COMMIT)
│  └─ security-rules.json             # Database security rules
│
├─ tests/                             # Test files
│  ├─ backend_tests.py                # Backend API tests
│  └─ api_tests.http                  # HTTP API test requests
│
├─ .gitignore                         # Root gitignore
├─ README.md                          # Project README
└─ LICENSE                            # MIT License

```

---

## 📄 File Descriptions

### Backend Files

#### `backend/main.py`
- **Purpose**: Main FastAPI application
- **Contains**:
  - API routes (`/api/ask`, `/api/sections`, etc.)
  - RAG-lite search logic
  - Groq AI integration
  - BNS database loader
- **Lines of Code**: ~450
- **Key Functions**:
  - `load_bns_database()` - Loads JSON on startup
  - `search_bns_sections()` - RAG-lite search
  - `ask_groq()` - Calls Groq AI
  - `ask_legal_ai()` - Main endpoint

#### `backend/requirements.txt`
- **Purpose**: Python dependencies
- **Contents**:
  ```
  fastapi==0.115.0
  uvicorn[standard]==0.32.0
  httpx==0.27.0
  python-dotenv==1.0.1
  pydantic==2.9.0
  ```

#### `backend/.env.example`
- **Purpose**: Template for environment variables
- **Should contain**:
  ```
  GROQ_API_KEY=your_key_here
  ENVIRONMENT=production
  ```

#### `backend/.env`
- **Purpose**: Actual environment variables
- **⚠️ NEVER COMMIT THIS FILE**
- **Contains**: Real Groq API key

#### `backend/vercel.json`
- **Purpose**: Vercel deployment configuration
- **Specifies**:
  - Build settings
  - Routes
  - Environment variables

#### `backend/README.md`
- **Purpose**: Backend documentation
- **Contains**:
  - Setup instructions
  - API reference
  - Deployment guide
  - Troubleshooting

---

### Data Files

#### `bns_sections.json`
- **Purpose**: Complete BNS database
- **Size**: ~500 KB
- **Structure**:
  ```json
  {
    "metadata": {
      "title": "Bharatiya Nyaya Sanhita, 2023",
      "total_sections": 384
    },
    "sections": {
      "1": { ... },
      "2": { ... },
      ...
      "384": { ... }
    }
  }
  ```
- **Each Section Contains**:
  - section (string)
  - title (string)
  - description (string)
  - punishment (string)
  - category (string)
  - act (string)

---

### Documentation Files

#### `FLUTTERFLOW_BUILD_GUIDE.md`
- **Purpose**: Complete FlutterFlow build instructions
- **Size**: ~15,000 words
- **Contains**:
  - Page-by-page widget trees
  - API configuration
  - Firebase setup
  - Design specifications
  - Complete action flows

#### `QUICK_START.md`
- **Purpose**: Get started in 30 minutes
- **Contains**:
  - 5-step setup
  - MVP build instructions
  - Quick troubleshooting

#### `PROJECT_STRUCTURE.md`
- **Purpose**: This file - project organization
- **Contains**:
  - Directory structure
  - File descriptions
  - Data flow diagrams

#### `DEPLOYMENT.md`
- **Purpose**: Production deployment guide
- **Contains**:
  - Backend deployment (Vercel)
  - App deployment (stores)
  - Environment configuration

#### `API_REFERENCE.md`
- **Purpose**: API documentation
- **Contains**:
  - All endpoints
  - Request/response formats
  - Examples
  - Error codes

---

### Firebase Files

#### `firebase/security-rules.json`
- **Purpose**: Realtime Database security rules
- **Ensures**:
  - Users can only access their own data
  - Authentication required
  - Proper data validation

#### `firebase/google-services.json` (Android)
- **Purpose**: Firebase Android configuration
- **⚠️ NEVER COMMIT THIS FILE**
- **Downloaded from**: Firebase Console

#### `firebase/GoogleService-Info.plist` (iOS)
- **Purpose**: Firebase iOS configuration
- **⚠️ NEVER COMMIT THIS FILE**
- **Downloaded from**: Firebase Console

---

### Asset Files

#### `assets/images/logo.png`
- **Dimensions**: 512x512
- **Format**: PNG with transparency
- **Usage**: App logo, splash screen

#### `assets/icons/app_icon.png`
- **Dimensions**: 1024x1024
- **Format**: PNG
- **Usage**: iOS/Android app icon

#### `assets/fonts/`
- **Fonts**:
  - Playfair Display (headings)
  - Inter (body text)
- **Formats**: TTF/OTF

---

## 🔄 Data Flow

### User Asks Legal Question

```
┌─────────────┐
│  User types │
│  question   │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ FlutterFlow │
│ AskAIPage   │
└──────┬──────┘
       │ POST /api/ask
       │ { "message": "..." }
       ▼
┌─────────────┐
│  FastAPI    │
│  Backend    │
└──────┬──────┘
       │
       ├──────────────────────┐
       │                      │
       ▼                      ▼
┌─────────────┐      ┌─────────────┐
│ Search BNS  │      │  Groq AI    │
│ Database    │      │  (LLaMA)    │
│ (RAG-lite)  │      │             │
└──────┬──────┘      └──────┬──────┘
       │                    │
       │  BNS Sections      │
       └──────────┬─────────┘
                  │
                  ▼
           ┌─────────────┐
           │ AI Response │
           │ (BNS-based) │
           └──────┬──────┘
                  │
                  │ JSON response
                  │ { "reply": "..." }
                  ▼
           ┌─────────────┐
           │ FlutterFlow │
           │ Display     │
           └──────┬──────┘
                  │
                  │ Save to Firebase
                  ▼
           ┌─────────────┐
           │  Firebase   │
           │  /chats/uid │
           └─────────────┘
```

---

## 🗄️ Database Schemas

### Firebase Realtime Database

#### Chat Schema
```json
{
  "chats": {
    "{uid}": {
      "{chatId}": {
        "messages": [
          {
            "role": "user",
            "content": "string",
            "timestamp": 1234567890
          },
          {
            "role": "assistant",
            "content": "string",
            "timestamp": 1234567891
          }
        ],
        "title": "string (first 50 chars of first message)",
        "createdAt": 1234567890,
        "updatedAt": 1234567891
      }
    }
  }
}
```

#### User Schema
```json
{
  "users": {
    "{uid}": {
      "email": "string",
      "displayName": "string",
      "photoURL": "string (optional)",
      "createdAt": 1234567890,
      "lastLoginAt": 1234567890,
      "bookmarks": {
        "{sectionId}": {
          "section": "string",
          "title": "string",
          "savedAt": 1234567890
        }
      },
      "stats": {
        "totalQueries": 0,
        "sectionsViewed": 0,
        "daysActive": 0
      }
    }
  }
}
```

---

## 📊 FlutterFlow App State

### Global App State Variables

```dart
// Authentication
String? currentUserId
String? userName
String? userEmail

// Current Chat
List<JSON> currentChatMessages = []
String? currentChatId
String messageText = ""
bool isAIResponding = false

// Browse Sections
List<JSON> allSections = []
List<JSON> filteredSections = []
String searchQuery = ""
String? selectedCategory = ""
List<String> categories = []
bool isLoadingSections = false

// History
List<JSON> chatHistory = []
bool isLoadingHistory = false

// User Stats
int totalQueries = 0
int sectionsViewed = 0
```

---

## 🎨 Asset Requirements

### Images

| Asset | Size | Format | Usage |
|-------|------|--------|-------|
| App Logo | 512x512 | PNG | Splash, Auth page |
| App Icon | 1024x1024 | PNG | iOS/Android icon |
| Scales of Justice | 256x256 | PNG | Loading animation |
| Onboarding 1 | 800x600 | PNG | Onboarding screen |
| Onboarding 2 | 800x600 | PNG | Onboarding screen |
| Onboarding 3 | 800x600 | PNG | Onboarding screen |

### Colors

| Name | Hex | Usage |
|------|-----|-------|
| Gold | #D4AF37 | Primary color, accents |
| Pure Black | #0D0D0D | Background |
| Dark Gray | #1E1E1E | Cards, surfaces |
| Dark Charcoal | #2A2A2A | Borders |
| White | #FFFFFF | Primary text |
| Light Gray | #CCCCCC | Secondary text |
| Error Red | #FF6B6B | Errors, warnings |

### Fonts

| Font | Weights | Usage |
|------|---------|-------|
| Playfair Display | Bold, SemiBold | Headings |
| Inter | Regular, Medium, Bold | Body text |

---

## 🔐 Environment Variables

### Backend (.env)

```bash
# Required
GROQ_API_KEY=gsk_1234567890abcdef

# Optional
ENVIRONMENT=production
DEBUG=false
LOG_LEVEL=info
```

### Vercel Environment Variables

Set in Vercel Dashboard:
- `GROQ_API_KEY` (Secret)

### FlutterFlow Environment

No environment variables needed - all keys are in Firebase config files.

---

## 📦 Dependencies

### Backend (Python)

```
fastapi==0.115.0        # Web framework
uvicorn==0.32.0         # ASGI server
httpx==0.27.0           # HTTP client for Groq
python-dotenv==1.0.1    # Environment variables
pydantic==2.9.0         # Data validation
```

### FlutterFlow (Auto-managed)

- `firebase_core` - Firebase initialization
- `firebase_auth` - Authentication
- `firebase_database` - Realtime Database
- `http` - API calls
- `provider` - State management
- `google_fonts` - Custom fonts

---

## 🧪 Testing Files

### `tests/backend_tests.py`

```python
# Test BNS database loading
# Test RAG-lite search
# Test Groq AI integration
# Test all API endpoints
```

### `tests/api_tests.http`

```http
### Test Health Check
GET https://your-backend.vercel.app/

### Test Ask AI
POST https://your-backend.vercel.app/api/ask
Content-Type: application/json

{
  "message": "What is murder under BNS?"
}

### Test Get Sections
GET https://your-backend.vercel.app/api/sections?search=murder

### Test Get Section by ID
GET https://your-backend.vercel.app/api/sections/103

### Test Get Categories
GET https://your-backend.vercel.app/api/categories
```

---

## 📝 Git Ignore Rules

### Root `.gitignore`

```gitignore
# Environment
.env
.env.local

# Firebase
firebase/google-services.json
firebase/GoogleService-Info.plist

# Python
__pycache__/
*.pyc
venv/
env/

# IDE
.vscode/
.idea/
*.swp

# OS
.DS_Store
Thumbs.db

# FlutterFlow
flutterflow/build/
flutterflow/.dart_tool/

# Secrets
*.key
*.pem
secrets/
```

---

## 🚀 Build Outputs

### Backend Deployment

**Vercel Output**:
- URL: `https://legally-xyz.vercel.app`
- Build logs in Vercel Dashboard
- Automatic HTTPS

### FlutterFlow Build

**iOS**:
- `.ipa` file for App Store
- Build via Xcode or FlutterFlow

**Android**:
- `.apk` file for testing
- `.aab` file for Play Store
- Build via FlutterFlow

---

## 📊 Performance Metrics

### Backend

- **Cold Start**: 2-3s (Vercel serverless)
- **Warm Request**: 1-2s
- **AI Response**: 2-4s (Groq API)
- **Total**: 3-6s per query

### Frontend

- **App Launch**: 1-2s
- **Page Navigation**: <100ms
- **Firebase Query**: 200-500ms
- **API Call**: 3-6s (backend + AI)

### Database

- **BNS JSON Size**: ~500 KB
- **Load Time**: <1s
- **Search Time**: <100ms (in-memory)

---

## 📈 Scalability

### Backend

- **Current**: Serverless (auto-scales)
- **Max Requests**: Unlimited (Vercel)
- **Rate Limiting**: Implement if needed

### Firebase

- **Free Tier**: 
  - 100K simultaneous connections
  - 10 GB storage
  - 1 GB download/day
- **Upgrade**: Blaze plan (pay-as-you-go)

### Groq

- **Free Tier**: Limited requests/month
- **Rate Limit**: Check Groq docs
- **Upgrade**: Pay for more usage

---

## 🔄 Version Control

### Git Branches

- `main` - Production code
- `develop` - Development branch
- `feature/*` - Feature branches
- `hotfix/*` - Bug fixes

### Release Process

1. Develop feature in `feature/*` branch
2. Merge to `develop` for testing
3. Merge to `main` for production
4. Tag releases: `v1.0.0`, `v1.1.0`, etc.

---

## 📞 Support Files

### `README.md` (Root)

Main project documentation:
- Project overview
- Quick start link
- Features list
- Tech stack
- Contributing guidelines
- License

### `LICENSE`

MIT License (or your choice)

---

## ✅ File Checklist

### Before Committing

- [ ] Remove all `.env` files
- [ ] Remove Firebase config files
- [ ] Remove API keys
- [ ] Update `.gitignore`
- [ ] Update documentation
- [ ] Test all endpoints
- [ ] Check for console errors

### Before Deploying

- [ ] Backend deployed to Vercel
- [ ] Environment variables set
- [ ] Firebase configured
- [ ] API endpoints tested
- [ ] FlutterFlow fully built
- [ ] Icons and splash added
- [ ] Test on real device

---

## 📚 Documentation Coverage

| Topic | File | Status |
|-------|------|--------|
| Quick Start | QUICK_START.md | ✅ Complete |
| Full Build Guide | FLUTTERFLOW_BUILD_GUIDE.md | ✅ Complete |
| Project Structure | PROJECT_STRUCTURE.md | ✅ This file |
| Backend API | backend/README.md | ✅ Complete |
| API Reference | API_REFERENCE.md | ⏳ Create next |
| Deployment | DEPLOYMENT.md | ⏳ Create next |
| Troubleshooting | In each guide | ✅ Complete |

---

## 🎯 Next Steps

1. Create `DEPLOYMENT.md` for production deployment
2. Create `API_REFERENCE.md` for API docs
3. Add test files in `tests/`
4. Gather assets in `assets/`
5. Build FlutterFlow project following guide
6. Deploy and test

---

**END OF PROJECT STRUCTURE**

Last Updated: 2026-02-27
