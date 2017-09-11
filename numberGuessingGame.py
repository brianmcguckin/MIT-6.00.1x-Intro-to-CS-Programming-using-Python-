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
