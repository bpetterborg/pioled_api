#
#	PiOLED API
#	- Websockets API for PiOLED screens
#
#


# very many imports

import asyncio			# Asynchronous I/O
import websockets		# Websockets

import busio									# i2c
from Board import SCL, SDA						# i2c probably
import adafruit_ssd1306							# piOLED
from time import sleep							# sleep
from PIL import Image, ImageDraw, ImageFont		# fonts and pictures

class PiOLED:
	
	def __init__(self) -> None:
		pass

	async def ping(websocket):
		await websocket.send("pong")

	async def write(websocket, text, ):
		pass

	async def draw(websocket, x, y, image):
		pass

	async def clear(websocket):
		pass

# i think this is correct??
asyncio.run(PiOLED)