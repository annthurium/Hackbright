from sys import argv
import string
script, read_file = argv


f = open(read_file)
filetext = f.read()
filetext = filetext.lower()
f.close()
seq = string.ascii_lowercase

dictionary = dict.fromkeys(seq)

for i in dictionary:
	dictionary[i] = 0

for i in filetext:
	for j in dictionary:
		if j == i:
			dictionary[i] += 1

sorted_dict = [x for x in dictionary.iteritems()]
sorted_dict.sort(key=lambda x: x[0]) # sort by key

for i in sorted_dict:
	print i

