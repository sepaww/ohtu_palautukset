import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )
    def test_existing_player(self):
        player = self.stats.search("Lemieux")
        self.assertEqual(player.name, "Lemieux")

    def test_search_nonexisting_player(self):
        player = self.stats.search("Jami")
        self.assertIsNone(player)

    def test_existing_team(self):
        players = self.stats.team("EDM")
        self.assertTrue(all(player.team == "EDM" for player in players))

    def test_nonexisting_team(self):
        players = self.stats.team("Tappara")
        self.assertEqual(len(players), 0)

    def test_top_score(self):
        top_players = self.stats.top(3)
        self.assertEqual(len(top_players), 4)
        self.assertEqual(top_players[0].name, "Gretzky")
        self.assertEqual(top_players[1].name, "Lemieux")
        self.assertEqual(top_players[2].name, "Yzerman")
        self.assertEqual(top_players[3].name, "Kurri")
        
    def test_top_goal(self):
        top_players = self.stats.top(3, 2)
        self.assertEqual(len(top_players), 4)
        self.assertEqual(top_players[0].name, "Lemieux")
        self.assertEqual(top_players[1].name, "Yzerman")
        self.assertEqual(top_players[2].name, "Kurri")
        self.assertEqual(top_players[3].name, "Gretzky")
        
    def test_top_assist(self):
        top_players = self.stats.top(3, 3)
        self.assertEqual(len(top_players), 4)
        self.assertEqual(top_players[0].name, "Gretzky")
        self.assertEqual(top_players[1].name, "Yzerman")
        self.assertEqual(top_players[2].name, "Lemieux")
        self.assertEqual(top_players[3].name, "Kurri")