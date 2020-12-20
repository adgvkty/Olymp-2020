names = ['Petryk', 'Marichka', 'Olenka']

l = input().split(' ')

for i in range(len(l)):
    l[i] = int(l[i])

lmax = max(l)

l_ind = l.index(lmax)

if l_ind == 0:
    print(names[0])
elif l_ind == 1:
    print(names[1])
else:
    print(names[2])