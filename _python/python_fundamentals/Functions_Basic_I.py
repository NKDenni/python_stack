#1 This function will accept any argument but always return the value 5. When returned it will print 5 to the terminal.
def a():
    return 5
print(a())

# Output: 5

#2 This function when called will retun 5. The print will return 5 + 5 which is 10.
def a():
    return 5
print(a()+a())

# Output: 10

#3 This function will return 5 and exit the function.
def a():
    return 5
    return 10
print(a())

# Output: 5

#4 This function will return 5 print 10 and then print 5.
def a():
    return 5
    print(10)
print(a())

# Output: 5, 10

#5 An argument is passed to function a() and then prints 5. Then the function is assigned to the variable x. Print(x) prints nothing
def a():
    print(5)
x = a()
print(x)

# Output: 5, None

#6 The print function calls the function a(b,c) twice passing first arguments 1 and 2 and then 2 and 3. The function prints 3 and then 5. We exit the function without returning anything and print none.
def a(b,c):
    print(b+c)
print(a(1,2) + a(2,3))

# Output: 2, 3, None

#7 The function takes in the integer arguments and returns them as strings and prints them sequentially. If we did not convert these arguments to strings and pass them as is they will be interperted as integers and add the values together rather than place them side by side. 
def a(b,c):
    return str(b)+str(c)
print(a(2,5))

# Output: 25

#8 The function gets called in the print function. It first prints 100 and then checks to see if the value of b is less than ten. Since it is greater than 10 it returns 10. Once it returns it exits the for loop and prints 10. 
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a())

# Output: 100, 10

#9 The function will first get passed 2 and 3 and return 7 because 2 is smaller than 3. 7 will get printed to the shell. When the function gets passed 5 and 3 it will return 14 because 5 is larger than 3. It will print 14. Finally the last line will print the sum of the four arguments passed to it which will be 21 which is 7 + 14. 3 never gets returned as the function exits before it gets to the last return.
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))

# Output: 7, 14, 21

#10 3 and 5 get passed to the function as b and c and the function returns the sum of the two arguments which is 8. We print the returned sum of 8 to terminal
def a(b,c):
    return b+c
    return 10
print(a(3,5))

# Output: 8

#11 First time we print b we see 500 in the terminal. We continue pass the function to print b again and see 500. We then call on the function and print 300 which is the assigned value of b within the functin and then exit the function. We print b a final time which is back to 500 as the function did not return 300 to the main program as the new value of b.
b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)

# Output: 500, 500, 300, 500

#12 Like question 11 we start by printing the value of b. We skip down past the function and print the value of b again which has not changed. We then call the function and print the new value of b which is 300. The function then returns the new value of b back to the program. This will over ride the original value of b and the final print will be 300.

# Orignial prediction was wrong. The final print is 500 not 300 because even though the value of b was returned it needed to be passed to the print function at the end for it to print the value of b which was returned. The final print would have needed to be print(a()).
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)

# Output: 500, 500, 300, 300 (Correct output: 500, 500, 300, 500)

#13 Same as above only this time b is reassigned the value of a() when returned before the final print. 
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)

# Output: 500, 500, 300, 300

#14 Function a() is invoked at the last line. a() prints 1 then invokes b() which prints 3 goes back to a() and prints 2.
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()

# Output: 1, 3, 2

#15 The value returned from a() will be stored in the variable y. a() gets invoked and prints 1 stores the value of the function b() in x and then prints x. When b() gets invoked we hop down and print 3 and then return 5 back to a() which then pints 5 and a() returns 10 to y and we finally print the value of y.
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)

# Output: 1, 3, 5, 10




