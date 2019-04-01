#!/usr/bin/env python3

from web2 import google_image
import requests
from bs4 import BeautifulSoup
import re
#import urllib2
#import cookielib
import json
import os
from google_images_download import google_images_download
import tkinter

#from web import image_getter !! Still to be created !!


song_name = os.popen('./nowplaying').read()

go = google_image()
go.download_song_imgs(song_name)


# Do tk stuff with: image_getter(song_name)


