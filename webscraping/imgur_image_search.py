import requests, bs4, webbrowser, sys

print("searching in imgur")
res = requests.get("https://imgur.com/search?q="+' '.join(sys.argv[1:]))
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')

LinksImages = soup.select('a.image-list-link')

num = min(5, len(LinksImages))

for i in range(num):
	webbrowser.open('imgur.com'+LinksImages[i].get('href'))