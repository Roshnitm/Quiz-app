def start_quiz(subject_name, question_bank, options):
    score=0
    print("************************")
    print("Welcome to the ",subject_name," quiz!!")

    def check_ans(guess,correct_answer):
        if guess==correct_answer:
            return True
        else:
            return False

    for ques_num in range(len(question_bank)):
        print("************************")
        print(question_bank[ques_num]["text"])
        for i in options[ques_num]:
            print(i)

        guess=input("Enter your answer(A/B/C/D):").upper()
        is_correct=check_ans(guess, question_bank[ques_num]["answer"])
        if is_correct:
            print("Correct answer!!")
            score += 1
        else:
            print("Incorrect answer")
            print(f"The correct answer is: {question_bank[ques_num]["answer"]}")
        print(f"Your current score is {score}/{len(question_bank)}")
    print(f"you have given {score} correct answer")     
    print(f"your final score is: {(score/len(question_bank))*100}%")