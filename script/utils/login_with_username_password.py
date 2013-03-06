import urllib
import urllib2
import cookielib

# https://pypi.python.org/pypi/linkchecker
# http://docs.python.org/2/library/cookielib.html
login = 'user@host.com'
password = 'secret'

cookiejar = cookielib.CookieJar()
urlOpener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookiejar))

# adjust this to match the form's field names
values = {'username': login, 'password': password}
data = urllib.urlencode(values)
request = urllib2.Request('http://target.of.POST-method', data)
url = urlOpener.open(request)
# from now on, we're authenticated and we can access the rest of the site
url = urlOpener.open('http://rest.of.user.area')
