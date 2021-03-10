import discord
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = "https://coinmarketcap.com/currencies/bitcoin/"

client = discord.Client()

def getBTC():
	# cleaning urllib cache
	urllib.urlcleanup()
  	
	# opening up connection, grabbing the page
	uClient = uReq(my_url)
	print('client opened')

	# assigning the contents of the page to page_html
	page_html = uClient.read()

	# closing the page
	uClient.close()
	print('client closed')

	# parsing the html and placing into the page_soup variable
	page_soup = soup(page_html, "html.parser")
	print(page_soup.findAll('div',{'class':'priceValue___11gHJ'})[0].text)
	print(page_soup.findAll('span',{'class':'sc-1v2ivon-0 gClTFY'})[0].text)

	# grab each row (later will iterate through each one to get the information from each)
	price = page_soup.findAll('div',{'class':'priceValue___11gHJ'})[0].text
	pctChange = page_soup.findAll('span',{'class':'sc-1v2ivon-0 gClTFY'})[0].text
	arrowChange = ''
	if 'icon-Caret-up' in str(page_soup.findAll('span',{'class':'sc-1v2ivon-0 gClTFY'})[0]):
		arrowChange = '\u25b2'
	else:
		arrowChange = '\u25bc'
	page_html = ''
	return [price, pctChange, arrowChange, page_html]

@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if 'btc' in message.content.lower():
		data = getBTC()
		await message.channel.send('Current $BTC price is: ' + data[0] + '.' + '(' + data[1] + data[2] +')')

	#if 'page_html' in message.content.lower():
	#	data = getBTC()
	#	await message.channel.send(data[3])
	#	return

client.run(#)
