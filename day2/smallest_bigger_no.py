input_number = (input("Enter the number to generate the next smallest bigger number"))
length=len(input_number)
input_number = list(map(int, str(input_number)))
current_digit=input_number[0]
location=0
for i in range(length):
    if input_number[i]<current_digit:
        current_digit=input_number[i]
        location=i
        break
input_number[0],input_number[i]=input_number[i],input_number[0]

for i in range(location+1,length):
    if input_number[i]>input_number[]
