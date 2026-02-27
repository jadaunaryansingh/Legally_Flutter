# 🚀 Legally - Quick Start Guide

Get your BNS Legal AI app running in 30 minutes!

---

## 📋 Prerequisites

- [ ] FlutterFlow account (https://flutterflow.io)
- [ ] Firebase account (https://firebase.google.com)
- [ ] Vercel account (https://vercel.com)
- [ ] Groq API key (https://console.groq.com)
- [ ] Python 3.9+ (for local backend testing)

---

## ⚡ 5-Step Setup

### STEP 1: Deploy Backend (10 minutes)

```bash
# 1. Navigate to backend folder
cd backend

# 2. Install dependencies (for local testing)
pip install -r requirements.txt

# 3. Create .env file
cp .env.example .env
# Edit .env and add your Groq API key

# 4. Test locally (optional)
uvicorn main:app --reload
# Visit http://localhost:8000 to verify

# 5. Deploy to Vercel
npm i -g vercel  # Install Vercel CLI
vercel login
vercel            # Follow prompts
vercel env add GROQ_API_KEY  # Add your Groq key
vercel --prod      # Deploy to production
```

**✅ Result**: You'll get a URL like `https://legally-abc123.vercel.app`

**📝 Save this URL** - you'll need it for FlutterFlow!

---

### STEP 2: Setup Firebase (5 minutes)

1. Go to [Firebase Console](https://console.firebase.google.com)
2. Click **Add Project** → Name it `Legally`
3. Enable **Realtime Database**:
   - Go to **Build** → **Realtime Database** → **Create Database**
   - Start in **Test Mode** (we'll secure it later)
4. Enable **Authentication**:
   - Go to **Build** → **Authentication** → **Get Started**
   - Enable **Email/Password**
   - Enable **Google Sign-In**

**✅ Result**: Firebase project ready!

---

### STEP 3: Create FlutterFlow Project (2 minutes)

1. Go to [FlutterFlow](https://flutterflow.io)
2. Click **Create New Project**
3. Choose **Blank Project**
4. Project Name: `Legally`
5. Platform: **iOS + Android**

**✅ Result**: Blank FlutterFlow project created!

---

### STEP 4: Connect Firebase to FlutterFlow (3 minutes)

1. In FlutterFlow, go to **Settings & Integrations** (gear icon)
2. Click **Firebase** tab
3. Click **Connect to Firebase**
4. Follow the guided setup:
   - Select your Firebase project
   - Download config files
   - Enable Authentication
   - Enable Realtime Database

**✅ Result**: FlutterFlow connected to Firebase!

---

### STEP 5: Add Backend API to FlutterFlow (5 minutes)

1. In FlutterFlow, click **API Calls** tab (left sidebar)
2. Click **+ Add API Call**
3. Configure **askLegalAI**:
   - **Name**: `askLegalAI`
   - **Method**: `POST`
   - **URL**: `https://YOUR-VERCEL-URL.vercel.app/api/ask`
   - **Headers**:
     ```json
     {
       "Content-Type": "application/json"
     }
     ```
   - **Body** (JSON):
     ```json
     {
       "message": "[message]"
     }
     ```
   - **Add Variable**: 
     - Name: `message`
     - Type: String
     - Required: ✅
   - **Test Request**:
     ```json
     {
       "message": "What is Section 103 BNS?"
     }
     ```
   - Click **Test** → Should return AI response!
   - **Response**: Add response field
     - Field Name: `reply`
     - JSON Path: `$.reply`
     - Type: String

4. Add remaining APIs (optional for initial testing):
   - `getAllSections` (GET)
   - `getSectionById` (GET)
   - `getCategories` (GET)

**✅ Result**: Backend connected to FlutterFlow!

---

## 🎨 Quick UI Build (10 minutes)

### Minimal Viable App

Build these 3 pages for a working prototype:

#### 1. AuthPage (3 minutes)

```
Scaffold
├─ Column
   ├─ Text: "Legally" (Heading1)
   ├─ TextField: Email
   ├─ TextField: Password (obscure)
   ├─ Button: "Sign In"
   │  OnPressed:
   │    - Authenticate User (Firebase)
   │    - Navigate to HomePage
   └─ Button: "Sign Up"
      OnPressed:
        - Create Account (Firebase)
        - Navigate to HomePage
```

#### 2. HomePage (2 minutes)

```
Scaffold
├─ AppBar: Title "Home"
├─ Column
   ├─ Text: "Welcome to Legally"
   └─ Button: "Ask AI"
      OnPressed: Navigate to AskAIPage
```

#### 3. AskAIPage (5 minutes)

```
Scaffold
├─ AppBar: Title "Ask Legal AI"
├─ Column
   ├─ ListView.builder (for messages)
   │  State Variable: messages (List<JSON>)
   └─ Row (input area)
      ├─ TextField: messageText
      └─ IconButton: Send
         OnPressed:
           1. Add user message to messages list
           2. API Call: askLegalAI (message: messageText)
           3. Add AI response to messages list
           4. Clear messageText
```

**✅ Result**: Working AI chat app!

---

## 🧪 Test Your App (5 minutes)

### In FlutterFlow

1. Click **▶ Run** (top right)
2. Choose **Test Mode**
3. Test flow:
   - Sign up with test email
   - Navigate to Ask AI
   - Send: "What is murder under BNS?"
   - Verify AI responds with BNS Section 103

### Expected Response:

```
Under Section 103 of the Bharatiya Nyaya Sanhita, 2023...

[AI provides detailed explanation]

⚖️ LEGAL DISCLAIMER: This is AI-generated educational 
information based on BNS, 2023. It is NOT legal advice...
```

**✅ If this works, you're done with MVP!**

---

## 📱 Full App Build (Continue from here)

Now follow the comprehensive guide:

👉 **[FLUTTERFLOW_BUILD_GUIDE.md](./FLUTTERFLOW_BUILD_GUIDE.md)**

This includes all 9 pages with complete widget trees, styling, and functionality.

---

## 🎯 What You've Built

✅ FastAPI backend with RAG-lite  
✅ Groq AI integration  
✅ Firebase authentication  
✅ Firebase Realtime Database  
✅ Basic chat interface  
✅ BNS-only legal responses

---

## 🐛 Common Issues

### Issue: Backend API call fails

**Check**:
- ✅ Vercel deployment successful?
- ✅ GROQ_API_KEY set in Vercel?
- ✅ Backend URL correct in FlutterFlow?
- ✅ Internet connection working?

**Test backend directly**:
```bash
curl https://YOUR-VERCEL-URL.vercel.app/
```

Should return:
```json
{
  "status": "online",
  "api": "Legally - BNS Legal AI",
  ...
}
```

### Issue: Firebase authentication not working

**Check**:
- ✅ Firebase configuration downloaded?
- ✅ Authentication enabled in Firebase Console?
- ✅ Email/Password provider enabled?

### Issue: App doesn't run in FlutterFlow

**Check**:
- ✅ No widget errors (red underlines)?
- ✅ All required fields filled?
- ✅ Navigation routes set correctly?

---

## 📊 Architecture Diagram

```
┌─────────────────┐
│  Mobile App     │
│  (FlutterFlow)  │
└────────┬────────┘
         │
         │ HTTPS
         │
┌────────▼────────┐      ┌──────────────┐
│  FastAPI        │─────▶│  Groq AI     │
│  (Vercel)       │◀─────│  (LLM)       │
└────────┬────────┘      └──────────────┘
         │
         │ Reads
         │
┌────────▼────────┐
│  bns_sections   │
│  .json          │
│  (384 sections) │
└─────────────────┘

┌─────────────────┐
│  Firebase       │
│  - Auth         │
│  - Database     │
└─────────────────┘
         ▲
         │
         │ SDK
         │
┌────────┴────────┐
│  Mobile App     │
│  (FlutterFlow)  │
└─────────────────┘
```

---

## 🎓 Learning Resources

### FlutterFlow
- **Docs**: https://docs.flutterflow.io
- **YouTube**: Search "FlutterFlow tutorial"
- **Community**: https://community.flutterflow.io

### FastAPI
- **Docs**: https://fastapi.tiangolo.com
- **Tutorial**: FastAPI official tutorial

### Firebase
- **Docs**: https://firebase.google.com/docs
- **Auth Guide**: Firebase Authentication docs

### Groq
- **Docs**: https://console.groq.com/docs
- **Models**: llama-3.3-70b-versatile (fastest)

---

## 🚀 Next Steps

### Enhance Your App

1. **Add all 9 pages** from the full guide
2. **Implement Browse BNS** with search/filter
3. **Add Chat History** with Firebase queries
4. **Style with dark theme** and gold accents
5. **Add animations** for premium feel

### Advanced Features

- [ ] Bookmark sections
- [ ] Share functionality
- [ ] Push notifications
- [ ] Offline mode
- [ ] Voice input
- [ ] Multi-language support
- [ ] Case law integration
- [ ] Legal news feed

### Deploy to Production

1. Test thoroughly
2. Add app icons & splash screen
3. Build for iOS & Android
4. Submit to App Store & Play Store

---

## 📞 Get Help

- **Backend Issues**: Check [backend/README.md](./backend/README.md)
- **FlutterFlow Issues**: See [FLUTTERFLOW_BUILD_GUIDE.md](./FLUTTERFLOW_BUILD_GUIDE.md)
- **BNS Questions**: Reference `bns_sections.json`

---

## ✅ Quick Start Complete!

You now have a working BNS Legal AI app!

**Time to complete**: ~30 minutes  
**Result**: Production-ready MVP

**Continue building** with the comprehensive guide for a full-featured app.

---

**Built for Bharatiya Nyaya Sanhita, 2023 🇮🇳**

**NOT Indian Penal Code (IPC)**

---

END OF QUICK START GUIDE
