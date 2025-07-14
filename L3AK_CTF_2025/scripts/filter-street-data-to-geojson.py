import json
from datetime import datetime
from typing import List, Tuple, Optional, Set

def latest_valid_date(tags: List[str]) -> Optional[datetime]:
    """Return the latest valid date from a list of 'YYYY-MM' strings."""
    dates = []
    for tag in tags:
        try:
            y, m = map(int, tag.split('-'))
            dates.append(datetime(y, m, 1))
        except ValueError:
            continue
    return max(dates) if dates else None

def build_geojson(features: List[dict]) -> dict:
    """Construct a GeoJSON FeatureCollection with metadata."""
    return {
        "type": "FeatureCollection",
        "generator": "Brunner geo script 1.0",
        "copyright": "The data included in this document is from www.openstreetmap.org. The data is made available under ODbL.",
        "timestamp": datetime.utcnow().isoformat(timespec='seconds') + "Z",
        "features": features
    }

def filter_and_convert(
    input_path: str,
    output_path: str,
    allowed_dates: Set[Tuple[int, int]]
):
    """Filter input coordinates and export as GeoJSON."""
    with open(input_path, 'r') as f:
        data = json.load(f)

    coords = data.get("customCoordinates", [])
    features = []

    for rec in coords:
        lat = rec.get("lat")
        lng = rec.get("lng")
        tags = rec.get("extra", {}).get("tags", [])

        if lat is None or lng is None or not tags:
            continue

        latest = latest_valid_date(tags)
        if latest and (latest.year, latest.month) in allowed_dates:
            feature = {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [lng, lat]
                },
                "properties": {
                    "latest": latest.strftime("%Y-%m")
                },
                "id": f"point/{lat:.4f}_{lng:.4f}"
            }
            features.append(feature)

    geojson = build_geojson(features)

    with open(output_path, "w") as f:
        json.dump(geojson, f, indent=2)

    print(f"Saved {len(features)} features to {output_path}")

if __name__ == "__main__":
    ALLOWED_DATES = {(2023, 5), (2023, 6), (2023, 7), (2023, 8)}
    filter_and_convert("united-states-of-america.json", "america-streetview.geojson", ALLOWED_DATES)
