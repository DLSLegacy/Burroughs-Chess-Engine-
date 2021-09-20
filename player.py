from random import shuffle, randint
>>> import sys, json, datetime
>>> 
>>> class player:
	def __init__(self, color):
		self.color = color

	def getColor(self):
		return self.color

	def setColor(self, color):
            self.color = color 
