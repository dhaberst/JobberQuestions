def createSpiral(N):
    '''
    This function returns a matrix (2D array) where number 1 to N are
    represented as a clockwise spiral.

        Ex:
            createSpiral(3) -> [[1,2,3],
                                [8,9,4],
                                [7,6,5]]

    Args:
        N: the size of the spiral matrix to make.

    Raises:
        SystemExit: exits program.
    '''
    # First we need to check for invalid parameters
    # If it is not a digit, exit
    if str(N).isdigit(): # Converting N to a str allows use of isdigit
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

    # Now we can start inserting the numbers into the matrix
    # We start by generating the spiral sequence using an iterator
    for s in spiralSequence(N):
        # If our current direction is right, insert from left to right
        #  which is equivalent to [i + level]. Note that [level] is static
        #  and does not change
        if currentDirection == "right":
            for i in range(s):
                spiralMatrix[level][i + level] = count
                count += 1

            # Now we move on to the down direction and continue
            currentDirection = "down"
            continue

        # If our current direction is down, insert from top to bottom
        #  which is equivalent to [i + level + 1]. Note that [N - level - 1]
        #  is static and does not change
        elif currentDirection == "down":
            for i in range(s):
                spiralMatrix[i + level + 1][N - level - 1] = count
                count += 1

            # We increment the level at this spot to make the rest of
            #  the calculations easier. The edges are '1' smaller now
            level += 1

             # Now we move on to the left direction and continue
            currentDirection = "left"
            continue

        
        # If our current direction is left, insert from right to left
        #  which is equivalent to [N - i - level - 1]. Note that [N - level]
        #  is static and does not change
        elif currentDirection == "left":
            for i in range(s):
                spiralMatrix[N - level][N - i - level - 1] = count
                count += 1

             # Now we move on to the up direction and continue
            currentDirection = "up"
            continue

        # If our current direction is up, insert from bottom to top
        #  which is equivalent to [N - level - i - 1]. Note that [level - 1]
        #  is static and does not change
        elif currentDirection == "up":
            for i in range(s):
                spiralMatrix[N - level - i - 1][level - 1] = count
                count += 1
            
             # Now we move back to the right direction and continue
            currentDirection = "right"
            continue

    return spiralMatrix

def spiralSequence(N):
    '''
    This function returns an iterator of a spiral sequence. If you
    trace a spiral matrix using right, down, left, up, you get the
    inital N then two of N - 1 repeating until 1.

        Ex:
            spiralSequence(3) -> 3,2,2,1,1

    Args:
        N: the sequence to generate.

    Raises:
        SystemExit: exits program.
    '''
    # First we need to check for invalid parameters
    # If it is not a digit, exit
    if str(N).isdigit(): # Converting N to a str allows use of isdigit
        N = int(N)
    else:
        exit(-1)
        
    # Here we initialize a count that increases by one every interation of 2
    count = 1

    # First we yield N
    yield N

    # Then while the count doesn't exceed N we yeild 2 of the current N - count
    while count < N:
        for i in range(2):
            yield N - count
        count += 1