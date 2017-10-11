import requests, webbrowser, bs4, sys
print("amazon searching")
res = requests.get('https://amazon.in/' , headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})
res.raise_for_status();
soup = bs4.BeautifulSoup(res.text, 'html.parser')

linkElems = soup.select('.imageWithText a')
for i in range(len(linkElems)):
	webbrowser.open('www.amazon.in'+linkElems[i].get('href'))