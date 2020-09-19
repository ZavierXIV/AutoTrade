from urllib import request
from html.parser import HTMLParser

class QueryMap:
  def township(self, str):
    dic = {
        '松山區':'A01',
        '大安區':'A02',
        '中正區':'A03',
        '萬華區':'A05',
        '大同區':'A09',
        '中山區':'A10',
        '文山區':'A11',
        '南港區':'A13',
        '內湖區':'A14',
        '士林區':'A15',
        '北投區':'A16',
        '信義區':'A17',
    }

    return dic[str]

  def city(self, str):
    dic = {
      '臺北市':'A',
      '新北市':'F',
      '桃園市':'H',
    }

    return dic[str]
