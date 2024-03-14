import os
import unittest
from manage_logs import init_log, reten_log

class TestManageLogs(unittest.TestCase):
    def setUp(self):
        self.log_path = 'test.log'
        init_log(self.log_path)

    def tearDown(self):
        os.remove(self.log_path)

    def test_init_log(self):
        self.assertTrue(os.path.exists(self.log_path))

    def test_reten_log_under_200(self):
        with open(self.log_path, 'w') as f:
            for i in range(100):
                f.write(f"test {i}\n")
        reten_log(self.log_path)
        with open(self.log_path, 'r') as f:
            lines = f.readlines()
            self.assertEqual(len(lines), 100)

    def test_reten_log_over_200(self):
        with open(self.log_path, 'w') as f:
            for i in range(300):
                f.write(f"test {i}\n")
        reten_log(self.log_path)
        with open(self.log_path, 'r') as f:
            self.assertEqual(f.read(), '')

if __name__ == '__main__':
    unittest.main()
