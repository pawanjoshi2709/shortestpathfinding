# Shortest Path Visualizer (Dijkstra + Folium + Flask)

This is a web application that helps users find the **shortest path** between major Indian cities using **Dijkstra's algorithm** and displays the result using **Folium** maps embedded directly in the browser. Users can select a source and destination city, and the app will show the shortest route on an interactive map along with the total distance.

---

## 🚀 Features

- Select **source and destination** cities from a dropdown menu.
- Visualizes the **shortest path** on a **Folium map** using polyline.
- Shows the **total distance** between cities.
- Uses **Dijkstra’s algorithm** for accurate shortest path computation.
- Simple **Flask** web interface.
- Styled with background image support (customizable).

---

## 📁 Project Structure

ShortestPathApp/
│
├── app.py                    # Main Flask application
├── templates/
│   └── index.html            # HTML page with city selection and map display
├── notebook/
│   └── index.html            # EDA and pre creation
├── static/
│   └── background.jpg        # Background image used in the HTML page
├── Distances.csv             # Distance matrix between cities
├── Lat_Long.csv              # Latitude and longitude of each city
├── requirements.txt          # installs exactly the same versions
├── README.md                 # This file

## 🛠️ Setup Instructions

### 1. 📥 Install Anaconda

If you don't have Anaconda installed, download it from:  
🔗 [Anaconda Distribution](https://www.anaconda.com/products/distribution)

---

### 2. 🧪 Create a Conda Environment

Open a terminal or Anaconda prompt and run:

```bash
conda create -p ./env python=3.10
conda activate ./env
pip install -r requirements.txt
python app.py

## CONCLUSION
This project showcases how Dijkstra's algorithm can be integrated with web-based visualization tools like Folium to offer interactive and educational visualizations. It acts as a mini GIS system focused on Indian cities and is ideal for:

📚 Educational purposes

🧪 Algorithm demonstration

🌐 Interactive route visualization projects

This application is lightweight and easy to extend with additional features such as:

🏙️ More cities

🚦 Real-time traffic data integration

🔁 Dynamic route updates

📱 Mobile-responsive layout





