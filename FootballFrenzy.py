from pyodide.http import pyxhr as requests 
 
url = 'https://football-frenzy.s3.eu-north-1.amazonaws.com/api' 

games = []
game_dates = []

year = str(input("Enter year: "))
home_score = int(input("Home score: "))
away_score = int(input("Away score: "))

r = requests.get(url+"/"+year)

dates = r.json()["gamedays"].copy()

for date in dates:
    r = requests.get(url+"/"+year+"/"+date)
    gamesJson = r.json()["games"]
    for game in gamesJson:
        if game["score"]["home"]["goals"] == home_score and game["score"]["away"]["goals"] == away_score:
            games.append(game)
            game_dates.append(year+"/"+date)

for i in range(len(games)):
    print("["+game_dates[i]+"] ("+str(home_score)+") "+ games[i]["score"]["home"]["team"]+" - "+ games[i]["score"]["away"]["team"]+" ("+str(away_score)+")")    