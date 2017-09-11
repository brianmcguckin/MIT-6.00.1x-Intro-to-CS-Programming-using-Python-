#Write a program that works as follows: you (the user) thinks of an integer between 0 (inclusive)
#and 100 (not inclusive). The computer makes guesses, and you give it input - is its guess too high
#or too low? Using bisection search, the computer will guess the user's secret number!

print('Please think of a number between 0 and 100!')

low = 0
high = 100
guess = int((low + high)/2)

print('Is your secret number '+str(guess)+'?')
print("Enter 'h' to indicate the guess is too high. \
Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.",end="")

userSays = input()

while userSays != 'c':
    if userSays == 'l':
        low = guess
        guess = int((low + high)/2)
        print('Is your secret number '+str(guess)+'?')
        print("Enter 'h' to indicate the guess is too high. \
Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.",end="")
        userSays = input()
    elif userSays == 'h':
        high = guess
        guess = int((low + high)/2)
        print('Is your secret number '+str(guess)+'?')
        print("Enter 'h' to indicate the guess is too high. \
Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.",end="")
        userSays = input()
    else:
        print('Sorry, I did not understand your input.')
        print('Is your secret number '+str(guess)+'?')
        print("Enter 'h' to indicate the guess is too high. \
Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.",end="")
        userSays = input()

print('Game over. Your secret number was: '+str(guess))
