from multiprocessing import Pool
import bs4 as bs
import random
import requests
import string
import json

def starting_url(): 
	starting = ''.join(random.SystemRandom().choice(string.ascii_lowercase) for _ in range(3)) 
	url = ''.join(['http://www.', starting, '.com']) 
	return url

def local_links(url, link): 
	if link.startswith('/'): 
		return ''.join([url,link])
	else: 
		return link

def get_links(url): 
	try: 
		resp = requests.get(url)
		soup = bs.BeautifulSoup(resp.txt,'lxml')
		body = soup.body
		links = [link.get('href')for link in body.find_all('a')]
		links = [local_links(url, link) for link in links]
		links = [str(link.enconde('ascii'))for link in links]
		return links

	except TypeError as e: 
		print(e)
		print('Got a type error. Probably got a none ') 
		return[]
	except IndexError as e: 
		print(e)
		print("Didn't get anything useful, returning empty list")
		return []
	except AttributeError as e: 
		print(e)
		print('likely got none. throwing error')
		return []
	except Exception as e: 
		print (str(e))
		# log this error
		return []

def main(): 
	how_many = 50
	p = Pool(processes=how_many)
	parse_us = [starting_url() for _ in range (how_many)]
	data = p.map(get_links, [link for link in parse_us])
	data = [url for url_list in data for url in url_list]
	parse_us = data
	p.close()

	with open('urls.txt', 'w') as f: 
		f.write(str(data))



if __name__ == '__main__': 
	main()







