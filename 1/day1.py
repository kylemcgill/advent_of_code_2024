import os

left = []
right = []
with open("input.txt", "r") as f:
    items = f.read().split()
    
    # white space was split between the items as well
    toggle_left = True
    for item in items:
        if toggle_left:
            left.append(int(item))
            toggle_left = False
        else:
            right.append(int(item))
            toggle_left = True
    f.close()

left.sort()
right.sort()
assert(len(left) == len(right))

sum = 0
for i in range(len(left)):
    sum += abs(left[i] - right[i])

print(f"Sum of distances is: {sum}")

    
