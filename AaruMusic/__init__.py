from AaruMusic.core.bot import Aaru
from AaruMusic.core.dir import dirr
from AaruMusic.core.git import git
from AaruMusic.core.userbot import Userbot
from AaruMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Aaru()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
