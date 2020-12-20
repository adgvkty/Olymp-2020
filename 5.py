array = input().split()

xa = array[0]
ya = array[1]

xb = array[2]
yb = array[3]

x3 = int(xa)
y3 = int(yb)

x4 = int(xb)
y4 = int(ya)

if x3 < 0 and y3 < 0 and x4 < 0 and y4 < 0:
    if x3 > x4:
        print(f'{x4} {y4} {x3} {y3}')
    else:
        print(f'{x3} {y3} {x4} {y4}')
else:
    if x3 > x4:
        print(f'{x4} {y4} {x3} {y3}')
    else:
        print(f'{x3} {y3} {x4} {y4}')