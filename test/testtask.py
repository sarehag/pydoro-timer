import unittest
from Tasks.Task import Task

class TestDatabase(unittest.TestCase):

    def test_insert_one(self):
        myTask = Task("My Task")
        self.assertEqual(myTask.title,"My Task")

if __name__ == '__main__':
    unittest.main()
