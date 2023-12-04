from tuomari import Tuomari
from tekoaly_parannettu import TekoalyParannettu
from tekoaly import Tekoaly

class KiviPaperiSakset:
    def __init__(self):
        self.valid_moves=['k', 'p', 's']
        
    def pelaa(self):
        tuomari = Tuomari()
        while(1):
            ekan_siirto = self._ensimmaisen_siirto()
            tokan_siirto = self._toisen_siirto(ekan_siirto)
            if ekan_siirto not in self.valid_moves or tokan_siirto not in self.valid_moves:
                print("Kiitos!")
                print(tuomari)
                break
            tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            print(tuomari)

    def _ensimmaisen_siirto(self):
        return input("Ensimmäisen pelaajan siirto: ")

    def _toisen_siirto(self, ensimmaisen_siirto):
        return "k"



class KPSParempiTekoaly(KiviPaperiSakset):
    def __init__(self):
        self.toinen_pelaaja=TekoalyParannettu(10)
        super().__init__()
    def _toisen_siirto(self, ensimmaisen_siirto):
        siirto= self.toinen_pelaaja.anna_siirto()
        self.toinen_pelaaja.aseta_siirto(ensimmaisen_siirto)
        return siirto
    
class KPSPelaajaVsPelaaja(KiviPaperiSakset):
    def __init__(self):
        super().__init__()
    def _toisen_siirto(self, ensimmaisen_siirto):
        return input("Toisen pelaajan siirto: ")
    
class KPSTekoaly(KiviPaperiSakset):
    def __init__(self):
        self.toinen_pelaaja=Tekoaly()
        super().__init__()
    def _toisen_siirto(self, ensimmaisen_siirto):
        self.toinen_pelaaja.aseta_siirto(ensimmaisen_siirto)
        return self.toinen_pelaaja.anna_siirto()