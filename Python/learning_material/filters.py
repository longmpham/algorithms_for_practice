# how to map in Python


def check_even(a):
    return a % 2 == 0

def main():
    
    # change it to a list
    print(list(filter(check_even, [1,2,3,4,5,6])))
    
    # iterate through the filtered list
    for item in filter(check_even, [1,2,3,4,5,6]):
        print(item)
    
    return

if __name__ == "__main__":
    main()  