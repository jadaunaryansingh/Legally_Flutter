# 🚀 Legally - Deployment Guide

Complete production deployment instructions for backend and mobile app.

---

## 📋 Pre-Deployment Checklist

### Backend
- [ ] Code tested locally
- [ ] All environment variables documented
- [ ] Groq API key obtained
- [ ] Error handling implemented
- [ ] CORS configured properly
- [ ] Security best practices followed

### Mobile App
- [ ] All pages built and tested
- [ ] Firebase fully configured
- [ ] API calls tested
- [ ] Authentication working
- [ ] Dark theme applied
- [ ] App icons prepared (1024x1024)
- [ ] Splash screen ready
- [ ] Privacy policy written
- [ ] Terms of service written

---

## 🔧 PART 1: Backend Deployment to Vercel

### Step 1: Prepare Backend

```bash
cd backend

# Test locally first
pip install -r requirements.txt
uvicorn main:app --reload

# Visit http://localhost:8000
# Test endpoints with curl or browser
```

### Step 2: Install Vercel CLI

```bash
# Install globally
npm install -g vercel

# Or use npx (no installation)
npx vercel
```

### Step 3: Login to Vercel

```bash
vercel login
```

Choose your preferred login method:
- Email
- GitHub
- GitLab
- Bitbucket

### Step 4: Deploy Backend

```bash
cd backend
vercel
```

**First-time deployment prompts**:

```
? Set up and deploy "~/backend"? [Y/n] Y
? Which scope do you want to deploy to? [Your Name]
? Link to existing project? [y/N] N
? What's your project's name? legally-backend
? In which directory is your code located? ./
```

**Output**:
```
🔗  Linked to your-username/legally-backend
🔍  Inspect: https://vercel.com/your-username/legally-backend/...
✅  Preview: https://legally-backend-xyz123.vercel.app
```

### Step 5: Add Environment Variables

```bash
# Add Groq API key
vercel env add GROQ_API_KEY

# When prompted:
? What's the value of GROQ_API_KEY? gsk_your_actual_groq_api_key
? Add GROQ_API_KEY to which Environments? Production, Preview, Development
```

### Step 6: Deploy to Production

```bash
vercel --prod
```

**Output**:
```
✅  Production: https://legally-backend.vercel.app
```

### Step 7: Test Deployment

```bash
# Test health check
curl https://legally-backend.vercel.app/

# Expected response:
{
  "status": "online",
  "api": "Legally - BNS Legal AI",
  "version": "1.0.0",
  "legal_framework": "Bharatiya Nyaya Sanhita, 2023",
  "total_sections": 384
}

# Test AI endpoint
curl -X POST https://legally-backend.vercel.app/api/ask \
  -H "Content-Type: application/json" \
  -d '{"message": "What is Section 103 BNS?"}'

# Should return:
{
  "reply": "Under Section 103 of the Bharatiya Nyaya Sanhita, 2023..."
}
```

### Step 8: Configure Custom Domain (Optional)

In Vercel Dashboard:
1. Go to your project
2. **Settings** → **Domains**
3. Add domain: `api.legally.app`
4. Follow DNS configuration instructions

---

## 🔥 PART 2: Firebase Configuration

### Step 1: Create Firebase Project

1. Go to [Firebase Console](https://console.firebase.google.com)
2. Click **Add Project**
3. Project name: `Legally`
4. Disable Google Analytics (optional)
5. Click **Create Project**

### Step 2: Enable Authentication

1. In Firebase Console, go to **Build** → **Authentication**
2. Click **Get Started**
3. Enable **Email/Password**:
   - Click on Email/Password
   - Toggle **Enable**
   - Click **Save**
4. Enable **Google Sign-In**:
   - Click on Google
   - Toggle **Enable**
   - Enter support email
   - Click **Save**

### Step 3: Setup Realtime Database

1. Go to **Build** → **Realtime Database**
2. Click **Create Database**
3. Choose location (e.g., us-central1)
4. Start in **Test Mode** (for development)
5. Click **Enable**

### Step 4: Configure Security Rules

In **Realtime Database** → **Rules** tab:

```json
{
  "rules": {
    "chats": {
      "$uid": {
        ".read": "$uid === auth.uid",
        ".write": "$uid === auth.uid",
        ".validate": "auth != null"
      }
    },
    "users": {
      "$uid": {
        ".read": "$uid === auth.uid",
        ".write": "$uid === auth.uid",
        ".validate": "auth != null",
        "email": {
          ".validate": "newData.isString()"
        },
        "displayName": {
          ".validate": "newData.isString()"
        },
        "createdAt": {
          ".validate": "newData.isNumber()"
        }
      }
    }
  }
}
```

Click **Publish** to save.

### Step 5: Generate Config Files

**For Android**:
1. In Firebase Console, click **Project Settings** (gear icon)
2. Scroll to **Your apps**
3. Click **Android** icon
4. Register app:
   - Package name: `com.yourcompany.legally`
   - App nickname: `Legally`
   - Click **Register app**
5. Download `google-services.json`
6. **Save this file** - you'll need it for FlutterFlow

**For iOS**:
1. In **Project Settings** → **Your apps**
2. Click **iOS** icon
3. Register app:
   - Bundle ID: `com.yourcompany.legally`
   - App nickname: `Legally`
   - Click **Register app**
4. Download `GoogleService-Info.plist`
5. **Save this file** - you'll need it for FlutterFlow

### Step 6: Enable Firestore (Optional)

If you want to use Firestore in addition to Realtime Database:

1. Go to **Build** → **Firestore Database**
2. Click **Create Database**
3. Start in **Test Mode**
4. Choose location
5. Click **Enable**

---

## 📱 PART 3: FlutterFlow Mobile App Deployment

### Step 1: Complete App in FlutterFlow

Ensure everything is built according to [FLUTTERFLOW_BUILD_GUIDE.md](./FLUTTERFLOW_BUILD_GUIDE.md):

- [ ] All 9 pages created
- [ ] Navigation configured
- [ ] API calls added and tested
- [ ] Firebase connected
- [ ] Authentication working
- [ ] Theme applied
- [ ] All actions wired up

### Step 2: Update Backend URL

In FlutterFlow **API Calls**, update all URLs:

**Change from**:
```
https://your-backend.vercel.app
```

**To**:
```
https://legally-backend.vercel.app
```
(Your actual Vercel URL)

Update in:
- askLegalAI
- getAllSections
- getSectionById
- getCategories
- getMetadata

### Step 3: Add App Icons

1. In FlutterFlow, go to **Settings & Integrations** → **General**
2. Scroll to **App Icon**
3. Click **Upload Icon**
4. Upload your 1024x1024 PNG icon
5. FlutterFlow will auto-generate all sizes

### Step 4: Configure Splash Screen

1. In **Settings & Integrations** → **General**
2. Scroll to **Splash Screen**
3. Configure:
   - Background Color: `#0D0D0D` (black)
   - Logo: Upload your app logo
   - Logo Size: 200x200
   - Show Logo: ✅

### Step 5: Set App Information

In **Settings & Integrations** → **General**:

**App Details**:
- App Name: `Legally`
- Package Name (Android): `com.yourcompany.legally`
- Bundle ID (iOS): `com.yourcompany.legally`

**Version**:
- Version Number: `1.0.0`
- Build Number: `1`

**Description**:
```
Legally - Your BNS Legal AI Assistant

AI-powered legal assistant for Bharatiya Nyaya Sanhita, 2023 (BNS).
Get instant answers to legal questions, browse all 384 BNS sections,
and access comprehensive criminal law information.

Features:
• AI-powered legal Q&A
• Complete BNS 2023 database
• Search & filter sections
• Save chat history
• Bookmark important sections
• Dark premium UI

Disclaimer: This app provides educational information only.
Not a substitute for professional legal advice.
```

### Step 6: Configure Firebase in FlutterFlow

1. Go to **Settings & Integrations** → **Firebase**
2. Click **Connect to Firebase**
3. Select your Firebase project
4. Upload config files:
   - **Android**: Upload `google-services.json`
   - **iOS**: Upload `GoogleService-Info.plist`
5. Enable services:
   - ✅ Authentication
   - ✅ Realtime Database
   - ✅ Analytics (optional)

### Step 7: Test Build

1. Click **Run** button (top right)
2. Choose **Test Mode**
3. Select device (iOS/Android simulator)
4. Test all features:
   - Sign up/Sign in
   - Ask AI questions
   - Browse sections
   - View history
   - Profile features

### Step 8: Download Code (Optional)

If you want to customize further:

1. Click **Developer Menu** (+) icon, top right
2. Click **Download Code**
3. Choose **Full Code Download**
4. You'll receive a Flutter project

**Build locally**:
```bash
cd legally_flutter_project
flutter pub get
flutter run
```

---

## 📱 PART 4: iOS App Store Deployment

### Prerequisites

- [ ] Apple Developer Account ($99/year)
- [ ] Mac with Xcode installed
- [ ] iOS app tested on physical device

### Step 1: Prepare in FlutterFlow

1. Ensure all iOS-specific settings configured
2. Build Number: 1
3. Version: 1.0.0
4. Bundle ID: `com.yourcompany.legally`

### Step 2: Build iOS App

**Option A: FlutterFlow Web to TestFlight**

1. In FlutterFlow, click **Deploy** (rocket icon)
2. Choose **iOS**
3. Click **Build for iOS**
4. Wait for build (~10-15 minutes)
5. Download IPA file
6. Upload to App Store Connect using Transporter app

**Option B: Download Code and Build Locally**

1. Download code from FlutterFlow
2. Open project in Xcode:
   ```bash
   cd legally_flutter_project/ios
   open Runner.xcworkspace
   ```
3. Configure signing:
   - Select **Runner** in project navigator
   - Go to **Signing & Capabilities**
   - Select your team
   - Check **Automatically manage signing**
4. Build for release:
   ```bash
   flutter build ios --release
   ```
5. Archive in Xcode:
   - Product → Archive
   - Once archived, click **Distribute App**

### Step 3: App Store Connect Setup

1. Go to [App Store Connect](https://appstoreconnect.apple.com)
2. Click **My Apps** → **+** → **New App**
3. Fill in details:
   - Platform: iOS
   - Name: Legally
   - Primary Language: English
   - Bundle ID: com.yourcompany.legally
   - SKU: LEGALLY001
4. Click **Create**

### Step 4: Prepare App Store Listing

**App Information**:
- Category: Productivity (or Education)
- Subcategory: Reference

**Pricing**:
- Price: Free

**Screenshots** (Required):
- 6.5" iPhone (1284x2778): 3-10 screenshots
- 5.5" iPhone (1242x2208): 3-10 screenshots
- iPad Pro (2048x2732): 3-10 screenshots (if supporting iPad)

**App Preview Video** (Optional):
- 15-30 second demo video

**Description**:
```
Legally - Your Bharatiya Nyaya Sanhita (BNS) Legal AI Assistant

Introducing Legally, the most comprehensive AI-powered legal assistant for India's new criminal code - the Bharatiya Nyaya Sanhita, 2023 (BNS).

🤖 AI-POWERED LEGAL ASSISTANCE
Ask any question about Indian criminal law and receive instant, accurate answers based on BNS 2023. Our advanced AI analyzes all 384 sections to provide comprehensive legal information.

📚 COMPLETE BNS DATABASE
Browse, search, and explore all 384 sections of the Bharatiya Nyaya Sanhita, 2023. Find relevant sections by keyword, category, or section number.

💬 SMART CHAT INTERFACE
Natural conversation interface with legal AI. All your conversations are saved for future reference.

🔍 POWERFUL SEARCH
Find exactly what you need with advanced search and category filters.

⚖️ KEY FEATURES:
• AI-powered legal Q&A
• Complete BNS 2023 section database
• Section-wise detailed information
• Punishment details for each offense
• Category-based filtering
• Save chat history
• Bookmark important sections
• Dark premium UI
• Secure authentication

📖 EDUCATIONAL & RELIABLE
All information is based strictly on the official Bharatiya Nyaya Sanhita, 2023, which replaced the Indian Penal Code (IPC) on July 1, 2024.

⚖️ DISCLAIMER
Legally provides educational information about BNS 2023. This is NOT legal advice. For specific legal matters, consult a qualified advocate or legal professional.

Perfect for:
✓ Law students
✓ Legal professionals
✓ Citizens seeking legal awareness
✓ Police officers
✓ Researchers
✓ Anyone interested in Indian criminal law

Download Legally today and empower yourself with legal knowledge!
```

**Keywords**:
```
law, legal, BNS, Bharatiya Nyaya Sanhita, Indian law, criminal law,
legal advice, IPC, penal code, legal assistant, AI legal, law app
```

**Promotional Text**:
```
AI-powered BNS legal assistant. Ask questions, browse 384 sections,
get instant answers based on Bharatiya Nyaya Sanhita, 2023.
```

**Privacy Policy URL**: 
Create and host privacy policy (see template below)

**Terms of Service URL**:
Create and host terms of service

### Step 5: Submit for Review

1. Upload build via Transporter or Xcode
2. Select build in App Store Connect
3. Fill in all required fields
4. Answer **App Review Information** questions:
   - Demo account (if auth required): Create test account
   - Contact information
   - Notes: Explain app is for educational purposes
5. Click **Submit for Review**
6. Wait 1-7 days for review

### Step 6: App Review Tips

**Common Rejection Reasons**:
- Missing privacy policy
- Incomplete functionality
- Crashes
- Misleading description

**Legal Disclaimer Requirements**:
Ensure prominent disclaimer that app is not legal advice.

### Step 7: Go Live!

Once approved:
- App will be available on App Store
- Monitor reviews and ratings
- Respond to user feedback
- Plan updates

---

## 🤖 PART 5: Android Play Store Deployment

### Prerequisites

- [ ] Google Play Developer Account ($25 one-time)
- [ ] App tested on Android device

### Step 1: Build Android App

**Option A: FlutterFlow Build**

1. In FlutterFlow, click **Deploy** (rocket icon)
2. Choose **Android**
3. Click **Build for Android**
4. Choose **App Bundle (AAB)** for Play Store
5. Wait for build
6. Download AAB file

**Option B: Build Locally**

```bash
cd legally_flutter_project

# Build App Bundle (for Play Store)
flutter build appbundle --release

# Or APK (for testing)
flutter build apk --release
```

Output: 
- AAB: `build/app/outputs/bundle/release/app-release.aab`
- APK: `build/app/outputs/flutter-apk/app-release.apk`

### Step 2: Sign the App

FlutterFlow handles signing automatically. If building locally:

1. Create keystore:
   ```bash
   keytool -genkey -v -keystore ~/legally-key.jks \
     -keyalg RSA -keysize 2048 -validity 10000 \
     -alias legally
   ```

2. Create `android/key.properties`:
   ```properties
   storePassword=your_password
   keyPassword=your_password
   keyAlias=legally
   storeFile=/path/to/legally-key.jks
   ```

3. Update `android/app/build.gradle`:
   ```gradle
   android {
       ...
       signingConfigs {
           release {
               keyAlias keystoreProperties['keyAlias']
               keyPassword keystoreProperties['keyPassword']
               storeFile file(keystoreProperties['storeFile'])
               storePassword keystoreProperties['storePassword']
           }
       }
       buildTypes {
           release {
               signingConfig signingConfigs.release
           }
       }
   }
   ```

### Step 3: Google Play Console Setup

1. Go to [Google Play Console](https://play.google.com/console)
2. Click **Create app**
3. Fill in details:
   - App name: Legally
   - Default language: English (United States)
   - App or game: App
   - Free or paid: Free
   - Declarations: Accept all
4. Click **Create app**

### Step 4: Complete Store Listing

**Main store listing**:

**App name**: Legally

**Short description** (80 chars):
```
BNS Legal AI Assistant - Ask questions, browse 384 sections of BNS 2023
```

**Full description** (4000 chars):
```
[Same as iOS description above]
```

**App icon**:
- Upload 512x512 PNG

**Feature graphic**:
- Create 1024x500 banner image
- Show app screenshot with logo

**Screenshots**:
- Phone: At least 2 (upload 4-8)
- 7" Tablet: At least 2 (if supporting tablets)
- 10" Tablet: At least 2 (if supporting tablets)

**App category**:
- Category: Productivity
- Tags: legal, law, education

**Contact details**:
- Email: support@yourcompany.com
- Website: https://yourcompany.com
- Phone: (optional)

**Privacy policy**:
- URL: https://yourcompany.com/privacy

### Step 5: Content Rating

1. Go to **Content rating** section
2. Fill out questionnaire:
   - App category: Utility, Productivity, Communication, or Other
   - Answer all questions (usually all "No" for this app)
3. Generate rating

### Step 6: App Content

Complete all required sections:
- **Privacy policy**: Add URL
- **Ads**: Select "No, my app does not contain ads"
- **App access**: If auth required, provide test account
- **Content ratings**: Complete questionnaire
- **Target audience**: Select age groups
- **News apps**: Not applicable
- **COVID-19 contact tracing**: Not applicable
- **Data safety**: Complete form

**Data Safety Form**:
- Data collected: Email, User ID (if using Firebase Auth)
- Data usage: Account management, App functionality
- Data sharing: No data shared with third parties
- Security practices: Data encrypted in transit

### Step 7: Release

1. Go to **Production** (or **Internal testing** for beta)
2. Click **Create new release**
3. Upload AAB file
4. Release name: `1.0.0`
5. Release notes:
   ```
   Initial release of Legally - BNS Legal AI Assistant
   
   Features:
   • AI-powered legal Q&A based on BNS 2023
   • Browse 384 sections of Bharatiya Nyaya Sanhita
   • Search and filter functionality
   • Save chat history
   • Dark premium theme
   
   Please report any issues to support@yourcompany.com
   ```
6. Review and rollout
7. Click **Start rollout to Production**

### Step 8: Submit for Review

Play Store review typically takes 1-3 days.

**Review Tips**:
- Make sure all required fields filled
- Provide test account if auth required
- Privacy policy accessible and complete
- App doesn't crash on common devices

### Step 9: Go Live!

Once approved:
- App will be live on Play Store
- Usually within hours
- Monitor reviews and crashes
- Respond to user feedback

---

## 📄 PART 6: Privacy Policy & Terms

### Privacy Policy Template

Host this at `https://yourcompany.com/privacy`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Privacy Policy - Legally</title>
</head>
<body>
    <h1>Privacy Policy for Legally</h1>
    <p>Last updated: [Date]</p>
    
    <h2>1. Information We Collect</h2>
    <p>We collect the following information:</p>
    <ul>
        <li>Email address (for account creation)</li>
        <li>Display name (optional)</li>
        <li>Chat history (stored securely in Firebase)</li>
        <li>Usage analytics (if enabled)</li>
    </ul>
    
    <h2>2. How We Use Your Information</h2>
    <p>We use your information to:</p>
    <ul>
        <li>Provide legal AI assistance</li>
        <li>Save your chat history</li>
        <li>Improve app functionality</li>
        <li>Send important updates (with consent)</li>
    </ul>
    
    <h2>3. Data Storage</h2>
    <p>Your data is stored securely using Firebase Realtime Database
    with encryption in transit and at rest.</p>
    
    <h2>4. Data Sharing</h2>
    <p>We do NOT share your personal data with third parties, except:</p>
    <ul>
        <li>Firebase (Google) - our hosting provider</li>
        <li>required by law</li>
    </ul>
    
    <h2>5. Your Rights</h2>
    <p>You have the right to:</p>
    <ul>
        <li>Access your data</li>
        <li>Delete your account and data</li>
        <li>Opt out of analytics</li>
    </ul>
    
    <h2>6. Contact Us</h2>
    <p>For privacy concerns, contact: support@yourcompany.com</p>
</body>
</html>
```

### Terms of Service Template

Host this at `https://yourcompany.com/terms`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Terms of Service - Legally</title>
</head>
<body>
    <h1>Terms of Service for Legally</h1>
    <p>Last updated: [Date]</p>
    
    <h2>1. Acceptance of Terms</h2>
    <p>By using Legally, you agree to these terms.</p>
    
    <h2>2. Description of Service</h2>
    <p>Legally provides AI-powered legal information based on
    Bharatiya Nyaya Sanhita, 2023 (BNS) for educational purposes.</p>
    
    <h2>3. No Legal Advice</h2>
    <p><strong>IMPORTANT:</strong> Legally does NOT provide legal advice.
    The information provided is for educational purposes only.
    For legal advice, consult a qualified advocate.</p>
    
    <h2>4. User Responsibilities</h2>
    <p>You agree to:</p>
    <ul>
        <li>Use the app lawfully</li>
        <li>Provide accurate information</li>
        <li>Not attempt to hack or abuse the service</li>
    </ul>
    
    <h2>5. Disclaimer</h2>
    <p>We provide information "as is" without warranties.
    We are not liable for any decisions made based on information
    from this app.</p>
    
    <h2>6. Changes to Terms</h2>
    <p>We may update these terms. Continued use constitutes acceptance.</p>
    
    <h2>7. Contact</h2>
    <p>Questions? Contact: support@yourcompany.com</p>
</body>
</html>
```

---

## 🔄 PART 7: Updates & Maintenance

### Releasing Updates

**Backend Updates**:
```bash
cd backend
# Make changes
git add .
git commit -m "Update: description"
git push origin main
vercel --prod
```

**Mobile App Updates**:
1. Make changes in FlutterFlow
2. Increment version number:
   - Version: 1.0.0 → 1.1.0 (features)
   - Version: 1.0.0 → 1.0.1 (bug fixes)
   - Build number: Always increment
3. Build new version
4. Submit to stores
5. Wait for review

**Update BNS Data**:
1. Update `bns_sections.json`
2. Redeploy backend to Vercel
3. No mobile app update needed (data is fetched from backend)

---

## 📊 PART 8: Monitoring & Analytics

### Backend Monitoring

**Vercel Dashboard**:
- Go to your project
- Check **Analytics** tab
- Monitor:
  - Request count
  - Response time
  - Error rate
  - Bandwidth usage

**Set up Alerts**:
- Go to **Settings** → **Notifications**
- Enable alerts for:
  - Deployment failures
  - High error rates
  - Downtime

### Mobile App Analytics

**Firebase Analytics**:
1. In Firebase Console, go to **Analytics**
2. View:
   - Daily active users
   - User engagement
   - Screen views
   - Custom events

**Track Key Metrics**:
```dart
// In FlutterFlow, add custom events:
FirebaseAnalytics.instance.logEvent(
  name: 'ask_ai_query',
  parameters: {'query_length': messageLength}
);

FirebaseAnalytics.instance.logEvent(
  name: 'view_section',
  parameters: {'section_id': sectionId}
);
```

### Crash Reporting

**Firebase Crashlytics**:
1. Enable in Firebase Console
2. In FlutterFlow: **Settings** → **Firebase** → Enable Crashlytics
3. Monitor crashes in Firebase Console

---

## ✅ Post-Deployment Checklist

### Backend
- [✓] Deployed to Vercel
- [ ] Custom domain configured (optional)
- [ ] Environment variables set
- [ ] Monitoring enabled
- [ ] Logs reviewed
- [ ] Performance acceptable

### Mobile App
- [ ] iOS app live on App Store
- [ ] Android app live on Play Store
- [ ] All features working
- [ ] No crashes reported
- [ ] Good user reviews
- [ ] Analytics tracking

### Documentation
- [ ] Privacy policy published
- [ ] Terms of service published
- [ ] Support email active
- [ ] User guide available

### Marketing
- [ ] App Store Optimization (ASO) done
- [ ] Screenshots professional
- [ ] Description compelling
- [ ] Social media announced
- [ ] Website updated

---

## 🎉 CONGRATULATIONS!

Your Legally app is now live in production!

**What you've accomplished**:
✅ Deployed FastAPI backend to Vercel  
✅ Configured Firebase (Auth + Database)  
✅ Built and deployed iOS app  
✅ Built and deployed Android app  
✅ Created privacy policy & terms  
✅ Set up monitoring & analytics

**Next Steps**:
1. Monitor user feedback
2. Fix bugs quickly
3. Plan feature updates
4. Market your app
5. Build user community

---

**END OF DEPLOYMENT GUIDE**

Good luck with your app! 🚀
