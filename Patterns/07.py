num = str(input('Enter the number: '))
length = len(str(num))
 
for i in range(length):
    right = num[:i + 1]
    left_value = num[i:length]
    left = f"{left_value:>{length}}"
    print(left, right, sep='\t' )