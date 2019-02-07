import csv

rows = [
	{'name': 'Yogi', 'gender': 'laki-laki', 'status': 'bekerja'},
	{'name': 'Novi', 'gender': 'perempuan', 'status': 'bekerja'},
	{'name': 'Zena', 'gender': 'laki-laki', 'status': 'kuliah'},
]

with open('data.csv', 'a') as csvfile:
	fields = ['name', 'gender', 'status']
	writer = csv.DictWriter(csvfile, fieldnames  = fields)

	writer.writeheader()
	writer.writerows(rows)

print("Sukses membuat csv")