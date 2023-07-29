# YouTube Music Downloader
This is a Python project to help you download songs from your YouTube Music playlists.

## Project setup
Make sure that you have installed [Poetry](https://python-poetry.org/) before setting up the project.

### 1. Installing Poetry
#### Linux, macOS, Windows (WSL)
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

#### Windows (Powershell)
```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

### 2. Activating virtual environment
#### Linux, macOS, Windows (WSL)
```bash
source $(poetry env info --path)/bin/activate
```
#### Windows (Powershell)
```powershell
& ((poetry env info --path) + "\Scripts\activate.ps1")
```

#### 3. Install dependencies
```
poetry install
```

### Downloading songs
You need to create a `.env` file and specify the ids of the playlists you want to download using the `PLAYLIST_IDS` variable.

For example
```
PLAYLIST_IDS='[PLu0ocO48LFms5WsI1ipaeanxqRjn2fC_5]'
```
where 'PLu0ocO48LFms5WsI1ipaeanxqRjn2fC_5' is the id of the ['Sweaty EDM Workout'](https://music.youtube.com/playlist?list=RDCLAK5uy_m-YJyz6cquN8dHWwbuwWJpoY7gC2dSaVo&feature=share&playnext=1)

After that, execute the `download.py` script. Make sure that you update the options to be passed down to the [YouTube downloader](https://github.com/ytdl-org/youtube-dl) using 
the `ydl_opts`. For more details, check out [the Python file](https://github.com/ytdl-org/youtube-dl/blob/abef53466da1f7d2e79f5644718a2cf7524abc49/youtube_dl/YoutubeDL.py#L157).



