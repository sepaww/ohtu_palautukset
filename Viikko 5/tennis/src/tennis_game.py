class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.names=[player1_name, player2_name]
        self.state={}
        self.state[player1_name]=0
        self.state[player2_name]=0

    def won_point(self, player_name):
        self.state[player_name]+=1

    def get_draw_name(self):
        names=['Love-All', 'Fifteen-All', 'Thirty-All', 'Deuce']
        if self.state[self.names[0]]<3:
            return names[self.state[self.names[0]]]
        return 'Deuce'
    
    def get_late_advantage_name(self):
            winning_name = max(self.state, key=lambda k: self.state[k])
            if abs(self.state[self.names[0]]-self.state[self.names[1]])>=2:
                return f'Win for {winning_name}'
            return f'Advantage {winning_name}'
        
    def get_early_state_name(self):  
            s_name=["Love","Fifteen","Thirty","Forty"]
            return f'{s_name[self.state[self.names[0]]]}-{s_name[self.state[self.names[1]]]}'  
        
    def get_score(self):
        if self.state[self.names[0]] == self.state[self.names[1]]:
            return self.get_draw_name()
        
        if self.state[self.names[0]] >= 4 or self.state[self.names[1]] >= 4:
            return self.get_late_advantage_name()
        
        return self.get_early_state_name()

