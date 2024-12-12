"""
Задача "Проверка на выносливость"
"""
from runner import Runner
from unittest import TestCase


class RunnerTest(TestCase, Runner):

    def test_walk(self):
        """
        Тест на метод walk()
        """
        name = Runner('Name')
        for _ in range(10):
            name.walk()
        self.assertEqual(name.distance, 50)
        self.assertNotEqual(name.distance, 100)

    def test_run(self):
        """
        Тест на метод run()
        """
        name = Runner('Name')
        for _ in range(10):
            name.run()
        self.assertEqual(name.distance, 100)
        self.assertNotEqual(name.distance, 50)

    def test_challenge(self):
        """
        Тест на метод run и walk
        :return:
        """
        name = Runner('Name')
        name1 = Runner('Name1')
        for _ in range(10):
            name.walk()
            name1.run()
        self.assertEqual(name.distance, 50)
        self.assertNotEqual(name.distance, 100)
        self.assertEqual(name1.distance, 100)
        self.assertNotEqual(name1.distance, 50)


if __name__ == '__main__':
    TestCase.main()
