# -*- coding: utf-8 -*- 
import telebot
from bs4 import BeautifulSoup
import requests
import time

URL = 'https://m.vk.com/dablyat177237500'
HEADERS = {
	'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Mobile Safari/537.36'
}
response = requests.get(URL, headers = HEADERS)
soup = BeautifulSoup(response.content, 'html.parser')
post = soup.find('div', class_='wall_item')
photo = post.find('a', class_='al_photo')
copyright = post.find('a', class_='copyright_label')
img = photo.attrs["href"]
src = 'vk.com/'
img_src = src + img
bot = telebot.TeleBot("1391389886:AAFZahFSMxg_J3CrVhDdjc2xHemCzV0uONU")


def send_photo():
	if (open('link.txt').read() == img_src or copyright != None):
		print(copyright)
		open('link.txt').close()
		print('Ссылки одинаковые или реклама, пропускаю итерацию')
		time.sleep(600)
	elif(open('link.txt').read() != img_src):
		open('link.txt').close()
		print('Ссылка в файле: ' + open('link.txt').read())
		open('link.txt').close()
		print('Ссылка img_src: ' + img_src)
		print('Ссылки разные, делаю пост')
		open('link.txt', 'w').write(img_src)
		open('link.txt').close()
		print('Ссылка в файле перезаписанная: ' + open('link.txt').read())
		bot.send_photo('@hype_posti', img_src)
		time.sleep(600)
while True:
	send_photo()