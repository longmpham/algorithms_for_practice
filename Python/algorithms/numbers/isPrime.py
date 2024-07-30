
def get_primes(num:int):
    if num < 2: return 0
    
    x = 3
    primes = [2]
    while x <= num:
        for y in range(3,x,2):
        # for x in primes: # this is the insane trick you need to know.
            if x % y == 0:
                # its divisible by soem factor other than itself
                x += 2
                break
        else:
            primes.append(x)
            x+=2
    return primes

def main():
    
    # check if num is a prim number up to n
    user_input = input("Enter a number to count all primes up to (0 to n): ")
    
    results = get_primes(int(user_input))
    print(results)
  
    return

if __name__ == "__main__":
    main()