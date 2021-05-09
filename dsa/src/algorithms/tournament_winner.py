from typing import List


def tournament_winner(competitions: List[List[str]], results: List[int]):
    tournament_results = {}
    current_winner = ["", 0]

    for idx in range(len(competitions)):
        [home, away] = competitions[idx]
        winner = home if results[idx] == 1 else away
        tournament_results[winner] = 1 if winner not in tournament_results else tournament_results[winner] + 1

        if current_winner[1] < tournament_results[winner]:
            current_winner = [winner, tournament_results[winner]]

    return current_winner[0]


def main():
    # [hometeam, awayteam]
    # [1, 0]
    competitions = [["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"]]
    results = [0, 0, 1]
    print(tournament_winner(competitions, results))
