import urllib
import httplib2
import base64
import json

# see https://developers.google.com/web-search/docs/#fonje
def google_search(phrase):
	"""Get google search results for the phrase"""
	url = "http://ajax.googleapis.com/ajax/services/search/web?v=1.0&" + urllib.parse.urlencode({'q':phrase});
	referer = "http://kevinrodrigues.com"
	h = httplib2.Http(".cache")
	resp, content = h.request(url, "GET", headers={'Referer': referer})
	if resp.status == 200:
		str_content = str(content)[2:-1]
		search_result = json.loads(str_content)
		print(search_result)
	else:
		print('Error')
if __name__ == '__main__':
	google_search('Kevin Rodrigues')
