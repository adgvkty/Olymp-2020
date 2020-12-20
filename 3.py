names = ['Petryk', 'Marichka', 'Olenka']

array = input().split(' ')
array1 = input().split(' ')

array = [int(elem) for elem in array]
array1 = [int(elem) for elem in array1]

u1 = array[0]
p2 = array[1]
u2 = array1[1]
p1 = array1[0]

u = u1 + u2
p = p1 + p2

if u > p:
    print('U')
elif p > u:
    print('P')
elif p == u:
    if p2 == u2:
        print('T')
    elif p2 > u2:
        print('P')
    else:
        print('U')



