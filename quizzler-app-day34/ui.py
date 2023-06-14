from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ('Arial',20,'italic')

class QuizInterface:
    def __init__(self,quiz:QuizBrain) -> None:
        self.quiz = quiz

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(background=THEME_COLOR,padx=20)

        self.score_label = Label(text= f"Score: {self.quiz.score}",fg='white',background=THEME_COLOR, highlightthickness=0,pady=20)
        self.score_label.grid(column=1,row=0)

        self.canvas = Canvas(width=300,height=250,highlightthickness=0,highlightcolor=THEME_COLOR)
        self.question_text = self.canvas.create_text(150,125,width= 280,text='00:00',font=FONT,fill=THEME_COLOR)
        self.canvas.grid(row=1,column=0,columnspan=2,pady=30)

        true_image = PhotoImage(file="./images/true.png",width=100,height=97)
        self.true_button = Button(image=true_image, command=self.pressed_true,highlightthickness=0,highlightbackground=THEME_COLOR)
        self.true_button.grid(column=0,row=2,pady=20)

        false_image = PhotoImage(file="./images/false.png",width=100,height=97)
        self.false_button = Button(image=false_image, command=self.pressed_false,highlightthickness=0,highlightbackground= THEME_COLOR)
        self.false_button.grid(column=1,row=2,pady=20)

        self.get_next_question()

        self.window.mainloop() 

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.canvas.itemconfig(self.question_text, text= self.quiz.next_question())
        else:
            self.canvas.itemconfig(self.question_text, text= f"You've completed the quiz.\nYour final score was: {self.quiz.score}/{self.quiz.question_number}")
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')
        
    def pressed_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def pressed_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self,is_right):
        self.score_label.config(text=f"Score: {self.quiz.score}")
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')

        self.window.after(1000, self.get_next_question)

        
        