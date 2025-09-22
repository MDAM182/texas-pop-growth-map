- # Texas Service Areas & Population Growth

An interactive geospatial analysis of Texas communities where **CenterPoint Energy (gas)** and **Optimum Internet** both provide service. This project overlays utility service areas with **population growth trends** using U.S. Census estimates, helping identify regions with both infrastructure overlap and strong growth potential.  

## 🔗 Live Demo
👉 [View Interactive Map](https://mdam182.github.io/texas-pop-growth-map/)
*(Open on desktop or mobile for an interactive experience.)*

---

## 📊 Features
- Interactive **map** built with Folium:
  - Circle markers color-coded by population growth % (2020–2024).
  - Heatmap overlay for **all overlapping cities**.
  - Separate heatmap highlighting **Top 10 most populated cities**.
  - Custom legend and popups for clear interpretation.
- Clean, merged dataset (`CSV`) of overlapping communities with:
  - Service availability
  - Latitude/Longitude
  - Population growth metrics
- Visual analytics with **Matplotlib**:
  - Top 10 fastest-growing cities (2020–2024)
  - Top 10 most populated Texas cities (2024)

---

## 📂 Project Files
- `index.html` → Interactive map (GitHub Pages hosted)  
- `texas_both_services_data.csv` → Clean dataset of overlapping service areas  
- `population_growth_top10.png` → Chart of fastest-growing Texas cities  
- `top10_population_2024.png` → Chart of most populated Texas cities  

---

## 📸 Visualizations

### Top 10 Fastest Growing Cities (2020–2024)
![Top 10 Growth](population_growth_top10.png)

### Top 10 Most Populated Cities (2024)
![Top 10 Population](top10_population_2024.png)

---

## 📈 Insights
- Rapid growth is concentrated in **smaller emerging communities** rather than the largest cities.  
- Major population centers like **Houston, Dallas, and Austin** continue to dominate in absolute size.  
- Areas of service overlap represent **strategic markets** where infrastructure demand is expected to rise.  

---

## 🛠️ Tools & Technologies
- **Python** (Pandas, Folium, Matplotlib)  
- **GitHub Pages** for hosting interactive map  
- **CSV / U.S. Census Data** for population trends  

---

## 👤 About
Created by Michael Morris as a data analytics portfolio project.  

📌 Connect with me on [LinkedIn](https://www.linkedin.com/in/mikemorris92/)  
