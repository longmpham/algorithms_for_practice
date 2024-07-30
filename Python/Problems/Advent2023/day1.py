# The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

# For example:

# 1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet

# In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

# Consider your entire calibration document. What is the sum of all of the calibration values?

# 1. create a function read to a file input line by line
# 2. in each line i need to read the input and look for the first digit leftwards and the first digit rightwards following the examples above
# 3. once number is found on 1 side, find the other number on other side
# 4. put those digits together to create a double digit number for each line
# 5. take the sum of those digits as your output

# read file


# create array of tuples 
digits_map = []

with open("day1_data.txt", "r") as file:
  
  # line is a string
  for line in file:
    
    # each line is being read now grab the digits
    # digits_map.append(digit) for digit in line if digit == digit.isdigit()
    stop_index = 0
    for index in range(len(line)):
      if line[index].isdigit():
        digit_first = line[index]
        stop_index = index
        break
    
    # now go in reverse
    for index in range(len(line) - 1, stop_index-1, -1):
      if line[index].isdigit():
        digit_second = line[index]
        break
    
    # now check if both digits are digits
    if digit_first and digit_second:
      digit_pair = digit_first + digit_second
      # convert to number
      digit_pair = int(digit_pair)
      digits_map.append(digit_pair)
      

total = sum([x for x in digits_map])
print(digits_map)
print(f"total={total}")