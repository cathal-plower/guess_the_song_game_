import random
import time

# -------------------------------------------------------------------
# HARD ZACH BRYAN SONG DATABASE
# -------------------------------------------------------------------
HARD_ZACH_BRYAN_SONGS = [
    {
        "lyric_clue": "I remember everything, the nights we spent under the stars...",
        "answer": "I Remember Everything",
        "options": ["I Remember Everything", "Dawns", "Something in the Orange", "Oklahoma Smokeshow"],
        "album": "Zach Bryan"
    },
    {
        "lyric_clue": "It'll be fine by dusk light I'm tellin' you baby...",
        "answer": "Something in the Orange",
        "options": ["Something in the Orange", "Heading South", "Burn, Burn, Burn", "Mine Again"],
        "album": "American Heartbreak"
    },
    {
        "lyric_clue": "People ruin people, I don't wanna ruin you...",
        "answer": "Dawns",
        "options": ["Dawns", "Sun to Me", "Heavy Eyes", "Snow"],
        "album": "Single"
    },
    {
        "lyric_clue": "Wish I could explain how the toxins in my brain...",
        "answer": "Mine Again",
        "options": ["Mine Again", "Revival", "East Side of Sorrow", "Open the Gate"],
        "album": "American Heartbreak"
    },
    {
        "lyric_clue": "Don't you give up on me yet...",
        "answer": "Sun to Me",
        "options": ["Sun to Me", "Oklahoma Smokeshow", "Quittin' Time", "Corinthians"],
        "album": "American Heartbreak"
    },
    {
        "lyric_clue": "The boys are breakin' bottles out behind the county jail...",
        "answer": "Oklahoma Smokeshow",
        "options": ["Oklahoma Smokeshow", "Revival", "Tourniquet", "Motorcycle Drive By"],
        "album": "American Heartbreak"
    },
    {
        "lyric_clue": "Find someone who grows flowers in the darkest parts of you...",
        "answer": "East Side of Sorrow",
        "options": ["East Side of Sorrow", "Holy Roller", "Tishomingo", "Blue"],
        "album": "Zach Bryan"
    },
    {
        "lyric_clue": "Well, the highway boys are all drinkin' whiskey...",
        "answer": "Heading South",
        "options": ["Heading South", "Burn, Burn, Burn", "God Speed", "Cold Damn Vampires"],
        "album": "DeAnn"
    }
]


def run_zach_quiz():
    while True:
        score = 0
        total_questions = min(5, len(HARD_ZACH_BRYAN_SONGS))

        print("=" * 60)
        print("HARD MODE: ZACH BRYAN LYRIC QUIZ")
        print("=" * 60)
        print("Only true Zach Bryan fans can score 5/5!\n")

        shuffled_pool = HARD_ZACH_BRYAN_SONGS.copy()
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
                print(f"✅ Correct! '{q['answer']}' is right.")
                score += 1
            else:
                print(f"❌ Incorrect. The correct answer was '{q['answer']}'.")

            time.sleep(1)

        print("\n" + "=" * 60)
        print(f"FINAL SCORE: {score}/{total_questions}")
        print("=" * 60)

        if score == total_questions:
            print("🏆 LEGENDARY! You're a Zach Bryan expert!")
        elif score >= 3:
            print("👏 Great job! You know your Zach Bryan songs.")
        else:
            print("🎵 That was tough! Try again.")

        replay = input("\nPlay again? (Y/N): ").strip().upper()

        if replay != "Y":
            print("\nThanks for playing!")
            break


if __name__ == "__main__":
    run_zach_quiz()