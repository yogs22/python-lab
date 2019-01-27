"""
File python
"""

file = open('data.txt', 'a+')
file.write("\nSemoga bisa menikah")

file.seek(0)
text = file.read()
print(text)