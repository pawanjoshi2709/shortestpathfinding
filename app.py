from flask import Flask, render_template, request
import pandas as pd
import folium

app = Flask(__name__)

# Load city distances and coordinates
def getGraphPoints():
    data_dist = pd.read_csv('Distances.csv', index_col=0)
    data_dist.replace(100000.0, None, inplace=True)
    city_list = pd.read_csv('Lat_Long.csv')

    cities = city_list['City'].tolist()

    graph = {city: {} for city in cities}
    for source in cities:
        for target in cities:
            dist = data_dist.loc[source, target]
            if pd.notna(dist) and dist != 0:
                graph[source][target] = int(dist)

    points = {row['City']: (row['Latitude'], row['Longitude']) for _, row in city_list.iterrows()}
    return graph, points, cities

graph, points, cities = getGraphPoints()

# Dijkstra's algorithm
def dijkstra(graph, src, dest):
    visited = {city: False for city in graph}
    distance = {city: float('inf') for city in graph}
    path = {}
    distance[src] = 0
    path[src] = None

    for _ in range(len(graph)):
        min_city = None
        min_dist = float('inf')
        for city in graph:
            if not visited[city] and distance[city] < min_dist:
                min_city = city
                min_dist = distance[city]

        if min_city is None:
            break
        visited[min_city] = True

        for neighbor, dist in graph[min_city].items():
            if not visited[neighbor]:
                new_dist = distance[min_city] + dist
                if new_dist < distance[neighbor]:
                    distance[neighbor] = new_dist
                    path[neighbor] = min_city

    if distance[dest] == float('inf'):
        return None, None

    rev_path = []
    cur = dest
    while cur is not None:
        rev_path.append(cur)
        cur = path.get(cur)
    rev_path.reverse()
    return distance[dest], rev_path

@app.route("/", methods=["GET", "POST"])
def index():
    shortest_path = None
    distance = None
    map_html = None

    if request.method == "POST":
        src = request.form.get("source")
        dest = request.form.get("destination")
        if src and dest and src != dest:
            distance, path = dijkstra(graph, src, dest)
            if path:
                mid_lat = sum(points[city][0] for city in path) / len(path)
                mid_lon = sum(points[city][1] for city in path) / len(path)

                # Set height and zoom level for better fit
                m = folium.Map(location=[mid_lat, mid_lon], zoom_start=5.2, height="500px")

                # Add markers for cities
                for city in path:
                    folium.Marker(location=points[city], popup=city).add_to(m)

                # Draw lines and distance labels
                for i in range(len(path) - 1):
                    city1, city2 = path[i], path[i + 1]
                    coord1, coord2 = points[city1], points[city2]
                    dist = graph[city1][city2]

                    # Draw line
                    folium.PolyLine([coord1, coord2], color="blue", weight=5, opacity=0.7).add_to(m)

                    # Place distance label at the midpoint
                    mid_lat = (coord1[0] + coord2[0]) / 2
                    mid_lon = (coord1[1] + coord2[1]) / 2
                    folium.Marker(
                        location=[mid_lat, mid_lon],
                        icon=folium.DivIcon(html=f"""<div style="font-size: 10pt; color: red;"><b>{dist}km</b></div>""")
                    ).add_to(m)

                map_html = m._repr_html_()
                shortest_path = " → ".join(path)

    return render_template("index.html", cities=cities, map_html=map_html, distance=distance, path=shortest_path)

if __name__ == "__main__":
    app.run(debug=True)
