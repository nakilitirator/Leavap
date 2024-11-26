from runner import Runner
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        """Test walk method in runner
        :return
        """
        run = Runner("boy")
        for i in range(10):
            run.walk()
        self.assertEqual(run.distance, 50)

    def test_run(self):
        """ Test run method in runner
        :return
        """
        run = Runner("girls")
        for i in range(10):
            run.run()
        self.assertEqual(run.distance, 100)

    def test_challenge(self):
        """Test of two objects
        :return
        """
        run1 = Runner("boy")
        run2 = Runner("girls")
        for i in range(10):
            run1.walk()
            run2.run()
        self.assertNotEqual(run1.distance, run2.distance)


if __name__ == "__main__":
    unittest.main()