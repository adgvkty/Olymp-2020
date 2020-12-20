la = ['A', 'C', 'E', 'G']
na = ['1', '3', '5', '7']

string = input()

l_c = 0
n_c = 0

l = string[0]
n = string[1]

print(l)

if l in la and n in na:
    print('BLACK')
elif l in la or n in na:
    print('WHITE')
else:
    print('BLACK')




