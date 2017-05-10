import json
from collections import defaultdict

# def format_date(s):
# 	return 

output = defaultdict(list)
nyc_stations = ["NY CITY CENTRAL PARK NY US", "STATEN ISLAND 1.4 SE NY US", "LA GUARDIA AIRPORT NY US", "STATEN ISLAND 4.5 SSE NY US", "JFK INTERNATIONAL AIRPORT NY US"]
with open("weather.csv") as f:
	next(f)
	for line in f:
		line = line.split(',')
		date = line[5]
		year = date[:4]
		date = date[4:6] + "/" + date[6:8] + "/" + date[:4]
		snow_d = float(line[11])
		station = line[1]
		if year == "2016" and snow_d != -9999 and snow_d != 0 and station in nyc_stations:
			output[date].append(snow_d)

output = { key: round(sum(output[key])/len(output[key]), 2) for key in output}

with open('weather.json', 'w') as f: 
	json.dump(output, f)