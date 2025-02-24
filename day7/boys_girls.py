def arrange(boys, girls):
    boys.sort()
    girls.sort()

    pattern1 = []
    for i in range(len(boys)):
        pattern1.append(boys[i])
        pattern1.append(girls[i])

    pattern2 = []
    for i in range(len(boys)):
        pattern2.append(girls[i])
        pattern2.append(boys[i])

    possible1 = all(pattern1[i] <= pattern1[i + 1] for i in range(len(pattern1) - 1))

    possible2 = all(pattern2[i] <= pattern2[i + 1] for i in range(len(pattern2) - 1))

    if possible1 or possible2:
        return "YES"
    else:
        return "NO"

t = int(input("Enter the number of test cases: "))
for i in range(t):
    n = int(input("Enter the number of boys "))
    m = int(input("Enter the number of girls "))
    boys = list(map(int, input("Enter the heights of the boys: ").split()))
    girls = list(map(int, input("Enter the heights of the girls: ").split()))
    print(arrange(boys, girls))
