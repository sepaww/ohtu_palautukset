from KiviPaperiSakset import KPSParempiTekoaly, KPSPelaajaVsPelaaja, KPSTekoaly

class tehdas:
    def __init__(self):
        self._types={'a':KPSPelaajaVsPelaaja, 'b':KPSTekoaly, 'c':KPSParempiTekoaly}
    def select(self, val):
        if val in self._types.keys():
            return self._types[val]