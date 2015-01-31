from sys import argv

# Estabilishes the number of inputs needed for 'argv', which need to be input in the command line when launching the program
script, filename = argv

# prints output. %r is a formatter that returns raw data. the % separates the string from the variables that will be put in place of the formatters
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

# raw input is a way of getting input from a user
raw_input("?")

# Creates/opens the file store in the variable 'filename' in write more ('w')
print "Opening the file..."
target = open(filename, 'w')

# truncating the file removes the contents of a file. This is dangerous.
print "Truncating the file. Goodbye!"
target.truncate()

# collects input from the user
print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

# takes the user input and writes it to the file, which we have opened and stored in 'target'
# make sure to put multiple formatters in parentheses
# when using formatters and escape sequences there is no reason to use spaces unless you explicitly want spaces
target.write("%r\n%r\n%r\n" % (line1, line2, line3))


# this closes the file. Closing the file is important because it is like saving files
print "And finally, we close it."
target.close()

