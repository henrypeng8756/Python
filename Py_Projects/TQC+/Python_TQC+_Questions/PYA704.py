# %%
import urllib
res = urllib.request.urlopen('https://google.com.tw')
content = res.read()
print(content)