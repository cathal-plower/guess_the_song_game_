import random
import time

# -------------------------------------------------------------------
# HARD DRAKE SONG DATABASE
# -------------------------------------------------------------------
HARD_DRAKE_SONGS = [
    {
        "lyric_clue": "Started from the bottom, now we're here...",
        "answer": "Started From the Bottom",
        "options": ["Started From the Bottom", "God's Plan", "Headlines", "Energy"],
        "album": "Nothing Was the Same"
    },
    {
        "lyric_clue": "I only love my bed and my momma, I'm sorry...",
        "answer": "God's Plan",
        "options": ["God's Plan", "Hotline Bling", "One Dance", "Nice For What"],
        "album": "Scorpion"
    },
    {
        "lyric_clue": "You used to call me on my cell phone...",
        "answer": "Hotline Bling",
        "options": ["Hotline Bling", "Controlla", "One Dance", "Find Your Love"],
        "album": "Views"
    },
    {
        "lyric_clue": "Know yourself, know your worth...",
        "answer": "Know Yourself",
        "options": ["Know Yourself", "Energy", "Worst Behavior", "Nonstop"],
        "album": "If You're Reading This It's Too Late"
    },
    {
        "lyric_clue": "Last name ever, first name greatest...",
        "answer": "Forever",
        "options": ["Forever", "Over", "Best I Ever Had", "Successful"],
        "album": "Single"
    },
    {
        "lyric_clue": "Working on the weekend like usual...",
        "answer": "Nonstop",
        "options": ["Nonstop", "Mob Ties", "Laugh Now Cry Later", "Energy"],
        "album": "Scorpion"
    },
    {
        "lyric_clue": "I've been moving calm, don't start no trouble with me...",
        "answer": "In My Feelings",
        "options": ["In My Feelings", "Passionfruit", "One Dance", "Fake Love"],
        "album": "Scorpion"
    },
    {
        "lyric_clue": "Got so many chains they call me Chaining Tatum...",
        "answer": "Pop Style",
        "options": ["Pop Style", "Energy", "10 Bands", "Jumpman"],
        "album": "Views"
    }
]


def run_quiz():
    while True:
        score = 0
        total_questions = min(5, len(HARD_DRAKE_SONGS))

        print("=" * 60)
        print("HARD MODE: DRAKE LYRIC QUIZ")
        print("=" * 60)
        print("Only true Drake fans can score 5/5!\n")

        shuffled_pool = HARD_DRAKE_SONGS.copy()
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
            print("LEGENDARY! You're a Drake expert!")
        elif score >= 3:
            print("Great job! You know your Drake songs.")
        else:
            print("That was tough! Try again.")

        replay = input("\nPlay again? (Y/N): ").strip().upper()

        if replay != "Y":
            print("\nThanks for playing!")
            break


if __name__ == "__main__":
    run_quiz()