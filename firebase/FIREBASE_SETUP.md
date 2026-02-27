# 🔥 Firebase Configuration for Legally App

## ✅ Firebase Project Details

**Project ID**: `legally-c1kjbo`  
**Database URL**: `https://legally-c1kjbo-default-rtdb.firebaseio.com`  
**Auth Domain**: `legally-c1kjbo.firebaseapp.com`  
**Storage Bucket**: `legally-c1kjbo.firebasestorage.app`

---

## 📊 Realtime Database Structure

### 1. Chats Collection

Stores all user conversations with the AI.

```json
{
  "chats": {
    "{uid}": {
      "{chatId}": {
        "messages": [
          {
            "role": "user",
            "content": "What is Section 103 BNS?",
            "timestamp": 1709075400000
          },
          {
            "role": "assistant",
            "content": "Under Section 103 of the Bharatiya Nyaya Sanhita, 2023...",
            "timestamp": 1709075405000
          }
        ],
        "title": "Query about Section 103",
        "createdAt": 1709075400000,
        "updatedAt": 1709075405000
      }
    }
  }
}
```

**Fields**:
- `messages`: Array of message objects
  - `role`: "user" or "assistant"
  - `content`: Message text (max 10,000 chars)
  - `timestamp`: Unix timestamp in milliseconds
- `title`: Chat title (first 50-100 chars of first message)
- `createdAt`: Chat creation timestamp
- `updatedAt`: Last update timestamp

### 2. Users Collection

Stores user profile and preferences.

```json
{
  "users": {
    "{uid}": {
      "email": "user@example.com",
      "displayName": "John Doe",
      "photoURL": "https://...",
      "createdAt": 1709075400000,
      "lastLoginAt": 1709075400000,
      "bookmarks": {
        "103": {
          "section": "103",
          "title": "Punishment for murder",
          "description": "Punishment for murder.",
          "savedAt": 1709075400000
        }
      },
      "stats": {
        "totalQueries": 15,
        "sectionsViewed": 8,
        "daysActive": 5
      }
    }
  }
}
```

**Fields**:
- `email`: User email (required)
- `displayName`: User's display name
- `photoURL`: Profile photo URL (optional)
- `createdAt`: Account creation timestamp
- `lastLoginAt`: Last login timestamp
- `bookmarks`: Saved BNS sections
- `stats`: Usage statistics

---

## 🔒 Security Rules

### Current Rules

The security rules ensure:
1. ✅ Users can only read/write their own data
2. ✅ Authentication is required
3. ✅ Data validation for all fields
4. ✅ Email format validation
5. ✅ Message content length limits

### Apply Security Rules

1. Go to [Firebase Console](https://console.firebase.google.com/project/legally-c1kjbo/database/legally-c1kjbo-default-rtdb/rules)
2. Copy contents from `security-rules.json`
3. Paste in the Rules editor
4. Click **Publish**

---

## 🔐 Authentication Setup

### Enabled Providers

1. **Email/Password** ✅
   - Allow users to sign up with email
   - Password reset available

2. **Google Sign-In** ✅
   - One-tap sign-in
   - Auto-populate user info

### FlutterFlow Authentication Actions

**Sign Up**:
```dart
Action: Authenticate User
Provider: Firebase
Auth Type: Email & Password
Create Account: true
On Success: 
  - Save user to /users/{uid}
  - Navigate to HomePage
```

**Sign In**:
```dart
Action: Authenticate User
Provider: Firebase
Auth Type: Email & Password
On Success: 
  - Update lastLoginAt
  - Navigate to HomePage
```

**Google Sign In**:
```dart
Action: Authenticate User
Provider: Firebase
Auth Type: Google
On Success:
  - Save/Update user to /users/{uid}
  - Navigate to HomePage
```

**Sign Out**:
```dart
Action: Log Out
Provider: Firebase
On Success:
  - Navigate to AuthPage
```

---

## 💾 FlutterFlow Firebase Actions

### Save Chat Message

**When**: User sends message and receives AI response

**Action**: Backend Call → Firebase Realtime Database → Update

**Path**: `/chats/[AuthUID]/[currentChatId]`

**Data**:
```json
{
  "messages": [currentChatMessages],
  "title": [firstMessagePreview],
  "createdAt": [chatCreatedAt],
  "updatedAt": [CurrentTimestamp]
}
```

**Variables Needed**:
- `currentChatId`: Generate with `Timestamp` or UUID
- `currentChatMessages`: App State List<JSON>

### Load Chat History

**When**: User opens History page

**Action**: Backend Call → Firebase Realtime Database → Query Collection

**Path**: `/chats/[AuthUID]`

**Parameters**:
- Order By: `createdAt`
- Order: Descending
- Limit: 50

**Store Result**: `chatHistory` (App State)

### Load Specific Chat

**When**: User taps on a chat in history

**Action**: Backend Call → Firebase Realtime Database → Get Document

**Path**: `/chats/[AuthUID]/[chatId]`

**Store Result**: Page state variable

### Delete Chat

**When**: User deletes a conversation

**Action**: Backend Call → Firebase Realtime Database → Delete Document

**Path**: `/chats/[AuthUID]/[chatId]`

### Bookmark Section

**When**: User bookmarks a BNS section

**Action**: Backend Call → Firebase Realtime Database → Update

**Path**: `/users/[AuthUID]/bookmarks/[sectionId]`

**Data**:
```json
{
  "section": [sectionId],
  "title": [sectionTitle],
  "description": [sectionDescription],
  "savedAt": [CurrentTimestamp]
}
```

### Update User Stats

**When**: User performs actions

**Action**: Backend Call → Firebase Realtime Database → Update

**Path**: `/users/[AuthUID]/stats`

**Data**:
```json
{
  "totalQueries": [increment by 1],
  "sectionsViewed": [increment by 1],
  "daysActive": [calculate from lastLoginAt]
}
```

---

## 🧪 Testing Firebase Setup

### 1. Test in Firebase Console

1. Go to [Realtime Database](https://console.firebase.google.com/project/legally-c1kjbo/database/legally-c1kjbo-default-rtdb/data)
2. Create test data manually:
   ```json
   {
     "chats": {
       "testUser123": {
         "chat001": {
           "messages": [
             {
               "role": "user",
               "content": "Test message",
               "timestamp": 1709075400000
             }
           ],
           "title": "Test Chat",
           "createdAt": 1709075400000,
           "updatedAt": 1709075400000
         }
       }
     }
   }
   ```

### 2. Test Authentication

In FlutterFlow Test Mode:
1. Create test account
2. Sign in
3. Verify UID in Firebase Authentication tab

### 3. Test Chat Saving

1. Send message in AskAIPage
2. Check Firebase Console → Realtime Database
3. Verify data structure matches schema
4. Check `/chats/{uid}/{chatId}`

---

## 📱 FlutterFlow Integration Checklist

### Setup
- [x] Firebase config added to FlutterFlow
- [x] Authentication enabled (Email + Google)
- [x] Realtime Database enabled
- [ ] Security rules published
- [ ] Test authentication flow
- [ ] Test chat saving
- [ ] Test chat loading

### App State Variables

Create these in FlutterFlow:

```dart
// Authentication
String? currentUserId = Auth.uid
String? userName = Auth.displayName
String? userEmail = Auth.email

// Current Chat
List<JSON> currentChatMessages = []
String currentChatId = ""
String messageText = ""
bool isAIResponding = false

// Chat History
List<JSON> chatHistory = []
bool isLoadingHistory = false

// User Data
JSON? userData
```

---

## 🚀 Quick Start Guide

### Step 1: Apply Security Rules

```bash
# Copy security-rules.json content
# Go to Firebase Console → Realtime Database → Rules
# Paste and Publish
```

### Step 2: Test in FlutterFlow

1. **Sign Up**: Create test account
2. **Ask AI**: Send a question
3. **Check Firebase**: Verify chat saved
4. **View History**: Load past chats
5. **Bookmark**: Save a section

### Step 3: Initialize User Profile

On first sign-up, create user document:

**Action**: Backend Call → Firebase Realtime Database → Create Document

**Path**: `/users/[AuthUID]`

**Data**:
```json
{
  "email": [AuthEmail],
  "displayName": [AuthDisplayName],
  "photoURL": [AuthPhotoURL],
  "createdAt": [CurrentTimestamp],
  "lastLoginAt": [CurrentTimestamp],
  "stats": {
    "totalQueries": 0,
    "sectionsViewed": 0,
    "daysActive": 1
  }
}
```

**Trigger**: After successful sign-up

---

## 🔍 Debugging

### Common Issues

**1. Permission Denied**
- Check security rules published
- Verify user is authenticated
- Check UID matches path

**2. Data Not Saving**
- Verify data structure matches rules
- Check field validation
- Look for Firebase errors in console

**3. Data Not Loading**
- Check query path
- Verify user is authenticated
- Check network connection

### Firebase Console Links

- **Authentication**: https://console.firebase.google.com/project/legally-c1kjbo/authentication/users
- **Realtime Database**: https://console.firebase.google.com/project/legally-c1kjbo/database/legally-c1kjbo-default-rtdb/data
- **Rules**: https://console.firebase.google.com/project/legally-c1kjbo/database/legally-c1kjbo-default-rtdb/rules
- **Usage**: https://console.firebase.google.com/project/legally-c1kjbo/usage

---

## 📊 Database Limits (Firebase Free Tier)

- **Concurrent Connections**: 100
- **Storage**: 1 GB
- **Download**: 10 GB/month
- **Bandwidth**: 360 MB/day

**Upgrade to Blaze Plan** if you exceed these limits.

---

## ✅ Verification Checklist

- [x] Firebase project created
- [x] Configuration added to FlutterFlow
- [x] Authentication enabled
- [x] Realtime Database enabled
- [ ] Security rules applied
- [ ] Test account created
- [ ] Chat saving tested
- [ ] Chat loading tested
- [ ] History page tested
- [ ] Bookmarks tested

---

**Your Firebase backend is configured and ready!** 🎉

Apply the security rules and start testing in FlutterFlow.
