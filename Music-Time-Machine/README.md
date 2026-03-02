# Music Time Machine 🎵

Travel back in time through music.

This Python project creates a Spotify playlist from the Billboard Hot 100 chart of any date you choose.

## Features

• Enter any date in history
• Scrapes the Billboard Hot 100 chart
• Finds the songs on Spotify
• Automatically creates a private playlist
• Adds the songs to your account

## Tech Stack

* Python
* Requests
* BeautifulSoup
* Spotify API
* OAuth Authentication

## How It Works

1. Enter a date in the format `YYYY-MM-DD`
2. The script scrapes Billboard’s Hot 100 songs for that date
3. Each song is searched on Spotify
4. A playlist is created in your account
5. All songs are added automatically

## Installation

Clone the repository

```
git clone https://github.com/yourusername/music-time-machine.git
cd music-time-machine
```

Install dependencies

```
pip install -r requirements.txt
```

## Setup Spotify API

Create an app in the Spotify Developer Dashboard from Spotify.

Add your credentials inside the script:

```
SPOTIFY_CLIENT_ID = "your_client_id"
SPOTIFY_CLIENT_SECRET = "your_client_secret"
```

Set Redirect URI to

```
https://example.com
```

## Run the Project

```
python main.py
```

Example input

```
2002-07-20
```

The program will generate a playlist called

```
2002-07-20 Billboard 100
```

inside your Spotify account.

## Future Improvements

* Add artist names
* Save songs to a CSV file
* Web version using Flask
* Add a UI
* Deploy online
