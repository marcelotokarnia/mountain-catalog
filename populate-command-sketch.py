from django.contrib.gis.geos import Point
import json
mountains = json.loads(open('mountains%s.json').read())
for m in mountains:
  Mountain(
    name=mountain['name'], 
    point=Point(float(mountain['Latitude']), float(mountain['Longitude'])), 
    ele=int(mountain['Elevation (meters)'].replace(',', ''))
  ).save()
