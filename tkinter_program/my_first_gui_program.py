import tkinter

window = tkinter.Tk()
window.title("My first GUI program")
# if the window contains items which are bigger than the minsize, the size of window might go bigger
window.minsize(width = 500, height = 300)

# label is used to specify the container box where we can place the text or images
text_label = tkinter.Label(text="I am a label", font= ("Arial", 24))
# pack = place the label on the window
text_label.grid(row=0,column=0)

# button
def button_clicked():
    text_label['text'] = entry.get()
    # or text_label.config(text = "Button Got Clicked!")

button = tkinter.Button(text='click me',command=button_clicked)
button.grid(row=1,column=1)

new_button = tkinter.Button(text='new button',command=button_clicked)
new_button.grid(row=0,column=2)

# entry = input block
entry = tkinter.Entry(width=10)
entry.grid(row=2,column=3)

tkinter.mainloop()