from questions import QUESTIONS

# Valida las opciones sin llamadas recursivas.
def choose(options):
    while True:
        answer = input("-> ").strip().lower()
        if answer in options:
            return answer
        print("Opción inválida. Intenta de nuevo.")


def play(topic):
    points = 0
    correct_count = 0
    questions = QUESTIONS[topic].values()
    for question, options, correct, reward in questions:
        if reward == 20:
            print("\n¡Pregunta con puntos dobles!")
        print(question)
        for letter, answer in options.items():
            print(f"    {letter}. {answer}")
        if choose(options) == correct:
            points += reward
            correct_count += 1
            print(f"Respuesta correcta. +{reward} puntos.")
        else:
            points -= 3
            print(f"Respuesta incorrecta. Correcta: {correct}. -3 puntos.")
        print(f"Puntos: {points}")
    print(f"Total: {points} puntos. Aciertos: {correct_count / len(questions) * 100:g}%")


def main():
    topics = list(QUESTIONS)
    while True:
        print("\n¿Quieres jugar una trivia?\n1. Sí\n2. No")
        if choose(("1", "2")) == "2":
            break
        for index, topic in enumerate(topics, 1):
            print(f"{index}. {topic.capitalize()}")
        selection = choose(tuple(str(i) for i in range(1, len(topics) + 1)))
        play(topics[int(selection) - 1])


if __name__ == "__main__":
    main()
