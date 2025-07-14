import json
import math

def haversine(lat1, lon1, lat2, lon2):
    R = 6371 
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)
    a = math.sin(dphi/2)**2 + math.cos(phi1)*math.cos(phi2)*math.sin(dlambda/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

def parse_point_id(point_id):
    # For airport: 'node/27265716' (no coordinates in id)
    # For streetview: 'point/44.3973_-92.4751'
    if point_id.startswith('point/'):
        lat, lon = point_id[6:].split('_')
        return float(lat), float(lon)
    return None

def main(airport_geojson_path, streetview_geojson_path, output_path):
    with open(airport_geojson_path) as f:
        airports = json.load(f)
    with open(streetview_geojson_path) as f:
        streetview = json.load(f)

    sv_points = []
    for feat in streetview['features']:
        pt = parse_point_id(feat['id'])
        if pt:
            sv_points.append(pt)

    # For each airport, we need coordinates. If not present, skip.
    filtered_features = []
    for feat in airports['features']:
        # Try to get coordinates from geometry, else skip
        geom = feat.get('geometry')
        if geom and geom.get('type') == 'Point':
            lon, lat = geom['coordinates']
        else:
            continue
        # Check if any streetview point is within 2 km
        for sv_lat, sv_lon in sv_points:
            if haversine(lat, lon, sv_lat, sv_lon) <= 2:
                filtered_features.append(feat)
                break

    out = dict(airports)
    out['features'] = filtered_features
    with open(output_path, 'w') as f:
        json.dump(out, f, indent=2)
    print(f"Saved {len(filtered_features)} airports to {output_path}")

if __name__ == "__main__":
    main("us-overpass-airports-has-answer.geojson", "america-streetview.geojson", "haversine-airports.geojson")
