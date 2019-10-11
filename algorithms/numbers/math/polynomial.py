"""


    # find if N can be a multiple of xyz given this formula
    
    N = 6x + 9y + 20z  

    20 = 6(0) + 9(0) + 20(1)
    30 = 6(5)
    15 = 6(1) + 9(1)
    35 = 6(1) + 9(1) + 20(1)


    23 = fail
    43 = fail
    < 6 is a fail.

    n = 36
    n = 6(6)
    n = 6(0) + 9(4) + 20(0)
    n = 20 + remainder of 16 -> fails.

    20 + 20 = 40 -> over
    20 + 9 + 9 -> over
    20 + 9 + 6 -> over
    9 + 9 + 9 + 9


"""

def poly(n: int):

# first iteration / thought
    x_count = 0
    y_count = 0
    z_count = 0
    x = 6
    y = 9
    z = 20

    # sort this or hardcode for now to test
    variables = [z,y,x]
    var_count = [z_count, y_count, x_count]
    #23 - 20 - 3
    #25 = fail
    #36 = 4y OR 6x

    # this loop makes it so that it works if number works with 20
    for i in range(len(variables)):
        var_count[i] = n // variables[i]
        print(var_count[i], n)

        # if remainder is divisible by 6 or 9

        n = n % variables[i]
        if not n:
            break

    if n:
        return False

    return var_count

n = 36
print(poly(n))

