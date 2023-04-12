from tkinter import *

window = Tk()
window.title('Mile to Km Converter')
window.config(padx=20,pady=20)

miles_entry = Entry(width=6)
miles_entry.insert(END, string="0")
miles_entry.focus()
miles_entry.grid(row=0,column=1)

miles_unit_text = Label(text="Miles")
miles_unit_text.grid(row=0,column=2)

equal_to_text = Label(text="is equal to")
equal_to_text.grid(row=1,column=0)

km_text = Label(text="0")
km_text.grid(row=1, column=1)

km_unit_text =  Label(text="Km")
km_unit_text.grid(row=1, column=2)

def mile_to_km():
    km = int(miles_entry.get()) * 1.60934
    km_text['text'] = f"{km:.2f}"

calc_button = Button(text='Calculate', command=mile_to_km,width=4)
calc_button.grid(row=2, column=1)

window.mainloop()