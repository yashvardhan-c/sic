amount = int(input("enter the amount: "))
note_list = list(map(int,input("Enter the denomination of the notes").split()))
note_list.sort(reverse = True)
for note in note_list:
    num = amount // note
    print("No of ",note,"'s required is ",num)
    amount %= note