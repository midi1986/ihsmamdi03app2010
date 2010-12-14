from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db

import os
from google.appengine.ext.webapp import template

from util.string import notEmpty

def render(object, templateFile):
    template_values = {'object' : object}
    path = os.path.join(os.path.dirname(__file__), templateFile)
    return template.render(path, template_values)

class Group(db.Model):
    name = db.StringProperty()
    
    def valid(self):
        return notEmpty(self.name) and self.new()
    
    def new(self):
        return self.gql("WHERE name = :1", self.name).count() == 0
    
    def asXML(self):
        return render(self, 'group.tpl.xml')    
    
class Add(webapp.RequestHandler):    

    def get(self):
        self.handle()
        
    def post(self):
        self.handle()        
    
    def handle(self):
        group = Group()
        group.name = self.request.get("name")
        if (group.valid()):
            group.put()
            self.response.out.write('<html><body>OK</body></html>')
        else:
            self.response.out.write('<html><body>NACK</body></html>')    
    
class List(webapp.RequestHandler):        
    def get(self):
        self.response.headers['Content-Type'] = 'text/xml; charset=utf-8'
        
        messages = db.GqlQuery("SELECT * FROM Group ORDER BY name")
    
        self.response.out.write(render(messages, 'groups.tpl.xml'))

application = webapp.WSGIApplication(
                                     [('/groups/add', Add),
                                      ('/groups/list', List)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
