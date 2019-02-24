# OBJETIVO

El objetivo de este progama es leer la rss <http://feeds.feedburner.com/descargas2020new> de la pagina y guardar
datos para no ver la publicidad intrusiva.

Datos interesantes para el scraping del *titulo* del *RSS* ejemplos reales:

* **Titulos de las peliculas**

    Moulin Rouge [MicroHD 1080p][AC3 5.1-Castellano-AC3 5.1-Ingles+Subs][ES-EN]

    Hotel Transilvania 3 Unas Vacaciones Monstruosas [BluRay Rip][AC3 5.1 Castellano][2018][www.descargas2020.com]

    En La Playa De Chesil [BluRayRIP][AC 3 5.1 Castellano][2018][wwwrapid.com].torrent

* **Titulos de las series**

    Jersey Shore Family Vacation - Temporada 2 [HDTV 720p][Cap.206_209][AC3 5.1 Castellano][www.descargas2020.com]

    Deutschland 83 - Temporada 2 [HDTV][Cap.203][Castellano][www.descargas2020.com]

    Tu Cara Me Suena - Temporada 7 [HDTV][Cap.706][Castellano][www.descargas2020.com]

    Embrujadas 2018 - Temporada 1 [HDTV 720p][Cap.103][AC3 5.1 Castellano][www.descargas2020.com]

    Into The Dark The Body - Temporada 1 [HDTV 720p][Cap.102][V.O. Subt. Castellano][www.descargas2020.com]

    The Flash - Temporada 5 [HDTV 720p][Cap.503][AC3 5.1 Castellano][wwwrapid.com].torrent

Observando estos datos utilizaremos esta espresion regular para los datos entre los corchetes

    \[(.*?)\]

De estos datos podemos concluir que de los titulos podemos extraer estos datos:

* **Peliculas**
  * Calidad
  * Audio
  * Extra. Este campo puede ser año o idiomas

* **Series**
  * Calidad
  * Capitulo
  * Audio

## INFRAESTRUCTURA

El programa esta desarrolado y probado con python3.
Aplicacion de scraping escrita en python que lee los datos y los guarda en
una base de datos postgres, esto programa se jecutara mediante cron.

    pip install feedparser
    pip install request
    pip install scrapy
    pip install psycopg2-binary
    pip install peewee
    pip install notify2

Instalar PostgreSQL con docker.

   docker run --name postgres -p 5432:5432 -e POSTGRES_PASSWORD=demo -e POSTGRES_USER=demo -d postgres

### TODO

* Quitar data extra y poner titulo
* Quitar data ( Mirar en peliculas da el titulo de la pelicual)
* Quitar campo media

Campos para series:

* Quality

* Audio

* Season

* Episode