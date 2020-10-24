import unittest

class RedditBotTest(unittest.TestCase):

    # Test the list
    def testList(self):
        self.list = ['Steyr', 'AUG', 'What do you think ', 'The game is ', 'I like the game ', 'CPU issues ']

        # Test that the length of the list is equal to 6
        self.assertEqual(len(self.list), 6)

        # Verify that the list contains some of the terms
        self.assertIn('Steyr', self.list)
        self.assertIn('The game in', self.list)
        self.assertIn('CPU', self.list)

        # Verify



if __name__ == '__main__':
    unittest.main()

