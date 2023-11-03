
from player import Player

class PlayerStats:
    def __init__(self, reader):
        self.reader=reader
    
    
    def top_scorers_by_nationality(self, nat):
        print(f'player from {nat} \n')
        for player_dict in self.reader.response:
            if player_dict['nationality']==nat:
                print(Player(player_dict))
           