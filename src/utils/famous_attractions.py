"""Famous attractions database - Tourist Guide Mode.

This acts as a professional tourist guide, ensuring the most iconic
and must-see attractions are always displayed for major cities worldwide.
"""

# Comprehensive database of MUST-SEE attractions for major cities
# These are the iconic landmarks every tourist should know about
FAMOUS_ATTRACTIONS = {
    # ========== EUROPE ==========
    
    # Paris - City of Light
    'paris': [
        {'name': 'Eiffel Tower', 'type': 'monument', 'lat': 48.8584, 'lon': 2.2945, 'priority': 1},
        {'name': 'Louvre Museum', 'type': 'museum', 'lat': 48.8606, 'lon': 2.3376, 'priority': 2},
        {'name': 'Notre-Dame de Paris', 'type': 'monument', 'lat': 48.8530, 'lon': 2.3499, 'priority': 3},
        {'name': 'Arc de Triomphe', 'type': 'monument', 'lat': 48.8738, 'lon': 2.2950, 'priority': 4},
        {'name': 'Champs-Élysées', 'type': 'attraction', 'lat': 48.8698, 'lon': 2.3081, 'priority': 5},
        {'name': 'Montmartre', 'type': 'attraction', 'lat': 48.8867, 'lon': 2.3431, 'priority': 6},
        {'name': 'Musée d\'Orsay', 'type': 'museum', 'lat': 48.8600, 'lon': 2.3266, 'priority': 7},
        {'name': 'Seine River', 'type': 'attraction', 'lat': 48.8566, 'lon': 2.3522, 'priority': 8},
    ],
    
    # London - Historic Capital
    'london': [
        {'name': 'Big Ben', 'type': 'monument', 'lat': 51.4994, 'lon': -0.1245, 'priority': 1},
        {'name': 'Tower Bridge', 'type': 'monument', 'lat': 51.5055, 'lon': -0.0754, 'priority': 2},
        {'name': 'British Museum', 'type': 'museum', 'lat': 51.5194, 'lon': -0.1270, 'priority': 3},
        {'name': 'London Eye', 'type': 'attraction', 'lat': 51.5033, 'lon': -0.1196, 'priority': 4},
        {'name': 'Buckingham Palace', 'type': 'monument', 'lat': 51.5014, 'lon': -0.1419, 'priority': 5},
        {'name': 'Westminster Abbey', 'type': 'monument', 'lat': 51.4994, 'lon': -0.1274, 'priority': 6},
        {'name': 'Tower of London', 'type': 'monument', 'lat': 51.5081, 'lon': -0.0759, 'priority': 7},
        {'name': 'Hyde Park', 'type': 'park', 'lat': 51.5073, 'lon': -0.1657, 'priority': 8},
    ],
    
    # Rome - Eternal City
    'rome': [
        {'name': 'Colosseum', 'type': 'monument', 'lat': 41.8902, 'lon': 12.4922, 'priority': 1},
        {'name': 'Trevi Fountain', 'type': 'monument', 'lat': 41.9009, 'lon': 12.4833, 'priority': 2},
        {'name': 'Pantheon', 'type': 'monument', 'lat': 41.8986, 'lon': 12.4769, 'priority': 3},
        {'name': 'Vatican City', 'type': 'monument', 'lat': 41.9029, 'lon': 12.4534, 'priority': 4},
        {'name': 'Roman Forum', 'type': 'monument', 'lat': 41.8925, 'lon': 12.4853, 'priority': 5},
        {'name': 'Spanish Steps', 'type': 'monument', 'lat': 41.9058, 'lon': 12.4822, 'priority': 6},
        {'name': 'Sistine Chapel', 'type': 'monument', 'lat': 41.9029, 'lon': 12.4545, 'priority': 7},
        {'name': 'St. Peter\'s Basilica', 'type': 'monument', 'lat': 41.9022, 'lon': 12.4539, 'priority': 8},
    ],
    
    # Barcelona - Catalan Gem
    'barcelona': [
        {'name': 'Sagrada Familia', 'type': 'monument', 'lat': 41.4036, 'lon': 2.1744, 'priority': 1},
        {'name': 'Park Güell', 'type': 'park', 'lat': 41.4145, 'lon': 2.1527, 'priority': 2},
        {'name': 'Casa Batlló', 'type': 'monument', 'lat': 41.3917, 'lon': 2.1649, 'priority': 3},
        {'name': 'La Rambla', 'type': 'attraction', 'lat': 41.3809, 'lon': 2.1734, 'priority': 4},
        {'name': 'Gothic Quarter', 'type': 'attraction', 'lat': 41.3833, 'lon': 2.1769, 'priority': 5},
        {'name': 'Casa Milà (La Pedrera)', 'type': 'monument', 'lat': 41.3950, 'lon': 2.1617, 'priority': 6},
        {'name': 'Camp Nou', 'type': 'monument', 'lat': 41.3809, 'lon': 2.1228, 'priority': 7},
        {'name': 'Barceloneta Beach', 'type': 'attraction', 'lat': 41.3800, 'lon': 2.1894, 'priority': 8},
    ],
    
    # Amsterdam - Canal City
    'amsterdam': [
        {'name': 'Anne Frank House', 'type': 'museum', 'lat': 52.3751, 'lon': 4.8841, 'priority': 1},
        {'name': 'Van Gogh Museum', 'type': 'museum', 'lat': 52.3584, 'lon': 4.8811, 'priority': 2},
        {'name': 'Rijksmuseum', 'type': 'museum', 'lat': 52.3600, 'lon': 4.8852, 'priority': 3},
        {'name': 'Canal Ring', 'type': 'attraction', 'lat': 52.3676, 'lon': 4.9041, 'priority': 4},
        {'name': 'Dam Square', 'type': 'attraction', 'lat': 52.3731, 'lon': 4.8927, 'priority': 5},
        {'name': 'Red Light District', 'type': 'attraction', 'lat': 52.3702, 'lon': 4.8952, 'priority': 6},
        {'name': 'Vondelpark', 'type': 'park', 'lat': 52.3572, 'lon': 4.8686, 'priority': 7},
        {'name': 'Royal Palace Amsterdam', 'type': 'monument', 'lat': 52.3731, 'lon': 4.8911, 'priority': 8},
    ],
    
    # Berlin - Historic Capital
    'berlin': [
        {'name': 'Brandenburg Gate', 'type': 'monument', 'lat': 52.5163, 'lon': 13.3777, 'priority': 1},
        {'name': 'Berlin Wall', 'type': 'monument', 'lat': 52.5074, 'lon': 13.3904, 'priority': 2},
        {'name': 'Reichstag Building', 'type': 'monument', 'lat': 52.5186, 'lon': 13.3761, 'priority': 3},
        {'name': 'Museum Island', 'type': 'museum', 'lat': 52.5219, 'lon': 13.4012, 'priority': 4},
        {'name': 'Checkpoint Charlie', 'type': 'monument', 'lat': 52.5074, 'lon': 13.3904, 'priority': 5},
        {'name': 'East Side Gallery', 'type': 'monument', 'lat': 52.5050, 'lon': 13.4396, 'priority': 6},
        {'name': 'Pergamon Museum', 'type': 'museum', 'lat': 52.5210, 'lon': 13.3969, 'priority': 7},
        {'name': 'Charlottenburg Palace', 'type': 'monument', 'lat': 52.5200, 'lon': 13.2958, 'priority': 8},
    ],
    
    # Istanbul - Crossroads of Continents
    'istanbul': [
        {'name': 'Hagia Sophia', 'type': 'monument', 'lat': 41.0086, 'lon': 28.9802, 'priority': 1},
        {'name': 'Blue Mosque', 'type': 'monument', 'lat': 41.0054, 'lon': 28.9774, 'priority': 2},
        {'name': 'Topkapi Palace', 'type': 'monument', 'lat': 41.0117, 'lon': 28.9850, 'priority': 3},
        {'name': 'Grand Bazaar', 'type': 'attraction', 'lat': 41.0106, 'lon': 28.9681, 'priority': 4},
        {'name': 'Bosphorus Bridge', 'type': 'monument', 'lat': 41.0444, 'lon': 29.0347, 'priority': 5},
        {'name': 'Basilica Cistern', 'type': 'monument', 'lat': 41.0082, 'lon': 28.9778, 'priority': 6},
        {'name': 'Galata Tower', 'type': 'monument', 'lat': 41.0256, 'lon': 28.9744, 'priority': 7},
        {'name': 'Spice Bazaar', 'type': 'attraction', 'lat': 41.0167, 'lon': 28.9700, 'priority': 8},
    ],
    
    # Moscow - Russian Capital
    'moscow': [
        {'name': 'Red Square', 'type': 'attraction', 'lat': 55.7539, 'lon': 37.6208, 'priority': 1},
        {'name': 'Kremlin', 'type': 'monument', 'lat': 55.7520, 'lon': 37.6175, 'priority': 2},
        {'name': 'St. Basils Cathedral', 'type': 'monument', 'lat': 55.7525, 'lon': 37.6231, 'priority': 3},
        {'name': 'Bolshoi Theatre', 'type': 'theatre', 'lat': 55.7596, 'lon': 37.6194, 'priority': 4},
        {'name': 'Gorky Park', 'type': 'park', 'lat': 55.7294, 'lon': 37.6014, 'priority': 5},
        {'name': 'Moscow Metro', 'type': 'attraction', 'lat': 55.7558, 'lon': 37.6173, 'priority': 6},
        {'name': 'Tretyakov Gallery', 'type': 'museum', 'lat': 55.7415, 'lon': 37.6208, 'priority': 7},
        {'name': 'Cathedral of Christ the Saviour', 'type': 'monument', 'lat': 55.7445, 'lon': 37.6051, 'priority': 8},
    ],
    
    # Vienna - City of Music
    'vienna': [
        {'name': 'Schönbrunn Palace', 'type': 'monument', 'lat': 48.1845, 'lon': 16.3122, 'priority': 1},
        {'name': 'St. Stephen\'s Cathedral', 'type': 'monument', 'lat': 48.2085, 'lon': 16.3731, 'priority': 2},
        {'name': 'Hofburg Palace', 'type': 'monument', 'lat': 48.2060, 'lon': 16.3649, 'priority': 3},
        {'name': 'Belvedere Palace', 'type': 'monument', 'lat': 48.1926, 'lon': 16.3807, 'priority': 4},
        {'name': 'Vienna State Opera', 'type': 'theatre', 'lat': 48.2035, 'lon': 16.3691, 'priority': 5},
        {'name': 'Prater', 'type': 'park', 'lat': 48.2167, 'lon': 16.3950, 'priority': 6},
        {'name': 'Museumsquartier', 'type': 'museum', 'lat': 48.2038, 'lon': 16.3594, 'priority': 7},
        {'name': 'Ringstrasse', 'type': 'attraction', 'lat': 48.2100, 'lon': 16.3700, 'priority': 8},
    ],
    
    # Prague - City of a Hundred Spires
    'prague': [
        {'name': 'Prague Castle', 'type': 'monument', 'lat': 50.0910, 'lon': 14.4015, 'priority': 1},
        {'name': 'Charles Bridge', 'type': 'monument', 'lat': 50.0865, 'lon': 14.4114, 'priority': 2},
        {'name': 'Old Town Square', 'type': 'attraction', 'lat': 50.0875, 'lon': 14.4214, 'priority': 3},
        {'name': 'Astronomical Clock', 'type': 'monument', 'lat': 50.0870, 'lon': 14.4208, 'priority': 4},
        {'name': 'St. Vitus Cathedral', 'type': 'monument', 'lat': 50.0909, 'lon': 14.4006, 'priority': 5},
        {'name': 'Wenceslas Square', 'type': 'attraction', 'lat': 50.0814, 'lon': 14.4261, 'priority': 6},
        {'name': 'Jewish Quarter', 'type': 'attraction', 'lat': 50.0900, 'lon': 14.4178, 'priority': 7},
        {'name': 'Petřín Hill', 'type': 'park', 'lat': 50.0833, 'lon': 14.3958, 'priority': 8},
    ],
    
    # Madrid - Spanish Capital
    'madrid': [
        {'name': 'Prado Museum', 'type': 'museum', 'lat': 40.4138, 'lon': -3.6921, 'priority': 1},
        {'name': 'Royal Palace of Madrid', 'type': 'monument', 'lat': 40.4180, 'lon': -3.7142, 'priority': 2},
        {'name': 'Retiro Park', 'type': 'park', 'lat': 40.4150, 'lon': -3.6833, 'priority': 3},
        {'name': 'Plaza Mayor', 'type': 'attraction', 'lat': 40.4154, 'lon': -3.7074, 'priority': 4},
        {'name': 'Puerta del Sol', 'type': 'attraction', 'lat': 40.4168, 'lon': -3.7038, 'priority': 5},
        {'name': 'Reina Sofía Museum', 'type': 'museum', 'lat': 40.4081, 'lon': -3.6946, 'priority': 6},
        {'name': 'Gran Vía', 'type': 'attraction', 'lat': 40.4194, 'lon': -3.7038, 'priority': 7},
        {'name': 'Santiago Bernabéu Stadium', 'type': 'monument', 'lat': 40.4530, 'lon': -3.6883, 'priority': 8},
    ],
    
    # ========== ASIA ==========
    
    # Tokyo - Modern Metropolis
    'tokyo': [
        {'name': 'Tokyo Skytree', 'type': 'monument', 'lat': 35.7101, 'lon': 139.8107, 'priority': 1},
        {'name': 'Senso-ji Temple', 'type': 'monument', 'lat': 35.7148, 'lon': 139.7967, 'priority': 2},
        {'name': 'Tokyo Tower', 'type': 'monument', 'lat': 35.6586, 'lon': 139.7454, 'priority': 3},
        {'name': 'Meiji Shrine', 'type': 'monument', 'lat': 35.6764, 'lon': 139.6993, 'priority': 4},
        {'name': 'Shibuya Crossing', 'type': 'attraction', 'lat': 35.6598, 'lon': 139.7006, 'priority': 5},
        {'name': 'Imperial Palace', 'type': 'monument', 'lat': 35.6852, 'lon': 139.7528, 'priority': 6},
        {'name': 'Tsukiji Fish Market', 'type': 'attraction', 'lat': 35.6654, 'lon': 139.7706, 'priority': 7},
        {'name': 'Harajuku', 'type': 'attraction', 'lat': 35.6702, 'lon': 139.7026, 'priority': 8},
    ],
    
    # Singapore - Garden City
    'singapore': [
        {'name': 'Marina Bay Sands', 'type': 'monument', 'lat': 1.2831, 'lon': 103.8603, 'priority': 1},
        {'name': 'Gardens by the Bay', 'type': 'park', 'lat': 1.2816, 'lon': 103.8636, 'priority': 2},
        {'name': 'Merlion', 'type': 'monument', 'lat': 1.2868, 'lon': 103.8545, 'priority': 3},
        {'name': 'Sentosa Island', 'type': 'attraction', 'lat': 1.2494, 'lon': 103.8304, 'priority': 4},
        {'name': 'Singapore Flyer', 'type': 'attraction', 'lat': 1.2894, 'lon': 103.8631, 'priority': 5},
        {'name': 'Universal Studios Singapore', 'type': 'attraction', 'lat': 1.2540, 'lon': 103.8238, 'priority': 6},
        {'name': 'Chinatown', 'type': 'attraction', 'lat': 1.2838, 'lon': 103.8436, 'priority': 7},
        {'name': 'Orchard Road', 'type': 'attraction', 'lat': 1.3048, 'lon': 103.8318, 'priority': 8},
    ],
    
    # Hong Kong - Pearl of the Orient
    'hong kong': [
        {'name': 'Victoria Peak', 'type': 'attraction', 'lat': 22.2711, 'lon': 114.1498, 'priority': 1},
        {'name': 'Hong Kong Disneyland', 'type': 'attraction', 'lat': 22.3130, 'lon': 114.0414, 'priority': 2},
        {'name': 'Tian Tan Buddha', 'type': 'monument', 'lat': 22.2539, 'lon': 113.9044, 'priority': 3},
        {'name': 'Star Ferry', 'type': 'attraction', 'lat': 22.2864, 'lon': 114.1495, 'priority': 4},
        {'name': 'Temple Street Night Market', 'type': 'attraction', 'lat': 22.3050, 'lon': 114.1714, 'priority': 5},
        {'name': 'Ocean Park', 'type': 'attraction', 'lat': 22.2474, 'lon': 114.1744, 'priority': 6},
        {'name': 'Lantau Island', 'type': 'attraction', 'lat': 22.2670, 'lon': 113.9460, 'priority': 7},
        {'name': 'Avenue of Stars', 'type': 'attraction', 'lat': 22.2933, 'lon': 114.1719, 'priority': 8},
    ],
    
    # Bangkok - City of Angels
    'bangkok': [
        {'name': 'Wat Phra Kaew', 'type': 'monument', 'lat': 13.7500, 'lon': 100.4925, 'priority': 1},
        {'name': 'Wat Pho', 'type': 'monument', 'lat': 13.7464, 'lon': 100.4931, 'priority': 2},
        {'name': 'Grand Palace', 'type': 'monument', 'lat': 13.7500, 'lon': 100.4914, 'priority': 3},
        {'name': 'Chatuchak Market', 'type': 'attraction', 'lat': 13.8006, 'lon': 100.5514, 'priority': 4},
        {'name': 'Floating Markets', 'type': 'attraction', 'lat': 13.7272, 'lon': 100.5342, 'priority': 5},
        {'name': 'Wat Arun', 'type': 'monument', 'lat': 13.7438, 'lon': 100.4889, 'priority': 6},
        {'name': 'Lumpini Park', 'type': 'park', 'lat': 13.7310, 'lon': 100.5411, 'priority': 7},
        {'name': 'Khao San Road', 'type': 'attraction', 'lat': 13.7588, 'lon': 100.4974, 'priority': 8},
    ],
    
    # Mumbai - Gateway of India
    'mumbai': [
        {'name': 'Gateway of India', 'type': 'monument', 'lat': 18.9220, 'lon': 72.8347, 'priority': 1},
        {'name': 'Taj Mahal Palace', 'type': 'monument', 'lat': 18.9217, 'lon': 72.8331, 'priority': 2},
        {'name': 'Marine Drive', 'type': 'attraction', 'lat': 18.9444, 'lon': 72.8250, 'priority': 3},
        {'name': 'Elephanta Caves', 'type': 'monument', 'lat': 18.9633, 'lon': 72.9314, 'priority': 4},
        {'name': 'Chhatrapati Shivaji Terminus', 'type': 'monument', 'lat': 18.9400, 'lon': 72.8353, 'priority': 5},
        {'name': 'Haji Ali Dargah', 'type': 'monument', 'lat': 18.9833, 'lon': 72.8167, 'priority': 6},
        {'name': 'Juhu Beach', 'type': 'attraction', 'lat': 19.1000, 'lon': 72.8264, 'priority': 7},
        {'name': 'Bandra-Worli Sea Link', 'type': 'monument', 'lat': 19.0406, 'lon': 72.8203, 'priority': 8},
    ],
    
    # Delhi - Capital of India
    'delhi': [
        {'name': 'Red Fort', 'type': 'monument', 'lat': 28.6562, 'lon': 77.2410, 'priority': 1},
        {'name': 'India Gate', 'type': 'monument', 'lat': 28.6129, 'lon': 77.2295, 'priority': 2},
        {'name': 'Qutub Minar', 'type': 'monument', 'lat': 28.5244, 'lon': 77.1855, 'priority': 3},
        {'name': 'Lotus Temple', 'type': 'monument', 'lat': 28.5535, 'lon': 77.2588, 'priority': 4},
        {'name': 'Humayun\'s Tomb', 'type': 'monument', 'lat': 28.5933, 'lon': 77.2506, 'priority': 5},
        {'name': 'Jama Masjid', 'type': 'monument', 'lat': 28.6507, 'lon': 77.2334, 'priority': 6},
        {'name': 'Akshardham Temple', 'type': 'monument', 'lat': 28.6127, 'lon': 77.2773, 'priority': 7},
        {'name': 'Connaught Place', 'type': 'attraction', 'lat': 28.6304, 'lon': 77.2177, 'priority': 8},
    ],
    
    # Bengaluru - Silicon Valley of India
    'bengaluru': [
        {'name': 'Lalbagh Botanical Garden', 'type': 'park', 'lat': 12.9507, 'lon': 77.5848, 'priority': 1},
        {'name': 'Bangalore Palace', 'type': 'monument', 'lat': 12.9984, 'lon': 77.5925, 'priority': 2},
        {'name': 'Cubbon Park', 'type': 'park', 'lat': 12.9716, 'lon': 77.5946, 'priority': 3},
        {'name': 'ISKCON Temple', 'type': 'monument', 'lat': 13.0103, 'lon': 77.5510, 'priority': 4},
        {'name': 'Tipu Sultan\'s Summer Palace', 'type': 'monument', 'lat': 12.9614, 'lon': 77.5736, 'priority': 5},
        {'name': 'Vidhana Soudha', 'type': 'monument', 'lat': 12.9791, 'lon': 77.5913, 'priority': 6},
        {'name': 'Bannerghatta National Park', 'type': 'park', 'lat': 12.8000, 'lon': 77.5767, 'priority': 7},
        {'name': 'Nandi Hills', 'type': 'attraction', 'lat': 13.3700, 'lon': 77.6800, 'priority': 8},
    ],
    
    # Also support "bangalore" as an alias
    'bangalore': [
        {'name': 'Lalbagh Botanical Garden', 'type': 'park', 'lat': 12.9507, 'lon': 77.5848, 'priority': 1},
        {'name': 'Bangalore Palace', 'type': 'monument', 'lat': 12.9984, 'lon': 77.5925, 'priority': 2},
        {'name': 'Cubbon Park', 'type': 'park', 'lat': 12.9716, 'lon': 77.5946, 'priority': 3},
        {'name': 'ISKCON Temple', 'type': 'monument', 'lat': 13.0103, 'lon': 77.5510, 'priority': 4},
        {'name': 'Tipu Sultan\'s Summer Palace', 'type': 'monument', 'lat': 12.9614, 'lon': 77.5736, 'priority': 5},
        {'name': 'Vidhana Soudha', 'type': 'monument', 'lat': 12.9791, 'lon': 77.5913, 'priority': 6},
        {'name': 'Bannerghatta National Park', 'type': 'park', 'lat': 12.8000, 'lon': 77.5767, 'priority': 7},
        {'name': 'Nandi Hills', 'type': 'attraction', 'lat': 13.3700, 'lon': 77.6800, 'priority': 8},
    ],
    
    # Seoul - Dynamic Capital
    'seoul': [
        {'name': 'Gyeongbokgung Palace', 'type': 'monument', 'lat': 37.5796, 'lon': 126.9770, 'priority': 1},
        {'name': 'N Seoul Tower', 'type': 'monument', 'lat': 37.5512, 'lon': 126.9882, 'priority': 2},
        {'name': 'Myeongdong', 'type': 'attraction', 'lat': 37.5636, 'lon': 126.9826, 'priority': 3},
        {'name': 'Bukchon Hanok Village', 'type': 'attraction', 'lat': 37.5816, 'lon': 126.9840, 'priority': 4},
        {'name': 'DMZ', 'type': 'attraction', 'lat': 37.9564, 'lon': 126.7186, 'priority': 5},
        {'name': 'Insadong', 'type': 'attraction', 'lat': 37.5735, 'lon': 126.9860, 'priority': 6},
        {'name': 'Lotte World', 'type': 'attraction', 'lat': 37.5111, 'lon': 127.0980, 'priority': 7},
        {'name': 'Changdeokgung Palace', 'type': 'monument', 'lat': 37.5794, 'lon': 126.9910, 'priority': 8},
    ],
    
    # Beijing - Ancient Capital
    'beijing': [
        {'name': 'Great Wall of China', 'type': 'monument', 'lat': 40.4319, 'lon': 116.5704, 'priority': 1},
        {'name': 'Forbidden City', 'type': 'monument', 'lat': 39.9163, 'lon': 116.3972, 'priority': 2},
        {'name': 'Tiananmen Square', 'type': 'attraction', 'lat': 39.9037, 'lon': 116.3974, 'priority': 3},
        {'name': 'Temple of Heaven', 'type': 'monument', 'lat': 39.8832, 'lon': 116.4065, 'priority': 4},
        {'name': 'Summer Palace', 'type': 'monument', 'lat': 39.9990, 'lon': 116.2750, 'priority': 5},
        {'name': 'Beijing Hutongs', 'type': 'attraction', 'lat': 39.9042, 'lon': 116.4074, 'priority': 6},
        {'name': 'Lama Temple', 'type': 'monument', 'lat': 39.9476, 'lon': 116.4189, 'priority': 7},
        {'name': '798 Art Zone', 'type': 'attraction', 'lat': 39.9834, 'lon': 116.4944, 'priority': 8},
    ],
    
    # Shanghai - Pearl of the Orient
    'shanghai': [
        {'name': 'The Bund', 'type': 'attraction', 'lat': 31.2397, 'lon': 121.4994, 'priority': 1},
        {'name': 'Oriental Pearl Tower', 'type': 'monument', 'lat': 31.2397, 'lon': 121.4994, 'priority': 2},
        {'name': 'Yu Garden', 'type': 'park', 'lat': 31.2269, 'lon': 121.4928, 'priority': 3},
        {'name': 'Shanghai Museum', 'type': 'museum', 'lat': 31.2304, 'lon': 121.4692, 'priority': 4},
        {'name': 'Jade Buddha Temple', 'type': 'monument', 'lat': 31.2471, 'lon': 121.4450, 'priority': 5},
        {'name': 'Nanjing Road', 'type': 'attraction', 'lat': 31.2342, 'lon': 121.4750, 'priority': 6},
        {'name': 'Shanghai Disneyland', 'type': 'attraction', 'lat': 31.1443, 'lon': 121.6570, 'priority': 7},
        {'name': 'Tianzifang', 'type': 'attraction', 'lat': 31.2100, 'lon': 121.4650, 'priority': 8},
    ],
    
    # ========== AMERICAS ==========
    
    # New York - The Big Apple
    'new york': [
        {'name': 'Statue of Liberty', 'type': 'monument', 'lat': 40.6892, 'lon': -74.0445, 'priority': 1},
        {'name': 'Empire State Building', 'type': 'monument', 'lat': 40.7484, 'lon': -73.9857, 'priority': 2},
        {'name': 'Central Park', 'type': 'park', 'lat': 40.7829, 'lon': -73.9654, 'priority': 3},
        {'name': 'Times Square', 'type': 'attraction', 'lat': 40.7580, 'lon': -73.9855, 'priority': 4},
        {'name': 'Brooklyn Bridge', 'type': 'monument', 'lat': 40.7061, 'lon': -73.9969, 'priority': 5},
        {'name': 'Metropolitan Museum of Art', 'type': 'museum', 'lat': 40.7794, 'lon': -73.9632, 'priority': 6},
        {'name': 'One World Trade Center', 'type': 'monument', 'lat': 40.7127, 'lon': -74.0134, 'priority': 7},
        {'name': 'High Line', 'type': 'park', 'lat': 40.7480, 'lon': -74.0048, 'priority': 8},
    ],
    
    # Los Angeles - City of Angels
    'los angeles': [
        {'name': 'Hollywood Sign', 'type': 'monument', 'lat': 34.1341, 'lon': -118.3215, 'priority': 1},
        {'name': 'Universal Studios', 'type': 'attraction', 'lat': 34.1381, 'lon': -118.3534, 'priority': 2},
        {'name': 'Santa Monica Pier', 'type': 'attraction', 'lat': 34.0089, 'lon': -118.4973, 'priority': 3},
        {'name': 'Griffith Observatory', 'type': 'monument', 'lat': 34.1184, 'lon': -118.3004, 'priority': 4},
        {'name': 'Venice Beach', 'type': 'attraction', 'lat': 33.9850, 'lon': -118.4695, 'priority': 5},
        {'name': 'Disneyland', 'type': 'attraction', 'lat': 33.8121, 'lon': -117.9190, 'priority': 6},
        {'name': 'Hollywood Walk of Fame', 'type': 'attraction', 'lat': 34.1016, 'lon': -118.3267, 'priority': 7},
        {'name': 'Getty Center', 'type': 'museum', 'lat': 34.0781, 'lon': -118.4742, 'priority': 8},
    ],
    
    # San Francisco - City by the Bay
    'san francisco': [
        {'name': 'Golden Gate Bridge', 'type': 'monument', 'lat': 37.8199, 'lon': -122.4783, 'priority': 1},
        {'name': 'Alcatraz Island', 'type': 'monument', 'lat': 37.8267, 'lon': -122.4230, 'priority': 2},
        {'name': 'Fishermans Wharf', 'type': 'attraction', 'lat': 37.8080, 'lon': -122.4177, 'priority': 3},
        {'name': 'Lombard Street', 'type': 'attraction', 'lat': 37.8021, 'lon': -122.4186, 'priority': 4},
        {'name': 'Cable Cars', 'type': 'attraction', 'lat': 37.7946, 'lon': -122.4094, 'priority': 5},
        {'name': 'Golden Gate Park', 'type': 'park', 'lat': 37.7694, 'lon': -122.4862, 'priority': 6},
        {'name': 'Chinatown', 'type': 'attraction', 'lat': 37.7941, 'lon': -122.4078, 'priority': 7},
        {'name': 'Palace of Fine Arts', 'type': 'monument', 'lat': 37.8024, 'lon': -122.4488, 'priority': 8},
    ],
    
    # Rio de Janeiro - Marvelous City
    'rio de janeiro': [
        {'name': 'Christ the Redeemer', 'type': 'monument', 'lat': -22.9519, 'lon': -43.2105, 'priority': 1},
        {'name': 'Copacabana Beach', 'type': 'attraction', 'lat': -22.9711, 'lon': -43.1822, 'priority': 2},
        {'name': 'Sugarloaf Mountain', 'type': 'attraction', 'lat': -22.9494, 'lon': -43.1553, 'priority': 3},
        {'name': 'Ipanema Beach', 'type': 'attraction', 'lat': -22.9838, 'lon': -43.1992, 'priority': 4},
        {'name': 'Maracanã Stadium', 'type': 'monument', 'lat': -22.9121, 'lon': -43.2302, 'priority': 5},
        {'name': 'Tijuca Forest', 'type': 'park', 'lat': -22.9500, 'lon': -43.2333, 'priority': 6},
        {'name': 'Selarón Steps', 'type': 'monument', 'lat': -22.9147, 'lon': -43.1792, 'priority': 7},
        {'name': 'Santa Teresa', 'type': 'attraction', 'lat': -22.9200, 'lon': -43.1833, 'priority': 8},
    ],
    
    # Mexico City - Aztec Capital
    'mexico city': [
        {'name': 'Zócalo', 'type': 'attraction', 'lat': 19.4326, 'lon': -99.1332, 'priority': 1},
        {'name': 'National Palace', 'type': 'monument', 'lat': 19.4200, 'lon': -99.1319, 'priority': 2},
        {'name': 'Frida Kahlo Museum', 'type': 'museum', 'lat': 19.3550, 'lon': -99.1622, 'priority': 3},
        {'name': 'Chapultepec Park', 'type': 'park', 'lat': 19.4208, 'lon': -99.1817, 'priority': 4},
        {'name': 'Teotihuacan', 'type': 'monument', 'lat': 19.6925, 'lon': -98.8439, 'priority': 5},
        {'name': 'Xochimilco', 'type': 'attraction', 'lat': 19.2578, 'lon': -99.1036, 'priority': 6},
        {'name': 'Basilica of Guadalupe', 'type': 'monument', 'lat': 19.4847, 'lon': -99.1169, 'priority': 7},
        {'name': 'Anthropology Museum', 'type': 'museum', 'lat': 19.4260, 'lon': -99.1863, 'priority': 8},
    ],
    
    # ========== MIDDLE EAST & AFRICA ==========
    
    # Dubai - Modern Marvel
    'dubai': [
        {'name': 'Burj Khalifa', 'type': 'monument', 'lat': 25.1972, 'lon': 55.2744, 'priority': 1},
        {'name': 'Burj Al Arab', 'type': 'monument', 'lat': 25.1412, 'lon': 55.1853, 'priority': 2},
        {'name': 'Palm Jumeirah', 'type': 'attraction', 'lat': 25.1124, 'lon': 55.1390, 'priority': 3},
        {'name': 'Dubai Mall', 'type': 'attraction', 'lat': 25.1984, 'lon': 55.2794, 'priority': 4},
        {'name': 'Dubai Fountain', 'type': 'attraction', 'lat': 25.1972, 'lon': 55.2794, 'priority': 5},
        {'name': 'Dubai Marina', 'type': 'attraction', 'lat': 25.0767, 'lon': 55.1394, 'priority': 6},
        {'name': 'Dubai Museum', 'type': 'museum', 'lat': 25.2637, 'lon': 55.2972, 'priority': 7},
        {'name': 'Jumeirah Beach', 'type': 'attraction', 'lat': 25.1972, 'lon': 55.2278, 'priority': 8},
    ],
    
    # Cairo - City of a Thousand Minarets
    'cairo': [
        {'name': 'Great Pyramid of Giza', 'type': 'monument', 'lat': 29.9792, 'lon': 31.1342, 'priority': 1},
        {'name': 'Sphinx', 'type': 'monument', 'lat': 29.9753, 'lon': 31.1376, 'priority': 2},
        {'name': 'Egyptian Museum', 'type': 'museum', 'lat': 30.0478, 'lon': 31.2336, 'priority': 3},
        {'name': 'Khan el-Khalili', 'type': 'attraction', 'lat': 30.0475, 'lon': 31.2625, 'priority': 4},
        {'name': 'Nile River', 'type': 'attraction', 'lat': 30.0444, 'lon': 31.2357, 'priority': 5},
        {'name': 'Cairo Citadel', 'type': 'monument', 'lat': 30.0286, 'lon': 31.2597, 'priority': 6},
        {'name': 'Al-Azhar Mosque', 'type': 'monument', 'lat': 30.0456, 'lon': 31.2625, 'priority': 7},
        {'name': 'Coptic Cairo', 'type': 'attraction', 'lat': 30.0056, 'lon': 31.2303, 'priority': 8},
    ],
    
    # ========== OCEANIA ==========
    
    # Sydney - Harbor City
    'sydney': [
        {'name': 'Sydney Opera House', 'type': 'monument', 'lat': -33.8568, 'lon': 151.2153, 'priority': 1},
        {'name': 'Sydney Harbour Bridge', 'type': 'monument', 'lat': -33.8523, 'lon': 151.2108, 'priority': 2},
        {'name': 'Bondi Beach', 'type': 'attraction', 'lat': -33.8915, 'lon': 151.2767, 'priority': 3},
        {'name': 'Royal Botanic Garden', 'type': 'park', 'lat': -33.8642, 'lon': 151.2167, 'priority': 4},
        {'name': 'Darling Harbour', 'type': 'attraction', 'lat': -33.8705, 'lon': 151.2020, 'priority': 5},
        {'name': 'Taronga Zoo', 'type': 'zoo', 'lat': -33.8436, 'lon': 151.2408, 'priority': 6},
        {'name': 'The Rocks', 'type': 'attraction', 'lat': -33.8591, 'lon': 151.2090, 'priority': 7},
        {'name': 'Blue Mountains', 'type': 'attraction', 'lat': -33.7000, 'lon': 150.3000, 'priority': 8},
    ],
    
    # Melbourne - Cultural Capital
    'melbourne': [
        {'name': 'Federation Square', 'type': 'attraction', 'lat': -37.8183, 'lon': 144.9671, 'priority': 1},
        {'name': 'Royal Botanic Gardens', 'type': 'park', 'lat': -37.8304, 'lon': 144.9796, 'priority': 2},
        {'name': 'Melbourne Cricket Ground', 'type': 'monument', 'lat': -37.8200, 'lon': 144.9833, 'priority': 3},
        {'name': 'Great Ocean Road', 'type': 'attraction', 'lat': -38.6806, 'lon': 143.3906, 'priority': 4},
        {'name': 'St. Kilda Beach', 'type': 'attraction', 'lat': -37.8676, 'lon': 144.9780, 'priority': 5},
        {'name': 'Eureka Skydeck', 'type': 'monument', 'lat': -37.8200, 'lon': 144.9647, 'priority': 6},
        {'name': 'Queen Victoria Market', 'type': 'attraction', 'lat': -37.8076, 'lon': 144.9567, 'priority': 7},
        {'name': 'Yarra River', 'type': 'attraction', 'lat': -37.8183, 'lon': 144.9671, 'priority': 8},
    ],
    
    # ========== ADDITIONAL MAJOR CITIES WORLDWIDE ==========
    
    # ========== EUROPE (Additional) ==========
    
    # Athens - Ancient Capital
    'athens': [
        {'name': 'Acropolis', 'type': 'monument', 'lat': 37.9715, 'lon': 23.7267, 'priority': 1},
        {'name': 'Parthenon', 'type': 'monument', 'lat': 37.9715, 'lon': 23.7267, 'priority': 2},
        {'name': 'Plaka', 'type': 'attraction', 'lat': 37.9715, 'lon': 23.7298, 'priority': 3},
    ],
    
    # Lisbon - City of Seven Hills
    'lisbon': [
        {'name': 'Belém Tower', 'type': 'monument', 'lat': 38.6916, 'lon': -9.2160, 'priority': 1},
        {'name': 'Jerónimos Monastery', 'type': 'monument', 'lat': 38.6979, 'lon': -9.2065, 'priority': 2},
        {'name': 'Alfama District', 'type': 'attraction', 'lat': 38.7108, 'lon': -9.1296, 'priority': 3},
    ],
    
    # Edinburgh - Scottish Capital
    'edinburgh': [
        {'name': 'Edinburgh Castle', 'type': 'monument', 'lat': 55.9486, 'lon': -3.2008, 'priority': 1},
        {'name': 'Royal Mile', 'type': 'attraction', 'lat': 55.9500, 'lon': -3.1900, 'priority': 2},
        {'name': 'Arthur\'s Seat', 'type': 'attraction', 'lat': 55.9444, 'lon': -3.1617, 'priority': 3},
    ],
    
    # Dublin - Irish Capital
    'dublin': [
        {'name': 'Trinity College', 'type': 'monument', 'lat': 53.3438, 'lon': -6.2546, 'priority': 1},
        {'name': 'Guinness Storehouse', 'type': 'attraction', 'lat': 53.3419, 'lon': -6.2864, 'priority': 2},
        {'name': 'Temple Bar', 'type': 'attraction', 'lat': 53.3450, 'lon': -6.2600, 'priority': 3},
    ],
    
    # Stockholm - Nordic Capital
    'stockholm': [
        {'name': 'Gamla Stan', 'type': 'attraction', 'lat': 59.3250, 'lon': 18.0700, 'priority': 1},
        {'name': 'Vasa Museum', 'type': 'museum', 'lat': 59.3280, 'lon': 18.0914, 'priority': 2},
        {'name': 'Royal Palace', 'type': 'monument', 'lat': 59.3269, 'lon': 18.0717, 'priority': 3},
    ],
    
    # Copenhagen - Danish Capital
    'copenhagen': [
        {'name': 'Nyhavn', 'type': 'attraction', 'lat': 55.6794, 'lon': 12.5886, 'priority': 1},
        {'name': 'Tivoli Gardens', 'type': 'park', 'lat': 55.6736, 'lon': 12.5684, 'priority': 2},
        {'name': 'The Little Mermaid', 'type': 'monument', 'lat': 55.6929, 'lon': 12.5994, 'priority': 3},
    ],
    
    # Warsaw - Polish Capital
    'warsaw': [
        {'name': 'Old Town', 'type': 'attraction', 'lat': 52.2298, 'lon': 21.0118, 'priority': 1},
        {'name': 'Royal Castle', 'type': 'monument', 'lat': 52.2477, 'lon': 21.0144, 'priority': 2},
        {'name': 'Warsaw Uprising Museum', 'type': 'museum', 'lat': 52.2322, 'lon': 20.9956, 'priority': 3},
    ],
    
    # Budapest - Pearl of the Danube
    'budapest': [
        {'name': 'Buda Castle', 'type': 'monument', 'lat': 47.4960, 'lon': 19.0392, 'priority': 1},
        {'name': 'Parliament Building', 'type': 'monument', 'lat': 47.5071, 'lon': 19.0456, 'priority': 2},
        {'name': 'Chain Bridge', 'type': 'monument', 'lat': 47.4984, 'lon': 19.0436, 'priority': 3},
    ],
    
    # Florence - Renaissance City
    'florence': [
        {'name': 'Duomo', 'type': 'monument', 'lat': 43.7731, 'lon': 11.2560, 'priority': 1},
        {'name': 'Uffizi Gallery', 'type': 'museum', 'lat': 43.7678, 'lon': 11.2553, 'priority': 2},
        {'name': 'Ponte Vecchio', 'type': 'monument', 'lat': 43.7679, 'lon': 11.2530, 'priority': 3},
    ],
    
    # Venice - City of Canals
    'venice': [
        {'name': 'St. Mark\'s Square', 'type': 'attraction', 'lat': 45.4342, 'lon': 12.3388, 'priority': 1},
        {'name': 'Grand Canal', 'type': 'attraction', 'lat': 45.4378, 'lon': 12.3155, 'priority': 2},
        {'name': 'Rialto Bridge', 'type': 'monument', 'lat': 45.4380, 'lon': 12.3358, 'priority': 3},
    ],
    
    # Milan - Fashion Capital
    'milan': [
        {'name': 'Duomo di Milano', 'type': 'monument', 'lat': 45.4642, 'lon': 9.1914, 'priority': 1},
        {'name': 'The Last Supper', 'type': 'monument', 'lat': 45.4659, 'lon': 9.1708, 'priority': 2},
        {'name': 'Galleria Vittorio Emanuele II', 'type': 'attraction', 'lat': 45.4654, 'lon': 9.1900, 'priority': 3},
    ],
    
    # ========== ASIA (Additional) ==========
    
    # Kuala Lumpur - Malaysian Capital
    'kuala lumpur': [
        {'name': 'Petronas Twin Towers', 'type': 'monument', 'lat': 3.1579, 'lon': 101.7116, 'priority': 1},
        {'name': 'Batu Caves', 'type': 'monument', 'lat': 3.2373, 'lon': 101.6839, 'priority': 2},
        {'name': 'Merdeka Square', 'type': 'attraction', 'lat': 3.1481, 'lon': 101.6952, 'priority': 3},
    ],
    
    # Jakarta - Indonesian Capital
    'jakarta': [
        {'name': 'National Monument', 'type': 'monument', 'lat': -6.1751, 'lon': 106.8650, 'priority': 1},
        {'name': 'Istiqlal Mosque', 'type': 'monument', 'lat': -6.1699, 'lon': 106.8314, 'priority': 2},
        {'name': 'Old Town (Kota Tua)', 'type': 'attraction', 'lat': -6.1352, 'lon': 106.8133, 'priority': 3},
    ],
    
    # Manila - Philippine Capital
    'manila': [
        {'name': 'Intramuros', 'type': 'monument', 'lat': 14.5906, 'lon': 120.9750, 'priority': 1},
        {'name': 'Rizal Park', 'type': 'park', 'lat': 14.5832, 'lon': 120.9797, 'priority': 2},
        {'name': 'Manila Cathedral', 'type': 'monument', 'lat': 14.5912, 'lon': 120.9739, 'priority': 3},
    ],
    
    # Ho Chi Minh City - Vietnamese Metropolis
    'ho chi minh city': [
        {'name': 'War Remnants Museum', 'type': 'museum', 'lat': 10.7793, 'lon': 106.6927, 'priority': 1},
        {'name': 'Notre-Dame Cathedral', 'type': 'monument', 'lat': 10.7797, 'lon': 106.6992, 'priority': 2},
        {'name': 'Ben Thanh Market', 'type': 'attraction', 'lat': 10.7720, 'lon': 106.6983, 'priority': 3},
    ],
    
    # Hanoi - Vietnamese Capital
    'hanoi': [
        {'name': 'Hoan Kiem Lake', 'type': 'attraction', 'lat': 21.0285, 'lon': 105.8542, 'priority': 1},
        {'name': 'Temple of Literature', 'type': 'monument', 'lat': 21.0267, 'lon': 105.8356, 'priority': 2},
        {'name': 'Old Quarter', 'type': 'attraction', 'lat': 21.0333, 'lon': 105.8500, 'priority': 3},
    ],
    
    # Taipei - Taiwanese Capital
    'taipei': [
        {'name': 'Taipei 101', 'type': 'monument', 'lat': 25.0340, 'lon': 121.5645, 'priority': 1},
        {'name': 'National Palace Museum', 'type': 'museum', 'lat': 25.1024, 'lon': 121.5485, 'priority': 2},
        {'name': 'Longshan Temple', 'type': 'monument', 'lat': 25.0364, 'lon': 121.4998, 'priority': 3},
    ],
    
    # Osaka - Japanese Metropolis
    'osaka': [
        {'name': 'Osaka Castle', 'type': 'monument', 'lat': 34.6873, 'lon': 135.5259, 'priority': 1},
        {'name': 'Dotonbori', 'type': 'attraction', 'lat': 34.6698, 'lon': 135.5006, 'priority': 2},
        {'name': 'Universal Studios Japan', 'type': 'attraction', 'lat': 34.6654, 'lon': 135.4322, 'priority': 3},
    ],
    
    # Kyoto - Ancient Capital
    'kyoto': [
        {'name': 'Fushimi Inari Shrine', 'type': 'monument', 'lat': 34.9671, 'lon': 135.7727, 'priority': 1},
        {'name': 'Kinkaku-ji (Golden Pavilion)', 'type': 'monument', 'lat': 35.0394, 'lon': 135.7299, 'priority': 2},
        {'name': 'Arashiyama Bamboo Grove', 'type': 'attraction', 'lat': 35.0094, 'lon': 135.6772, 'priority': 3},
    ],
    
    # Chennai - Indian Metropolis
    'chennai': [
        {'name': 'Marina Beach', 'type': 'attraction', 'lat': 13.0475, 'lon': 80.2827, 'priority': 1},
        {'name': 'Kapaleeshwarar Temple', 'type': 'monument', 'lat': 13.0330, 'lon': 80.2707, 'priority': 2},
        {'name': 'Fort St. George', 'type': 'monument', 'lat': 13.0800, 'lon': 80.2897, 'priority': 3},
    ],
    
    # Kolkata - Cultural Capital
    'kolkata': [
        {'name': 'Victoria Memorial', 'type': 'monument', 'lat': 22.5448, 'lon': 88.3426, 'priority': 1},
        {'name': 'Howrah Bridge', 'type': 'monument', 'lat': 22.5950, 'lon': 88.3436, 'priority': 2},
        {'name': 'Dakshineswar Kali Temple', 'type': 'monument', 'lat': 22.6550, 'lon': 88.3578, 'priority': 3},
    ],
    
    # Hyderabad - City of Pearls
    'hyderabad': [
        {'name': 'Charminar', 'type': 'monument', 'lat': 17.3616, 'lon': 78.4747, 'priority': 1},
        {'name': 'Golconda Fort', 'type': 'monument', 'lat': 17.3833, 'lon': 78.4011, 'priority': 2},
        {'name': 'Hussain Sagar Lake', 'type': 'attraction', 'lat': 17.4239, 'lon': 78.4738, 'priority': 3},
    ],
    
    # Pune - Cultural Hub
    'pune': [
        {'name': 'Shaniwar Wada', 'type': 'monument', 'lat': 18.5204, 'lon': 73.8567, 'priority': 1},
        {'name': 'Aga Khan Palace', 'type': 'monument', 'lat': 18.5522, 'lon': 73.9014, 'priority': 2},
        {'name': 'Sinhagad Fort', 'type': 'monument', 'lat': 18.3667, 'lon': 73.7500, 'priority': 3},
    ],
    
    # Jaipur - Pink City
    'jaipur': [
        {'name': 'Hawa Mahal', 'type': 'monument', 'lat': 26.9239, 'lon': 75.8267, 'priority': 1},
        {'name': 'Amber Fort', 'type': 'monument', 'lat': 26.9855, 'lon': 75.8513, 'priority': 2},
        {'name': 'City Palace', 'type': 'monument', 'lat': 26.9258, 'lon': 75.8236, 'priority': 3},
    ],
    
    # Agra - Taj City
    'agra': [
        {'name': 'Taj Mahal', 'type': 'monument', 'lat': 27.1751, 'lon': 78.0421, 'priority': 1},
        {'name': 'Agra Fort', 'type': 'monument', 'lat': 27.1795, 'lon': 78.0211, 'priority': 2},
        {'name': 'Fatehpur Sikri', 'type': 'monument', 'lat': 27.0945, 'lon': 77.6610, 'priority': 3},
    ],
    
    # ========== AMERICAS (Additional) ==========
    
    # Chicago - Windy City
    'chicago': [
        {'name': 'Willis Tower', 'type': 'monument', 'lat': 41.8789, 'lon': -87.6359, 'priority': 1},
        {'name': 'Millennium Park', 'type': 'park', 'lat': 41.8825, 'lon': -87.6240, 'priority': 2},
        {'name': 'Navy Pier', 'type': 'attraction', 'lat': 41.8917, 'lon': -87.6081, 'priority': 3},
    ],
    
    # Miami - Magic City
    'miami': [
        {'name': 'South Beach', 'type': 'attraction', 'lat': 25.7907, 'lon': -80.1300, 'priority': 1},
        {'name': 'Art Deco Historic District', 'type': 'attraction', 'lat': 25.7907, 'lon': -80.1300, 'priority': 2},
        {'name': 'Vizcaya Museum', 'type': 'museum', 'lat': 25.7430, 'lon': -80.2106, 'priority': 3},
    ],
    
    # Las Vegas - Entertainment Capital
    'las vegas': [
        {'name': 'Las Vegas Strip', 'type': 'attraction', 'lat': 36.1215, 'lon': -115.1739, 'priority': 1},
        {'name': 'Bellagio Fountains', 'type': 'attraction', 'lat': 36.1125, 'lon': -115.1750, 'priority': 2},
        {'name': 'Fremont Street Experience', 'type': 'attraction', 'lat': 36.1699, 'lon': -115.1398, 'priority': 3},
    ],
    
    # Toronto - Canadian Metropolis
    'toronto': [
        {'name': 'CN Tower', 'type': 'monument', 'lat': 43.6426, 'lon': -79.3871, 'priority': 1},
        {'name': 'Royal Ontario Museum', 'type': 'museum', 'lat': 43.6677, 'lon': -79.3948, 'priority': 2},
        {'name': 'Distillery District', 'type': 'attraction', 'lat': 43.6509, 'lon': -79.3606, 'priority': 3},
    ],
    
    # Vancouver - Pacific Gateway
    'vancouver': [
        {'name': 'Stanley Park', 'type': 'park', 'lat': 49.3043, 'lon': -123.1443, 'priority': 1},
        {'name': 'Capilano Suspension Bridge', 'type': 'attraction', 'lat': 49.3427, 'lon': -123.1149, 'priority': 2},
        {'name': 'Granville Island', 'type': 'attraction', 'lat': 49.2713, 'lon': -123.1340, 'priority': 3},
    ],
    
    # Montreal - French Canadian City
    'montreal': [
        {'name': 'Notre-Dame Basilica', 'type': 'monument', 'lat': 45.5046, 'lon': -73.5563, 'priority': 1},
        {'name': 'Old Montreal', 'type': 'attraction', 'lat': 45.5088, 'lon': -73.5540, 'priority': 2},
        {'name': 'Mount Royal Park', 'type': 'park', 'lat': 45.5048, 'lon': -73.5878, 'priority': 3},
    ],
    
    # Buenos Aires - Argentine Capital
    'buenos aires': [
        {'name': 'La Recoleta Cemetery', 'type': 'monument', 'lat': -34.5875, 'lon': -58.3933, 'priority': 1},
        {'name': 'Teatro Colón', 'type': 'theatre', 'lat': -34.6014, 'lon': -58.3835, 'priority': 2},
        {'name': 'Caminito', 'type': 'attraction', 'lat': -34.6411, 'lon': -58.3656, 'priority': 3},
    ],
    
    # Lima - Peruvian Capital
    'lima': [
        {'name': 'Historic Centre', 'type': 'attraction', 'lat': -12.0464, 'lon': -77.0428, 'priority': 1},
        {'name': 'Larco Museum', 'type': 'museum', 'lat': -12.0756, 'lon': -77.0706, 'priority': 2},
        {'name': 'Miraflores', 'type': 'attraction', 'lat': -12.1194, 'lon': -77.0303, 'priority': 3},
    ],
    
    # Santiago - Chilean Capital
    'santiago': [
        {'name': 'San Cristóbal Hill', 'type': 'attraction', 'lat': -33.4250, 'lon': -70.6333, 'priority': 1},
        {'name': 'Plaza de Armas', 'type': 'attraction', 'lat': -33.4378, 'lon': -70.6506, 'priority': 2},
        {'name': 'La Moneda Palace', 'type': 'monument', 'lat': -33.4419, 'lon': -70.6539, 'priority': 3},
    ],
    
    # ========== MIDDLE EAST & AFRICA (Additional) ==========
    
    # Tel Aviv - Israeli Metropolis
    'tel aviv': [
        {'name': 'Old Jaffa', 'type': 'attraction', 'lat': 32.0550, 'lon': 34.7597, 'priority': 1},
        {'name': 'Tel Aviv Beaches', 'type': 'attraction', 'lat': 32.0853, 'lon': 34.7818, 'priority': 2},
        {'name': 'Carmel Market', 'type': 'attraction', 'lat': 32.0642, 'lon': 34.7706, 'priority': 3},
    ],
    
    # Jerusalem - Holy City
    'jerusalem': [
        {'name': 'Western Wall', 'type': 'monument', 'lat': 31.7767, 'lon': 35.2345, 'priority': 1},
        {'name': 'Church of the Holy Sepulchre', 'type': 'monument', 'lat': 31.7784, 'lon': 35.2297, 'priority': 2},
        {'name': 'Dome of the Rock', 'type': 'monument', 'lat': 31.7781, 'lon': 35.2354, 'priority': 3},
    ],
    
    # Doha - Qatari Capital
    'doha': [
        {'name': 'Museum of Islamic Art', 'type': 'museum', 'lat': 25.2924, 'lon': 51.5414, 'priority': 1},
        {'name': 'Souq Waqif', 'type': 'attraction', 'lat': 25.2886, 'lon': 51.5331, 'priority': 2},
        {'name': 'The Pearl-Qatar', 'type': 'attraction', 'lat': 25.3678, 'lon': 51.5500, 'priority': 3},
    ],
    
    # Abu Dhabi - UAE Capital
    'abu dhabi': [
        {'name': 'Sheikh Zayed Grand Mosque', 'type': 'monument', 'lat': 24.4129, 'lon': 54.4750, 'priority': 1},
        {'name': 'Louvre Abu Dhabi', 'type': 'museum', 'lat': 24.5333, 'lon': 54.4000, 'priority': 2},
        {'name': 'Yas Island', 'type': 'attraction', 'lat': 24.5333, 'lon': 54.6000, 'priority': 3},
    ],
    
    # Riyadh - Saudi Capital
    'riyadh': [
        {'name': 'Kingdom Centre', 'type': 'monument', 'lat': 24.7136, 'lon': 46.6753, 'priority': 1},
        {'name': 'Masmak Fortress', 'type': 'monument', 'lat': 24.6333, 'lon': 46.7167, 'priority': 2},
        {'name': 'National Museum', 'type': 'museum', 'lat': 24.6475, 'lon': 46.7214, 'priority': 3},
    ],
    
    # Johannesburg - South African Metropolis
    'johannesburg': [
        {'name': 'Apartheid Museum', 'type': 'museum', 'lat': -26.2389, 'lon': 28.0069, 'priority': 1},
        {'name': 'Soweto', 'type': 'attraction', 'lat': -26.2678, 'lon': 27.8585, 'priority': 2},
        {'name': 'Gold Reef City', 'type': 'attraction', 'lat': -26.2389, 'lon': 28.0069, 'priority': 3},
    ],
    
    # Cape Town - Mother City
    'cape town': [
        {'name': 'Table Mountain', 'type': 'attraction', 'lat': -33.9625, 'lon': 18.4106, 'priority': 1},
        {'name': 'Robben Island', 'type': 'monument', 'lat': -33.8067, 'lon': 18.3667, 'priority': 2},
        {'name': 'V&A Waterfront', 'type': 'attraction', 'lat': -33.9048, 'lon': 18.4241, 'priority': 3},
    ],
    
    # Nairobi - Kenyan Capital
    'nairobi': [
        {'name': 'Nairobi National Park', 'type': 'park', 'lat': -1.2921, 'lon': 36.8219, 'priority': 1},
        {'name': 'Giraffe Centre', 'type': 'attraction', 'lat': -1.3656, 'lon': 36.7364, 'priority': 2},
        {'name': 'Karen Blixen Museum', 'type': 'museum', 'lat': -1.3194, 'lon': 36.7125, 'priority': 3},
    ],
    
    # Marrakech - Red City
    'marrakech': [
        {'name': 'Jemaa el-Fnaa', 'type': 'attraction', 'lat': 31.6258, 'lon': -7.9891, 'priority': 1},
        {'name': 'Bahia Palace', 'type': 'monument', 'lat': 31.6200, 'lon': -7.9811, 'priority': 2},
        {'name': 'Koutoubia Mosque', 'type': 'monument', 'lat': 31.6239, 'lon': -7.9936, 'priority': 3},
    ],
    
    # Casablanca - Moroccan Metropolis
    'casablanca': [
        {'name': 'Hassan II Mosque', 'type': 'monument', 'lat': 33.6083, 'lon': -7.6328, 'priority': 1},
        {'name': 'Old Medina', 'type': 'attraction', 'lat': 33.5731, 'lon': -7.5897, 'priority': 2},
        {'name': 'Corniche', 'type': 'attraction', 'lat': 33.6000, 'lon': -7.6167, 'priority': 3},
    ],
    
    # ========== OCEANIA (Additional) ==========
    
    # Auckland - New Zealand's Largest
    'auckland': [
        {'name': 'Sky Tower', 'type': 'monument', 'lat': -36.8485, 'lon': 174.7633, 'priority': 1},
        {'name': 'Auckland Harbour Bridge', 'type': 'monument', 'lat': -36.8250, 'lon': 174.7500, 'priority': 2},
        {'name': 'Waiheke Island', 'type': 'attraction', 'lat': -36.7950, 'lon': 175.0167, 'priority': 3},
    ],
    
    # Wellington - New Zealand Capital
    'wellington': [
        {'name': 'Te Papa Museum', 'type': 'museum', 'lat': -41.2906, 'lon': 174.7822, 'priority': 1},
        {'name': 'Cable Car', 'type': 'attraction', 'lat': -41.2767, 'lon': 174.7678, 'priority': 2},
        {'name': 'Zealandia', 'type': 'park', 'lat': -41.2906, 'lon': 174.7500, 'priority': 3},
    ],
    
    # Brisbane - Australian Metropolis
    'brisbane': [
        {'name': 'South Bank Parklands', 'type': 'park', 'lat': -27.4748, 'lon': 153.0170, 'priority': 1},
        {'name': 'Lone Pine Koala Sanctuary', 'type': 'zoo', 'lat': -27.5300, 'lon': 152.9700, 'priority': 2},
        {'name': 'Story Bridge', 'type': 'monument', 'lat': -27.4700, 'lon': 153.0333, 'priority': 3},
    ],
    
    # Perth - Western Australian Capital
    'perth': [
        {'name': 'Kings Park', 'type': 'park', 'lat': -31.9605, 'lon': 115.8409, 'priority': 1},
        {'name': 'Swan River', 'type': 'attraction', 'lat': -31.9505, 'lon': 115.8605, 'priority': 2},
        {'name': 'Fremantle', 'type': 'attraction', 'lat': -32.0567, 'lon': 115.7472, 'priority': 3},
    ],
    
    # ========== ADDITIONAL ASIAN CITIES ==========
    
    # Kathmandu - Nepalese Capital
    'kathmandu': [
        {'name': 'Swayambhunath Stupa', 'type': 'monument', 'lat': 27.7149, 'lon': 85.2903, 'priority': 1},
        {'name': 'Durbar Square', 'type': 'attraction', 'lat': 27.7044, 'lon': 85.3078, 'priority': 2},
        {'name': 'Pashupatinath Temple', 'type': 'monument', 'lat': 27.7106, 'lon': 85.3486, 'priority': 3},
    ],
    
    # Colombo - Sri Lankan Capital
    'colombo': [
        {'name': 'Gangaramaya Temple', 'type': 'monument', 'lat': 6.9271, 'lon': 79.8612, 'priority': 1},
        {'name': 'Galle Face Green', 'type': 'park', 'lat': 6.9271, 'lon': 79.8450, 'priority': 2},
        {'name': 'National Museum', 'type': 'museum', 'lat': 6.9106, 'lon': 79.8608, 'priority': 3},
    ],
    
    # Dhaka - Bangladeshi Capital
    'dhaka': [
        {'name': 'Lalbagh Fort', 'type': 'monument', 'lat': 23.7183, 'lon': 90.3886, 'priority': 1},
        {'name': 'Ahsan Manzil', 'type': 'monument', 'lat': 23.7104, 'lon': 90.4074, 'priority': 2},
        {'name': 'National Parliament House', 'type': 'monument', 'lat': 23.7625, 'lon': 90.3781, 'priority': 3},
    ],
    
    # Yangon - Myanmar Capital
    'yangon': [
        {'name': 'Shwedagon Pagoda', 'type': 'monument', 'lat': 16.7983, 'lon': 96.1494, 'priority': 1},
        {'name': 'Sule Pagoda', 'type': 'monument', 'lat': 16.7742, 'lon': 96.1586, 'priority': 2},
        {'name': 'Bogyoke Aung San Market', 'type': 'attraction', 'lat': 16.7850, 'lon': 96.1567, 'priority': 3},
    ],
    
    # Phnom Penh - Cambodian Capital
    'phnom penh': [
        {'name': 'Royal Palace', 'type': 'monument', 'lat': 11.5564, 'lon': 104.9282, 'priority': 1},
        {'name': 'Tuol Sleng Genocide Museum', 'type': 'museum', 'lat': 11.5494, 'lon': 104.9175, 'priority': 2},
        {'name': 'Wat Phnom', 'type': 'monument', 'lat': 11.5764, 'lon': 104.9231, 'priority': 3},
    ],
    
    # Vientiane - Laotian Capital
    'vientiane': [
        {'name': 'Pha That Luang', 'type': 'monument', 'lat': 17.9750, 'lon': 102.6331, 'priority': 1},
        {'name': 'Patuxai', 'type': 'monument', 'lat': 17.9756, 'lon': 102.6144, 'priority': 2},
        {'name': 'Wat Si Saket', 'type': 'monument', 'lat': 17.9581, 'lon': 102.6147, 'priority': 3},
    ],
    
    # ========== ADDITIONAL EUROPEAN CITIES ==========
    
    # Brussels - European Capital
    'brussels': [
        {'name': 'Grand Place', 'type': 'attraction', 'lat': 50.8466, 'lon': 4.3528, 'priority': 1},
        {'name': 'Atomium', 'type': 'monument', 'lat': 50.8949, 'lon': 4.3414, 'priority': 2},
        {'name': 'Manneken Pis', 'type': 'monument', 'lat': 50.8450, 'lon': 4.3497, 'priority': 3},
    ],
    
    # Amsterdam - Already exists, skip
    
    # Zurich - Swiss Metropolis
    'zurich': [
        {'name': 'Old Town', 'type': 'attraction', 'lat': 47.3769, 'lon': 8.5417, 'priority': 1},
        {'name': 'Lake Zurich', 'type': 'attraction', 'lat': 47.3667, 'lon': 8.5500, 'priority': 2},
        {'name': 'Swiss National Museum', 'type': 'museum', 'lat': 47.3786, 'lon': 8.5481, 'priority': 3},
    ],
    
    # Geneva - International City
    'geneva': [
        {'name': 'Jet d\'Eau', 'type': 'monument', 'lat': 46.2078, 'lon': 6.1558, 'priority': 1},
        {'name': 'United Nations', 'type': 'monument', 'lat': 46.2260, 'lon': 6.1408, 'priority': 2},
        {'name': 'Old Town', 'type': 'attraction', 'lat': 46.2044, 'lon': 6.1432, 'priority': 3},
    ],
    
    # Oslo - Norwegian Capital
    'oslo': [
        {'name': 'Vigeland Park', 'type': 'park', 'lat': 59.9236, 'lon': 10.7000, 'priority': 1},
        {'name': 'Royal Palace', 'type': 'monument', 'lat': 59.9170, 'lon': 10.7276, 'priority': 2},
        {'name': 'Viking Ship Museum', 'type': 'museum', 'lat': 59.9042, 'lon': 10.6844, 'priority': 3},
    ],
    
    # Helsinki - Finnish Capital
    'helsinki': [
        {'name': 'Helsinki Cathedral', 'type': 'monument', 'lat': 60.1699, 'lon': 24.9524, 'priority': 1},
        {'name': 'Suomenlinna', 'type': 'monument', 'lat': 60.1478, 'lon': 24.9892, 'priority': 2},
        {'name': 'Market Square', 'type': 'attraction', 'lat': 60.1695, 'lon': 24.9522, 'priority': 3},
    ],
    
    # ========== ADDITIONAL AMERICAN CITIES ==========
    
    # Seattle - Emerald City
    'seattle': [
        {'name': 'Space Needle', 'type': 'monument', 'lat': 47.6205, 'lon': -122.3493, 'priority': 1},
        {'name': 'Pike Place Market', 'type': 'attraction', 'lat': 47.6085, 'lon': -122.3401, 'priority': 2},
        {'name': 'Chihuly Garden and Glass', 'type': 'museum', 'lat': 47.6205, 'lon': -122.3493, 'priority': 3},
    ],
    
    # Boston - Historic City
    'boston': [
        {'name': 'Freedom Trail', 'type': 'attraction', 'lat': 42.3601, 'lon': -71.0589, 'priority': 1},
        {'name': 'Fenway Park', 'type': 'monument', 'lat': 42.3467, 'lon': -71.0972, 'priority': 2},
        {'name': 'Harvard University', 'type': 'monument', 'lat': 42.3770, 'lon': -71.1167, 'priority': 3},
    ],
    
    # Washington DC - US Capital
    'washington dc': [
        {'name': 'White House', 'type': 'monument', 'lat': 38.8977, 'lon': -77.0365, 'priority': 1},
        {'name': 'Lincoln Memorial', 'type': 'monument', 'lat': 38.8893, 'lon': -77.0502, 'priority': 2},
        {'name': 'National Mall', 'type': 'park', 'lat': 38.8895, 'lon': -77.0233, 'priority': 3},
    ],
    
    # Philadelphia - City of Brotherly Love
    'philadelphia': [
        {'name': 'Liberty Bell', 'type': 'monument', 'lat': 39.9496, 'lon': -75.1503, 'priority': 1},
        {'name': 'Independence Hall', 'type': 'monument', 'lat': 39.9489, 'lon': -75.1500, 'priority': 2},
        {'name': 'Philadelphia Museum of Art', 'type': 'museum', 'lat': 39.9656, 'lon': -75.1810, 'priority': 3},
    ],
    
    # Atlanta - Southern Metropolis
    'atlanta': [
        {'name': 'Georgia Aquarium', 'type': 'attraction', 'lat': 33.7630, 'lon': -84.3947, 'priority': 1},
        {'name': 'World of Coca-Cola', 'type': 'museum', 'lat': 33.7629, 'lon': -84.3946, 'priority': 2},
        {'name': 'Centennial Olympic Park', 'type': 'park', 'lat': 33.7600, 'lon': -84.3933, 'priority': 3},
    ],
    
    # ========== ADDITIONAL MIDDLE EASTERN CITIES ==========
    
    # Muscat - Omani Capital
    'muscat': [
        {'name': 'Sultan Qaboos Grand Mosque', 'type': 'monument', 'lat': 23.5859, 'lon': 58.4059, 'priority': 1},
        {'name': 'Mutrah Souq', 'type': 'attraction', 'lat': 23.6175, 'lon': 58.5922, 'priority': 2},
        {'name': 'Royal Opera House', 'type': 'theatre', 'lat': 23.6142, 'lon': 58.5908, 'priority': 3},
    ],
    
    # Kuwait City - Kuwaiti Capital
    'kuwait city': [
        {'name': 'Kuwait Towers', 'type': 'monument', 'lat': 29.3375, 'lon': 48.0758, 'priority': 1},
        {'name': 'Grand Mosque', 'type': 'monument', 'lat': 29.3375, 'lon': 47.9758, 'priority': 2},
        {'name': 'Souq Mubarakiya', 'type': 'attraction', 'lat': 29.3750, 'lon': 47.9750, 'priority': 3},
    ],
    
    # ========== ADDITIONAL AFRICAN CITIES ==========
    
    # Lagos - Nigerian Metropolis
    'lagos': [
        {'name': 'Lekki Conservation Centre', 'type': 'park', 'lat': 6.4653, 'lon': 3.5314, 'priority': 1},
        {'name': 'National Museum', 'type': 'museum', 'lat': 6.4474, 'lon': 3.3947, 'priority': 2},
        {'name': 'Tarkwa Bay Beach', 'type': 'attraction', 'lat': 6.4167, 'lon': 3.4000, 'priority': 3},
    ],
    
    # Accra - Ghanaian Capital
    'accra': [
        {'name': 'Independence Square', 'type': 'attraction', 'lat': 5.5500, 'lon': -0.2000, 'priority': 1},
        {'name': 'Kwame Nkrumah Memorial Park', 'type': 'monument', 'lat': 5.5500, 'lon': -0.2000, 'priority': 2},
        {'name': 'Jamestown', 'type': 'attraction', 'lat': 5.5333, 'lon': -0.2167, 'priority': 3},
    ],
    
    # Dar es Salaam - Tanzanian Metropolis
    'dar es salaam': [
        {'name': 'National Museum', 'type': 'museum', 'lat': -6.8167, 'lon': 39.2833, 'priority': 1},
        {'name': 'Kivukoni Fish Market', 'type': 'attraction', 'lat': -6.8167, 'lon': 39.2833, 'priority': 2},
        {'name': 'Coco Beach', 'type': 'attraction', 'lat': -6.7500, 'lon': 39.2833, 'priority': 3},
    ],
}


def normalize_city_name(city_name: str) -> str:
    """Normalize city name for matching.
    
    Args:
        city_name: Original city name
        
    Returns:
        Normalized city name (lowercase, stripped, without country/state)
    """
    # Convert to lowercase and strip
    normalized = city_name.lower().strip()
    
    # Remove common suffixes (country names, state names, etc.)
    suffixes = [
        ', france', ', fr', ', usa', ', united states', ', us', ', uk', ', united kingdom',
        ', italy', ', it', ', spain', ', es', ', germany', ', de', ', japan', ', jp',
        ', china', ', cn', ', india', ', in', ', australia', ', au', ', brazil', ', br',
        ', russia', ', ru', ', turkey', ', tr', ', egypt', ', eg', ', thailand', ', th',
        ', singapore', ', sg', ', hong kong', ', hk', ', uae', ', emirates', ', ae',
        ', south korea', ', kr', ', mexico', ', mx', ', south africa', ', za',
        ', canada', ', ca', ', argentina', ', ar', ', chile', ', cl',
        ', greece', ', gr', ', portugal', ', pt', ', scotland', ', ireland', ', ie',
        ', sweden', ', se', ', denmark', ', dk', ', poland', ', pl', ', hungary', ', hu',
        ', malaysia', ', my', ', indonesia', ', id', ', philippines', ', ph', ', vietnam', ', vn',
        ', taiwan', ', tw', ', thailand', ', th', ', nepal', ', np', ', sri lanka', ', lk',
        ', bangladesh', ', bd', ', myanmar', ', mm', ', cambodia', ', kh', ', laos', ', la',
        ', new zealand', ', nz', ', morocco', ', ma', ', south africa', ', za', ', kenya', ', ke',
        ', tanzania', ', tz', ', ghana', ', gh', ', nigeria', ', ng', ', oman', ', om',
        ', kuwait', ', kw', ', israel', ', il', ', palestine', ', ps', ', qatar', ', qa',
        ', saudi arabia', ', sa', ', switzerland', ', ch', ', norway', ', no', ', finland', ', fi',
        ', belgium', ', be', ', netherlands', ', nl', ', austria', ', at', ', czech republic', ', cz',
        # Indian states
        ', karnataka', ', maharashtra', ', delhi', ', tamil nadu', ', west bengal',
        ', gujarat', ', rajasthan', ', punjab', ', haryana', ', uttar pradesh',
        ', andhra pradesh', ', telangana', ', kerala', ', odisha', ', bihar',
        # US states (common ones)
        ', california', ', new york', ', texas', ', florida', ', illinois',
        ', pennsylvania', ', ohio', ', georgia', ', north carolina', ', michigan'
    ]
    
    for suffix in suffixes:
        if normalized.endswith(suffix):
            normalized = normalized[:-len(suffix)].strip()
    
    # Remove extra whitespace
    normalized = ' '.join(normalized.split())
    
    return normalized


def get_famous_attractions(city_name: str, coordinates) -> list:
    """Get famous attractions for a city - TOURIST GUIDE MODE.
    
    This function acts as a professional tourist guide, ensuring
    the most iconic and must-see attractions are always returned.
    
    Args:
        city_name: Name of the city (case-insensitive, can include country)
        coordinates: Coordinates object with latitude and longitude
        
    Returns:
        List of attraction dictionaries sorted by priority, or empty list
    """
    # Normalize the city name
    normalized = normalize_city_name(city_name)
    
    # Try exact match first
    if normalized in FAMOUS_ATTRACTIONS:
        attractions = FAMOUS_ATTRACTIONS[normalized]
        # Sort by priority and return
        return sorted(attractions, key=lambda x: x.get('priority', 999))
    
    # Try partial matches (e.g., "paris, france" -> "paris")
    # Check if any key is contained in the normalized name or vice versa
    for key, attractions in FAMOUS_ATTRACTIONS.items():
        # Check if key is in normalized name (e.g., "bengaluru" in "bengaluru, karnataka")
        if key in normalized:
            return sorted(attractions, key=lambda x: x.get('priority', 999))
        # Check if normalized name is in key (for abbreviations)
        if normalized in key:
            return sorted(attractions, key=lambda x: x.get('priority', 999))
        # Check if they share the same first word (e.g., "bengaluru" matches "bengaluru")
        normalized_words = set(normalized.split())
        key_words = set(key.split())
        if normalized_words & key_words:  # If they share any words
            return sorted(attractions, key=lambda x: x.get('priority', 999))
    
    # Try matching first word (e.g., "new york" -> "new")
    first_word = normalized.split()[0] if normalized.split() else ''
    for key, attractions in FAMOUS_ATTRACTIONS.items():
        if key.startswith(first_word) or first_word in key:
            return sorted(attractions, key=lambda x: x.get('priority', 999))
    
    return []


def calculate_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """Calculate distance between two coordinates in kilometers."""
    import math
    R = 6371  # Earth radius in kilometers
    
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    
    a = (math.sin(dlat / 2) ** 2 +
         math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
         math.sin(dlon / 2) ** 2)
    c = 2 * math.asin(math.sqrt(a))
    
    return R * c


def is_famous_city(city_name: str) -> bool:
    """Check if city is in our famous attractions database.
    
    Args:
        city_name: Name of the city
        
    Returns:
        True if city has famous attractions, False otherwise
    """
    normalized = normalize_city_name(city_name)
    return normalized in FAMOUS_ATTRACTIONS or any(
        key in normalized or normalized in key 
        for key in FAMOUS_ATTRACTIONS.keys()
    )
