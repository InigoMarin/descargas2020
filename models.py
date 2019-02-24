from peewee import *
import datetime

db = PostgresqlDatabase('postgres', user='demo', password='demo',
                           host='localhost', port=5432)

class BaseModel(Model):
    class Meta:
        database = db

class Post():
    def __init__(self,title,url):
        self.title = title
        self.url = url
    
    def __str__(self):
        return "Post\n\tTitle:" +self.title + "\n\tUrl:" + self.url

class Media(BaseModel):
    
    url  = CharField(unique =True)
    quality = CharField()
    audio = CharField()
    season = CharField()
    episode = CharField
    clasification = CharField()
    media = CharField()
    data = CharField()
    title = CharField()
    img = CharField()
    torrent = CharField()
    size =CharField()
    fecha = DateTimeField()
    fecha_scraping = DateTimeField(default = datetime.datetime.now()) 
    descripcion = TextField()



    def __str__(self):
        return "Media\n" \
        "\tTitle: " +self.title+"\n"\
        "\tUrl: " + self.url +"\n" \
        "\tClasification: " +self.clasification +"\n"\
        "\tMedia: " +self.media+"\n"\
        "\tData: " +self.data+"\n"\
        "\tImg: " +self.img+"\n"\
        "\tTorrent: " +self.torrent+"\n"\
        "\tSize: " +self.size+"\n"\
        "\tFechaSubida: " +self.fecha+"\n"
        
    def  to_json(self):
        return {
            'title': self.title,
            'url': self.url,
            'quality': self.quality,
            'audio': self.audio,
            'season': self.season,
            'episode': self.episode,
            'clasification': self.clasification,
            'media':self.media,
            'data':self.data,
            'img':self.img,
            'torrent':self.torrent,
            'size':self.size,
            'fecha_subida':self.fecha,
            'fecha_scraping':self.fecha_scraping,
            'descripcion':self.descripcion
        }