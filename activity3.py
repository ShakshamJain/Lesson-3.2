import array as arr

array_1 = arr.array("i",[1,3,5,3,7,9,3])
print("Original Array: ", array_1)

a = array_1.count(3)
print("Number of Reuccurences: ", a)

b = array_1[::-1]
print("Array reversed: ", b)