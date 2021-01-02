import os

onlyfiles = next(os.walk('/Users/VAZ3773/Desktop/chess_downloader_api/fetch_games/saved_games'))[2] #dir is your directory path as string
print(len(onlyfiles))

