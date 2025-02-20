input_number = input("Enter the input number to find sum of odd placed even numbers")
sum = 0
for i in range(0,len(input_number)-1,2):
    temp = int(input_number[i])
    if temp % 2 == 0:
        sum+=temp
print("Result is ", sum)