#
#	PiOLED API
#	- RESTful API for PiOLED screens
#
#


# very many imports
from flask import Flask, request				# api stuff
from flask_restful import Resource, Api

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

# flask
app = Flask(__name__)
api = Api(app)


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

# just api things <4
class ClearScreen(Resource):
	# clears the screen	
	def post(self):
		draw.rectangle((0,0,width,height), outline=0, fill=0)
		return {'message': 'cleared'}

class DrawText(Resource):
	# writes text to the screen
	def post(self, text, x, y):
		self.text = text
		self.x = x
		self.y
		draw.text((self.x, self.y), self.text,  font=font, fill=255)

class DrawImage(Resource):
	# draw stuff on screen
	def post(self, image, x, y):
		self.image = image
		self.x = x
		self.y = y
		pass

class Run(Resource):
	def post(self):
		display.image(image)
		display.display()


# you need to make the mappings for the paths
api.add_resource(ClearScreen, '/clear')
api.add_resource(DrawText, '/write')
api.add_resource(DrawImage, '/draw')

# make app go brr
if __name__ == '__main__':
	app.run(port='5002')
