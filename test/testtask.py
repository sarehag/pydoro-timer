import unittest
from Tasks.Task import Task

class TestTask(unittest.TestCase):

    def test_construction(self):
        myTask = Task("My Task")
        self.assertEqual(myTask.title,"My Task")

if __name__ == '__main__':
    unittest.main()
