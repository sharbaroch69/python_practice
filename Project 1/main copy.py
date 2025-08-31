# same project made by ai

import random

# human-readable names
names = {"s": "snake", "w": "water", "g": "gun"}

# which choice beats which (key beats value)
beats = {
    "s": "w",  # snake beats water
    "w": "g",  # water beats gun
    "g": "s",  # gun beats snake
}

def decide_winner(comp_key: str, you_key: str) -> str:
    """Return 'draw', 'you', or 'comp'."""
    if comp_key == you_key:
        return "draw"
    if beats[you_key] == comp_key:
        return "you"
    return "comp"

def main():
    score_you = 0
    score_comp = 0
    rounds = 0

    print("Snake-Water-Gun: enter s (snake), w (water), g (gun). q to quit.")
    while True:
        comp_key = random.choice(["s", "w", "g"])
        you_key = input("Your turn (s/w/g, q to quit): ").strip().lower()
        if you_key == "q":
            break
        if you_key not in names:
            print("Invalid choice — use s, w, g or q to quit.")
            continue

        result = decide_winner(comp_key, you_key)
        rounds += 1
        if result == "you":
            score_you += 1
            outcome_text = "You win"
        elif result == "comp":
            score_comp += 1
            outcome_text = "You lose"
        else:
            outcome_text = "It's a draw"

        print(f"Computer chose {names[comp_key]}. You chose {names[you_key]}. {outcome_text}")
        print(f"Score — You: {score_you}  Computer: {score_comp}  Rounds: {rounds}\n")

    print(f"Final score — You: {score_you}  Computer: {score_comp}  Rounds: {rounds}")
    print("Thanks for playing!")

if __name__ == "__main__":
    main()
