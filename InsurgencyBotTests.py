import unittest
import pytest

class RedditBotTest(pytest.PytestAssertRewriteWarning):

    # Test the list
    def testList(self):
        self.list = ['Steyr', 'AUG', 'What do you think ', 'The game is ', 'I like the game ', 'CPU issues ']



if __name__ == '__main__':
    unittest.main()

