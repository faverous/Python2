from sys import argv
script, filename = argv
fo = open(filename,"r+")
print fo.readline()
print fo.readline()
fo.truncate()
print fo.read()
fo.close()