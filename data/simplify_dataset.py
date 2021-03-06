import json
from collections import defaultdict

with open('nyc_collision.csv') as f:
	content = f.read()



# json format
# date
# 		zipcode
#			count
spec = ['00083', '10044', '11371']
zipcodes = ['10065', '10069', '10453', '10452', '10451', '10457', '10456', '10455', '10454', '10105', '10459', '10458', '11232', '10103', '10010', '11385', '10017', '11235', '0', '11222', '10014', '11218', '10282', '10280', '10281', '10118', '10119', '10110', '10111', '11109', '11379', '11378', '11102', '11103', '11377', '11101', '11106', '11370', '11104', '11105', '11375', '11374', '10278', '10803', '10048', '10028', '10040', '11228', '11201', '11203', '10128', '11205', '11204', '11207', '11206', '11209', '11208', '10121', '11372', '11225', '10025', '10106', '11368', '11369', '11366', '11367', '11364', '11365', '11362', '11363', '11360', '11361', '10020', '10123', '10021', '11040', '11212', '11213', '11210', '11211', '10039', '11217', '10022', '11215', '10035', '10034', '10037', '10036', '10031', '10030', '10033', '10032', '11001', '11358', '11005', '11004', '11697', '11694', '11695', '11692', '11693', '11355', '11354', '11216', '10038', '11214', '10309', '10308', '10307', '10306', '10305', '10304', '10303', '10302', '10301', '11229', '10029', '10026', '10027', '10024', '11224', '11223', '10023', '11221', '11220', '11219', '10169', '10168', '11429', '11428', '11421', '11420', '11423', '11422', '11427', '11426', '10153', '10154', '10155', '10310', '10312', '10314', '11359', '11231', '11238', '11239', '10019', '10018', '11230', '10012', '10011', '11233', '11234', '10016', '11236', '11237', '11432', '11433', '11430', '11436', '11434', '11435', '10004', '10005', '10006', '10007', '10000', '10001', '10002', '10003', '10167', '11357', '10165', '10009', '11356', '10475', '10474', '10471', '10470', '10473', '10472', '11691', '10120', '11249', '11242', '10107', '11226', '10178', '10075', '10170', '10171', '10172', '10173', '10466', '10467', '10464', '10465', '10462', '10463', '10460', '10461', '10468', '10469', '11411', '11412', '11413', '11414', '11415', '11416', '11417', '11418', '11419', '11251', '10013', '11373']
zipcodes.extend(spec)

output = defaultdict(lambda: {z:0 for z in zipcodes})

for line in content.split('\n')[1:-1]:
	line_split = line.split(',')
	date, time, borough, zipcode = line_split[1:5]
	# print(date)
	if not all([date, time, borough, zipcode]) or time == "0" or int(zipcode) == 0:
		continue

	time = ("0" + time[:-2])[-3:] + "00"
	year = date[-4:]
	if year != "2016":
		continue
	output[time][zipcode] += 1

# print(zipcodes)
print(len(zipcodes))

with open('nyc_collision_time.json', 'w') as f:
	json.dump(output, f)

