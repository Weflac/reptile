
from pyquery import PyQuery as pq

doc = pq('<html>hello world</html>')

result = doc('html').text()

print(result)
