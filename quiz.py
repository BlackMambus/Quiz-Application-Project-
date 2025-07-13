questions = {
    "What is the capital of France?": "Paris",
    "What is 2 + 2?": "4",
    "What is the color of the sky on a clear day?": "Blue"
}

score = 0
for question, answer in questions.items():
    user_answer = input(question + " ")
    if user_answer.strip().lower() == answer.lower():
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer is {answer}.")

print(f"\nYour final score is {score}/{len(questions)}")



