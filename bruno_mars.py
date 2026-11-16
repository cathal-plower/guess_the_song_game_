import random
import time

# -------------------------------------------------------------------
# HARD BRUNO MARS SONG DATABASE
# -------------------------------------------------------------------
HARD_BRUNO_MARS_SONGS = [
    {
        "lyric_clue": "Easy come, easy go, that's just how you live...",
        "answer": "Grenade",
        "options": ["Grenade", "When I Was Your Man", "Talking to the Moon", "It Will Rain"],
        "album": "Doo-Wops & Hooligans"
    },
    {
        "lyric_clue": "I know you're somewhere out there, somewhere far away...",
        "answer": "Talking to the Moon",
        "options": ["Talking to the Moon", "Just The Way You Are", "Liquor Store Blues", "Count On Me"],
        "album": "Doo-Wops & Hooligans"
    },
    {
        "lyric_clue": "Same bed but it feels just a little bit bigger now...",
        "answer": "When I Was Your Man",
        "options": ["When I Was Your Man", "Grenade", "It Will Rain", "Marry You"],
        "album": "Unorthodox Jukebox"
    },
    {
        "lyric_clue": "Don't believe me? Just watch!",
        "answer": "Uptown Funk",
        "options": ["Uptown Funk", "24K Magic", "Finesse", "Treasure"],
        "album": "Single / Feature"
    },
    {
        "lyric_clue": "Players, put your pinky rings up to the moon...",
        "answer": "24K Magic",
        "options": ["24K Magic", "Chunky", "Perm", "Finesse"],
        "album": "24K Magic"
    },
    {
        "lyric_clue": "Why? Why? Why? Why? Mmm, why?",
        "answer": "Versace on the Floor",
        "options": ["Versace on the Floor", "Too Good To Say Goodbye", "Calling All My Lovelies", "Chunky"],
        "album": "24K Magic"
    },
    {
        "lyric_clue": "I wanna be a billionaire so freakin' bad...",
        "answer": "Billionaire",
        "options": ["Billionaire", "Nothin' on You", "Lighters", "Young Girls"],
        "album": "Feature / Single"
    },
    {
        "lyric_clue": "Cause girls like you run round with guys like me...",
        "answer": "Girls Like You",
        "options": ["Girls Like You", "Leave The Door Open", "Skate", "Treasure"],
        "album": "Feature / Single"
    }
]


def run_quiz():
    while True:
        score = 0
        total_questions = min(5, len(HARD_BRUNO_MARS_SONGS))

        print("=" * 60)
        print("HARD MODE: BRUNO MARS LYRIC QUIZ")
        print("=" * 60)
        print("Only true Bruno Mars fans can get 5/5!\n")

        shuffled_pool = HARD_BRUNO_MARS_SONGS.copy()
        random.shuffle(shuffled_pool)
        selected_questions = shuffled_pool[:total_questions]

        for index, q in enumerate(selected_questions, start=1):
            print(f"\n--- Question {index} of {total_questions} ---")
            print(f"Lyric Clue: {q['lyric_clue']}")
            print(f"Album Hint: {q['album']}")
            print("\nChoose your answer:")

            options = q["options"].copy()
            random.shuffle(options)

            labels = ["A", "B", "C", "D"]

            for label, option in zip(labels, options):
                print(f"[{label}] {option}")

            user_choice = input("\nYour Choice (A/B/C/D): ").strip().upper()

            choice_map = dict(zip(labels, options))
            selected_song = choice_map.get(user_choice)

            if selected_song == q["answer"]:
                print(f"Correct! '{q['answer']}' is right.")
                score += 1
            else:
                print(f"Incorrect. The correct answer was '{q['answer']}'.")

            time.sleep(1)

        print("\n" + "=" * 60)
        print(f"FINAL SCORE: {score}/{total_questions}")
        print("=" * 60)

        if score == total_questions:
            print("LEGENDARY! You're a Bruno Mars expert!")
        elif score >= 3:
            print("Great job! You know your Bruno Mars songs.")
        else:
            print("That was tough! Try again.")

        replay = input("\nPlay again? (Y/N): ").strip().upper()

        if replay != "Y":
            print("\nThanks for playing!")
            break


if __name__ == "__main__":
    run_quiz()