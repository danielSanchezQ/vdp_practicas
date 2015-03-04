__author__ = 'Netwave'


from unittest import *
from modules.LolCounterMaker import *

class CounterTest(TestCase):
    def __init__(self):
        self.cm = CounterMaker()

    def connection_test(self):
        self.assertRaises(Exception, self.cm.connect)

    def counter_userId_test(self):
        self.assertRaises(ValueError, self.cm.check, "userIduno", "champ1")

    def counter_champ_name_test(self):
        self.assertRaises(ValueError, self.cm.check, "userIduno", "champ1")