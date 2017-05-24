import os
from cgitb import text
def read_txt():
	quotes = open('hosts.txt', 'r')
	print (quotes.read())
	quotes.close

	
read_txt()