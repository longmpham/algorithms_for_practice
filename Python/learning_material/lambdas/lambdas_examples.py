"""
	Learning all about lambdas. Yay
"""

# how to map in Python


def square2(a):
    return a ** 2

def main():
    
    mylist = [1,2,3,4,5,6]
    
    newlist = [(lambda num : num ** 2)(num) for num in mylist]
    
    print(list(map(lambda num:num**2, mylist)))
    
    print (newlist)
    return

if __name__ == "__main__":
    main()  