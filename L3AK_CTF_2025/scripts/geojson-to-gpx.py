import json
from xml.etree.ElementTree import Element, SubElement, tostring, ElementTree
import sys

def geojson_to_gpx(geojson_path, gpx_path):
    with open(geojson_path) as f:
        data = json.load(f)
    
    gpx = Element('gpx', version="1.1", creator="geojson-to-gpx-script", xmlns="http://www.topografix.com/GPX/1/1")
    
    for feature in data.get('features', []):
        geom = feature.get('geometry')
        if not geom or geom.get('type') != 'Point':
            continue
        lon, lat = geom['coordinates']
        wpt = SubElement(gpx, 'wpt', lat=str(lat), lon=str(lon))
        # Optionally add name or id
        name = feature.get('id') or feature.get('properties', {}).get('name')
        if name:
            SubElement(wpt, 'name').text = str(name)
    
    tree = ElementTree(gpx)
    tree.write(gpx_path, encoding='utf-8', xml_declaration=True)
    print(f"Saved GPX to {gpx_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python geojson-to-gpx.py input.geojson output.gpx")
    else:
        geojson_to_gpx(sys.argv[1], sys.argv[2])
