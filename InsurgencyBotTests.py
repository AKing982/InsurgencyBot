import unittest

class RedditBotTest(unittest.TestCase):

    # Test the list
    def testList(self):
        self.list = ['Steyr', 'AUG', 'What do you think ', 'The game is ', 'I like the game ', 'CPU issues ']

        # Test that the length of the list is equal to 6
        self.assertEqual(len(self.list), 6)


if __name__ == '__main__':
    unittest.main()

