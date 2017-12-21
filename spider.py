from multiprocessing import pool
import bs4 as bs
import random
import requests
import string

def starting_url(): 
	starting = ''.join(random.SystemRandom().choice(string.ascii_lowercase) for _ in range(3))
	url = ''.join(['http://www.', starting, '.com'])
	return url

def local_links(url, link): 
	if link.startswith('/'): 
		return ''.join([url,link])
	else: 
		return link