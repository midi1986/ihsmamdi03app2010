from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

from stupla.parser import parseStudiengaenge
from stupla.client import get_studiengaenge_from_server

class Studiengaenge(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/xml; charset=utf-8'
        html = get_studiengaenge_from_server()
        self.response.out.write(parseStudiengaenge(html).asXML())

application = webapp.WSGIApplication(
                                     [('/stupla/studiengaenge', Studiengaenge)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
    