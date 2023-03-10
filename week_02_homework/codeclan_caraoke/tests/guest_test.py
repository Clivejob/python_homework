import unittest
from src.guest import *
from src.venue import *
from src.room import *
from src.drink import *
from src.song import *

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.venue1 = Venue("Funkin Folk", 5, 500)
        self.songfunk1 = Song("Can't be funked", "Funk")
        self.songfunk2 = Song("Funkless task", "Funk")
        self.songfolk1 = Song("When the folk will that be", "Folk")
        self.songfolk2 = Song("The folk you talking about", "Folk")
        self.drink1 = Drink("IPA", 10)
        self.guest1 = Guest("Clive", 20, self.songfunk1)
        self.guest2 = Guest("Burt", 20, self.songfunk2)
        self.guest3 = Guest("Barnabus", 5, self.songfolk1)
        self.guest4 = Guest("Otto", 25, self.songfolk2)

    def test_guest__has_name(self):
        self.assertEqual("Clive", self.guest1.name)

    def test_guest__has_cash(self):
        self.assertEqual(20, self.guest1.cash)

    def test_guest__can_enter(self):
        self.guest1.guest_buy_entry(self.venue1)
        self.assertEqual(15, self.guest1.cash)

    def test_guest__can_enter_and_buy_drink(self):
        self.guest1.guest_buy_entry(self.venue1)
        self.guest1.guest_buy_drink(self.drink1)
        self.assertEqual(5, self.guest1.cash)

    def test_guest__cant_afford_anything_else(self):
        self.guest1.guest_buy_entry(self.venue1)
        self.guest1.guest_buy_drink(self.drink1)
        self.guest1.guest_buy_drink(self.drink1)
        self.assertEqual(5, self.guest1.cash)

    def test_guest__has_favourite_song(self):
        self.assertEqual("Can't be funked", self.guest1.favourite_song.name)

    