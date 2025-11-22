# Web UI Guide

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Start the Web Server
```bash
python app.py
```

### 3. Open in Browser
Navigate to: **http://localhost:5000**

## 🎨 Features

### Modern Weather Forecast Display
- **Current Weather Card**: Large, prominent display with:
  - Current temperature
  - Weather condition with icon
  - Wind speed and direction
  
- **7-Day Forecast**: Beautiful cards showing:
  - Day name
  - Weather icon
  - Condition description
  - High and low temperatures

### Tourist Attractions Grid
- **Attraction Cards**: Each card displays:
  - Attraction icon (museum, hotel, monument, etc.)
  - Name and type
  - Distance from center point
  
- **Responsive Layout**: Automatically adjusts for mobile, tablet, and desktop

### Interactive Search
- **Real-time Search**: Enter any place name and get instant results
- **Error Handling**: Clear error messages for invalid places
- **Loading States**: Visual feedback during API calls

## 📱 Responsive Design

The web interface is fully responsive and works on:
- 📱 Mobile phones
- 📱 Tablets
- 💻 Desktop computers

## 🎯 Usage Tips

1. **Search Examples**:
   - Major cities: "Paris", "Tokyo", "New York"
   - Smaller places: "Barcelona", "Sydney", "Dubai"
   - International: Works with any language/script

2. **Weather Information**:
   - Current weather updates in real-time
   - 7-day forecast for planning ahead
   - Weather icons for quick visual reference

3. **Attractions**:
   - Shows up to 5 nearest attractions
   - Sorted by distance
   - Includes museums, hotels, monuments, and more

## 🔧 Troubleshooting

### Port Already in Use
If port 5000 is busy, edit `app.py` and change:
```python
app.run(debug=True, host='0.0.0.0', port=5000)
```
to a different port (e.g., 5001, 8080).

### Module Not Found
Make sure all dependencies are installed:
```bash
pip install -r requirements.txt
```

### API Errors
- Check your internet connection
- Some APIs may have rate limits
- Overpass API can be slow (10-30 seconds) - be patient

## 🌐 Accessing from Other Devices

To access from other devices on your network:

1. Find your local IP address:
   ```bash
   # macOS/Linux
   ifconfig | grep "inet "
   
   # Windows
   ipconfig
   ```

2. Access from other device:
   ```
   http://YOUR_IP_ADDRESS:5000
   ```

## 🎨 Customization

### Changing Colors
Edit `static/css/style.css` and modify the CSS variables:
```css
:root {
    --primary-color: #2563eb;
    --secondary-color: #10b981;
    /* ... */
}
```

### Modifying Layout
- HTML structure: `templates/index.html`
- Styling: `static/css/style.css`
- JavaScript: `static/js/app.js`

---

**Enjoy the beautiful web interface! 🎉**

