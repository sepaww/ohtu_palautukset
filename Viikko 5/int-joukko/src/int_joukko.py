KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko
    
    def __init__(self, kapasiteetti=5, kasvatuskoko=5):
        if kapasiteetti < 0:
            raise Exception("Väärä kapasiteetti")  # heitin vaan jotain :D

        elif kasvatuskoko < 0:
            raise Exception("Väärä kasvatuskoko")  # heitin vaan jotain :D
        
        self.kapasiteetti=kapasiteetti
        self.kasvatuskoko = kasvatuskoko
        self.ljono = self._luo_lista(self.kapasiteetti)
        self.alkioiden_lkm = 0

    def kuuluu(self, n):
        return n in self.ljono

    def lisaa(self, n):

        if not self.kuuluu(n):
            self.ljono[self.alkioiden_lkm] = n
            self.alkioiden_lkm += 1

            # ei mahdu enempää, luodaan uusi säilytyspaikka luvuille
            if self.alkioiden_lkm == len(self.ljono):
                taulukko_old = self.ljono[:]
                self.ljono = self._luo_lista(self.alkioiden_lkm + self.kasvatuskoko)
                self.kopioi_lista(taulukko_old, self.ljono)

            return True

        return False

    def poista(self, n):
        for i in range(0, self.alkioiden_lkm):
            if n == self.ljono[i]:
                self.ljono=self.ljono[:i]+self.ljono[i+1:]
                print(self.ljono)
                self.alkioiden_lkm-=1
                return True

        return False

    def kopioi_lista(self, a, b):
        b[:len(a)]=a[:]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = self._luo_lista(self.alkioiden_lkm)
        taulu=self.ljono[:len(taulu)]
        return taulu

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            x.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            x.lisaa(b_taulu[i])

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa(b_taulu[j])

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            z.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            z.poista(b_taulu[i])

        return z

    def __str__(self):
        liststr="{"+ ', '.join(str(x) for x in self.ljono[:self.alkioiden_lkm])+"}"
        return f'{liststr}'
        
