import re

def nextVersion(version):
    '''
    This function increments a version number given a properly formatted
    input!

        Ex:
            nextVersion("1.2.3") -> "1.2.4"
            nextVersion("9.9") -> "10.0"

    Args:
        version: the version number to be incremented.

    Raises:
        SystemExit: exits program.
    '''
    
    # First we need to check for invalid parameters
    # If it is not a string, exit
    if not isinstance(version, str):
        exit(-1)

    # If it does not contain only digits [0-9] and '.', exit
    if not bool(re.match('^[0-9\.]*$', version)):
        exit(-1)

    # For simplicity we strip out the periods and rejoin as a string
    number = ''.join(version.split("."))

    # We need to store the length for the future
    length = len(number)

    # Here we can increment the number now by converting to int first
    number = int(number) + 1

    # Now we convert it back to a version number
    strNumber = str(number)
    newVersion = '.'.join(list(strNumber))

    # If the length increases then we know the first number > 9,
    #  therefore we can safely remove the first occuring period
    if len(strNumber) > length:
        newVersion = newVersion.replace('.', '', 1)

    return newVersion