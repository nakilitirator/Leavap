import logging
import unittest
from rt_with_exceptions import Runner


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            hodba = Runner('Ходьба', -5)
            for i in range(10):
                hodba.walk()
            self.assertEqual(hodba.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    def test_run(self):
        try:
            beg = Runner(25896)
            for i in range(10):
                beg.run()
            self.assertEqual(beg.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)


if __name__ == '__main__':
    unittest.main()
    logging.basicConfig(level=logging.INFO, filemode='w',
                        filename='runner_tests.log', encoding='utf-8',
                        format='%(asctime)s | %(levelname)s | %(message)s')

