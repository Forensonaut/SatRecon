import folium

def generate_map(devices):
    m = folium.Map(location=[0, 0], zoom_start=2)
    for dev in devices:
        if dev["Location"] != "Unknown":
            folium.Marker(
                location=[dev.get("Latitude", 0), dev.get("Longitude", 0)],
                popup=f"{dev['IP']} - {dev['Org']}"
            ).add_to(m)
    m.save("output/sat_map.html")
