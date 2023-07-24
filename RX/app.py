from db import Geodata_plotting
from flask import Flask, render_template, request
import sqlite3
DB_mapper = Geodata_plotting()


import folium

app = Flask(__name__)


@app.route("/")
def base_point():
        map = folium.Map(location=[48.20, 2.10], zoom_start=10)
        first_marker = True
        first_value = ""
        array_coords = []
        try:
            connexion = sqlite3.connect("geodata.db")

            cursor = connexion.execute("SELECT DATETIME, LATITUDE, LONGITUDE FROM GEO")
            for row in cursor:
                array_coords.append((row[1], row[2]))
                if first_marker:
                     folium.Marker(array_coords[0], popup = row[0], icon=folium.Icon(color="green", icon="glyphicon glyphicon-ok-circle")).add_to(map)
                     first_marker == False
                    
                folium.PolyLine(array_coords, tooltip=row[0]).add_to(map)
               
        except: pass
        connexion.close()
    
        return map.get_root().render()

if __name__ == '__main__':
   app.run()
