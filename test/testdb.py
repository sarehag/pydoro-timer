import unittest
from Databases.Mongo import Database

class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.database = Database();

    def test_insert_one(self):
        task = {"test":"849"}
        objectId = self.database.create("testTasks", task)
        storedTask = self.database.read("testTasks",{"_id": objectId})
        self.assertEqual(task["test"],storedTask["test"])

    def test_update_one(self):
        task =   {"insert":"121"}
        objectId = self.database.create("testTasks", task)
        task = {"update":"123"}
        self.database.update("testTasks", {"_id": objectId}, task)
        storedTask = self.database.read("testTasks", {"_id": objectId})
        self.assertEqual(task["update"],storedTask["update"])

if __name__ == '__main__':
    unittest.main()
