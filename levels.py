level = 0
points = 0

def level_up():
    global level
    level += 1
    return level

if points >= 100:
    level_up()

print(level)
