# Store the target word
target = "osvjud"

# Loop through 5 times, giving the user 5 chances to guess the target word
for i in range(5):
    guess = input("Guess the Wordle: ")
    if guess == target:
        print("You got it!")
        break
    else:
        # Loop through the user's guess, returning the position and value
        for t,value in enumerate(guess):
            # Determine if the value of each letter in the user's guess is equal to the value in the same position of the target word
            if value == target[t]:
                print("The letter",value,"is in position",t+1)
            # Determine if the letter in the user's guess is in the target word but was not guessed in the correct position
            elif value in target:
                print("The letter",value,"is in the word, but not in position", t+1)
if guess == target:
    pass
else:
    print("You're out of tries! The word was:",target)

    
