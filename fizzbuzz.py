# ask the user to give you the highest number they'd like to go
# format the input as an integar

highest=int (input ("Insert Highest Number: "))

# create a for loop for the range between 1 and the highest number chosen
# note that python's range will end at the number before what you chose, hence we add 1
for y in range (1,highest+1):

    # if the number is evenly divisible by 3 and 5, print FIZZBUZZ and skip it
    if y%3==0 and y%5==0:
        print ("FizzBuzz")
        continue
    # if the number is evenly divisible by 3, print FIZZ and skip the number
    elif y%3==0:
        print ("Fizz")
        continue
    # if the number is evenly divisble by 5, print BUZZ and skip the number
    elif y%5==0:        
        print ("Buzz")
        continue

# print the numbers
    print (y)
        
