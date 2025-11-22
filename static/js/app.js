// DOM Elements
const placeInput = document.getElementById('placeInput');
const searchBtn = document.getElementById('searchBtn');
const errorMessage = document.getElementById('errorMessage');
const resultsSection = document.getElementById('resultsSection');
const loadingOverlay = document.getElementById('loadingOverlay');
const placeName = document.getElementById('placeName');
const placeLocation = document.getElementById('placeLocation');
const weatherSection = document.getElementById('weatherSection');
const attractionsSection = document.getElementById('attractionsSection');
const currentWeather = document.getElementById('currentWeather');
const forecastContainer = document.getElementById('forecastContainer');
const attractionsGrid = document.getElementById('attractionsGrid');

// Event Listeners
searchBtn.addEventListener('click', handleSearch);
placeInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        handleSearch();
    }
});

// Add input animation
placeInput.addEventListener('focus', () => {
    placeInput.parentElement.style.transform = 'scale(1.02)';
});

placeInput.addEventListener('blur', () => {
    placeInput.parentElement.style.transform = 'scale(1)';
});

// Handle Search
async function handleSearch() {
    const place = placeInput.value.trim();
    
    if (!place) {
        showError('Please enter a place name');
        shakeElement(searchBtn);
        return;
    }
    
    // Hide previous results and errors
    hideError();
    hideResults();
    showLoading();
    
    // Add button loading state
    searchBtn.disabled = true;
    searchBtn.querySelector('.btn-text').textContent = 'Searching...';
    
    try {
        const response = await fetch('/api/search', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ place: place })
        });
        
        const data = await response.json();
        
        if (data.success) {
            // Small delay for smooth transition
            await new Promise(resolve => setTimeout(resolve, 300));
            displayResults(data.data);
        } else {
            showError(data.error || 'An error occurred');
        }
    } catch (error) {
        showError('Failed to connect to server. Please try again.');
        console.error('Error:', error);
    } finally {
        hideLoading();
        searchBtn.disabled = false;
        searchBtn.querySelector('.btn-text').textContent = 'Search';
    }
}

// Display Results
function displayResults(data) {
    if (data.error) {
        showError(data.message);
        return;
    }
    
    // Display place info with animation
    const place = data.place || {};
    placeName.textContent = place.display_name || place.name || 'Unknown Place';
    placeLocation.textContent = place.country 
        ? `${place.country} • ${place.coordinates?.latitude?.toFixed(4)}, ${place.coordinates?.longitude?.toFixed(4)}` 
        : '';
    
    // Animate place info
    animateElement(placeName.parentElement);
    
    // Display weather
    if (data.weather) {
        displayWeather(data.weather);
        weatherSection.style.display = 'block';
        // Animate weather section
        setTimeout(() => animateElement(weatherSection), 100);
    } else {
        weatherSection.style.display = 'none';
    }
    
    // Display attractions
    if (data.attractions && data.attractions.length > 0) {
        displayAttractions(data.attractions);
        attractionsSection.style.display = 'block';
        // Animate attractions section
        setTimeout(() => animateElement(attractionsSection), 200);
    } else {
        attractionsSection.style.display = 'none';
    }
    
    showResults();
}

// Display Weather
function displayWeather(weather) {
    // Current weather with animation
    const current = weather.current || {};
    const tempElement = document.getElementById('currentTemp');
    const iconElement = document.getElementById('currentIcon');
    const conditionElement = document.getElementById('currentCondition');
    
    // Animate temperature change
    animateValue(tempElement, 0, current.temperature || 0, 1000, (value) => {
        tempElement.textContent = Math.round(value);
    });
    
    iconElement.textContent = current.icon || '🌤️';
    conditionElement.textContent = current.condition || '--';
    
    // Animate icon
    iconElement.style.animation = 'none';
    setTimeout(() => {
        iconElement.style.animation = 'float 3s ease-in-out infinite';
    }, 10);
    
    if (current.windspeed) {
        document.getElementById('windSpeed').textContent = `${current.windspeed} km/h`;
    } else {
        document.getElementById('windSpeed').textContent = '-- km/h';
    }
    
    // Forecast with staggered animation
    forecastContainer.innerHTML = '';
    
    if (weather.forecast && weather.forecast.length > 0) {
        weather.forecast.forEach((day, index) => {
            setTimeout(() => {
                const card = createForecastCard(day);
                forecastContainer.appendChild(card);
                // Animate card appearance
                card.style.opacity = '0';
                card.style.transform = 'translateY(20px)';
                setTimeout(() => {
                    card.style.transition = 'all 0.5s ease';
                    card.style.opacity = '1';
                    card.style.transform = 'translateY(0)';
                }, 50);
            }, index * 100);
        });
    }
}

// Animate numeric value
function animateValue(element, start, end, duration, callback) {
    const startTime = performance.now();
    const range = end - start;
    
    function update(currentTime) {
        const elapsed = currentTime - startTime;
        const progress = Math.min(elapsed / duration, 1);
        const easeOutCubic = 1 - Math.pow(1 - progress, 3);
        const current = start + range * easeOutCubic;
        
        callback(current);
        
        if (progress < 1) {
            requestAnimationFrame(update);
        }
    }
    
    requestAnimationFrame(update);
}

// Create Forecast Card
function createForecastCard(day) {
    const card = document.createElement('div');
    card.className = 'forecast-card';
    
    card.innerHTML = `
        <div class="forecast-day">${day.day_name || day.date}</div>
        <div class="forecast-icon">${day.icon || '🌤️'}</div>
        <div class="forecast-condition">${day.condition || '--'}</div>
        <div class="forecast-temps">
            <div class="forecast-temp">
                <div class="forecast-temp-label">High</div>
                <div class="forecast-temp-value">${day.max_temp}°</div>
            </div>
            <div class="forecast-temp">
                <div class="forecast-temp-label">Low</div>
                <div class="forecast-temp-value">${day.min_temp}°</div>
            </div>
        </div>
    `;
    
    // Add hover effect
    card.addEventListener('mouseenter', () => {
        card.style.transform = 'translateY(-8px) scale(1.02)';
    });
    
    card.addEventListener('mouseleave', () => {
        card.style.transform = 'translateY(0) scale(1)';
    });
    
    return card;
}

// Display Attractions
function displayAttractions(attractions) {
    attractionsGrid.innerHTML = '';
    
    attractions.forEach((attraction, index) => {
        setTimeout(() => {
            const card = createAttractionCard(attraction);
            attractionsGrid.appendChild(card);
            // Animate card appearance
            card.style.opacity = '0';
            card.style.transform = 'translateX(-20px)';
            setTimeout(() => {
                card.style.transition = 'all 0.5s ease';
                card.style.opacity = '1';
                card.style.transform = 'translateX(0)';
            }, 50);
        }, index * 150);
    });
}

// Create Attraction Card
function createAttractionCard(attraction) {
    const card = document.createElement('div');
    card.className = 'attraction-card';
    
    const distanceText = attraction.distance 
        ? `📍 ${attraction.distance} km away`
        : '';
    
    const imageUrl = attraction.image_url || '';
    const imageHTML = imageUrl 
        ? `<div class="attraction-image-container">
            <img src="${imageUrl}" alt="${attraction.name}" class="attraction-image" loading="lazy" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
            <div class="attraction-image-placeholder" style="display: none;">
                <span class="attraction-icon-large">${attraction.icon || '📍'}</span>
            </div>
        </div>`
        : `<div class="attraction-image-placeholder">
            <span class="attraction-icon-large">${attraction.icon || '📍'}</span>
        </div>`;
    
    card.innerHTML = `
        ${imageHTML}
        <div class="attraction-content">
            <div class="attraction-header">
                <div class="attraction-icon">${attraction.icon || '📍'}</div>
                <div class="attraction-info">
                    <div class="attraction-name">${attraction.name || 'Unknown'}</div>
                    <div class="attraction-type">${attraction.type || 'attraction'}</div>
                </div>
            </div>
            ${distanceText ? `<div class="attraction-distance">${distanceText}</div>` : ''}
        </div>
    `;
    
    // Add click effect
    card.addEventListener('click', () => {
        card.style.transform = 'scale(0.98)';
        setTimeout(() => {
            card.style.transform = '';
        }, 150);
    });
    
    return card;
}

// Animation helpers
function animateElement(element) {
    element.style.animation = 'none';
    setTimeout(() => {
        element.style.animation = 'fadeInUp 0.6s ease';
    }, 10);
}

function shakeElement(element) {
    element.style.animation = 'shake 0.5s ease';
    setTimeout(() => {
        element.style.animation = '';
    }, 500);
}

// UI Helper Functions
function showLoading() {
    loadingOverlay.style.display = 'flex';
    loadingOverlay.style.opacity = '0';
    setTimeout(() => {
        loadingOverlay.style.transition = 'opacity 0.3s ease';
        loadingOverlay.style.opacity = '1';
    }, 10);
}

function hideLoading() {
    loadingOverlay.style.opacity = '0';
    setTimeout(() => {
        loadingOverlay.style.display = 'none';
    }, 300);
}

function showError(message) {
    errorMessage.textContent = message;
    errorMessage.style.display = 'block';
    errorMessage.style.animation = 'shake 0.5s ease';
    setTimeout(() => {
        errorMessage.style.animation = '';
    }, 500);
}

function hideError() {
    errorMessage.style.display = 'none';
}

function showResults() {
    resultsSection.style.display = 'block';
    resultsSection.style.opacity = '0';
    setTimeout(() => {
        resultsSection.style.transition = 'opacity 0.5s ease';
        resultsSection.style.opacity = '1';
    }, 10);
    
    // Smooth scroll to results
    setTimeout(() => {
        resultsSection.scrollIntoView({ 
            behavior: 'smooth', 
            block: 'start' 
        });
    }, 100);
}

function hideResults() {
    resultsSection.style.display = 'none';
}

// Add parallax effect on scroll
let lastScroll = 0;
window.addEventListener('scroll', () => {
    const currentScroll = window.pageYOffset;
    const header = document.querySelector('.header');
    
    if (header) {
        const parallax = currentScroll * 0.5;
        header.style.transform = `translateY(${parallax}px)`;
        header.style.opacity = 1 - (currentScroll / 500);
    }
    
    lastScroll = currentScroll;
});

// Add keyboard shortcuts
document.addEventListener('keydown', (e) => {
    // Focus search on '/' key
    if (e.key === '/' && e.target !== placeInput) {
        e.preventDefault();
        placeInput.focus();
    }
    
    // Clear on Escape
    if (e.key === 'Escape' && document.activeElement === placeInput) {
        placeInput.blur();
    }
});

// Add input suggestions (optional enhancement)
placeInput.addEventListener('input', (e) => {
    const value = e.target.value;
    if (value.length > 2) {
        // Could add autocomplete here
    }
});
