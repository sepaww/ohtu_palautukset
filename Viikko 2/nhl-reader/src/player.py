class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.team=dict['team']
        self.assists=dict['assists']
        self.goals=dict['goals']
        
    def __str__(self):
        return f'{self.name:20} {self.team:5} {self.goals} + {self.assists} = {self.goals+self.assists}'
