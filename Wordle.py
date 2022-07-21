from tkinter import *

target = "slack"

def myClick():
    guess = e.get()
    if guess == target:
        myLabel3 = Label(root, text="_____________________") 
        myLabel3.pack()
        myLabel2 = Label(root, text="You got it!",height=3)
        myLabel2.pack()
        
    else:
        myLabel3 = Label(root, text="_____________________") 
        myLabel3.pack()
        # Loop through the user's guess, returning the position and value
        for t,value in enumerate(guess):
            # Determine if the value of each letter in the user's guess is equal to the value in the same position of the target word
            if value == target[t]:
                myLabel = Label(root, text="The letter {} is in position {}".format(value,t+1))
                myLabel.pack()
                    
            # Determine if the letter in the user's guess is in the target word but was not guessed in the correct position
            elif value in target:
                myLabel1 = Label(root, text="The letter {} is in the word, but not in position {}".format(value,t+1))
                myLabel1.pack()


root = Tk()
e = Entry(root, width=50)
e.pack()
myButton = Button(root, text="Guess the Wordle!", padx=30, pady=5,command = myClick)
myButton.pack()

root.mainloop()



    
