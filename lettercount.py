from sys import argv
import string
script, read_file = argv

f = open(read_file)
filetext = f.read()
filetext = filetext.lower()
f.close()

# creates string of a-z lowercase letters
seq = string.ascii_lowercase

# creates dictionary from string
dictionary = dict.fromkeys(seq)

# initializes values to zero
for i in dictionary:
	dictionary[i] = 0

for i in filetext:
	for j in dictionary:
		if j == i:
			dictionary[i] += 1

# creates a sorted list containing dictionary values
# The assignment doesn't need this, but it's pretty!

#sorted_dict = [x for x in dictionary.iteritems()]
#sorted_dict.sort(key=lambda x: x[0]) # sort by key

#for i in sorted_dict:
	#print i

# creating a list of only the numbers, as per assignment specifications
new_list = []
for i in dictionary:
	new_list.append(dictionary[i])

# for some reason, b and c are out of order in dictionary
# a quick and dirty fix:
b = new_list[1]
new_list[1] = new_list[2]
new_list[2] = b

for i in new_list:
	print i

