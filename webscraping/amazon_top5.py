import requests, webbrowser, bs4, sys

print("amazon searching")
res = requests.get("https://www.amazon.in/s/url=search-alias%3Daps&field-keywords="+" ".join(sys.argv[1:]), headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')

linkImages = soup.select('a.a-link-normal.s-access-detail-page.s-color-twister-title-link.a-text-normal')
print(len(linkImages))
numOpen = min(5, len(linkImages))
for i in range(numOpen):
	webbrowser.open(linkImages[i].get('href'))