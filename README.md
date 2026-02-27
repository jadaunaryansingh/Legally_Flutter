# ⚖️ Legally - BNS Legal AI Mobile App

<div align="center">

![Legally Logo](assets/logo.png)

**Your AI-Powered Legal Assistant for Bharatiya Nyaya Sanhita, 2023**

[![FastAPI](https://img.shields.io/badge/FastAPI-0.115.0-009688?logo=fastapi)](https://fastapi.tiangolo.com)
[![FlutterFlow](https://img.shields.io/badge/FlutterFlow-Latest-02569B?logo=flutter)](https://flutterflow.io)
[![Firebase](https://img.shields.io/badge/Firebase-Latest-FFCA28?logo=firebase)](https://firebase.google.com)
[![Groq](https://img.shields.io/badge/Groq-LLaMA%203.3-FF6B00)](https://groq.com)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

</div>

---

## 📱 About

**Legally** is a production-ready mobile application that provides AI-powered legal assistance based exclusively on the **Bharatiya Nyaya Sanhita, 2023 (BNS)** - India's new criminal code that replaced the Indian Penal Code (IPC) on July 1, 2024.

### 🎯 Key Features

- 🤖 **AI Legal Assistant** - Ask legal questions and get instant BNS-based answers
- 📚 **Complete BNS Database** - Browse all 384 sections
- 🔍 **Smart Search** - Find sections by keyword or category
- 💬 **Chat History** - All conversations saved securely
- 🔐 **Secure Authentication** - Email/Password and Google Sign-In
- 🎨 **Premium Dark UI** - Professional legal-tech design
- 📱 **Cross-Platform** - iOS & Android

### ⚠️ Important Notice

**This app uses ONLY Bharatiya Nyaya Sanhita, 2023 (BNS) - NOT IPC**

All legal information is for educational purposes only. Not a substitute for professional legal advice.

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────┐
│          Mobile App (FlutterFlow)               │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐     │
│  │   Home   │  │  Ask AI  │  │  Browse  │     │
│  └──────────┘  └──────────┘  └──────────┘     │
│  ┌──────────┐  ┌──────────┐                    │
│  │ History  │  │ Profile  │                    │
│  └──────────┘  └──────────┘                    │
└────────────┬────────────────────────────────────┘
             │
             │ HTTPS API Calls
             ▼
┌─────────────────────────────────────────────────┐
│      FastAPI Backend (Vercel)                   │
│  ┌──────────────────────────────────────────┐  │
│  │  RAG-lite: Search bns_sections.json     │  │
│  │  Extract relevant sections               │  │
│  │  Send to Groq AI                         │  │
│  │  Return structured answer                │  │
│  └──────────────────────────────────────────┘  │
└────────────┬─────────────────┬──────────────────┘
             │                 │
             │                 │ AI Generation
             │                 ▼
             │     ┌─────────────────────────┐
             │     │   Groq AI               │
             │     │   (LLaMA 3.3-70B)       │
             │     └─────────────────────────┘
             │
             │ Data Source
             ▼
┌─────────────────────────────────────────────────┐
│       bns_sections.json                         │
│       (384 BNS sections)                        │
└─────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────┐
│       Firebase (Google)                         │
│  ┌──────────────┐  ┌──────────────────────┐    │
│  │ Auth         │  │ Realtime Database    │    │
│  │ - Email/Pass │  │ - Chat history       │    │
│  │ - Google     │  │ - User data          │    │
│  └──────────────┘  └──────────────────────┘    │
└─────────────────────────────────────────────────┘
```

---

## 🚀 Quick Start

Get your app running in 30 minutes!

### Prerequisites

- FlutterFlow account
- Firebase account
- Vercel account
- Groq API key ([Get here](https://console.groq.com/keys))
- Python 3.9+ (for local development)

### Step 1: Deploy Backend

```bash
# Navigate to backend
cd backend

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env
# Add your Groq API key to .env

# Test locally (optional)
uvicorn main:app --reload

# Deploy to Vercel
npm i -g vercel
vercel login
vercel
vercel env add GROQ_API_KEY  # Enter your Groq key
vercel --prod
```

**Result**: Backend URL → `https://legally-xyz.vercel.app`

### Step 2: Setup Firebase

1. Create Firebase project: [console.firebase.google.com](https://console.firebase.google.com)
2. Enable **Authentication** (Email/Password + Google)
3. Enable **Realtime Database**
4. Download config files (`google-services.json` & `GoogleService-Info.plist`)

### Step 3: Build in FlutterFlow

1. Create new FlutterFlow project
2. Connect Firebase (upload config files)
3. Add API calls (see [FLUTTERFLOW_BUILD_GUIDE.md](./FLUTTERFLOW_BUILD_GUIDE.md))
4. Build all pages following the guide
5. Test and deploy!

📚 **Detailed Instructions**: See [QUICK_START.md](./QUICK_START.md)

---

## 📁 Project Structure

```
LegallyFlutter/
│
├── backend/                     # FastAPI Backend
│   ├── main.py                 # Main API server
│   ├── requirements.txt        # Python dependencies
│   ├── vercel.json             # Vercel config
│   └── README.md               # Backend docs
│
├── bns_sections.json           # BNS Database (384 sections)
│
├── docs/                       # Documentation
│   ├── FLUTTERFLOW_BUILD_GUIDE.md   # Complete build guide
│   ├── QUICK_START.md               # 30-min quick start
│   ├── PROJECT_STRUCTURE.md         # Project organization
│   ├── DEPLOYMENT.md                # Deployment guide
│   └── API_REFERENCE.md             # API documentation
│
├── assets/                     # App assets (icons, images)
│
├── firebase/                   # Firebase configs
│
└── README.md                   # This file
```

---

## 🛠️ Tech Stack

### Frontend
- **FlutterFlow** - No-code Flutter development
- **Flutter/Dart** - Mobile framework
- **Firebase Auth** - User authentication
- **Firebase Realtime Database** - Data storage

### Backend
- **FastAPI** - Python web framework
- **Python 3.9+** - Programming language
- **Groq** - AI/LLM provider (LLaMA 3.3-70B)
- **Vercel** - Serverless deployment
- **Uvicorn** - ASGI server

### Data
- **JSON** - BNS sections database
- **RAG-lite** - Retrieval-Augmented Generation

---

## 📖 Documentation

| Document | Description |
|----------|-------------|
| [QUICK_START.md](./QUICK_START.md) | Get started in 30 minutes |
| [FLUTTERFLOW_BUILD_GUIDE.md](./FLUTTERFLOW_BUILD_GUIDE.md) | Complete build instructions |
| [API_REFERENCE.md](./API_REFERENCE.md) | Backend API documentation |
| [DEPLOYMENT.md](./DEPLOYMENT.md) | Production deployment guide |
| [PROJECT_STRUCTURE.md](./PROJECT_STRUCTURE.md) | Project organization |
| [backend/README.md](./backend/README.md) | Backend-specific docs |

---

## 🔌 API Endpoints

**Base URL**: `https://your-backend.vercel.app`

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Health check |
| `/api/ask` | POST | Ask legal AI |
| `/api/sections` | GET | Get all sections |
| `/api/sections/{id}` | GET | Get specific section |
| `/api/categories` | GET | Get categories |
| `/api/metadata` | GET | Get BNS metadata |

**Example**:
```bash
curl -X POST https://your-backend.vercel.app/api/ask \
  -H "Content-Type: application/json" \
  -d '{"message": "What is Section 103 BNS?"}'
```

📚 **Complete API Docs**: [API_REFERENCE.md](./API_REFERENCE.md)

---

## 📱 Mobile App Pages

1. **AuthPage** - Sign in / Sign up
2. **HomePage** - Welcome dashboard
3. **AskAIPage** - AI chat interface ⭐
4. **BrowsePage** - Browse BNS sections
5. **SectionDetailPage** - Section details
6. **HistoryPage** - Past conversations
7. **ChatDetailPage** - View specific chat
8. **ProfilePage** - User profile & settings
9. **OnboardingPage** - First-time user guide

---

## 🎨 Design

### Theme

- **Style**: Premium dark legal-tech
- **Primary Color**: Gold (#D4AF37)
- **Background**: Pure Black (#0D0D0D)
- **Surface**: Dark Gray (#1E1E1E)
- **Typography**: Playfair Display (headings), Inter (body)

### Screenshots

<div align="center">
  <img src="assets/screenshots/home.png" width="200" alt="Home Screen" />
  <img src="assets/screenshots/chat.png" width="200" alt="AI Chat" />
  <img src="assets/screenshots/browse.png" width="200" alt="Browse BNS" />
  <img src="assets/screenshots/detail.png" width="200" alt="Section Detail" />
</div>

---

## 🧪 Testing

### Backend Tests

```bash
cd backend

# Run tests
python -m pytest tests/

# Or test endpoints manually
curl https://your-backend.vercel.app/

curl -X POST https://your-backend.vercel.app/api/ask \
  -H "Content-Type: application/json" \
  -d '{"message": "What is murder under BNS?"}'
```

### Mobile App Tests

1. Test Mode in FlutterFlow
2. Run on iOS Simulator
3. Run on Android Emulator
4. Test on physical devices
5. TestFlight (iOS) / Internal Testing (Android)

---

## 🚀 Deployment

### Backend to Vercel

```bash
cd backend
vercel --prod
```

### Mobile App to Stores

**iOS App Store**:
1. Build in FlutterFlow or Xcode
2. Submit via App Store Connect
3. Review process: 1-7 days

**Android Play Store**:
1. Build AAB in FlutterFlow
2. Submit via Google Play Console
3. Review process: 1-3 days

📚 **Complete Guide**: [DEPLOYMENT.md](./DEPLOYMENT.md)

---

## 📊 Features & Roadmap

### ✅ Current Features (v1.0.0)

- [x] AI-powered legal Q&A
- [x] Complete BNS 2023 database
- [x] Search & filter sections
- [x] Chat history with Firebase
- [x] User authentication
- [x] Dark premium UI
- [x] Cross-platform (iOS & Android)

### 🔮 Planned Features

- [ ] Bookmark sections
- [ ] Share functionality
- [ ] Offline mode
- [ ] Multi-language support (Hindi, etc.)
- [ ] Voice input/output
- [ ] Push notifications
- [ ] Case law integration
- [ ] Legal news feed
- [ ] Document scanner
- [ ] Lawyer directory

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Guidelines

- Follow PEP 8 for Python code
- Use meaningful commit messages
- Add tests for new features
- Update documentation
- Ensure backend tests pass

---

## 🐛 Known Issues

- None at this time

**Report Issues**: [GitHub Issues](https://github.com/yourusername/legally/issues)

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

### What This Means

✅ You can:
- Use commercially
- Modify
- Distribute
- Use privately

❌ You cannot:
- Hold liable
- Use trademark

📝 You must:
- Include license and copyright notice

---

## ⚖️ Legal Disclaimer

**IMPORTANT**: This application provides educational information about the Bharatiya Nyaya Sanhita, 2023 (BNS). 

### Not Legal Advice

The information provided by this app is AI-generated and for educational purposes only. It is **NOT legal advice** and should not be relied upon as such.

### Consult a Lawyer

For specific legal advice or representation, please consult a qualified advocate or legal professional.

### No Warranty

The app is provided "as is" without warranty of any kind. We are not liable for any decisions made based on information from this app.

### Accuracy

While we strive for accuracy, we cannot guarantee that all information is complete, correct, or up-to-date.

---

## 👥 Credits

### Development Team

- **Backend**: FastAPI + Python
- **Frontend**: FlutterFlow
- **AI**: Groq (LLaMA 3.3-70B)
- **Database**: Firebase
- **Deployment**: Vercel

### Data Source

- **Bharatiya Nyaya Sanhita, 2023** - Government of India

### Tools & Services

- FastAPI - Web framework
- FlutterFlow - No-code platform
- Firebase - Backend services
- Groq - AI infrastructure
- Vercel - Deployment platform

---

## 📞 Support & Contact

### Get Help

- **Documentation**: See [docs/](./docs/) folder
- **GitHub Issues**: Report bugs and request features
- **Email**: support@yourcompany.com

### Community

- **Discord**: [Join our community](#) (future)
- **Twitter**: [@LegallyApp](#) (future)
- **Website**: [legally.app](#) (future)

---

## 🌟 Show Your Support

If you find this project useful:

- ⭐ Star this repository
- 🐛 Report bugs
- 💡 Suggest features
- 🔀 Submit pull requests
- 📢 Share with others

---

## 📈 Stats

- **Total BNS Sections**: 384
- **Lines of Code**: ~2,000+ (backend)
- **Documentation Pages**: 5
- **API Endpoints**: 6
- **Supported Platforms**: iOS & Android

---

## 🎓 Educational Purpose

This app was built to:

1. ✅ Democratize legal knowledge
2. ✅ Make BNS 2023 accessible to everyone
3. ✅ Educate citizens about criminal law
4. ✅ Help law students learn BNS
5. ✅ Showcase AI in legal tech

**Remember**: Knowledge is power, but professional legal advice is irreplaceable.

---

## 🇮🇳 Made for India

Built with ❤️ for the Bharatiya Nyaya Sanhita, 2023 - India's new criminal code.

**Effective Date**: July 1, 2024  
**Replaces**: Indian Penal Code, 1860 (IPC)  
**Total Sections**: 384

---

<div align="center">

**⚖️ Legally - Empowering Legal Awareness ⚖️**

[Documentation](./docs/) • [Quick Start](./QUICK_START.md) • [API Reference](./API_REFERENCE.md) • [Deployment](./DEPLOYMENT.md)

Made with 🧠 AI • 💻 Code • ⚖️ Law

</div>

---

**Last Updated**: February 27, 2026

**Version**: 1.0.0

**Status**: Production Ready ✅

---

END OF README
