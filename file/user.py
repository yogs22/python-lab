import csv

rows = []

with open('person.csv') as csvfile:
	csvreader = csv.DictReader(csvfile)
	# for user in csvreader:
	# 	rows.append(user)
	rows = list(csvreader)
	print('total baris : ', csvreader.line_num)

for row in rows:
	print(row['first_name'] + ' - ' + row['email'])