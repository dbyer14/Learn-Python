
# this creates the function cheese_and_crackers, which takes two variables. the first variable is the number of cheeses, the second is the number of boxes of crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket. \n"

# this line calls the function and uses numbers for the variables directly
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

# these lines asign numbers to variabls, and then pass the variables to the function cheese_and_crackers
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# this linke shows that you can do math within the function durectky
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# this line shows that math between named variables and numbers can be completed within funtions
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

