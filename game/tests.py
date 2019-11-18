from django.test import TestCase
from game.models import Player
import game.constants

# Create your tests here.

class PlayerTestCase(TestCase):

    def test_create(self):
        response = self.client.post("/game/player/create/",
        { 'tag': 'T', 'row':3, 'col':7 })
            p = Player.objects.get(tag='T')
            self.assertEqual(p.tag, 'T')
            self.assertEqual(p.row, 3)
            self.assertEqual(p.col, 7)

    def test_out_bounds(self):
        #test for row out of bounds(too low)
        response = self.client.post("/game/player/create", { 'tag': 'U', 'row': -3, 'col':4 })
        self.assertFormError(response, 'form', 'row', 'Out of range')
        try:
            Player.objects.get(tag='U')
            self.fail()
        except Player.DoesNotExist::
            pass
        #test for row out of bounds(too high)
        response = self.client.post("/game/player/create", { 'tag': 'U', 'row': 11, 'col':4 })
        self.assertFormError(response, 'form', 'row', 'Out of range')
        try:
            Player.objects.get(tag='U')
            self.fail()
        except Player.DoesNotExist::
            pass
        #test for col out of bounds(too low)
        response = self.client.post("/game/player/create", { 'tag': 'U', 'row': 3, 'col':-1 })
        self.assertFormError(response, 'form', 'row', 'Out of range')
        try:
            Player.objects.get(tag='U')
            self.fail()
        except Player.DoesNotExist::
            pass
        #test for col out of bounds(too high)
        response = self.client.post("/game/player/create", { 'tag': 'U', 'row': 3, 'col':22 })
        self.assertFormError(response, 'form', 'row', 'Out of range')
        try:
            Player.objects.get(tag='U')
            self.fail()
        except Player.DoesNotExist:
            pass

        
