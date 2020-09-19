from urllib import request
from html.parser import HTMLParser

class CustomHTMLParser(HTMLParser):
  def handle_starttag(self, tag, attrs):
    if tag == "select":
      for attr in attrs:
        if attr[0] == 'name' and attr[1] == 'country':
          print(attrs)

  def handle_endtag(self, tag):
    if tag == "select":
      print(self)
    if tag == "123":
      print("Encountered an end tag :", tag)

  def handle_data(self, data):
    if data == "請選擇":
      print(data)
    # print("Encountered some data  :", data)