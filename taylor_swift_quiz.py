import random
import time

# -------------------------------------------------------------------
# COMPREHENSIVE TAYLOR SWIFT SONG DATABASE (All Eras)
# -------------------------------------------------------------------
ALL_TAYLOR_SONGS = [
    # Fearless
    {
        "lyric_clue": '"It\'s a love story, baby, just say, Yes..."',
        "answer": "Love Story",
        "options": ["Love Story", "You Belong With Me", "Mine", "Wildest Dreams"],
        "album": "Fearless"
    },
    {
        "lyric_clue": '"If you could see that I\'m the one who understands you..."',
        "answer": "You Belong With Me",
        "options": ["You Belong With Me", "White Horse", "Fifteen", "Fearless"],
        "album": "Fearless"
    },

    # Red
    {
        "lyric_clue": '"And I know it\'s long gone and that magic\'s not here no more..."',
        "answer": "All Too Well",
        "options": ["22", "Red", "All Too Well", "Begin Again"],
        "album": "Red"
    },
    {
        "lyric_clue": '"I don\'t know about you, but I\'m feeling 22..."',
        "answer": "22",
        "options": ["22", "Red", "Stay Stay Stay", "Holy Ground"],
        "album": "Red"
    },

    # 1989
    {
        "lyric_clue": '"\'Cause the players gonna play, play, play, play, play..."',
        "answer": "Shake It Off",
        "options": ["Blank Space", "Shake It Off", "Style", "Bad Blood"],
        "album": "1989"
    },
    {
        "lyric_clue": '"Got a long list of ex-lovers, they\'ll tell you I\'m insane..."',
        "answer": "Blank Space",
        "options": ["Blank Space", "Style", "Out of the Woods", "Wildest Dreams"],
        "album": "1989"
    },

    # Reputation
    {
        "lyric_clue": '"I\'m sorry, the old Taylor can\'t come to the phone right now..."',
        "answer": "Look What You Made Me Do",
        "options": ["Delicate", "End Game", "Look What You Made Me Do", "Getaway Car"],
        "album": "Reputation"
    },

    # Lover
    {
        "lyric_clue": '"Fever dream high in the quiet of the night..."',
        "answer": "Cruel Summer",
        "options": ["Lover", "Cruel Summer", "Paper Rings", "The Archer"],
        "album": "Lover"
    },

    # Folklore & Evermore
    {
        "lyric_clue": '"Vintage tee, brand new phone, high heels on cobblestones..."',
        "answer": "Cardigan",
        "options": ["Cardigan", "August", "Betty", "Exile"],
        "album": "Folklore"
    },

    # Midnights
    {
        "lyric_clue": '"It\'s me, hi, I\'m the problem, it\'s me..."',
        "answer": "Anti-Hero",
        "options": ["Bejeweled", "Lavender Haze", "Anti-Hero", "Karma"],
        "album": "Midnights"
    }
]

def run_quiz():
    while True:
        score = 0
        total_questions = min(5, len(ALL_TAYLOR_SONGS))
        
        print("=" * 60)
        print(" 🐍 ULTIMATE TAYLOR SWIFT RANDOMIZED SONG QUIZ 🐍")
        print("=" * 60)