from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank=[]
for val in question_data:
    val_text = val["question"]
    val_answer = val["correct_answer"]
    new_question=Question(val_text, val_answer)
    question_bank.append(new_question)
print(question_bank)
quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()
if quiz.still_has_question() == False:
    print(f"Your final score is{quiz.score}")




