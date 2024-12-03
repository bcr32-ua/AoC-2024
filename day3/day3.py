import re
import math


##################
### SOLUCION 1 ###
##################

total = 0

with open("./day3/testInput") as file:
#with open("./day3/input") as file:
    for line in file:
        s = line
        matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)", s)

        for m in matches:
            numbers = m.replace("mul(", "").replace(")", "").split(",")

            numbers = list(map(int, numbers))
            
            total += math.prod(numbers)

    print(total)

##################
### SOLUCION 2 ###
##################

total = 0
enabled = True

#with open("./day3/testInput") as file:
with open("./day3/input") as file:
    for line in file:
        s = line
        matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", s)

        for m in matches:
            if m == "do()":
                enabled = True

            elif m == "don't()":
                enabled = False
            
            if enabled and m != "do()" and m != "don't()":
                numbers = m.replace("mul(", "").replace(")", "").split(",")

                numbers = list(map(int, numbers))
                
                total += math.prod(numbers)

    print(total)


