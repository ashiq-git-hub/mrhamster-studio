import urllib.request, re, json

url = 'https://in.pinterest.com/pin/642748178106648967/'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
html = urllib.request.urlopen(req).read().decode('utf-8')

# Find 736x and originals
urls = set(re.findall(r'https://i\.pinimg\.com/(?:originals|736x|474x)/[a-f0-9/]+(?:\.jpg|\.png)', html))
print('Count:', len(urls))
for u in sorted(urls):
    print(u)
