game_rounds = open("input.txt").read().splitlines()
#converting each line into a list item


def find_match_scores():
    score = 0
    choice = ""
    for match in game_rounds:
        #calculate score from choice
        if "X" in match:
            score += 1
            choice = "rock"
        if "Y" in match:
            score += 2
            choice = "paper"
        if "Z" in match:
            score += 3
            choice = "scissors"

        #find out what the opponent chose
        if "A" in match:
            opponent_choice = "rock"
        if "B" in match:
            opponent_choice = "paper"
        if "C" in match:
            opponent_choice = "scissors"

        #find result
        if choice == opponent_choice:
            score +=3
            print("draw!")

        if choice == "rock" and opponent_choice == "paper":
            score +=0
            print("lose!")

        if choice == "rock" and opponent_choice == "scissors":
            score +=6
            print("win!")

        if choice == "scissors" and opponent_choice == "rock":
            score += 0
            print("lose!")

        if choice == "scissors" and opponent_choice == "paper":
            score += 6
            print("win!")

        if choice == "paper" and opponent_choice == "scissors":
            score += 0
            print("lose!")

        if choice == "paper" and opponent_choice == "rock":
            score += 6
            print("win!")

    print(f"Your total score for the first problem is {score}!")

#find_match_scores()

def find_match_results():
    score = 0
    choice = ""
    for match in game_rounds:
        #calculate what result is needed
        if "X" in match:
            score += 0
            choice = "lose"
        if "Y" in match:
            score += 3
            choice = "draw"
        if "Z" in match:
            score += 6
            choice = "win"

        #find out what the opponent chose
        if "A" in match:
            opponent_choice = "rock"
            if "X" in match: #lose with scissors
                score += 3
            if "Y" in match: #draw with rock
                score += 1
            if "Z" in match: #win with paper
                score += 2
        if "B" in match:
            opponent_choice = "paper"
            if "X" in match: #lose with rock
                score += 1
            if "Y" in match: #draw with paper
                score += 2
            if "Z" in match: #win with scissors
                score += 3
        if "C" in match:
            opponent_choice = "scissors"
            if "X" in match: #lose with paper
                score += 2
            if "Y" in match: #draw with scissors
                score += 3
            if "Z" in match: #win with rock
                score += 1

        #find result


    print(f"Your new total score for the second problem is {score}!")

find_match_scores()
find_match_results()
