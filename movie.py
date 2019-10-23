import time
import os

frameList = [
'''
( ͡° ͜ʖ ͡°)''','''
( ͡~ ͜ʖ ͡°) ''','''
( ͡o ͜ʖ ͡o)''', '''
 (╯°□°)╯ ~~ ┻━┻ ''', '''
 [̲̅$̲̅(̲̅ ͡° ͜ʖ ͡°̲̅)̲̅$̲̅] ''', '''
 /\/( ͡°͡° ͜ʖ ͡°͡°)\/\ ''', '''
 ┬┴┬┴┤( ͡° ͜ʖ├┬┴┬┴  ''' 

]

while True:
	for frame in frameList:
		os.system("cls")
		print(frame)
		time.sleep(.2)
