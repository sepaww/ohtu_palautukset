class Sovelluslogiikka:
    def __init__(self, arvo=0):
        self._arvo = arvo
        self.history=[]
    def miinus(self, operandi):
        self._arvo = self._arvo - operandi
        self.history.append(self._arvo)
    def plus(self, operandi):
        self._arvo = self._arvo + operandi
        self.history.append(self._arvo)
    def nollaa(self):
        self._arvo = 0
        self.history=[]
    def kumoa(self):
        self.history.pop()
        self._arvo=self.history[-1]
        
    def aseta_arvo(self, arvo):
        self._arvo = arvo

    def arvo(self):
        return self._arvo
