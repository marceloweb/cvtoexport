import web
import requests
from oauthlib import *

urls = (
  '/', 'index',
  '/generator', 'generator'
)

class index:
   def GET(self):
      title = "Gera PDF formatado a partir de perfil do Linkedin"
      return title

class generator:
   def GET(self):
      url = 'https://api.linkedin.com/v1/companies/1337/updates?start=20&count=10&format=json'
      return requests.get(url)

if __name__ == "__main__":
   app = web.application(urls, globals())
   app.run()
