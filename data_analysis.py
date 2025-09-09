# ======================================
# Texas Service Areas & Population Growth Map
# ======================================

# Step 1: Import required libraries
import pandas as pd
import folium
from folium.plugins import HeatMap

# Step 2: Load CSV files
centerpoint = pd.read_csv('centerpoint_service_area_tx.csv')
optimum = pd.read_csv('optimum_service_area_tx.csv')
population = pd.read_csv('2023_txpopest_place.csv')
coordinates = pd.read_csv('texas_city_coordinates.csv')

# Step 3: Standardize city names to lowercase for merging
centerpoint['city'] = centerpoint['city'].str.lower()
optimum['city'] = optimum['city'].str.lower()
population['Place'] = population['Place'].str.lower()
coordinates['city'] = coordinates['city'].str.lower()

# Step 4: Find cities served by both CenterPoint and Optimum
both_services = pd.merge(centerpoint, optimum, on='city')

# Step 5: Merge population growth + population estimate data
both_services = pd.merge(
    both_services, 
    population[['Place','pct_chg_20_24','jan1_2024_pop_est']], 
    left_on='city', right_on='Place', 
    how='left'
)

# Step 6: Merge coordinates for mapping
both_services = pd.merge(both_services, coordinates, on='city', how='left')

# Step 7: Function to color markers by population growth %
def get_color(pct_growth):
    if pd.isna(pct_growth):
        return 'gray'
    elif pct_growth < 0:
        return 'red'
    elif pct_growth < 5:
        return 'orange'
    elif pct_growth < 10:
        return 'yellow'
    else:
        return 'green'

# Step 8: Create base map centered on Texas
texas_map = folium.Map(location=[31.0, -99.0], zoom_start=6)

# Step 9: Add circle markers
for index, row in both_services.iterrows():
    growth = row['pct_chg_20_24']
    folium.CircleMarker(
        location=[row['latitude'], row['longitude']],
        radius=5 + (growth if pd.notna(growth) else 0)/2,  # size scaled by growth %
        popup=f"{row['city'].title()}\nPopulation Growth: {growth}%",
        color=get_color(growth),
        fill=True,
        fill_color=get_color(growth),
        fill_opacity=0.7
    ).add_to(texas_map)

# Step 10: Add legend for circle markers
legend_html = '''
<div style="
position: fixed; 
bottom: 50px; left: 50px; width: 220px; height: 180px; 
background-color: white; 
border:2px solid grey; z-index:9999; font-size:14px;
padding: 10px;
line-height: 20px;
overflow: auto;
">
<b>Population Growth %</b><br>
<i style="background:red;width:18px;height:18px;display:inline-block;"></i>&nbsp;Negative<br>
<i style="background:orange;width:18px;height:18px;display:inline-block;"></i>&nbsp;0-5%<br>
<i style="background:yellow;width:18px;height:18px;display:inline-block;"></i>&nbsp;5-10%<br>
<i style="background:green;width:18px;height:18px;display:inline-block;"></i>&nbsp;10%+<br>
<i style="background:gray;width:18px;height:18px;display:inline-block;"></i>&nbsp;No data
</div>
'''
texas_map.get_root().html.add_child(folium.Element(legend_html))

# Step 11: Full heatmap for all cities
heat_df = both_services.dropna(subset=["jan1_2024_pop_est", "latitude", "longitude"])
heat_data = heat_df[["latitude", "longitude", "jan1_2024_pop_est"]].values.tolist()
HeatMap(
    heat_data, 
    radius=25, 
    blur=15, 
    max_zoom=6, 
    min_opacity=0.5,
    name='All Cities Heatmap'
).add_to(texas_map)

# Step 12: Heatmap for top 10 most populated cities
top10 = heat_df.sort_values(by="jan1_2024_pop_est", ascending=False).head(10)
top10_data = top10[["latitude", "longitude", "jan1_2024_pop_est"]].values.tolist()
HeatMap(
    top10_data,
    radius=40, 
    blur=20, 
    max_zoom=6,
    min_opacity=0.6,
    gradient={0.2: 'blue', 0.4: 'lime', 0.6: 'orange', 1: 'red'},
    name='Top 10 Populated Cities'
).add_to(texas_map)

# Step 13: Add layer control so user can toggle layers
folium.LayerControl().add_to(texas_map)

# Step 14: Set custom page title for browser tab
texas_map.get_root().html.add_child(folium.Element('<title>Texas Service Areas & Population Growth</title>'))

# Step 15: Save final interactive map
texas_map.save('texas_both_services_interactive_map.html')
print("✅ Interactive map created: texas_both_services_interactive_map.html")

# Step 16: Export combined data to CSV
both_services.to_csv('texas_both_services_data.csv', index=False)
print("✅ CSV file created: texas_both_services_data.csv")
