def count_pretty_numbers(l,r):
    pretty_count = 0
    # Iterate through the range and count pretty numbers
    for num in range(l,r+1):
        last_digit = num % 10
        if last_digit == 5:
            pretty_count += 1
    return pretty_count
# Input the number of test cases
t = int(input())
# Process each test case
for _ in range(t):
    # Input the range L and R for each test case
    l,r = map(int,input().split())
    #Call the function to count pretty numbers in the given range
    result = count_pretty_numbers(l,r)
    #print the result for each test case
    print(result)
