i1 = input()
i2 = input().split()

i2 = [int(elem) for elem in i2]

i2.sort()

temp = 0

for i in i2:
    if len(i2) == 2:
        temp = i2[1] - i2[0]
        temp = temp*2
    else:
        if not i == i2[len(i2)-1]:
            temp += i2[i+1] - i2[i]

print(temp)