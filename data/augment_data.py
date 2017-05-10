import json

with open('nyc-zip.json') as f:
	base = json.loads(f.read())
with open('nyc-zip.geojson') as f:
	add = json.loads(f.read())

# print(base.keys())
# print(base['objects']['nyc_zip']['geometries'])
for b, a in zip(base['objects']['nyc_zip']['geometries'], add['features']):
	b['properties'] = a['properties']

with open('nyc-zip-aug.json', 'w') as f:
	json.dump(base, f)
