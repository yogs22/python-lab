"""
 -- WORK WIT JSON
"""

import json
data = {}
data['member'] = [
	{'name': 'Yogi', 'gender': 'laki-laki', 'status': 'bekerja'},
	{'name': 'Novi', 'gender': 'perempuan', 'status': 'bekerja'},
	{'name': 'Zena', 'gender': 'laki-laki', 'status': 'kuliah'}
]

# print(json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}]))

with open('penduduk.txt', 'w+') as populationfile:
	json.dump(data, populationfile)