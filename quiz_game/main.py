#%%
from question_model import Question
from data import anime_manga_data
from quiz_brain import QuizBrain

question_bank = []
for q in anime_manga_data:
    q_text = q["question"]
    q_ans = q["correct_answer"]
    question_bank.append(Question(q_text, q_ans))
 
quiz_game = QuizBrain(question_bank)
while quiz_game.still_has_questions():
    quiz_game.next_question()

print("You've completed the quiz.")
print(f"Your final score was: {quiz_game.score}/{quiz_game.question_number} !")
 # %%
