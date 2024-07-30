# how to map in Python


def mySquare(a):
    return a**2

def main():
    
    for item in map(mySquare, [1,2,3,4,5,6]):
        print(item)
    
    return

if __name__ == "__main__":
    main()  