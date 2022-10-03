import random
array = []
for i in range(0, 10):
    array.append(random.randint(1, 20))
print(array)

sum = 0
smallest = array[0];
index = 0;
# goes through each element in the list and checks if the element is smaller than the smallest num it's seen so far
# if the current element is smaller, it changes the values of the variables accordingly
for i in range(0, 10):
    sum += array[i]
    if (array[i] < smallest):
        smallest = array[i]
        index = i
print("mean: " + str(sum/10))
print("smallest number: " + str(smallest))
print("index of smallest number: " + str(index))

## part 2
manipulatedNum = int(input("enter a number: "))
numArray = []
# loop basically adds digits to the array in reverse order
# the input number%10 to get the last digit and adds it to numArray
# then, divides manipulated number by 10 to get rid of the last digit
while (manipulatedNum != 0):
    numArray.append(manipulatedNum%10)
    manipulatedNum = int(manipulatedNum/10)
numArray.reverse()
print(numArray)

## part 3
array1 = []
array2 = []
for i in range(0, 10):
    array1.append(random.randint(1, 20))
    array2.append(random.randint(1, 20))
array1.sort()
array2.sort()
combined = array2
# for each element in array1, it checks against each element in the combined array
# and inserts the value in that spot if it is smaller
for i in range(0, 10): # i is for array1
    num1inserted = False
    for j in range(0, len(combined)): # j is for combined
        if (array1[i] <= combined[j]) and (not num1inserted):
            combined.insert(j, array1[i])
            num1inserted = True
        elif (not num1inserted) and (j == len(combined)):
            combined.append(array1[i])
            num1inserted = True
print(combined)
