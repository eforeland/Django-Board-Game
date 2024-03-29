from django.db import models
from game import constants
from django.core.exceptions import ValidationError


# Create your models here.
def validate_num_players(value):
	if len(Player.objects.all()) >= constants.MAX_PLAYERS:
		raise ValidationError('Max Number of Players Reached',)

def validate_col_range(value):
	if value < 0 or value > constants.MAX_COLS - 1:
		raise ValidationError('Out of range',)

def validate_row_range(value):
	if value < 0 or value > constants.MAX_ROWS - 1:
		raise ValidationError('Out of range',)

def validate_unique_tag(value):
	for player in Player.objects.all():
		if player.tag == value:
			raise ValidationsError('Tag already taken',)


class Player(models.Model):
	tag = models.CharField(max_length=1, validators=[validate_unique_tag, validate_num_players])
	row = models.IntegerField(validators=[validate_row_range])
	col = models.IntegerField(validators=[validate_col_range])
		

	def __str__(self):
		return self.tag + ' @(' + str(self.row) + ',' + str(self.col) + ')'

	def __init__(self, *args, **kwargs):
		super(Player, self).__init__(*args, **kwargs)
		self._prev_row = self.row
		self._prev_col = self.col

	def clean(self):
		if(self._prev_row == None):
			return
		if abs(self.row - self._prev_row) > 1:
			raise ValidationError('row too far')
		if abs(self.col - self._prev_col) > 1:
			raise ValidationError('col too far')

	

class Board(models.Model):
	tag = models.CharField(max_length=1)
	row = models.IntegerField()
	col = models.IntegerField()

	def __str__(self):
		return self.tag + ' @(' + str(self.row) + ',' + str(self.col) + ')'

	def __init__(self, *args, **kwargs):
		super(Board, self).__init__(*args, **kwargs)
		self._prev_row = self.row
		self._prev_col = self.col
