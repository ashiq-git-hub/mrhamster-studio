import urllib.request, re

url = 'https://in.pinterest.com/pin/642748178106648967/'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
try:
    with urllib.request.urlopen(req) as resp:
        html = resp.read().decode('utf-8')
    imgs = set(re.findall(r'https://i\.pinimg\.com/(?:originals|736x|564x)/[a-zA-Z0-9/_.\-]+(?:\.jpg|\.png)', html))
    print('Found images:', len(imgs))
    for u in sorted(imgs):
        print(u)
except Exception as e:
    print('Error:', e)
