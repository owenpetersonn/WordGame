from tkinter import *

target = "slack"

# Principle game function, a player attempts to guess a secret word and is given hints if they guess a letter that is contained in the secret word
def myClick():
    guess = e.get()
    if guess == target:
        myLabel = Label(root, text="_____________________") 
        myLabel.pack()
        myLabel = Label(root, text="You got it!",height=3)
        myLabel.pack()
        
    else:
        myLabel = Label(root, text="_____________________") 
        myLabel.pack()
        # Loop through the user's guess, returning the position and value
        for t,value in enumerate(guess):
            # Determine if the value of each letter in the user's guess is equal to the value in the same position of the target word
            if value == target[t]:
                myLabel = Label(root, text="The letter {} is in position {}".format(value,t+1))
                myLabel.pack()
                    
            # Determine if the letter in the user's guess is in the target word but was not guessed in the correct position
            elif value in target:
                myLabel = Label(root, text="The letter {} is in the word, but not in position {}".format(value,t+1))
                myLabel.pack()

# Create the root window
root = Tk()
root.title("Completely Unique Word Game")
root.geometry('350x500')

# Create the input field
e = Entry(root, width=20)
e.pack(ipady=3)

# Create the button that calls the game function when clicked
myButton = Button(root, text="Guess the Wordle!", padx=30, pady=7,command = myClick)
myButton.pack()

# Runs the event loop for the root window
root.mainloop()



    
