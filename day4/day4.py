

##################
### SOLUCION 1 ###
##################

total = 0

#with open("./day4/testInput") as file:
with open("./day4/input") as file:
    matrix = []
    for line in file:
        matrix.append(list(line))

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 'X':
                if i >= 3:
                    if matrix[i-1][j] == 'M':
                        if matrix[i-2][j] == 'A':
                            if matrix[i-3][j] == 'S':
                                total += 1

                if j >= 3:
                    if matrix[i][j-1] == 'M':
                        if matrix[i][j-2] == 'A':
                            if matrix[i][j-3] == 'S':
                                total += 1

                if i < len(matrix)-3:
                    if matrix[i+1][j] == 'M':
                        if matrix[i+2][j] == 'A':
                            if matrix[i+3][j] == 'S':
                                total += 1

                if j < len(matrix[i])-3:
                    if matrix[i][j+1] == 'M':
                        if matrix[i][j+2] == 'A':
                            if matrix[i][j+3] == 'S':
                                total += 1

                if i >= 3 and j >= 3:
                    if matrix[i-1][j-1] == 'M':
                        if matrix[i-2][j-2] == 'A':
                            if matrix[i-3][j-3] == 'S':
                                total += 1

                if i < len(matrix)-3 and j < len(matrix[i])-3:
                    if matrix[i+1][j+1] == 'M':
                        if matrix[i+2][j+2] == 'A':
                            if matrix[i+3][j+3] == 'S':
                                total += 1

                if i >= 3 and j < len(matrix[i])-3:
                    if matrix[i-1][j+1] == 'M':
                        if matrix[i-2][j+2] == 'A':
                            if matrix[i-3][j+3] == 'S':
                                total += 1
                
                if i < len(matrix)-3 and j >= 3:
                    if matrix[i+1][j-1] == 'M':
                        if matrix[i+2][j-2] == 'A':
                            if matrix[i+3][j-3] == 'S':
                                total += 1
        
    print(total)

    ##################
    ### SOLUCION 2 ###
    ##################

    total = 0

    #with open("./day4/testInput") as file:
    with open("./day4/input") as file:
        matrix = []
        for line in file:
            matrix.append(list(line))
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 'A':
                if i >= 1 and j >= 1 and i < len(matrix)-1 and j < len(matrix[i])-1:
                    if matrix[i-1][j-1] == 'M':
                        if matrix[i-1][j+1] == 'S':
                            if matrix[i+1][j+1] == 'S':
                                if matrix [i+1][j-1] == 'M':
                                    total += 1
                    
                    if matrix[i-1][j-1] == 'S':
                        if matrix[i-1][j+1] == 'M':
                            if matrix[i+1][j+1] == 'M':
                                if matrix [i+1][j-1] == 'S':
                                    total += 1

                    if matrix[i-1][j-1] == 'M':
                        if matrix[i-1][j+1] == 'M':
                            if matrix[i+1][j+1] == 'S':
                                if matrix [i+1][j-1] == 'S':
                                    total += 1

                    if matrix[i-1][j-1] == 'S':
                        if matrix[i-1][j+1] == 'S':
                            if matrix[i+1][j+1] == 'M':
                                if matrix [i+1][j-1] == 'M':
                                    total += 1

    print(total)

