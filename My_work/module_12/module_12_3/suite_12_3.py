import unittest
from unittest import TextTestRunner

"""
Задача: Заморозка кейсов
Модуль для описания TestSuite
"""
from My_work.module_12.module_12_3 import tests_12_3

st = unittest.TestSuite()
st.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))
st.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))

run_test = TextTestRunner(verbosity=2)
run_test.run(st)
