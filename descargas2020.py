import feedparser
import sys
import logging
import re
import requests
import datetime
import hashlib
import notificar
from models import Post,Media
from scrapy.http import HtmlResponse
from scrapy.selector import Selector

from models import db,Media

db.connect()
db.create_tables([Media])

def scrapingRssPost( post):
    logging.info("Start scraping post " + post.title )
    logging.debug("Url ->" + post.url)

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    logging.debug(headers['User-Agent'])

    url = requests.get(post.url,headers= headers)

    response = HtmlResponse(url=post.url,body=url.text, encoding='utf-8')

    data_extracted_title = re.split(r'\[(.*?)\]',post.title)


    clasification = response.xpath('//ul[@class="breadcrumbs"]/li[position()=2]/a/text()').extract_first()
    logging.debug("Clasification:" + clasification)


    if "Series" in clasification:
        episode = data_extracted_title[3]
        audio = data_extracted_title[5]
    else:
        episode = ""
        audio = data_extracted_title[3]

    quality = data_extracted_title[1]
    logging.debug("Quality:" +quality)
    logging.debug("Episode:" +episode)
    logging.debug("Audio:" +audio)

    # DEJAR PARA FUTURO
    media = response.xpath('//ul[@class="breadcrumbs"]/li[position()=3]/a/text()').extract_first()
    logging.debug("media:" + media)

    data = response.xpath('//div[@class="page-box"]/h1/strong/text()').extract_first()
    season = data
    logging.debug("data:" + data)

    """
    dataextra = response.xpath('//div[@class="page-box"]/h1/strong/following-sibling::node()').extract_first()
    logging.debug("dataextra:" + dataextra)
    """

    divbox = response.xpath('//div[@class="entry-left"]')
    img = divbox.xpath('.//img/@src').extract_first()
    logging.debug("img:" + img)

    size = divbox.xpath('.//span/text()')[0].root.strip(' ')
    logging.debug("size:" + size)

    fecha = divbox.xpath('.//span/text()')[1].root.strip(' ')
    logging.debug("fecha:" + fecha)
    format = '%d-%m-%Y'
    try:
        fecha_convertida = datetime.datetime.strptime(fecha, format)
    except:
        fecha_convertida =  datetime.datetime(datetime.datetime.now().year,datetime.datetime.now().month,datetime.datetime.now().day)

    logging.debug(fecha_convertida.date())

    # SACAR DESCRIPCION
    textosel = response.xpath('//div[@class="descripcion_top"]')
    datos = textosel.xpath('.//text()').extract()
    datos = '\n'.join(datos)

    # SACAR TORRENT
    texto=response.xpath('//div[@id="tab1"]//script/text()').extract()
    texto = texto[0]
    url_reg = re.compile(r'window.location.href \s*=\s"(\S*)\"')
    
    try:
        torrent ="http:" + url_reg.findall(texto)[0]
    except:
        torrent= "ERROR"
    
    media =Media.create(url = post.url,quality = quality, audio = audio, season = season, episode = episode, clasification = clasification, media = media, data = data, title = post.title, img = img, torrent = torrent, size = size, fecha = fecha_convertida, descripcion = datos)
    media.save()
    logging.debug(media.to_json())
    ##logging.info(media)
    logging.info("End scraping post")


def main():
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
    url = 'http://feeds.feedburner.com/descargas2020new'

    feed  = feedparser.parse(url)

    posts = []

    for post in feed.entries:
        post = Post(post.title,post.link)
        posts.append(post)
        #logging.info(post)

    for post in posts:
        contar = (Media.select().where(Media.url == post.url).count())
        if contar ==0:
            scrapingRssPost(post)
            notificar.notificar(post.title)
        else:
            break


if __name__ == '__main__':
    main()
