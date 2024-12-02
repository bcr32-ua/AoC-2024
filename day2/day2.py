import copy
import math

##################
### SOLUCION 1 ###
##################

safe = 0

#with open("./day2/testInput") as file:
with open("./day2/input") as file:
    for line in file:
        is_safe = True
        max_previous_value = math.inf
        min_previous_value = -math.inf

        values = line.split()

        values = list(map(int, values))

        if values[0] > values[-1]:
            for value in values:
                if int(value) > max_previous_value:
                    is_safe = False
                
                if max_previous_value != math.inf and max_previous_value - int(value) > 3:
                    is_safe = False

                if max_previous_value == int(value):
                    is_safe = False

                max_previous_value = int(value)
            
            if is_safe:
                safe += 1


        if values[0] < values[-1]:
            for value in values:
                if int(value) < min_previous_value:
                    is_safe = False

                if min_previous_value != -math.inf and int(value) - min_previous_value > 3:
                    is_safe = False

                if min_previous_value == int(value):
                    is_safe = False
                
                min_previous_value = int(value)
            
            if is_safe:
                safe += 1
    
    print(f"El resultado del primer problema es: {safe}")

##################
### SOLUCION 2 ###
##################

safe = 0

def validator(values, is_safe = True):
    max_previous_value = math.inf
    min_previous_value = -math.inf
    
    if values[0] > values[-1]:
        for value in values:
            if int(value) > max_previous_value:
                is_safe = False
            
            if max_previous_value != math.inf and max_previous_value - int(value) > 3:
                is_safe = False

            if max_previous_value == int(value):
                is_safe = False

            max_previous_value = int(value)
        
        return is_safe


    if values[0] < values[-1]:
        for value in values:
            if int(value) < min_previous_value:
                is_safe = False

            if min_previous_value != -math.inf and int(value) - min_previous_value > 3:
                is_safe = False

            if min_previous_value == int(value):
                is_safe = False
            
            min_previous_value = int(value)
        
        return is_safe

#with open("./day2/testInput") as file:
with open("./day2/input") as file:
    for line in file:
        values = line.split()

        values = list(map(int, values))
            
        if validator(values):
            safe += 1
        else:
            for i in range(len(values)):
                edited_values = copy.deepcopy(values)
                edited_values.pop(i)
                if validator(edited_values):
                    safe += 1
                    break

    
    print(f"El resultado del primer problema es: {safe}")