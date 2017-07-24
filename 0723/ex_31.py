#-- coding:utf-8 --
print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
	print "There's a giant bear here eating a cheese cake. What do you do?"
	print "1. Take cake."
	print "2. Scream at the bear."

	bear = raw_input("> ")
	if bear == "1":
		print "bear 1."
	elif bear == "2":
		print "bear 2."
	else:
		print "Well, %s " % bear
elif door == "2":
	print "Goodbye!"
else:
	print "Wrong input."

