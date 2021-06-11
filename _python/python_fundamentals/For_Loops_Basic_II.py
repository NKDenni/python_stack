# Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
#   Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]

list = [3,-2,0,7,-10,2]

def a(x):
    for i in range(len(x)):
        if x[i] > 0:
            x[i] = "big"
    return x
print(a(list))

# Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
#   Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
#   Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it

arr = [-1, 3, 5, -5, 23, 1, -4, 12]

def a(x):
    count = 0
    for i in range(len(x)):
        if x[i] > 0:
            count = count + 1
    x[len(x)-1] = count
    return x
print(a(arr))

# Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
#   Example: sum_total([1,2,3,4]) should return 10
#   Example: sum_total([6,3,-2]) should return 7

list = [-1, 3, 5, -5, 22, -15, 9]

def a(x):
    sum = 0
    for i in range(len(x)):
        sum = sum + x[i]
    return sum

print(a(list))

# Average - Create a function that takes a list and returns the average of all the values.
#   Example: average([1,2,3,4]) should return 2.5

list = [1,2,3,4.0]

def a(x):
    avg = 0
    sum = 0
    for i in range(len(x)):
        sum = sum + x[i]
    avg = sum/len(x)
    return avg
print(a(list))

# Length - Create a function that takes a list and returns the length of the list.
#   Example: length([37,2,1,-9]) should return 4
#   Example: length([]) should return 0

arr = [1,1,1,1,1,1,1,1,1,1,1,1]

def length(x):
    length = len(x)
    return length
print(length(arr))

# Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
#   Example: minimum([37,2,1,-9]) should return -9
#   Example: minimum([]) should return False

list = [0, 5, -7, -2, 8, 3, 1, -4]

def min(x):
    min = 0
    for i in range(len(x)):
        if min > x[i]:
            min = x[i]
    return min
print(min(list))

# Maximum - Create a function that takes a list and returns the maximum value in the array. If the list is empty, have the function return False.
#   Example: maximum([37,2,1,-9]) should return 37
#   Example: maximum([]) should return False

def max(x):
    max = 0
    for i in range(len(x)):
        if max < x[i]:
            max = x[i]
    return max
print(max(list))

# Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
#   Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }

list = [ 11, 27, 86, 1, 7, 88, 8, 31, 95]

def UltAnalysis(x):
    
    Analysis = {
        'sumTotal':0,
        'average':0,
        'minimum':0,
        'maximum':0,
        'length':0,
    }


    avg = 0.0
    sum = 0
    add = 0
    min = x[0]
    max = 0
    
    for i in range(len(x)):
        sum = sum + x[i]
    Analysis['sumTotal'] = sum

    for i in range(len(x)):
        add = add + x[i]
    avg = float(add)/len(x)
    Analysis['average'] = avg

    for i in range(len(x)):
        if min > x[i]:
            min = x[i]
    Analysis['minimum'] = min

    for i in range(len(x)):
        if max < x[i]:
            max = x[i]
    Analysis['maximum'] = max

    length = len(x)
    Analysis['length'] = length

    return Analysis

object = UltAnalysis(list)

print(object)

# Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
#   Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]

list = [0,1,2,3,4,5,6,7,8,9]

def reverse_list(x):
    for i in range(len(x)):
        temp = x[i]
        x[i] = x[len(x)-1-i]
        x[len(x)-1-i] = temp
    return x

revers = reverse_list(list)
print(revers)


