class Shop:
    def __init__(self, n, x, ls):
        self.n = n
        self.x = x
        self.arr = ls

    # Using a sliding window algorithm to select x elements from array (python list)
    # sums first three values and stores in variable min
    # Assign sum to min if sum < min
    # sum next three
    # Check sum against min if min > sum set min = sum

    def min(self):
        # min initialized to be out of range of constraints
        minimum = 10001
        k = (self.n-self.x)+1
        i = 0

        while i < k:
            s = 0
            j = 0+i
            while j < self.x+i:
                s += self.arr[j]
                j += 1
            if s < minimum:
                minimum = s
            i += 1
        return minimum


a = [1, 2, 3, 4, 5, 1, 1, 1, 4]
b = 5
c = len(a)

d = Shop(9, 5, [1, 2, 3, 4, 5, 1, 1, 1, 4])

print(d.min())

# n = lenght of array
# x = number of values in array to be summed
# ls = array 
