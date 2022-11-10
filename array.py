array = [1,5,8,9,4,2,7,3,6,10]
for i in array:
    if i % 2 == 0:
        print (i)

array.sort()
print(array)

array.sort(reverse=True)
print(array)