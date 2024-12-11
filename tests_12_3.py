import unittest
import inspect
from runner_and_tournament import Runner, Tournament


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        peshehod = Runner('Пешеход')
        for i in range(10):
            peshehod.walk()
        self.assertEqual(peshehod.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        begun = Runner('Бегун')
        for i in range(10):
            begun.run()
        self.assertEqual(begun.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        peshehod = Runner('Пешеход')
        begun = Runner('Бегун')
        for i in range(10):
            peshehod.walk()
            begun.run()
        self.assertNotEqual(peshehod.distance, begun.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner('Усэйн', 10)
        self.andrey = Runner('Андрей', 9)
        self.nik = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results:
            temp = {}
            for k, v in result.items():
                temp[k] = v.__str__()
            print(temp)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_usain_nik(self):
        tournament = Tournament(90, self.usain, self.nik)
        TournamentTest.all_results.append(tournament.start())
        self.assertTrue(self.all_results[-1][max(self.all_results[-1].keys())] == self.nik)


    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_andrey_nik(self):
        tournament = Tournament(90, self.andrey, self.nik)
        TournamentTest.all_results.append(tournament.start())
        self.assertTrue(self.all_results[-1][max(self.all_results[-1].keys())] == self.nik)


    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_usain_andrey_nik(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nik)
        TournamentTest.all_results.append(tournament.start())
        self.assertTrue(self.all_results[-1][max(self.all_results[-1].keys())] == self.nik)


if __name__ == '__main__':
    unittest.main()