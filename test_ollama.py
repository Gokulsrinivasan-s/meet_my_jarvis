from brain import ask_ai

while True:

    question = input("You : ")

    if question.lower() == "exit":
        break

    answer = ask_ai(question)

    print("\nJarvis:\n")

    print(answer)

    print()