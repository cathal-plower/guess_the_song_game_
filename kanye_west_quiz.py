import random
import time

# -------------------------------------------------------------------
# COMPREHENSIVE KANYE WEST SONG DATABASE (All Eras)
# -------------------------------------------------------------------
ALL_KANYE_SONGS = [
    # The College Dropout
    {
        "lyric_clue": '"I wake up looking at the Netflix, but first, let\'s eat Waffle House..."',
        "answer": "Through the Wire",
        "options": ["Through the Wire", "All Falls Down", "Jesus Walks", "Spaceship"],
        "album": "The College Dropout"
    },
    {
        "lyric_clue": '"We the mill-e-ans, baby, the millionaires..."',
        "answer": "All Falls Down",
        "options": ["All Falls Down", "Slow Jamz", "Two Words", "Family Business"],
        "album": "The College Dropout"
    },
    {
        "lyric_clue": '"God show me the way because the Devil\'s tryna break me down..."',
        "answer": "Jesus Walks",
        "options": ["Jesus Walks", "Never Let Me Down", "Get Em High", "Workout Plan"],
        "album": "The College Dropout"
    },

    # Late Registration
    {
        "lyric_clue": '"She take my money when I\'m in need..."',
        "answer": "Gold Digger",
        "options": ["Touch the Sky", "Gold Digger", "Diamonds from Sierra Leone", "Hey Mama"],
        "album": "Late Registration"
    },
    {
        "lyric_clue": '"I\'m trying to right my wrongs, but it\'s funny the same wrongs help me write the songs..."',
        "answer": "Touch the Sky",
        "options": ["Drive Slow", "Touch the Sky", "Heard \'Em Say", "Late"],
        "album": "Late Registration"
    },

    # Graduation
    {
        "lyric_clue": '"N-now th-that that don\'t kill me, can only make me stronger..."',
        "answer": "Stronger",
        "options": ["Stronger", "Good Morning", "Champion", "Flashing Lights"],
        "album": "Graduation"
    },
    {
        "lyric_clue": '"She don\'t believe in shootin\' stars, but she believe in shoes and cars..."',
        "answer": "Flashing Lights",
        "options": ["Good Life", "Flashing Lights", "Can\'t Tell Me Nothing", "Homecoming"],
        "album": "Graduation"
    },

    # 808s & Heartbreak
    {
        "lyric_clue": '"In the coldest night, she hopes that our love will survive..."',
        "answer": "Heartless",
        "options": ["Heartless", "Love Lockdown", "Paranoid", "Say You Will"],
        "album": "808s & Heartbreak"
    },
    {
        "lyric_clue": '"I\'m not happy and I\'m not sad..."',
        "answer": "Paranoid",
        "options": ["Amazing", "Robocop", "Paranoid", "Coldest Winter"],
        "album": "808s & Heartbreak"
    },

    # My Beautiful Dark Twisted Fantasy
    {
        "lyric_clue": '"No one man should have all that power..."',
        "answer": "Power",
        "options": ["Runaway", "All of the Lights", "Power", "Monster"],
        "album": "My Beautiful Dark Twisted Fantasy"
    },
    {
        "lyric_clue": '"Let\'s have a toast for the douchebags, let\'s have a toast for the assholes..."',
        "answer": "Runaway",
        "options": ["Runaway", "Dark Fantasy", "Gorgeous", "Lost in the World"],
        "album": "My Beautiful Dark Twisted Fantasy"
    },

    # Yeezus
    {
        "lyric_clue": '"For my sport n----s, grabbin\' dat dough, grabbin\' dat dough..."',
        "answer": "New Slaves",
        "options": ["Black Skinhead", "New Slaves", "Blood on the Leaves", "Bound 2"],
        "album": "Yeezus"
    },
    {
        "lyric_clue": '"Uh-huh, honey..."',
        "answer": "Bound 2",
        "options": ["I Am a God", "On Sight", "Bound 2", "Hold My Liquor"],
        "album": "Yeezus"
    },

    # The Life of Pablo
    {
        "lyric_clue": '"I feel like me and Taylor might still have sex..."',
        "answer": "Famous",
        "options": ["Ultralight Beam", "Famous", "Father Stretch My Hands", "Fade"],
        "album": "The Life of Pablo"
    },
    {
        "lyric_clue": '"Now if I fuck this model..."',
        "answer": "Father Stretch My Hands Pt. 1",
        "options": ["Highlights", "Feedback", "Father Stretch My Hands Pt. 1", "Waves"],
        "album": "The Life of Pablo"
    },

    # Donda
    {
        "lyric_clue": '"God\'s not finished..."',
        "answer": "Jail",
        "options": ["Hurricane", "Jail", "Off the Grid", "Moon"],
        "album": "Donda"
    }
]

def run_quiz():
    while True:
        score = 0
        total_questions = min(5, len(ALL_KANYE_SONGS))
        
        print("=" * 60)
        print(" 🌊 ULTIMATE KANYE WEST RANDOMIZED SONG QUIZ 🌊")
        print("=" * 60)
        print(f"Loaded a massive database of Kanye tracks across all eras!")
        print(f"Randomly selecting {total_questions} questions for this round...\n")
        
        # Fully randomize and shuffle the entire database pool
        shuffled_pool = ALL_KANYE_SONGS.copy()
        random.shuffle(shuffled_pool)
        selected_questions = shuffled_pool[:total_questions]
        
        for index, q in enumerate(selected_questions, start=1):
            print(f"\n--- Question {index} of {total_questions} ---")
            print(f"Lyric Clue: {q['lyric_clue']}")
            print(f"Album Hint: 💿 {q['album']}")
            print("\nChoose your answer:")
            
            # Shuffle multiple-choice options so the correct answer moves around
            options = q["options"].copy()
            random.shuffle(options)
            
            labels = ["A", "B", "C", "D"]
            for label, option in zip(labels, options):
                print(f"  [{label}] {option}")
                
            # Get user input
            user_choice = input("\nYour Choice (A/B/C/D): ").strip().upper()
            
            # Map user selection back to the corresponding option text
            choice_map = dict(zip(labels, options))
            selected_song = choice_map.get(user_choice)
            
            # Validate answer
            if selected_song == q["answer"]:
                print(f"✨ CORRECT! It's '{q['answer']}' from the album '{q['album']}'!")
                score += 1
            else:
                print(f"❌ INCORRECT. The correct song was '{q['answer']}' ({q['album']}).")
                
            time.sleep(1)  # Brief pause between questions

        # Final Results
        print("\n" + "=" * 60)
        print(f"🏆 QUIZ COMPLETE! Your Score: {score} / {total_questions}")
        print("=" * 60)
        
        if score == total_questions:
            print("🐐 GOAT status achieved! You know your Kanye discography inside and out.")
        elif score >= total_questions / 2:
            print("🌊 Wave is here! Great job knowing your classic hits.")
        else:
            print("🎧 Time to queue up some dropout-era tracks and try again!")

        # Replay prompt loop
        print("\n" + "-" * 60)
        replay = input("🔁 Would you like to play another round? (Y/N): ").strip().upper()
        if replay != 'Y':
            print("\nThanks for playing! See you next time! 🌊\n")
            break
        print("\n\n")  # Spacing before the next game round starts

if __name__ == "__main__":
    run_quiz()