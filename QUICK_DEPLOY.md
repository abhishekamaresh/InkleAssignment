# Quick Deployment Guide

## Fastest Way: Render (Recommended)

### Step 1: Push to GitHub
```bash
git init
git add .
git commit -m "Initial commit - Tourism AI System"
git remote add origin <your-github-repo-url>
git push -u origin main
```

### Step 2: Deploy on Render
1. Go to [render.com](https://render.com) and sign up/login
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Render will auto-detect settings from `render.yaml`
5. Click "Create Web Service"
6. Wait 5-10 minutes for first deployment
7. Your app will be live at: `https://your-app-name.onrender.com`

**That's it!** 🎉

---

## Alternative: Railway (Also Fast)

1. Push to GitHub (same as above)
2. Go to [railway.app](https://railway.app)
3. Click "New Project" → "Deploy from GitHub repo"
4. Select your repository
5. Railway auto-deploys - done!

---

## Pre-Deployment Checklist

Before deploying, ensure:
- [x] All files are committed to Git
- [x] `requirements.txt` includes all dependencies
- [x] `app.py` is production-ready (no hardcoded debug=True)
- [x] Static files (`static/`, `templates/`) are in root directory

---

## Test Locally First (Optional)

```bash
# Install dependencies
pip install -r requirements.txt

# Run with gunicorn (production-like)
gunicorn app:app --bind 0.0.0.0:5001 --workers 2

# Or run with Flask (development)
python app.py
```

Visit: http://localhost:5001

---

## Need More Details?

See `DEPLOYMENT.md` for comprehensive deployment instructions for all platforms.

