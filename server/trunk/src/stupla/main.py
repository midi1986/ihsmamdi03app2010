from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

from stupla.parser import parseStudiengaenge, parseSemester, parseVorlesungen, parseStupla
from stupla.client import get_studiengaenge_from_server, get_query_from_server

class Studiengaenge(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/xml; charset=utf-8'
        html = get_studiengaenge_from_server()
        self.response.out.write(parseStudiengaenge(html).asXML())
        
class Semester(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/xml; charset=utf-8'
        query = self.request.query
        html = get_query_from_server(query)
        self.response.out.write(parseSemester(html).asXML())       
        
class Vorlesungen(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/xml; charset=utf-8'
        query = self.request.query
        html = get_query_from_server(query)
        self.response.out.write(parseVorlesungen(html).asXML())       
        
class Stupla(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/xml; charset=utf-8'
        query = self.request.query
        html = get_query_from_server(query)
        self.response.out.write(parseStupla(html).asXML())                      

application = webapp.WSGIApplication(
                                     [('/stupla/studiengaenge', Studiengaenge),
                                      ('/stupla/semester', Semester),
                                      ('/stupla/vorlesungen', Vorlesungen),
                                      ('/stupla', Stupla)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
    