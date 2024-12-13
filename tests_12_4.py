import unittest
import logging
from rt_with_exceptions import Runner


logging.basicConfig(level=logging.INFO,
                    filemode='w',
                    filename='runner_tests.log',
                    encoding='UTF-8',
                    format='%(asctime)s - %(levelname)s - %(message)s')

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(False,'')
    def test_walk(self):
        try:
            walker1 = Runner('blade_walker', -10)
            walker1.walk()
            logging.info('"test_walk" выполнен успешно')
        except:
            logging.warning('Неверная скорость для Runner', exc_info=True)


    @unittest.skipIf(False,'')
    def test_run(self):
        try:
            runner2 = Runner(2)
            runner2.run()
            logging.info('"test_run" выполнен успешно')
        except:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)
