#write a python program to find maximum middle and largest number

input1 = int(input("please enter 1st number : "))
input2 = int(input("please enter 2nd number : "))
input3 = int(input("please enter 3rd number : "))
alldata = [input3, input2, input1]
alldata.sort()
minimum = alldata[0]
middle = alldata[1]
maximum = alldata[2]
print(minimum, 'this is a minimum number')
print(middle, 'this is a middle number')
print(maximum, 'this is a maximum number')
