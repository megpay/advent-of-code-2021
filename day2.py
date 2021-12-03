def calc_x_y(x, y, newline):
    direction, value = newline.split(" ")
    if direction == 'forward':
        x = x + int(value) 
    elif direction == 'down':
        y = y + int(value)
    elif direction == 'up':
        y = y - int(value)
    else:
        print(direction)
        return -1
    return x, y


f = open("inputday2.txt")
x = 0
y = 0
for newline in f:
    x, y = calc_x_y(x, y, newline)
    
print(str(x) + ' ' + str(y))

print(x*y)
f.close()



def calc_x_y_aim(x, y, aim, newline):
    direction, value = newline.split(" ")
    if direction == 'forward':
        x = x + int(value)
        y = y + aim * int(value) 
    elif direction == 'down':
        aim = aim + int(value)
    elif direction == 'up':
        aim = aim - int(value)
    else:
        print(direction)
        return -1
    return x, y, aim

f = open("inputday2.txt")
x = 0
y = 0
aim = 0
for newline in f:
    x, y, aim = calc_x_y_aim(x, y, aim, newline)
    
print(str(x) + ' ' + str(y) + ' ' + str(aim))

print(x*y)
f.close()

