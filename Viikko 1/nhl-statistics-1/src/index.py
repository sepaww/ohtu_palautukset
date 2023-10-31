from statistics_service import StatisticsService
from player_reader import PlayerReader
from enum import Enum

class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3


def main():
    year=input('give required year')
    stats = StatisticsService(PlayerReader(year))
    philadelphia_flyers_players = stats.team("PHI")
    top_scorers = stats.top(10)

    print("Philadelphia Flyers:")
    for player in philadelphia_flyers_players:
        print(player)

    print("Top point getters:")
    for player in top_scorers:
        print(player)
        
    print("Top point goal scorers:")
    print(SortBy.GOALS)
    for player in stats.top(10, SortBy.GOALS.value):
        print(player)

    # järjestetään syöttöjen perusteella
    print("Top by assists:")
    for player in stats.top(10, SortBy.ASSISTS.value):
        print(player)

if __name__ == "__main__":
    main()
