names = ['Petryk', 'Marichka', 'Olenka']

l = input().split(' ')

for i in range(len(l)):
    l[i] = int(l[i])

a = l[0]
b = l[1]
c = l[2]

if (a + b == c) or (b + c == a) or (a + c == b):
    print('Yes')
else:
    print('No')