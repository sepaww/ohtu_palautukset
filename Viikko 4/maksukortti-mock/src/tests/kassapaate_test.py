import unittest
from unittest.mock import Mock, ANY
from kassapaate import Kassapaate, HINTA
from maksukortti import Maksukortti


class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()
        self.maksukortti_mock = Mock()
        self.maksukortti_mock.lataa()
        self.maksukortti_mock.osta()
    def test_kortilta_velotetaan_hinta_jos_rahaa_on(self):
        self.maksukortti_mock.saldo = 10

                
        self.kassa.osta_lounas(self.maksukortti_mock)

        self.maksukortti_mock.osta.assert_called_with(HINTA)

    def test_kortilta_ei_veloteta_jos_raha_ei_riita(self):
        maksukortti_mock = Mock()
        maksukortti_mock.saldo = 4
        maksukortti_mock.lataa()
        #maksukortti_mock.osta()
        self.kassa.osta_lounas(maksukortti_mock)

        maksukortti_mock.osta.assert_not_called()

    def test_kortille_ladataan_kun_yli_0(self):
        maksukortti_mock = Mock()
        maksukortti_mock.saldo = 10

                
        self.kassa.lataa(maksukortti_mock, 1)

        maksukortti_mock.lataa.assert_called_with(1)
        
    def test_kortille_ei_ladataan_kun_alle_0(self):
        maksukortti_mock = Mock()
        maksukortti_mock.saldo = 10

                
        self.kassa.lataa(self.maksukortti_mock, -1)

        maksukortti_mock.lataa.assert_not_called()