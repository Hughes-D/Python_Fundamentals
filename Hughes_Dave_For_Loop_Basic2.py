# Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]

def biggie_size(numList):
    for idx in range(len(numList)):
        if numList[idx] > 0:
            numList[idx] = "big"
    return numList

biggie_size([-1,3,5,-5])

# Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. 
# (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it

def count_positives(posList):
    sum = 0
    for idx in range(len(posList)):
        if posList[idx] > 0:
            sum += 1
    posList[len(posList)-1] = sum
    return posList

count_positives([1,6,-4,-2,-7,-2])


# Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7

def sum_total(numList):
    sum = 0
    for idx in range(len(numList)):
        sum += numList[idx]
    return sum

sum_total([1,2,3,4])

# Average - Create a function that takes a list and returns the average of all the values.
# Example: average([1,2,3,4]) should return 2.5

def average(numList):
    sum = 0
# created place to store total
    for idx in range(len(numList)):
        sum += numList[idx]
# looping through list and storing total to be divided by length of list
    return sum/len(numList)

average([1,2,3,4])


# Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0

def length(numList):
# since we only want the length of the list, we don't need to loop through the list
    return len(numList)

length([37,2,1,-9])

# Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False

def minimum(numList):
    if len(numList) == 0:
        return False
    min = numList[0]
    for idx in range(len(numList)):
        if numList[idx] < min:
            min = numList[idx]
    return min
        
minimum([])

# Maximum - Create a function that takes a list and returns the maximum value in the array. If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False

def maximum(numList): 
    if len(numList) == 0:
        return False
    max = numList[0]
    for idx in range(len(numList)):
        if numList[idx] > max:
            max = numList[idx]
    return max

maximum([37,2,1,-9])

# Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }

def ultimate_analysis(numList):
    sum = sum_total(numList)
    avg = sum/len(numList)
    min = minimum(numList)
    max = maximum(numList)
    lgt = length(numList)
    
    analysis = {
        'sumTotal': sum,
        'average': avg,
        'minimum': min,
        'maximum': max,
        'length': lgt
    }
    return analysis

ultimate_analysis([37,2,1,-9])

# Reverse List - Create a function that takes a list and return that list with values reversed. 
# Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]

def reverse_list(numList):
    temp = 0
# created temp to temporarily store nums w/o creating second list
    for idx in range(len(numList)):
        temp = numList[idx]
# couldn't figure this one out