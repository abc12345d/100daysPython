class QuizBrain:
    def __init__(self, question_bank) -> None:
        self.question_number = 0
        self.question_list = question_bank
        self.score = 0

    def check_answer(self,correct_answer, user_answer):
        is_correct = False

        if correct_answer == "True":
            if user_answer == "true" or user_answer == "t":
                is_correct = True
        else:
            if user_answer == "false" or user_answer == "f":
                is_correct = True
        
        if is_correct:
            self.score += 1
            print("You got it right!")
        else: 
            print("Unfortunately, you got it wrong.")
        
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is {self.score}/{self.question_number}")
        print("\n")
    
    def still_has_questions(self):
        return self.question_number < len(self.question_list)
    
    def next_question(self):
        curr_question = self.question_list[self.question_number]
        self.question_number += 1

        user_answer = input(f"Q.{self.question_number}: {curr_question.text} (True/False)?: ")
        self.check_answer(curr_question.answer, user_answer.lower())
        






