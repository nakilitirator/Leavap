import logging
import unittest
from rt_with_exceptions import Runner


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            hodba = Runner('Ходьба', -5)
            for i in range(10):
                hodba.walk()
            logging.info('"test_walk" выполнен успешно')
            self.assertEqual(hodba.distance, 50)
        except ValueError:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    def test_run(self):
        try:
            beg = Runner(25896)
            for i in range(10):
                beg.run()
            logging.info('"test_run" выполнен успешно')
            self.assertEqual(beg.distance, 100)
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filemode='w',
                        filename='runner_tests.log', encoding='utf-8',
                        format='%(asctime)s | %(levelname)s | %(message)s')
    unittest.main()
