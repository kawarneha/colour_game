import tkinter
import random
  
colours = ['Red','Blue','Green','Pink','Black',
           'Yellow','Orange','White','Purple','Brown'] #Colours which will going to be displayed
score = 0
timeleft = 30	    #Time remaining,total time will be 30 seconds  


def startGame(event):
    
    if(timeleft == 30):
        countdown()
    nextColour()

  
def nextColour():
    
    global score,timeleft
    if(timeleft > 0):                          #if game is not over 
        e.focus_set()
        if(e.get().lower() == colours[1].lower()):
            score += 1
        e.delete(0,tkinter.END)                #delete the entered value in text box
          
        random.shuffle(colours)
        label.config(fg = str(colours[1]), text = str(colours[0]))
        scoreLabel.config(text = "Score: " + str(score))

  
def countdown():
    
    global timeleft
    if (timeleft > 0):
        timeleft -= 1
        timeLabel.config(text = "Time left: "+ str(timeleft))
        timeLabel.after(1000, countdown)      #calling the function again after 1 second

  
window = tkinter.Tk()
window.title("COLOUR-GAME")
window.geometry("425x250")
  
info = tkinter.Label(window, text = "Type the colour of the words,not the word text!",font = ('Helvetica', 14))
info.pack() 
  
scoreLabel = tkinter.Label(window, text = "\n Press  ENTER  to start :)",font = ('Helvetica', 14))
scoreLabel.pack() 
  
timeLabel = tkinter.Label(window, text = "Time left: " +str(timeleft), font = ('Helvetica', 12))
timeLabel.pack()
  
label = tkinter.Label(window, font = ('Helvetica', 60))
label.pack()
  
e = tkinter.Entry(window)
window.bind('<Return>', startGame)
e.pack()
  
e.focus_set()
#root.configure(bg='black') 
window.mainloop()
