import io
import chess
import chess.pgn
import chess.svg
import requests
from IPython.display import display

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

    for game in games['archives']:
        r = requests.get(game)
        if not r.ok:
            raise Exception('url does not return: ', game, ' with message ', r.text)
        gameUnparsed = r.json()['games'][0]['pgn']
        pgn = io.StringIO(gameUnparsed)
        parsed = chess.pgn.read_game(pgn)
        board = parsed.board()

        display(chess.svg.board(board))
        break
    break
