import random
life = 10
length = 3

answer = random.randint(100, 999)

answer = str(answer)

while life:
    is_guessed = False
    print("=" * 10)

    print("Жизний:", life)

    quess = input("Предложения:")
    if len(quess) != 3 or not quess.isdigit():
        print("Число от 100 до 999, ПОЖВЛУЙСТА!")
        continue