from ytmusicapi import YTMusic, setup_oauth
from youtube_dl import YoutubeDL
from dotenv import dotenv_values
import os
import logging

class MyLogger(object):
    def debug(self, msg):
        logging.debug(msg)
    
    def warning(self, msg):
        logging.warning(msg)

    def error(self, msg):
        logging.error(msg)


if __name__ == '__main__':
    logging.basicConfig(filename='download.log', encoding='utf-8', level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    config = dotenv_values(".env")
    logging.info(config)
    logging.debug(os.listdir(os.getcwd()))
    if 'oauth.json' in os.listdir(os.getcwd()):
        ytmusic = YTMusic("oauth.json")
    else:
        setup_oauth("oauth.json")
        ytmusic = YTMusic("oauth.json")

    playlistIds = config['PLAYLIST_IDS'].strip('[]').split(',')
    logging.debug(f'Playlist IDs: {playlistIds}')

    for playlistId in playlistIds:
        logging.debug(f'Downloading playlist {playlistId}')
        playlist = ytmusic.get_playlist(playlistId=playlistId)
        video_ids = [track['videoId'] for track in playlist['tracks']]
        ydl_opts = {
            'verbose': True,
            'noplaylist': True,
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',
            'outtmpl': '%(title)s.%(ext)s',
            'logger': MyLogger()
        }
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([f'https://www.youtube.com/watch?v={video_id}&list={playlistId}' for video_id in video_ids])