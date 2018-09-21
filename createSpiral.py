def createSpiral(N):
    # First we need to check for invalid parameters
    # If it is not a digit, exit
    if str(N).isdigit(): # Converting height to str allows use of isdigit
        N = int(N)
    else:
        exit(-1)

    # If N is less than 1 then we can't make a spiral so we return []
    if N < 1:
        return []

    # Here we will create an N x N matrix full of None
    spiralMatrix = [[None for y in range(N)] for x in range(N)]

    # Here we define the current level (increases as depth increases)
    level = 0

    # Here we define the count for the incrementing number in the matrix
    count = 1

    # Here we define the current direction that we need to start in
    currentDirection = "right"

    # ddd
    for s in spiralSequence(N):
        if currentDirection == "right":
            for i in range(s):
                spiralMatrix[level][i + level] = count
                count += 1

            currentDirection = "down"
            continue

        elif currentDirection == "down":
            for i in range(s):
                spiralMatrix[i + level + 1][N - level - 1] = count
                count += 1

            level += 1
            currentDirection = "left"
            continue

        elif currentDirection == "left":
            for i in range(s):
                spiralMatrix[N - level][N - i - level - 1] = count
                count += 1

            currentDirection = "up"
            continue

        elif currentDirection == "up":
            for i in range(s):
                spiralMatrix[N - level - i - 1][level - 1] = count
                count += 1
                
            currentDirection = "right"
            continue

    return spiralMatrix

def spiralSequence(N):
    count = 1
    yield N
    while count < N:
        for i in range(2):
            yield N - count
        count += 1

for x in createSpiral(6):
    print(x)