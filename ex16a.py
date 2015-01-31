# imports the argv module
from sys import argv

# establishes variables for argv
script, filename = argv

# starts the user interaction
print "We are going to read %r" % filename
print "If you want that hit 'Enter' otherwise hit 'Ctrl+C'"

# asks user if they want to proceed
raw_input("> ")

print "Reading the file..."

# opens the file (which allows it to be examined) that we entered when we initial ran the script in command line
target = open(filename, 'r')

# reads the contents and prints them out
print target.read()

# closes the file 
target.close()

