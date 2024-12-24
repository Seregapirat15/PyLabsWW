import unittest
from refactoringCode import query_1, query_2, query_3, create_browsers, create_computers, link_browsers_with_computers

class TestRefactoringCode(unittest.TestCase):
    def test_query_1(self):
        browsers = create_browsers()
        computers = create_computers()
        link_browsers_with_computers(browsers, computers)
        result = query_1(browsers, computers)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][0], "Atom")

    def test_query_2(self):
        browsers = create_browsers()
        computers = create_computers()
        link_browsers_with_computers(browsers, computers)
        result = query_2(computers)
        self.assertEqual(len(result), 5)
        self.assertEqual(result[0][0], "Dell Inspiron")
        self.assertEqual(result[1][0], "HP Envy")
        self.assertEqual(result[2][0], "Apple MacBook")
        self.assertEqual(result[3][0], "Apple MacBook Pro")
        self.assertEqual(result[4][0], "Apple MacBook Air")

    def test_query_3(self):
        browsers = create_browsers()
        computers = create_computers()
        link_browsers_with_computers(browsers, computers)
        result = query_3(browsers, computers)
        self.assertEqual(len(result), 7)
        self.assertEqual(result[0][0], "Atom")
        self.assertEqual(result[1][0], "Google Chrome")
        self.assertEqual(result[2][0], "Microsoft Edge")
        self.assertEqual(result[3][0], "Mozilla Firefox")
        self.assertEqual(result[4][0], "Opera")
        self.assertEqual(result[5][0], "Safari")
        self.assertEqual(result[6][0], "Vivaldi")

if __name__ == "__main__":
    unittest.main()