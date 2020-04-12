from django.shortcuts import render, redirect
from .models import League, Team, Player
from django.db.models import Q

from . import team_maker

def index(request):
	context = {
		"baseball_leagues": League.objects.filter(sport="Baseball"),
		"womens_leagues": League.objects.filter(name__contains="Women"),
		"hockey_leagues": League.objects.filter(sport__contains="Hockey"),
		"other_than_football": League.objects.exclude(sport="Football"),
		"conference_leagues": League.objects.filter(name__contains="Conference"),
		"atlantic_leagues": League.objects.filter(name__contains="Atlantic"),
		"dallas_teams": Team.objects.filter(location="Dallas"),
		"raptor_teams": Team.objects.filter(team_name="Raptors"),
		"city_teams": Team.objects.filter(location__contains="City"),
		"t_teams": Team.objects.filter(team_name__startswith="T"),
		"alpha_teams": Team.objects.all().order_by("location"),
		"alpha_teams_rev": Team.objects.all().order_by("-team_name"),
		"cooper_players": Player.objects.filter(last_name="Cooper"),
		"joshua_players": Player.objects.filter(first_name="Joshua"),
		"cooper_not_josh": Player.objects.filter(last_name="Cooper").exclude(first_name="Joshua"),
		"alex_or_wyatt": Player.objects.filter(Q(first_name="Alexander") | Q(first_name="Wyatt")),
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")