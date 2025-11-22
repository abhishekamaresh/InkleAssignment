# Deployment Guide

This guide covers deploying the Tourism AI System to various platforms.

## Prerequisites

- Git repository initialized
- All dependencies listed in `requirements.txt`
- Python 3.11+ (recommended)

## Platform Options

### Option 1: Render (Recommended - Free Tier Available)

**Steps:**

1. **Create a Render account** at [render.com](https://render.com)

2. **Create a new Web Service:**
   - Click "New +" → "Web Service"
   - Connect your Git repository
   - Configure:
     - **Name:** `tourism-ai-system`
     - **Environment:** `Python 3`
     - **Build Command:** `pip install -r requirements.txt`
     - **Start Command:** `gunicorn app:app --bind 0.0.0.0:$PORT --workers 2 --threads 2 --timeout 120`
     - **Instance Type:** Free tier is sufficient

3. **Deploy:**
   - Render will automatically detect `render.yaml` if present
   - Or manually configure using the settings above
   - Click "Create Web Service"

4. **Access your app:**
   - Render provides a URL like: `https://tourism-ai-system.onrender.com`
   - First deployment may take 5-10 minutes

**Advantages:**
- Free tier available
- Automatic SSL certificates
- Easy Git-based deployments
- Auto-deploy on push to main branch

---

### Option 2: Railway

**Steps:**

1. **Create a Railway account** at [railway.app](https://railway.app)

2. **Create a new project:**
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your repository

3. **Configure:**
   - Railway auto-detects Python projects
   - Uses `railway.json` for configuration
   - Automatically installs dependencies

4. **Set environment variables (if needed):**
   - Go to project settings → Variables
   - Add any required environment variables

5. **Deploy:**
   - Railway automatically deploys on push
   - Check the "Deployments" tab for status

**Advantages:**
- Simple setup
- Free tier with $5 credit monthly
- Automatic deployments
- Built-in monitoring

---

### Option 3: Heroku

**Steps:**

1. **Install Heroku CLI:**
   ```bash
   # macOS
   brew tap heroku/brew && brew install heroku
   
   # Or download from https://devcenter.heroku.com/articles/heroku-cli
   ```

2. **Login to Heroku:**
   ```bash
   heroku login
   ```

3. **Create a Heroku app:**
   ```bash
   heroku create tourism-ai-system
   ```

4. **Deploy:**
   ```bash
   git push heroku main
   ```

5. **Open your app:**
   ```bash
   heroku open
   ```

**Note:** Heroku removed their free tier. Consider Render or Railway for free hosting.

---

### Option 4: PythonAnywhere

**Steps:**

1. **Create account** at [pythonanywhere.com](https://www.pythonanywhere.com)

2. **Upload your code:**
   - Use the Files tab to upload your project
   - Or use Git: `git clone <your-repo-url>`

3. **Configure Web App:**
   - Go to Web tab
   - Click "Add a new web app"
   - Choose Python 3.11
   - Set source code path
   - Set WSGI configuration file

4. **Create WSGI file:**
   ```python
   import sys
   path = '/home/yourusername/tourism-ai-system'
   if path not in sys.path:
       sys.path.append(path)
   
   from app import app as application
   ```

5. **Reload web app:**
   - Click the green "Reload" button

**Advantages:**
- Free tier available
- Good for Python apps
- Easy file management

---

### Option 5: Fly.io

**Steps:**

1. **Install Fly CLI:**
   ```bash
   curl -L https://fly.io/install.sh | sh
   ```

2. **Login:**
   ```bash
   fly auth login
   ```

3. **Create app:**
   ```bash
   fly launch
   ```

4. **Deploy:**
   ```bash
   fly deploy
   ```

---

## Environment Variables

The app uses the following environment variables (all optional):

- `PORT`: Port number (default: 5001)
- `FLASK_DEBUG`: Enable debug mode (default: False)

No API keys are required - all APIs used are public/free.

---

## Post-Deployment Checklist

- [ ] Test the homepage loads correctly
- [ ] Test search functionality with a known city (e.g., "Paris")
- [ ] Verify weather data displays
- [ ] Verify attractions display with images
- [ ] Check mobile responsiveness
- [ ] Test error handling (try invalid city name)

---

## Troubleshooting

### App crashes on startup
- Check logs for errors
- Verify all dependencies are in `requirements.txt`
- Ensure Python version is 3.11+

### API errors
- All APIs are public, no keys needed
- Check rate limits if many requests fail
- Verify internet connectivity

### Static files not loading
- Ensure `static/` and `templates/` folders are in root directory
- Check Flask static file configuration

### Timeout errors
- Increase timeout in gunicorn command
- Check API response times
- Consider caching for frequently accessed data

---

## Monitoring

After deployment, monitor:
- Response times
- Error rates
- API usage
- Resource usage (CPU, memory)

---

## Custom Domain (Optional)

Most platforms allow custom domains:
- **Render:** Settings → Custom Domain
- **Railway:** Settings → Domains
- **Heroku:** Settings → Domains

---

## Need Help?

Check platform-specific documentation:
- [Render Docs](https://render.com/docs)
- [Railway Docs](https://docs.railway.app)
- [Heroku Docs](https://devcenter.heroku.com)

