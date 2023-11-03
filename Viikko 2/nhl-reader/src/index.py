import requests
from player import Player
from PlayerReader import PlayerReader
from PlayerStats import PlayerStats

#print('run')
def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players"
    reader = PlayerReader(url)
    stats=PlayerStats(reader)
    stats.top_scorers_by_nationality('FIN')
    
main()