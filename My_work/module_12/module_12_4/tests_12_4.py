import logging
import unittest
from sys import exc_info

from rt_with_exeptions import Runner


class RunnerTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        logging.basicConfig(level=logging.WARNING,
                            format='%(asctime)s | %(levelname)s | %(message)s',
                            filename='runner_tests.log',
                            filemode='w',
                            encoding='utf-8'
                            )

    def test_walk(self):
        try:
            runner = Runner("Степан", -10)
            self.assertEqual(runner.distance, 20)
        except ValueError:
            # logging.error('', exc_info=True)
            logging.warning('Неверная скорость для Runner', exc_info=True)
        logging.info('"test_walk" выполнен успешно')

    def test_run(self):
        """
        Тест на метод run()
        """
        try:
            runner = Runner(("Василий",), 10)
            self.assertEqual(runner.distance, 20)
        except TypeError:
            # logging.error('',exc_info=True)
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)
        logging.info('"test_run" выполнен успешно')


if __name__ == '__main__':
    unittest.main()
