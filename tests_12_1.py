import runner as r
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner_1 = r.Runner('Данил')
        for _ in range(10):
            runner_1.walk()
        self.assertEqual(runner_1.distance, 50)

    def test_run(self):
        runner_2 = r.Runner('Миша')
        for _ in range(10):
            runner_2.run()
        self.assertEqual(runner_2.distance, 100)

    def test_challenge(self):
        runner_3 = r.Runner("Лёша")
        runner_4 = r.Runner("Вася")
        for _ in range(10):
            runner_3.run()
            runner_4.walk()
        self.assertNotEqual(runner_3.distance, runner_4.distance)


if __name__ == "__main__":
    unittest.main()