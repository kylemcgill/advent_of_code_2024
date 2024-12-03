import re
def get_data():
    try:
        with open("input.txt", "r") as f:
            return f.read()
    finally:
        f.close()

# easy way is with regex but 
def part_1():
    data = get_data()
    result = re.findall(r'(mul\([0-9]+,[0-9]+\))', data)
    # print(f"{result}")
    program = re.compile(r'([0-9]+),([0-9]+)')
    sum = 0
    for operation in result:
        numbers = re.findall(program, operation)
        tuple = numbers[0]
        sum = sum + (int(tuple[0]) * int(tuple[1]))
    print(f"{sum}")

def part_2():
    pass

if __name__ == "__main__":
    part_1()
    part_2()