
# imports argv from the sys module
from sys import argv

# assigns variables to argv, in this case only a single file name variable is assigned
script, input_file = argv

# this function prints out the contents of a file
def print_all(f):
	print f.read()

# this function moves to the first location (0) in the file
def rewind(f):
	f.seek(0)
	
""" 
this function prints a single line. it takes in a variable and prints that variable, 
then in calls the "readline" function on the file, f. I think that the "cursor" or where 
we are in the files memorory moves each time a line is read. So, when readline() is called 
in sucession, it will read subsequent lines. Need to confirm.
"""

def print_a_line(line_count, f):
	print line_count, f.readline()

# this line opens the file the user input when initially running the script and assigns the file object to a variable, 'current_file'
current_file = open(input_file)

print "First let's print the whole file:\n"

# this line prints the whole file
print_all(current_file)

print "Now let's rewind, kind of like a tape."

# this line returns the "cursor/memory" to the beginning of the file
rewind(current_file)

print "Let's print three lines:"

# this line assigns a value to the variable current line
current_line = 1

# this line runs the function print_a_line on two variables, current_line (an integer) and current_file (a file object)
print_a_line(current_line, current_file) ,

#  this line increments the value of current line and runs the print_a_line function
current_line += 1
print_a_line(current_line, current_file) ,

#  this line increments the value of current line and runs the print_a_line function
current_line += 1
print_a_line(current_line, current_file) ,