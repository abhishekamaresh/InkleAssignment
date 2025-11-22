# 🚀 Start the Web Application

## Quick Start

The web application is ready to use! Here's how to start it:

### Step 1: Install Dependencies (if not already done)
```bash
pip install -r requirements.txt
```

### Step 2: Start the Server
```bash
python app.py
```

### Step 3: Open in Browser
Open your web browser and navigate to:
```
http://localhost:5000
```

## ✨ What You'll See

1. **Beautiful Landing Page** with search interface
2. **Weather Forecast Cards** showing:
   - Current weather with large temperature display
   - 7-day forecast with icons and conditions
   - High/low temperatures for each day

3. **Tourist Attractions Grid** displaying:
   - Up to 5 nearby attractions
   - Icons for different types (museums, hotels, monuments)
   - Distance from the searched location

## 🎯 Try These Places

- **Paris** - Beautiful European city
- **Tokyo** - Major Asian metropolis
- **New York** - Iconic American city
- **Barcelona** - Mediterranean gem
- **Sydney** - Australian coastal city
- **Dubai** - Modern Middle Eastern city

## 📱 Features

- ✅ **Responsive Design** - Works on mobile, tablet, and desktop
- ✅ **Real-time Search** - Instant results as you search
- ✅ **Beautiful UI** - Modern, clean interface
- ✅ **Weather Icons** - Visual weather representation
- ✅ **Error Handling** - Clear messages for invalid places
- ✅ **Loading States** - Visual feedback during API calls

## 🛑 Stop the Server

Press `Ctrl+C` in the terminal to stop the server.

## 🔧 Troubleshooting

**Port 5000 already in use?**
Edit `app.py` and change the port number:
```python
app.run(debug=True, host='0.0.0.0', port=8080)  # Use port 8080 instead
```

**Module not found?**
```bash
pip install flask requests
```

---

**The web app is running! Open http://localhost:5000 in your browser! 🌐**

