import unittest

from runner_and_tournament import Runner, Tournament


class TournamentTest(unittest.TestCase):
    """
    Тестовый класс для Турнирного класса в модуле runner_and_tournament.py (с исправленным методом Start)
    """

    @classmethod
    def setUpClass(cls):
        """
        функция вызывается один раз перед тестированием используем ее для создания словаря
        :return:
        """
        cls.all_results = {}

    @classmethod
    def tearDownClass(cls):
        """"
        функция вызывается один раз после тестирования используем ее
        для вывода полученных результатов(словаря)
        :return:
        """
        for key, value in sorted(cls.all_results.items()):
            result_str = {place: participant.__str__() for place, participant in value.items()}
            print(result_str)

    def setUp(self):
        """
        функция вызывается перед каждым тестом
        используем ее для создания экземпляров класса Runner для проверки тестируемого класса
        :return:
        """
        self.runner1 = Runner('Усэйн', 10)
        self.runner2 = Runner('Андрей', 9)
        self.runner3 = Runner('Ник', 3)

    def test_1(self):
        """
        первая функция тестирования класса Tournament
        :return:
        """
        tournament = Tournament(90, self.runner1, self.runner3)
        results = tournament.start()
        self.all_results[len(self.all_results) + 1] = results
        self.assertTrue(results[max(results.keys())].name == "Ник")

    def test_2(self):
        """
        вторая функция тестирования класса Tournament
        :return:
        """
        tournament = Tournament(90, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results[len(self.all_results) + 1] = results
        self.assertTrue(results[max(results.keys())].name == "Ник")

    def test_3(self):
        """
        третья функция тестирования класса Tournament
        :return:
        """
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results[len(self.all_results) + 1] = results
        self.assertTrue(results[max(results.keys())].name == "Ник")

    def test_4(self):
        """
        дополнительная четвертая функция тестирования класса Tournament
        с использованием малых дистанций (5)
        :return:
        """
        tournament = Tournament(5, self.runner1, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results[len(self.all_results) + 1] = results
        self.assertTrue(results[max(results.keys())].name == "Ник")

    def test_5(self):
        """
        дополнительная пятая функция тестирования класса Tournament
        с использованием малых дистанций (6)
        :return:
        """
        tournament = Tournament(6, self.runner1, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results[len(self.all_results) + 1] = results
        self.assertTrue(results[max(results.keys())].name == "Ник")


if __name__ == '__main__':
    unittest.main(verbosity=2)
