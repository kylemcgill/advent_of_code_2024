import os

def get_lists():
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
    return (left, right)

def part_1():
    left, right = get_lists()

    left.sort()
    right.sort()
    assert(len(left) == len(right))

    sum = 0
    for i in range(len(left)):
        sum += abs(left[i] - right[i])

    print(f"Sum of distances is: {sum}")

def part_2():
    left, right = get_lists()

    right_frequency = {}
    for item in right:
        if item not in right_frequency:
            right_frequency[item] = 0
        right_frequency[item] += 1
    
    similarity_score = 0
    for item in left:
        if item in right_frequency:
            similarity_score += item * right_frequency[item]

    print(f"Similarity score: {similarity_score}")
    
if __name__ == "__main__":
    part_1()
    part_2()