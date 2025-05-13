from subjects import Data_science, mathematics, machine_learning, physics, chemistry
from utils.quiz_engine import start_quiz

print("Welcome!!!")
print("Choose the topic")
print("1.Machine learning")
print("2.Data Science")
print("3.Mathematics")
print("4.Physics")
print("5.Chemistry")

ch=int(input("Enter you choice:"))
if ch == 1:
    start_quiz("Machine Learning", machine_learning.question_bank, machine_learning.options)
elif ch==2:
    start_quiz("Data Science", Data_science.question_bank, Data_science.options)
elif ch ==3:
    start_quiz("Mathematics", mathematics.question_bank, mathematics.options)
elif ch==4:
    start_quiz("Physics", physics.question_bank, physics.options)
elif ch==5:
    start_quiz("Chemistry", chemistry.question_bank, chemistry.options)
else:
    print("Invalid choice, select a valid choice!!")