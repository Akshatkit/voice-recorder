from tkinter import *
from tkinter import messagebox
import sounddevice as sound
from scipy.io.wavfile import write
import time
import wavio as wv


root = Tk()
root.geometry("600x700+400+80")

root.resizable(False,False)

root.title("Voice Record")
root.configure(background="#606060")

def Record():
    freq=44100
    dur = int(duration.get())
    recording= sound.rec(dur*freq,  samplerate=freq,channels=2)
    #timer
    try:
        temp=int(duration.get())
    except:
        print("Please enter the right value")
    while temp>0:
        root.update()
        time.sleep(1)
        temp -=1
        if temp==0:
            messagebox.showinfo("Time countdown","Time's up")
        Label(text=f"{str(temp)}", font="arial 40", width=4, background="#606060").place(x=240,y=590)
        
    sound.wait()
    write("recording.wav",freq,recording)
 
# icon
image_icon=PhotoImage(file="voice.png")
root.iconphoto(False,image_icon)

# logo
photo=PhotoImage(file="record.png")
myimage=Label(image=photo,background="#606060")
myimage.pack(padx=5,pady=5)


# Name
Label(text="Voice Recorder", font="arial 25 bold", background="#606060",fg="white").pack()


# Entry
duration= StringVar()
entery = Entry(root,textvariable=duration,font="arial 25",width=15).pack(pady=10)
Label(text="Entertime in second",font="arial 15",background="#606060",fg="white").pack()

# Button
record = Button(root,font="arial 20" , text="Record",bg="#111111",fg="white", border=1 , command=Record).pack(pady=30)

root.mainloop()