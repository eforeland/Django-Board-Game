from django.shortcuts import render
from game.models import Player, Board
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.http import HttpResponse
import json

# Create your views here.

#def index(request):
#	return HttpResponse("Hello World!")

def get_player(request, id):
	player = Player.objects.filter(id=id)
	if (len(player) == 1):
		response = "Player %(id)s is at row %(row)s and col %(col)s" % {'id':player[0].tag, 'row':str(player[0].row), 'col':str(player[0].col)}
		#return HttpResonse("Player %(id)s is at row %(row)s and col %(col)s" % {'id':player[0].tag, 'row':str(player[0].row), 'col':str(player[0].col)})
		return HttpResponse(json.dumps(player[0], cls=PlayerEncoder))
	else:
		return HttpResponse("No such player")

def displayBoard(request):
	players = Player.objects.all()
	brd = Board.objects.filter()
	b = brd[0]

	brdArr = [['_' for c in range(b.col)] for r in range(b.row)]
	brdArr[players[0].row][players[0].col] = players[0].tag
	brdArr[players[1].row][players[1].col] = players[1].tag

	brdStr = ""
	for c in range (len(brdArr)):
		for r in range (len(brdArr[0])):
			brdStr += brdArr[c][r] + " "
		brdStr += "<br />"

	return HttpResponse(json.dumps(brdArr, cls=PlayerEncoder))

class PlayerCreate(CreateView):
	model = Player
	fields = '__all__'
	success_url = reverse_lazy('players')

class PlayerUpdate(UpdateView):
	model = Player
	fields = ['row', 'col']
	success_url = reverse_lazy('players')

class PlayerEncoder(json.JSONEncoder):
	def default(self, obj):
		if isinstance(obj, Player):
			return {'id' : obj.id, 'tag' : obj.tag, 'row' : obj.row, 'col' :obj.col}
			return json.JSONEncoder.default(self, obj)

