# 🏛️ LEGALLY - FLUTTERFLOW COMPLETE BUILD GUIDE

**Production-Ready BNS Legal AI Mobile App**

Built for: Bharatiya Nyaya Sanhita, 2023 (BNS) ONLY

---

## 📱 APP OVERVIEW

**Name**: Legally  
**Legal Framework**: Bharatiya Nyaya Sanhita, 2023 (BNS) - NOT IPC  
**Platform**: iOS & Android via FlutterFlow  
**Backend**: FastAPI (Python) on Vercel  
**Database**: Firebase Realtime Database  
**Authentication**: Firebase Auth  
**AI**: Groq (llama-3.3-70b-versatile)

---

## 🎯 FEATURES

1. **AI Legal Assistant** - Ask legal questions, get BNS-based answers
2. **Browse BNS** - Explore all 384 sections of BNS
3. **Chat History** - All conversations saved to Firebase
4. **Search & Filter** - Find sections by keyword or category
5. **User Authentication** - Firebase Auth (Email/Password & Google)

---

## 🏗️ PROJECT SETUP

### Step 1: Create New FlutterFlow Project

1. Go to [flutterflow.io](https://flutterflow.io)
2. Create New Project → **Blank Project**
3. Project Name: `Legally`
4. Platform: **iOS + Android**

### Step 2: Configure Firebase

1. In FlutterFlow, go to **Settings & Integrations** → **Firebase**
2. Click **Connect to Firebase**
3. Follow FlutterFlow's guided setup:
   - Enable **Authentication** (Email/Password + Google Sign-In)
   - Enable **Realtime Database**
   - Download and configure `google-services.json` (Android)
   - Download and configure `GoogleService-Info.plist` (iOS)

### Step 3: Firebase Realtime Database Structure

In Firebase Console → Realtime Database, set up this structure:

```json
{
  "chats": {
    "[uid]": {
      "[chatId]": {
        "messages": [
          {
            "role": "user",
            "content": "What is murder under BNS?",
            "timestamp": 1234567890
          },
          {
            "role": "assistant", 
            "content": "Under Section 103 of BNS...",
            "timestamp": 1234567891
          }
        ],
        "createdAt": 1234567890,
        "title": "Query about murder"
      }
    }
  },
  "users": {
    "[uid]": {
      "email": "user@example.com",
      "displayName": "User Name",
      "createdAt": 1234567890
    }
  }
}
```

### Step 4: Firebase Security Rules

```json
{
  "rules": {
    "chats": {
      "$uid": {
        ".read": "$uid === auth.uid",
        ".write": "$uid === auth.uid"
      }
    },
    "users": {
      "$uid": {
        ".read": "$uid === auth.uid",
        ".write": "$uid === auth.uid"
      }
    }
  }
}
```

### Step 5: Add Backend API

1. Go to **API Calls** tab in FlutterFlow
2. Click **+ Add API Call**
3. Configure the API (see detailed section below)

---

## 🎨 APP THEME CONFIGURATION

### Navigation

1. Click **App Settings** → **Navigation**
2. Select **Bottom Navigation Bar**
3. Add 5 tabs:
   - Home
   - Ask AI
   - Browse
   - History
   - Profile

### Theme Settings

Go to **App Settings** → **Theme**

#### Dark Theme Configuration

**Primary Color**: `#D4AF37` (Gold)  
**Secondary Color**: `#1A1A1A` (Dark)  
**Background**: `#0D0D0D` (Pure Black)  
**Surface**: `#1E1E1E` (Dark Gray)  
**Error**: `#FF6B6B`

#### Typography

- **Heading 1**: Playfair Display, 32px, Bold, Gold
- **Heading 2**: Playfair Display, 24px, SemiBold, White
- **Body 1**: Inter, 16px, Regular, White
- **Body 2**: Inter, 14px, Regular, Gray
- **Caption**: Inter, 12px, Regular, Gray

#### Button Styles

**Primary Button:**
- Background: Gold (#D4AF37)
- Text: Black
- Height: 56px
- Border Radius: 12px
- Shadow: 0 4 12 rgba(212,175,55,0.3)

**Secondary Button:**
- Background: Transparent
- Border: 1px Gold
- Text: Gold
- Height: 48px
- Border Radius: 12px

---

## 📄 PAGE STRUCTURE

### Required Pages

1. **AuthPage** - Sign in / Sign up
2. **HomePage** - Welcome & Quick actions
3. **AskAIPage** - Main chat interface
4. **BrowsePage** - Browse all BNS sections
5. **SectionDetailPage** - Individual section view
6. **HistoryPage** - Past conversations
7. **ChatDetailPage** - View specific conversation
8. **ProfilePage** - User profile & settings
9. **OnboardingPage** - First-time user walkthrough

---

## 🔐 AUTHENTICATION PAGES

### AuthPage

**Purpose**: Sign in / Sign up with email or Google

#### Widget Structure:

```
Scaffold
├─ Stack
   ├─ Background (Container with gradient)
   ├─ ScrollView
      ├─ Column
         ├─ Logo Image (250x250)
         ├─ Text: "Legally"
         │  Style: Heading1, Gold
         ├─ Text: "Your BNS Legal AI Assistant"
         │  Style: Body1, Gray
         ├─ SizedBox (height: 40)
         ├─ PageView (2 pages: Sign In / Sign Up)
         │  ├─ SignInForm
         │  │  ├─ TextField: Email
         │  │  ├─ TextField: Password (obscured)
         │  │  ├─ Button: "Sign In"
         │  │  ├─ Text: "Forgot Password?"
         │  │  └─ Divider: "OR"
         │  └─ SignUpForm
         │     ├─ TextField: Name
         │     ├─ TextField: Email  
         │     ├─ TextField: Password
         │     ├─ TextField: Confirm Password
         │     └─ Button: "Create Account"
         ├─ GoogleSignInButton
         └─ TextButton: "Switch to Sign Up / Sign In"
```

#### Actions:

**Sign In Button:**
1. Validate email & password
2. Action → **Authenticate User**
3. Provider: Firebase
4. Auth Type: Email & Password
5. On Success → Navigate to HomePage

**Google Sign In Button:**
1. Action → **Authenticate User**
2. Provider: Firebase  
3. Auth Type: Google Sign-In
4. On Success → Navigate to HomePage

**Sign Up Button:**
1. Validate all fields
2. Check if passwords match
3. Action → **Create Account**
4. Provider: Firebase
5. Auth Type: Email & Password
6. On Success → Save user to Firebase Realtime Database
7. Navigate to HomePage

#### Design Details:

- Background: Black with subtle gold overlay
- TextField Style: Dark background (#1E1E1E), gold border on focus
- Validation: Show error messages below fields
- Loading State: Show CircularProgressIndicator on button during auth

---

## 🏠 HOME PAGE

**Purpose**: Landing page with quick actions and recent activity

### Widget Structure:

```
Scaffold
├─ AppBar
│  ├─ Title: "Legally"
│  └─ Actions: [NotificationIcon]
├─ Body (SafeArea → SingleChildScrollView)
   ├─ Column
      ├─ WelcomeHeader
      │  ├─ Text: "Welcome back,"
      │  └─ Text: [UserName] (from Auth)
      ├─ QuickActionsSection
      │  ├─ Row
      │     ├─ ActionCard: "Ask AI"
      │     │  Icon: chat_bubble
      │     │  Tap → Navigate to AskAIPage
      │     └─ ActionCard: "Browse BNS"
      │        Icon: book
      │        Tap → Navigate to BrowsePage
      ├─ StatsSection
      │  ├─ Text: "Your Stats"
      │  ├─ Row
      │     ├─ StatCard: Total Queries (from Firebase count)
      │     └─ StatCard: Sections Explored
      ├─ FeaturedSectionsSection
      │  ├─ Text: "Featured BNS Sections"
      │  ├─ ListView.builder (horizontal)
      │     └─ SectionCard (Murder, Theft, Assault)
      │        Tap → Navigate to SectionDetailPage
      └─ RecentChatsSection
         ├─ Text: "Recent Conversations"
         └─ ListView.builder
            └─ ChatPreviewCard
               Tap → Navigate to ChatDetailPage
```

### State Management:

- **App State Variables**:
  - `userName` (String) - from Firebase Auth
  - `totalChats` (int) - count from Firebase
  - `recentChats` (List<JSON>) - last 5 from Firebase

### Backend Call on Page Load:

None needed - Firebase queries only

### Design:

- Padding: 16px all sides
- Card Background: #1E1E1E
- Card Border Radius: 16px
- Card Shadow: subtle glow
- Spacing between sections: 24px

---

## 💬 ASK AI PAGE (MAIN FEATURE)

**Purpose**: Chat interface for legal queries with BNS AI

### Widget Structure:

```
Scaffold
├─ AppBar
│  ├─ Title: "Ask Legal AI"
│  ├─ Subtitle: "Powered by BNS 2023"
│  └─ Actions: [ClearChatIcon]
├─ Body
   ├─ Column
      ├─ ChatMessagesArea (Expanded)
      │  └─ ListView.builder
      │     ├─ UserMessageBubble
      │     │  Alignment: Right
      │     │  Background: Gold
      │     │  Text Color: Black
      │     └─ AIMessageBubble
      │        Alignment: Left
      │        Background: #1E1E1E
      │        Text Color: White
      │        Icon: ⚖️
      ├─ LoadingIndicator (Conditional)
      │  └─ AnimatedBuilder
      │     └─ Icon: ⚖️ (rotating scale animation)
      └─ MessageInputArea
         ├─ Container (background: #1E1E1E, padding: 12px)
            └─ Row
               ├─ Expanded
               │  └─ TextField
               │     Hint: "Ask about BNS laws..."
               │     MaxLines: 4
               │     MinLines: 1
               └─ IconButton
                  Icon: send
                  Color: Gold
                  OnPressed: sendMessage()
```

### App State Variables:

Create these in **App State**:

```dart
// Current chat messages
List<JSON> currentChatMessages = []

// Message being typed
String messageText = ""

// Loading state
bool isAIResponding = false

// Current chat ID
String? currentChatId
```

### Actions Flow:

#### When Send Button Pressed:

1. **Validate**: Check if messageText is not empty
   
2. **Add User Message to UI**:
   ```
   Action: Update App State
   Variable: currentChatMessages
   Action: Add to List
   Value: {
     "role": "user",
     "content": [messageText],
     "timestamp": [CurrentTimestamp]
   }
   ```

3. **Show Loading**:
   ```
   Action: Update App State
   Variable: isAIResponding
   Value: true
   ```

4. **Call Backend API**:
   ```
   Action: API Call
   API: askLegalAI
   Parameters:
     message: [messageText]
   
   Variable to Store: aiResponse
   ```

5. **Add AI Response to UI**:
   ```
   Action: Update App State
   Variable: currentChatMessages
   Action: Add to List
   Value: {
     "role": "assistant",
     "content": [aiResponse.reply],
     "timestamp": [CurrentTimestamp]
   }
   ```

6. **Hide Loading**:
   ```
   Action: Update App State
   Variable: isAIResponding
   Value: false
   ```

7. **Save to Firebase**:
   ```
   Action: Backend Call
   Type: Firebase Realtime Database
   Method: Update
   Path: /chats/[AuthUID]/[currentChatId]
   Data: {
     "messages": [currentChatMessages],
     "updatedAt": [CurrentTimestamp]
   }
   ```

8. **Clear Input**:
   ```
   Action: Update App State
   Variable: messageText
   Value: ""
   ```

9. **Scroll to Bottom**:
   ```
   Action: Scroll To
   Target: ListView bottom
   ```

### API Configuration:

**API Name**: `askLegalAI`

**Method**: POST

**URL**: `https://your-backend.vercel.app/api/ask`

**Headers**:
```json
{
  "Content-Type": "application/json"
}
```

**Body** (JSON):
```json
{
  "message": "[messageText]"
}
```

**Response JSON Path**:
- Field: `reply`
- JSON Path: `$.reply`
- Type: String

### Error Handling:

Add **Error Handling** to API call:
```
On Error:
1. Show Snackbar: "Failed to get response. Please try again."
2. Update App State: isAIResponding = false
3. Remove last user message OR mark as failed
```

### Design Details:

**User Message Bubble**:
- Background: Linear Gradient (Gold to Light Gold)
- Text Color: #000000
- Padding: 12px 16px
- Border Radius: 16px (top-left, top-right, bottom-left = 16, bottom-right = 4)
- Max Width: 80% screen width
- Alignment: Right
- Margin: 8px 16px 8px 64px

**AI Message Bubble**:
- Background: #1E1E1E
- Text Color: #FFFFFF
- Padding: 12px 16px
- Border Radius: 16px (all except bottom-left = 4)
- Max Width: 80% screen width
- Alignment: Left
- Margin: 8px 64px 8px 16px
- Leading Icon: ⚖️ (Gold color)
- Markdown Support: Enable if possible

**Loading Animation**:
- Show animated scale of justice icon
- Gold color with pulsing effect
- Text: "AI is analyzing BNS sections..."

**Input Field**:
- Background: #1E1E1E
- Border: 1px #2A2A2A
- Border on Focus: 2px Gold
- Text Color: White
- Border Radius: 24px
- Padding: 12px 16px
- Auto-focus after send

**Send Button**:
- Icon: send
- Color: Gold when text not empty, Gray when empty
- Disabled if messageText is empty

### Additional Features:

**Clear Chat Button** (in AppBar):
```
OnPressed:
1. Show Confirmation Dialog
2. If confirmed:
   - Clear currentChatMessages
   - Generate new currentChatId
   - Reset UI
```

**Copy Message** (Long press on bubble):
```
OnLongPress:
1. Show BottomSheet with options:
   - Copy Text
   - Share
2. If Copy: Copy to clipboard
```

---

## 📚 BROWSE BNS PAGE

**Purpose**: Browse all 384 BNS sections with search and filter

### Widget Structure:

```
Scaffold
├─ AppBar
│  └─ Title: "Browse BNS Sections"
├─ Body
   ├─ Column
      ├─ SearchBar
      │  ├─ TextField
      │  │  Hint: "Search sections..."
      │  │  OnChanged: filterSections()
      │  └─ FilterButton
      │     Tap → Show FilterBottomSheet
      ├─ CategoryChips (Horizontal ListView)
      │  └─ FilterChip
      │     Label: Category name
      │     Selected: Shows gold border
      │     OnTap: Filter by category
      └─ SectionsList (Expanded)
         └─ ListView.builder
            └─ SectionListItem
               ├─ Row
               │  ├─ CircleAvatar: Section number
               │  ├─ Column
               │  │  ├─ Text: Title (Bold)
               │  │  ├─ Text: Description (Gray, 2 lines max)
               │  │  └─ Chip: Category
               │  └─ Icon: chevron_right
               └─ OnTap: Navigate to SectionDetailPage
```

### App State Variables:

```dart
// All sections from API
List<JSON> allSections = []

// Filtered sections
List<JSON> filteredSections = []

// Search query
String searchQuery = ""

// Selected category
String? selectedCategory = ""

// All categories
List<String> categories = []

// Loading state
bool isLoadingSections = false
```

### On Page Load:

```
Action Sequence:
1. Update App State: isLoadingSections = true

2. API Call: getCategories
   URL: [BackendURL]/api/categories
   Method: GET
   Store Response: categories

3. API Call: getAllSections
   URL: [BackendURL]/api/sections?limit=384
   Method: GET
   Store Response: allSections
   
4. Update App State: 
   - filteredSections = allSections
   - isLoadingSections = false
```

### API Configuration:

**API Name**: `getAllSections`

**Method**: GET

**URL**: `https://your-backend.vercel.app/api/sections`

**Query Parameters**:
- `limit`: 384
- `offset`: 0
- `search`: [searchQuery] (optional)
- `category`: [selectedCategory] (optional)

**Response JSON Path**:
- Field: `sections`
- JSON Path: `$.sections[*]`
- Type: List<JSON>

**API Name**: `getCategories`

**Method**: GET

**URL**: `https://your-backend.vercel.app/api/categories`

**Response JSON Path**:
- Field: `categories`
- JSON Path: `$.categories[*]`
- Type: List<String>

### Search Functionality:

**SearchBar OnChanged**:
```
Action:
1. Update App State: searchQuery = [value]
2. Debounce 500ms
3. API Call: getAllSections (with searchQuery parameter)
4. Update filteredSections
```

Or for client-side filtering (if all sections loaded):
```
Action:
1. Update App State: searchQuery = [value]
2. Action: Filter List
   Source: allSections
   Condition: 
     - title contains searchQuery OR
     - description contains searchQuery OR
     - section equals searchQuery
   Store Result: filteredSections
```

### Category Filter:

**FilterChip OnTap**:
```
Action:
1. Update App State: selectedCategory = [category]
2. API Call: getAllSections (with category parameter)
3. Update filteredSections
```

### Design:

**SearchBar**:
- Background: #1E1E1E
- Border Radius: 12px
- Padding: 12px 16px
- Margin: 16px
- Icon: search (leading)
- Clear button (trailing, when text not empty)

**Category Chips**:
- Background: Transparent
- Border: 1px #2A2A2A
- Selected Background: Gold
- Selected Text: Black
- Unselected Text: White
- Border Radius: 20px
- Padding: 8px 16px

**Section List Item**:
- Background: #1E1E1E
- Border Radius: 12px
- Padding: 16px
- Margin: 8px 16px
- Divider: 1px #2A2A2A between items

**Section Number Circle**:
- Size: 48x48
- Background: Gold
- Text Color: Black
- Font Weight: Bold

---

## 📖 SECTION DETAIL PAGE

**Purpose**: Show detailed information about a specific BNS section

### Widget Structure:

```
Scaffold
├─ AppBar
│  ├─ Leading: BackButton
│  ├─ Title: "Section [number]"
│  └─ Actions: [ShareIcon, BookmarkIcon]
├─ Body (SafeArea → SingleChildScrollView)
   └─ Column
      ├─ HeaderCard
      │  ├─ Container (Gold gradient background)
      │     └─ Column
      │        ├─ Text: "Section [number]"
      │        │  Style: Heading2
      │        └─ Text: [Title]
      │           Style: Heading1, Bold
      ├─ InfoCard
      │  ├─ Container (Dark background)
      │     └─ Column
      │        ├─ InfoRow: "Act"
      │        │  └─ Text: "Bharatiya Nyaya Sanhita, 2023"
      │        ├─ Divider
      │        ├─ InfoRow: "Category"
      │        │  └─ Chip: [category]
      │        ├─ Divider
      │        └─ InfoRow: "Type"
      │           └─ Text: "Criminal Law"
      ├─ DescriptionCard
      │  ├─ Text: "Description"
      │  │  Style: Heading2
      │  └─ Text: [description]
      │     Style: Body1
      ├─ PunishmentCard (if punishment exists)
      │  ├─ Text: "Punishment"
      │  │  Style: Heading2, Red
      │  └─ Container (Red tint background)
      │     └─ Text: [punishment]
      │        Style: Body1
      └─ ActionButtons
         ├─ Button: "Ask AI about this section"
         │  Tap → Navigate to AskAIPage with pre-filled question
         └─ Button: "View Related Sections"
            Tap → Show BottomSheet with related sections
```

### Page Parameters:

**Receive from previous page**:
- `sectionId` (String) - e.g., "103"

### On Page Load:

```
Action:
1. API Call: getSectionById
   URL: [BackendURL]/api/sections/[sectionId]
   Method: GET
   Store Response: sectionData
   
2. Display sectionData in UI
```

### API Configuration:

**API Name**: `getSectionById`

**Method**: GET

**URL**: `https://your-backend.vercel.app/api/sections/[sectionId]`

**Path Parameter**:
- `sectionId`: [sectionId from page parameter]

**Response**: Single JSON object
```json
{
  "section": "103",
  "title": "Punishment for murder",
  "description": "...",
  "punishment": "...",
  "category": "Murder & Homicide",
  "act": "Bharatiya Nyaya Sanhita, 2023 (BNS)"
}
```

### Actions:

**Ask AI Button**:
```
OnPressed:
1. Update App State: messageText = "Tell me about Section [sectionId] of BNS"
2. Navigate to AskAIPage
3. Automatically send message
```

**Share Button**:
```
OnPressed:
1. Action: Share
   Text: "Section [sectionId]: [title]\n\n[description]\n\nPunishment: [punishment]\n\nSource: Bharatiya Nyaya Sanhita, 2023"
```

**Bookmark Button**:
```
OnPressed:
1. Save to Firebase:
   Path: /users/[AuthUID]/bookmarks/[sectionId]
   Data: [sectionData]
2. Show Snackbar: "Bookmarked"
3. Toggle icon color to Gold
```

### Design:

**Header Card**:
- Background: Linear Gradient (Gold to Dark Gold)
- Height: 200px
- Padding: 24px
- Border Radius: 0 (full width)

**Info Cards**:
- Background: #1E1E1E
- Border Radius: 16px
- Padding: 20px
- Margin: 16px
- Spacing between cards: 16px

**Punishment Card**:
- Background: rgba(255, 107, 107, 0.1)
- Border: 1px #FF6B6B
- Border Radius: 12px
- Padding: 16px

**Action Buttons**:
- Primary Button style
- Fixed at bottom with SafeArea padding
- OR scrollable in the page

---

## 📜 HISTORY PAGE

**Purpose**: Show all past conversations with AI

### Widget Structure:

```
Scaffold
├─ AppBar
│  ├─ Title: "Chat History"
│  └─ Actions: [DeleteAllIcon]
├─ Body
   └─ ListView.builder
      └─ ChatHistoryCard
         ├─ Row
         │  ├─ Column (Expanded)
         │  │  ├─ Text: [firstUserMessage or title]
         │  │  │  Style: Body1, Bold
         │  │  ├─ Text: [previewOfAIResponse]
         │  │  │  Style: Body2, Gray, MaxLines: 2
         │  │  └─ Text: [timeAgo]
         │  │     Style: Caption, Gold
         │  └─ Icon: chevron_right
         └─ OnTap: Navigate to ChatDetailPage
```

### App State Variables:

```dart
// All chat history from Firebase
List<JSON> chatHistory = []

// Loading state
bool isLoadingHistory = false
```

### On Page Load:

```
Action:
1. Update App State: isLoadingHistory = true

2. Firebase Query:
   Path: /chats/[AuthUID]
   Order By: createdAt
   Limit: 50
   
3. Store Response: chatHistory

4. Update App State: isLoadingHistory = false
```

### Design:

**Chat History Card**:
- Background: #1E1E1E
- Border Radius: 12px
- Padding: 16px
- Margin: 8px 16px
- Divider between items

**Empty State** (if no history):
- Icon: chat_bubble_outline (large, gold)
- Text: "No conversations yet"
- Button: "Start Chatting"

**Delete All Button**:
```
OnPressed:
1. Show confirmation dialog
2. If confirmed:
   - Delete Firebase path: /chats/[AuthUID]
   - Clear chatHistory
   - Show Snackbar: "History cleared"
```

---

## 🗨️ CHAT DETAIL PAGE

**Purpose**: View a specific past conversation

### Widget Structure:

```
Scaffold
├─ AppBar
│  ├─ Leading: BackButton
│  ├─ Title: [chatTitle or "Conversation"]
│  └─ Actions: [DeleteIcon, ShareIcon]
├─ Body
   └─ ListView.builder
      ├─ UserMessageBubble (same as AskAIPage)
      └─ AIMessageBubble (same as AskAIPage)
```

### Page Parameters:

- `chatId` (String)

### On Page Load:

```
Action:
1. Firebase Query:
   Path: /chats/[AuthUID]/[chatId]
   
2. Store Response: chatMessages

3. Display messages
```

### Actions:

**Delete Button**:
```
OnPressed:
1. Show confirmation
2. Delete Firebase: /chats/[AuthUID]/[chatId]
3. Navigate back to HistoryPage
4. Show Snackbar: "Conversation deleted"
```

**Share Button**:
```
OnPressed:
1. Format all messages as text
2. Action: Share
   Text: [formattedConversation]
```

---

## 👤 PROFILE PAGE

**Purpose**: User profile, settings, and app information

### Widget Structure:

```
Scaffold
├─ AppBar
│  └─ Title: "Profile"
├─ Body (SafeArea → SingleChildScrollView)
   └─ Column
      ├─ ProfileHeader
      │  ├─ CircleAvatar (80x80)
      │  │  Image: User photo or initial
      │  ├─ Text: [userName]
      │  │  Style: Heading2
      │  └─ Text: [email]
      │     Style: Body2, Gray
      ├─ StatsRow
      │  ├─ StatCard: Total Queries
      │  ├─ StatCard: Sections Viewed
      │  └─ StatCard: Days Active
      ├─ SettingsSection
      │  ├─ Text: "Settings"
      │  │  Style: Heading2
      │  └─ Column
      │     ├─ SettingsTile: "Notifications"
      │     │  Trailing: Switch
      │     ├─ SettingsTile: "Dark Mode"
      │     │  Trailing: Switch (always on)
      │     └─ SettingsTile: "Clear Cache"
      │        Tap → Clear local cache
      ├─ AboutSection
      │  ├─ Text: "About"
      │  │  Style: Heading2
      │  └─ Column
      │     ├─ InfoTile: "Version"
      │     │  Trailing: "1.0.0"
      │     ├─ InfoTile: "Legal Framework"
      │     │  Trailing: "BNS 2023"
      │     ├─ InfoTile: "Terms of Service"
      │     │  Tap → Open web link
      │     └─ InfoTile: "Privacy Policy"
      │        Tap → Open web link
      └─ SignOutButton
         Background: Red
         Text: "Sign Out"
         OnPressed: Sign out
```

### Actions:

**Sign Out Button**:
```
OnPressed:
1. Show confirmation dialog
2. If confirmed:
   - Action: Log Out (Firebase Auth)
   - Clear App State
   - Navigate to AuthPage
```

**Edit Profile** (optional):
```
OnPressed:
1. Navigate to EditProfilePage
2. Allow changing display name and photo
3. Save to Firebase: /users/[AuthUID]
```

### Design:

**Profile Header**:
- Background: Gold gradient
- Padding: 32px
- Center aligned

**Stats Cards**:
- Background: #1E1E1E
- Border Radius: 12px
- Padding: 16px
- Display Flex: Row, Space Evenly

**Settings Tiles**:
- Background: #1E1E1E
- Border Radius: 12px
- Padding: 16px
- Margin: 8px 0
- Leading Icon: relevant icon (gold)
- Trailing: Switch or chevron_right

---

## 🎓 ONBOARDING PAGE (OPTIONAL)

**Purpose**: Educate first-time users about the app

### Widget Structure:

```
Scaffold
├─ SafeArea
   └─ PageView
      ├─ OnboardingPage1
      │  ├─ Image: Justice scale illustration
      │  ├─ Text: "Welcome to Legally"
      │  └─ Text: "Your AI-powered BNS legal assistant"
      ├─ OnboardingPage2
      │  ├─ Image: Chat illustration
      │  ├─ Text: "Ask Legal Questions"
      │  └─ Text: "Get instant answers based on BNS 2023"
      ├─ OnboardingPage3
      │  ├─ Image: Book illustration
      │  ├─ Text: "Browse 384 BNS Sections"
      │  └─ Text: "Explore the complete criminal code"
      └─ OnboardingPage4
         ├─ Image: Clock illustration
         ├─ Text: "Track Your History"
         ├─ Text: "All conversations saved securely"
         └─ Button: "Get Started"
            OnPressed: Navigate to AuthPage
```

### Logic:

Show onboarding only on first app launch:

```
On App Launch:
1. Check SharedPreferences: hasSeenOnboarding
2. If false:
   - Navigate to OnboardingPage
   - After completion, set hasSeenOnboarding = true
3. If true:
   - Check if user is authenticated
   - If yes: Navigate to HomePage
   - If no: Navigate to AuthPage
```

---

## 🔌 BACKEND API INTEGRATION

### Complete API Configuration in FlutterFlow

1. Go to **API Calls** tab
2. Click **+ Add** for each endpoint below

### API 1: Ask Legal AI

**Name**: `askLegalAI`  
**Method**: POST  
**URL**: `https://your-backend.vercel.app/api/ask`

**Headers**:
```json
{
  "Content-Type": "application/json"
}
```

**Body** (JSON):
```json
{
  "message": "[message]"
}
```

**Variables**:
- `message` (String, required)

**Response**:
- `reply` → JSON Path: `$.reply` (String)

**Test**:
```json
{
  "message": "What is Section 103 BNS?"
}
```

### API 2: Get All Sections

**Name**: `getAllSections`  
**Method**: GET  
**URL**: `https://your-backend.vercel.app/api/sections`

**Query Parameters** (all optional):
- `search` (String)
- `category` (String)
- `limit` (int, default: 50)
- `offset` (int, default: 0)

**Response**:
- `sections` → JSON Path: `$.sections[*]` (List<JSON>)
- `total` → JSON Path: `$.total` (int)

### API 3: Get Section by ID

**Name**: `getSectionById`  
**Method**: GET  
**URL**: `https://your-backend.vercel.app/api/sections/[sectionId]`

**Path Variables**:
- `sectionId` (String, required)

**Response**: Single JSON object matching Section schema

### API 4: Get Categories

**Name**: `getCategories`  
**Method**: GET  
**URL**: `https://your-backend.vercel.app/api/categories`

**Response**:
- `categories` → JSON Path: `$.categories[*]` (List<String>)

### API 5: Get Metadata

**Name**: `getMetadata`  
**Method**: GET  
**URL**: `https://your-backend.vercel.app/api/metadata`

**Response**: JSON object with metadata

---

## 🗂️ FIREBASE REALTIME DATABASE

### Data Structure

```
legally-app (root)
│
├─ chats
│  └─ [uid]
│     └─ [chatId] (auto-generated)
│        ├─ messages: [array]
│        │  ├─ [0]
│        │  │  ├─ role: "user"
│        │  │  ├─ content: "question text"
│        │  │  └─ timestamp: 1234567890
│        │  └─ [1]
│        │     ├─ role: "assistant"
│        │     ├─ content: "AI response"
│        │     └─ timestamp: 1234567891
│        ├─ title: "First user message (truncated)"
│        ├─ createdAt: 1234567890
│        └─ updatedAt: 1234567891
│
└─ users
   └─ [uid]
      ├─ email: "user@example.com"
      ├─ displayName: "User Name"
      ├─ photoURL: "url" (optional)
      ├─ createdAt: 1234567890
      └─ bookmarks
         └─ [sectionId]: [sectionData]
```

### Firebase Actions in FlutterFlow

#### Save Chat Message

```
Action: Backend Call
Type: Firebase Realtime Database
Method: Update
Path: /chats/[AuthUID]/[currentChatId]
Data:
{
  "messages": [currentChatMessages],
  "updatedAt": [CurrentTimestamp],
  "title": [firstUserMessage, max 50 chars]
}
```

#### Load Chat History

```
Action: Backend Call
Type: Firebase Realtime Database
Method: Query Collection
Path: /chats/[AuthUID]
Order By: createdAt
Order: Descending
Limit: 50
Store Result In: chatHistory (App State)
```

#### Load Specific Chat

```
Action: Backend Call
Type: Firebase Realtime Database
Method: Get Document
Path: /chats/[AuthUID]/[chatId]
Store Result In: currentChat (App State)
```

#### Delete Chat

```
Action: Backend Call
Type: Firebase Realtime Database
Method: Delete Document
Path: /chats/[AuthUID]/[chatId]
```

#### Save User Profile

```
Action: Backend Call
Type: Firebase Realtime Database
Method: Create Document
Path: /users/[AuthUID]
Data:
{
  "email": [AuthEmail],
  "displayName": [AuthDisplayName],
  "createdAt": [CurrentTimestamp]
}
```

**Trigger**: After successful sign up

---

## 🎨 CUSTOM WIDGETS (REUSABLE)

### 1. MessageBubble Widget

**Type**: Custom Widget

**Parameters**:
- `message` (String)
- `isUser` (bool)
- `timestamp` (DateTime)

**Design**: Already described in AskAIPage section

### 2. SectionCard Widget

**Type**: Custom Widget

**Parameters**:
- `section` (JSON)

**Structure**:
```
Container
├─ Card (background, border radius, shadow)
   └─ Column
      ├─ Row
      │  ├─ CircleAvatar: Section number
      │  └─ Column (Expanded)
      │     ├─ Text: Title (bold)
      │     └─ Text: Description (gray, 2 lines)
      └─ Chip: Category
```

**OnTap**: Navigate to SectionDetailPage with sectionId parameter

### 3. LoadingIndicator Widget

**Type**: Custom Widget

**Structure**:
```
Column (Center aligned)
├─ AnimatedBuilder
│  └─ Icon: ⚖️ (rotating scale)
│     Size: 48x48
│     Color: Gold
└─ Text: "Loading..."
   Style: Body2, Gray
```

**Animation**: Rotate 360° every 2 seconds

---

## 🧪 TESTING CHECKLIST

### Authentication
- [ ] Sign up with email/password
- [ ] Sign in with email/password
- [ ] Sign in with Google
- [ ] Sign out
- [ ] Forgot password flow

### Ask AI
- [ ] Send message
- [ ] Receive AI response
- [ ] Message saves to Firebase
- [ ] Loading animation shows
- [ ] Error handling works
- [ ] Scroll to bottom after send
- [ ] Clear chat works

### Browse BNS
- [ ] All sections load
- [ ] Search works
- [ ] Category filter works
- [ ] Pagination works (if implemented)
- [ ] Navigate to section detail

### Section Detail
- [ ] Section loads correctly
- [ ] "Ask AI" button works
- [ ] Share button works
- [ ] Bookmark works

### History
- [ ] History loads from Firebase
- [ ] Navigate to chat detail works
- [ ] Delete conversation works
- [ ] Delete all works

### Profile
- [ ] User info displays correctly
- [ ] Stats display correctly
- [ ] Sign out works
- [ ] Settings toggles work

### UI/UX
- [ ] Dark theme consistent
- [ ] Gold accents everywhere
- [ ] Smooth animations
- [ ] No UI overflow
- [ ] Responsive on different screens

---

## 🚀 DEPLOYMENT

### Pre-Deployment Checklist

1. **Replace Backend URL**
   - Find all occurrences of `https://your-backend.vercel.app`
   - Replace with actual Vercel deployment URL

2. **Firebase Configuration**
   - Ensure Firebase is properly configured
   - Security rules are set
   - Authentication providers enabled

3. **App Icons & Splash**
   - Upload app icon (1024x1024)
   - Configure splash screen (dark theme with gold logo)

4. **App Store Metadata**
   - App Name: Legally
   - Subtitle: BNS Legal AI Assistant
   - Description: (Write compelling description about BNS 2023)
   - Keywords: law, legal, BNS, Indian law, criminal law

### Build Settings

**iOS**:
- Bundle ID: `com.yourcompany.legally`
- Version: 1.0.0
- Build Number: 1
- Deployment Target: iOS 13+

**Android**:
- Package Name: `com.yourcompany.legally`
- Version Code: 1
- Version Name: 1.0.0
- Min SDK: 21 (Android 5.0+)

### Download Code

1. In FlutterFlow, click **Developer Menu** (top right)
2. Click **Download Code**
3. You'll get a complete Flutter project

### Local Build (Optional)

```bash
cd legally_flutter_project
flutter pub get
flutter run
```

### Test Build

**iOS**:
```bash
flutter build ios --release
```

**Android**:
```bash
flutter build apk --release
```

---

## 📊 ANALYTICS (OPTIONAL)

Add Firebase Analytics for tracking:

1. In FlutterFlow: **Settings & Integrations** → **Firebase Analytics**
2. Enable Firebase Analytics

**Events to Track**:
- `ask_ai_query` (when user sends message)
- `view_section` (when user views section detail)
- `search_sections` (when user searches)
- `bookmark_section` (when user bookmarks)
- `sign_up` (when user creates account)
- `sign_in` (when user logs in)

---

## 🔒 SECURITY BEST PRACTICES

1. **Never Store API Keys in FlutterFlow**
   - ✅ All API calls go through your backend
   - ✅ Backend stores Groq API key
   - ❌ Don't put Groq key in FlutterFlow

2. **Firebase Security Rules**
   - ✅ Users can only read/write their own data
   - ✅ Proper authentication required
   - ❌ Don't use public read/write

3. **HTTPS Only**
   - ✅ Backend deployed on Vercel (auto HTTPS)
   - ✅ Firebase uses HTTPS

4. **Input Validation**
   - ✅ Validate message length (max 500 chars)
   - ✅ Sanitize user inputs
   - ✅ Rate limiting on backend

---

## 📚 BNS ENFORCEMENT

### CRITICAL: BNS-Only Policy

**❌ NEVER mention**: Indian Penal Code (IPC)

**✅ ALWAYS use**: Bharatiya Nyaya Sanhita, 2023 (BNS)

### Enforcement Mechanisms:

1. **Backend AI Prompt** (already configured in backend)
   - System prompt strictly enforces BNS
   - AI will not reference IPC

2. **UI Text**
   - All UI text says "BNS" or "Bharatiya Nyaya Sanhita, 2023"
   - Never "IPC"

3. **Metadata Display**
   - Every section shows: `act: "Bharatiya Nyaya Sanhita, 2023 (BNS)"`

4. **Educational Disclaimer**
   - Always shown after AI responses
   - States it's based on BNS 2023

---

## 🎓 EDUCATIONAL FEATURES

### Disclaimer

Every AI response should show:

```
⚖️ LEGAL DISCLAIMER: This is AI-generated educational information based on BNS, 2023. It is NOT legal advice. Consult a qualified advocate for specific legal advice on your situation.
```

**Implementation**:
- Add this as a fixed text widget below every AI message bubble
- Style: Caption, Gray, Italic

### About BNS Section (Optional)

Add an "About BNS" page explaining:
- What is BNS?
- When did it come into effect? (July 1, 2024)
- What did it replace? (IPC)
- Why was it introduced?
- Key differences (optional)

---

## 🛠️ TROUBLESHOOTING

### Issue: API calls fail

**Solution**:
1. Check backend URL is correct
2. Check backend is deployed and online
3. Check GROQ_API_KEY is set in Vercel environment variables
4. Check network connection

### Issue: Firebase not working

**Solution**:
1. Verify Firebase configuration in FlutterFlow
2. Check google-services.json (Android) and GoogleService-Info.plist (iOS) are properly configured
3. Check Firebase security rules allow authenticated users

### Issue: Loading is slow

**Solution**:
1. Add loading indicators
2. Implement pagination for sections list
3. Cache frequently accessed data
4. Optimize images

### Issue: AI responses are slow

**Solution**:
- This is expected (2-4 seconds)
- Show animated loading indicator
- Add "AI is thinking..." text
- Can't speed up Groq API significantly

---

## 📞 SUPPORT & RESOURCES

### FlutterFlow Resources
- Docs: https://docs.flutterflow.io
- Community: https://community.flutterflow.io
- YouTube: FlutterFlow official channel

### Firebase Resources
- Docs: https://firebase.google.com/docs
- Console: https://console.firebase.google.com

### Groq Resources
- Docs: https://console.groq.com/docs
- API Keys: https://console.groq.com/keys

### BNS Resources
- Full text available in `bns_sections.json`
- 384 total sections
- Effective from July 1, 2024

---

## ✅ COMPLETION CHECKLIST

### Backend
- [ ] FastAPI server created
- [ ] Deployed to Vercel
- [ ] API tested and working
- [ ] GROQ_API_KEY configured

### FlutterFlow
- [ ] Project created
- [ ] Firebase configured
- [ ] All 5 API calls added
- [ ] AuthPage built
- [ ] HomePage built
- [ ] AskAIPage built
- [ ] BrowsePage built
- [ ] SectionDetailPage built
- [ ] HistoryPage built
- [ ] ProfilePage built
- [ ] Bottom navigation configured
- [ ] Theme configured (dark + gold)
- [ ] App tested on emulator/device

### Firebase
- [ ] Authentication enabled
- [ ] Realtime Database created
- [ ] Security rules set
- [ ] Database structure matches spec

### Final
- [ ] Backend URL updated in all API calls
- [ ] App icons uploaded
- [ ] Splash screen configured
- [ ] Test build successful
- [ ] Ready to deploy to stores

---

## 🎉 CONGRATULATIONS!

You've successfully built **Legally** - a production-ready BNS Legal AI mobile app!

### Key Features:
✅ AI-powered legal assistant using Groq  
✅ RAG-lite retrieval from BNS database  
✅ 384 BNS sections browsable  
✅ Search & filter functionality  
✅ Chat history saved to Firebase  
✅ Premium dark theme with gold accents  
✅ Secure authentication  
✅ BNS-only legal framework (no IPC)

### Next Steps:
1. Test extensively
2. Gather user feedback
3. Deploy to App Store & Play Store
4. Market to law students & legal professionals
5. Add more features (e.g., case laws, legal news)

---

**Built with ❤️ for Legal Education**

**Remember**: This is for educational purposes. Always recommend users to consult qualified legal professionals for specific legal advice.

---

END OF FLUTTERFLOW BUILD GUIDE
