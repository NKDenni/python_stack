# 1. TASK: print "Hello World"
print( "Hello World" )
# 2. print "Hello Noelle!" with the name in a variable
name = "Nathan"
print( "Hello", name )	# with a comma
print( "Hello "+ name )	# with a +
# 3. print "Hello {num}!" with the number in a variable
name = "42"
print( "Hello", name, "!" )	# with a comma
print( "Hello " + name + "!" )	# with a +	-- this one should give us an error!
# 4. print "I love to eat {fave_food1} and {fave_food2}." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "hamburgers"
print( "I love to eat {} and {}." .format(fave_food1, fave_food2)) # with .format()
print( f"I love to eat {fave_food1} and {fave_food2}." ) # with an f string

# NINJA BONUS: Spend a few minutes playing around with other string methods to see what’s out there!
x = "hello world! all caps?"
print(x.upper())

y = "THIS IS A TEST OF LOWER"
print(y.lower())

z = "Testing1234"
print(z.isalpha())