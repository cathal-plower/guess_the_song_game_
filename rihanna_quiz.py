import random
import time

# -------------------------------------------------------------------
# HARD RIHANNA SONG DATABASE (Deep Cuts & Tricky Lyric Clues)
# -------------------------------------------------------------------
HARD_RIHANNA_SONGS = [
    {
        "lyric_clue": '"Feeling like a silhouette in the dark..."',
        "answer": "Disturbia",
        "options": ["Disturbia", "SOS", "Shut Up and Drive", "Unfaithful"],
        "album": "Good Girl Gone Bad"
    },
    {
        "lyric_clue": '"I run this town, I\'m on control..."',
        "answer": "Run This Town",
        "options": ["Run This Town", "Hard", "Rockstar 101", "G4L"],
        "album": "Rated R"
    },
    {
        "lyric_clue": '"Wild, wild, wild thoughts... when I\'m with you, all I get is..."',
        "answer": "Wild Thoughts",
        "options": ["Wild Thoughts", "Work", "Needed Me", "Kiss It Better"],
        "album": "Single / Feature"
    },
    {
        "lyric_clue": '"I\'m standing with the army, full-armored tank..."',
        "answer": "Hard",
        "options": ["Hard", "Wait Your Turn", "Russian Roulette", "Rude Boy"],
        "album": "Rated R"
    },
    {
        "lyric_clue": '"Ten out of ten, I\'m a ten, yes I\'m a ten..."',
        "answer": "Phresh Out the Runway",
        "options": ["Phresh Out the Runway", "Pour It Up", "Jump", "Cockiness (Love It)"],
        "album": "Unapologetic"
    },
    {
        "lyric_clue": '"Didn\'t I do it for ya? Why won\'t you believe it?"',
        "answer": "Kiss It Better",
        "options": ["Kiss It Better", "Love on the Brain", "Higher", "Close to You"],
        "album": "Anti"
    },
    {
        "lyric_clue": '"He said, \'Keep it on the low-low, girl, nobody gotta know\'..."',
        "answer": "Sex with Me",
        "options": ["Sex with Me", "Yeah, I Said It", "Needed Me", "Consideration"],
        "album": "Anti"
    },
    {
        "lyric_clue": '"Round and around and around and around we go..."',
        "answer": "Stay",
        "options": ["Stay", "Diamonds", "What Now", "Cold Case Love"],
        "album": "Unapologetic"
    }
]

def run_quiz():
    while True:
        score = 0
        total_questions = min(5, len(HARD_RIHANNA_SONGS))
        
        print("=" * 60)
        print(" 🔥 HARD MODE: RIHANNA LYRIC QUIZ 🔥")
        print("=" * 60)
        print("Only true Navy fans can get 5/5 on these deep cuts!\n")
        
        # Shuffle questions for a completely fresh game each run
        shuffled_pool = HARD_RIHANNA_SONGS.copy()
        random.shuffle(shuffled_pool)
        selected_questions = shuffled_pool[:total_questions]
        
        for index, q in enumerate(selected_questions, start=1):
            print(f"\n--- Question {index} of {total_questions} ---")
            print(f"Tricky Lyric Clue: {q['lyric_clue']}")
            print(f"Album Hint: 💿 {q['album']}")
            print("\nChoose your answer:")
            
            # Shuffle options
            options = q["options"].copy()
            random.shuffle(options)
            
            labels = ["A", "B", "C", "D"]
            for label, option in zip(labels, options):
                print(f"  [{label}] {option}")
                
            user_choice = input("\nYour Choice (A/B/C/D): ").strip().upper()
            
            choice_map = dict(zip(labels, options))
            selected_song = choice_map.get(user_choice)
            
            if selected_song == q["answer"]:
                print(f"✨ CORRECT! You really know '{q['answer']}' ({q['album']})!")
                score += 1
            else:
                print(f"❌ INCORRECT. The correct song was '{q['answer']}' ({q['album']}).")
                
            time.sleep(1)

        # Final Results
        print("\n" + "=" * 60)
        print(f"🏆 HARD MODE COMPLETE! Score: {score} / {total_questions}")
        print("=" * 60)
        
        if score == total_questions:
            print("👑 LEGENDARY! You are officially an elite Rihanna expert.")
        elif score >= 3:
            print("👏 Impressive! You know way more than just the main radio singles.")
        else:
            print("🎧 That was tough! You can find full lyrics for these tracks by searching Google.")

        print("\n" + "-" * 60)
        replay = input("🔁 Want to try Hard Mode again? (Y/N): ").strip().upper()
        if replay != 'Y':
            print("\nThanks for playing Hard Mode! See you next time! 🔥\n")
            break
        print("\n\n")

if __name__ == "__main__":
    run_quiz()