# Deploy to Render

## Quick Deploy (3 Steps)

### 1. Sign Up / Log In
Go to [render.com](https://render.com) and sign in with GitHub

### 2. Create New Web Service
1. Click **"New +"** → **"Web Service"**
2. Connect your GitHub repository: `jadaunaryansingh/Legally_Flutter`
3. Render will auto-detect the `render.yaml` configuration

### 3. Deploy
Render will automatically:
- Install Python dependencies
- Start your FastAPI server
- Give you a production URL like: `https://legally-backend.onrender.com`

**That's it!** Your API will be live in ~3 minutes.

---

## Configuration Details

All configuration is in `render.yaml`:
- **Runtime:** Python 3.11
- **Build Command:** `pip install -r backend/requirements.txt`
- **Start Command:** `cd backend && uvicorn main:app --host 0.0.0.0 --port $PORT`
- **Environment Variables:** GROQ_API_KEY (already set)
- **Plan:** Free tier

---

## Test Your Deployed API

Once deployed, test with:

```bash
# Health check
curl https://YOUR-RENDER-URL.onrender.com/health

# AI endpoint
curl -X POST https://YOUR-RENDER-URL.onrender.com/api/ask \
  -H "Content-Type: application/json" \
  -d '{"message": "What is murder under BNS?"}'
```

---

## Why Render > Vercel for This Project

✅ **Simpler for Python apps** - No serverless complications  
✅ **No authentication protection** - Public API by default  
✅ **Free tier** - 750 hours/month  
✅ **Automatic deploys** - Push to GitHub = auto-deploy  
✅ **Better for FastAPI** - Designed for long-running Python servers

---

## Need to Update?

Just push to GitHub:
```bash
git add .
git commit -m "Update API"
git push
```

Render will automatically redeploy! 🚀
