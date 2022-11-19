string = 'abcd'
numbers = (10, 20, 30, 40)
cort = ((string[i], numbers[i]) for i in range(min(len(string), len(numbers))))
print(cort)
for i_elem in cort:
    print(i_elem)