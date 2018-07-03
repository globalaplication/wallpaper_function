
import urllib
class wallpaper (object):
	def __init__(self, url):
		self.url = url
		self.source = urllib.urlopen(url)
		self.source = self.source.read().replace("</li>", "</li>\n")
		self.title_list = {}
		self.picture_list = []
	def title(self):
		for beta in self.source.splitlines():
			if beta.find("</small></li>") is not -1:
				start1 = beta.find("title") 
				start = beta.find(">", start1) + 1
				end = beta.find("</a>", start)
				linkstart = beta.find('a href="/') + 9
				linkend = beta.find('"', linkstart)
				url = "{}{}".format("http://wallpaperswide.com/", beta[linkstart:linkend])
				self.title_list[beta[start:end]] = {"url":url}
		return self.title_list
	def download(self, title):
		title = "{}".format(title.title())
		source = urllib.urlopen(self.title_list[title]["url"])
		for beta in source.read().splitlines():
			if beta.find("thumb_img") > -1:
				start = beta.find('"') +1
				end = beta.find( '"', start+1) 
				file = str(beta[start:end].replace("thumbs", "download").
				replace(".jpg","-wallpaper-1366x768.jpg").
				replace("hd.", ""))
				self.picture_list.append(file)
		return self.picture_list
		
test = wallpaper("http://wallpaperswide.com")
test.title()
print test.download("funny")







		
	
