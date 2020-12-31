import os 
import io
import chess
import chess.pgn
import chess.svg
import requests
from IPython.display import display
import logging

logger = logging.getLogger(__name__)

GMPlayersUrl = 'https://api.chess.com/pub/titled/GM'
r = requests.get(GMPlayersUrl)
if not r.ok:
   raise Exception('url does not return: ', url, ' with message ', r.text)
j = r.json()

for player in j['players']:
    monthlyArchivesUrl =  f'https://api.chess.com/pub/player/{player}/games/archives'
    r = requests.get(monthlyArchivesUrl)
    if not r.ok:
        raise Exception('url does not return: ', monthlyArchivesUrl, ' with message ', r.text)
    games = r.json()

    for gamesFromTournament in games.get('archives'):
        r = requests.get(gamesFromTournament)
        if not r.ok:
            raise Exception('url does not return: ', gamesFromTournament, ' with message ', r.text)
        # print(r.json().get('games'))
        gamesFromTournamentJSON = r.json().get('games')
        
        for game in gamesFromTournamentJSON:
            gamePGN = game.get('pgn')
            pgn = io.StringIO(gamePGN)
            gameParsed = chess.pgn.read_game(pgn)
            path = '/Users/VAZ3773/Desktop/chess_downloader_api/fetch_games/saved_games'
            if gameParsed and gameParsed.headers:
                file = gameParsed.headers.get('Date') + '_' + gameParsed.headers.get('White') + '_' + gameParsed.headers.get('Black')
                print(gameParsed.headers.get('Date') + '_' + gameParsed.headers.get('White') + '_' + gameParsed.headers.get('Black'))
                if len(gamePGN) == 0:
                    print('game pgn is zero ', game) 
                if not gamePGN:
                    print('game pgn is nonexistent ', game)
                with open(os.path.join(path, file), 'w') as fp:
                    fp.write(gamePGN)
