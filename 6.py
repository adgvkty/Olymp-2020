i1 = int(input())
i2 = input().split()

i2 = [int(elem) for elem in i2]

count1 = i2.count(1)
count2 = i2.count(2)

print(min(count1, count2))