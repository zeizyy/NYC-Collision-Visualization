import json
from collections import defaultdict

month2int = {
	'Jan': 1,
	'Feb': 2,
	'Mar': 3,
	'Apr': 4,
	'May': 5,
	'Jun': 6,
	'Jul': 7,
	'Aug': 8,
	'Sep': 9,
	'Oct': 10,
	'Nov': 11,
	'Dec': 12
}

def format_date_str(mon, day):
	mon_str = ('0' + str(month2int[mon]))[-2:]
	day_str = ('0' + str(day))[-2:]
	return mon_str + '/' + day_str + '/2016'	

output = defaultdict(list)
with open('nyc_holiday') as f:
	for line in f:
		date, holiday = line.strip().split('\t')
		mon, day = date.split(' ')

		# print(mon, day, holiday)
		
		output[format_date_str(mon, day)].append(holiday)

print(output)
with open('nyc_holiday.json', 'w') as f:
	json.dump(output, f) 