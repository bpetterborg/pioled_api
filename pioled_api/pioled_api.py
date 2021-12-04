#
#	PiOLED API
#	- Websockets API for PiOLED screens
#
#


# very many imports

import asyncio			# Asynchronous I/O
import websockets		# Websockets
import json				# reading config
from time import sleep

import Adafruit_GPIO.SPI as SPI	
import adafruit_ssd1306							# piOLED

from PIL import Image, ImageDraw, ImageFont		# fonts and pictures


# reading config, some setup
with open('config.json') as configFile:
	config = json.load(configFile)

resX = config['resX']
resY = config['resY']
	
font = ImageFont.load_default() # eventally change this read from the config

# gpio stuff
rst = None	# unused pin
dc = 23
spiPort = 0
spiDevice = 0

# setup screen
display = adafruit_ssd1306.SSD1306_128_32(rst=rst)

display.begin()		# init and clear
display.clear()
display.display()

# make something to draw onto
width = display.width
height = display.height

image = Image.new('1', (width, height))					# 1 bit mode
draw = ImageDraw.Draw(image)	
draw.rectangle((0,0,width,height), outline=0, fill=0) 	# clear screen	

# padding
padding = -2
top = padding
bottom = height - padding

x = 0	# start at the left


# some functions
	
def __init__(self) -> None:
		pass

async def ping(websocket):
	await websocket.send("pong")

async def write(websocket, text):
	pass

async def clear(websocket):
	pass

# i think this is correct??


server = websockets.serve(write, "localhost", 8765)
listener = websockets.listen("localhost", 8765)			#  unsure if this is needed, will keep it for now.

asyncio.get_event_loop().run_until_complete(server)
asyncio.get_event_loop().run_forever()