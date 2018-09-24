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

    # Here we need to count the number of periods (never changes)
    periods = version.count('.')

    # For simplicity we strip out the periods and rejoin as a string
    number = ''.join(version.split("."))

    # Here we can increment the number now by converting to int first
    number = int(number) + 1

    # Now we convert it back to a str so we can manipulate it
    strNumber = str(number)

    # Here's the tricky part:
    #  Since we know how many periods there are and that they don't change
    #  we can simply join WITH PERIODS the last x (period count) numbers 
    #  with the first untouched numbers, also including a periodd in the middle.
    #  We need to also check if it is a single number otherwise we don't
    #  need to include the period.
    if len(strNumber) > 1:
        newVersion = strNumber[0:len(strNumber) - periods] + '.' + '.'.join(strNumber[len(strNumber) - periods:len(strNumber)])
    else:
        return '.'.join(strNumber)

    return newVersion