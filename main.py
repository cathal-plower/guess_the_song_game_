from drake_quiz import run_drake_quiz
from zach_bryan_quiz import run_zach_quiz
from bruno_mars_quiz import run_bruno_quiz
from kanye_west_quiz import run_kanye_quiz
from taylor_swift_quiz import run_taylor_quiz


while True:

    print("\n===== LYRIC GUESSING GAME =====")
    print("1. Drake")
    print("2. Zach Bryan")
    print("3. Bruno Mars")
    print("4. Rihanna")
    print("5. Kanye West")
    print("6. Taylor Swift")
    print("7. Exit")

    choice = input("\nChoose an artist: ")

    if choice == "1":
        run_drake_quiz()

    elif choice == "2":
        run_zach_quiz()

    elif choice == "3":
        run_bruno_quiz()

    elif choice == "4":
        run_rihanna_quiz()

    elif choice == "5":
        run_kanye_quiz()

    elif choice == "6":
        run_taylor_quiz()

    elif choice == "7":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
