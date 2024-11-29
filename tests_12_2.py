from runner_and_tournament import Runner, Tournament
import unittest


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_result = []

    def setUp(self):
        self.usain = Runner("Усэйн", 10)
        self.andrey = Runner("Андрей", 9)
        self.nik = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_result:
            temp = {}
            for k, v in result.items():
                temp[k] = v.__str__()
            print(temp)

    def test_tournament_1(self):
        tournament = Tournament(90, self.usain, self.nik)
        TournamentTest.all_result.append(tournament.start())
        self.assertTrue(self.all_result[-1][max(self.all_result[-1].keys())] == self.nik)

    def test_tournament_2(self):
        tournament = Tournament(90, self.andrey, self.nik)
        TournamentTest.all_result.append(tournament.start())
        self.assertTrue(self.all_result[-1][max(self.all_result[-1].keys())] == self.nik)

    def test_tournament_3(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nik)
        TournamentTest.all_result.append(tournament.start())
        self.assertTrue(self.all_result[-1][max(self.all_result[-1].keys())] == self.nik)


if __name__ == '__main__':
    unittest.main()