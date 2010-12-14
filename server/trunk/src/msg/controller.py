from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db

import os
from google.appengine.ext.webapp import template

from datetime import timedelta

def notEmpty(string):
    if string is None:
        return False
    elif len(string) == 0:
        return False
    else:
        return True
    
def render(object, templateFile):
    template_values = {'object' : object}
    path = os.path.join(os.path.dirname(__file__), templateFile)
    return template.render(path, template_values)
    
class Message(db.Model):
    author = db.StringProperty()
    content = db.StringProperty()
    group = db.StringProperty()
    date = db.DateTimeProperty(auto_now_add=True)
    
    def shortDate(self):
        d = timedelta(hours=1)
        short = self.date + d
        return str(short)[:16]
        
    
    def valid(self):
        return notEmpty(self.author) and notEmpty(self.content) and notEmpty(self.group)
    
    def asXML(self):
        return render(self, 'message.tpl.xml')
        
        

class Post(webapp.RequestHandler):
    
    def get(self):
        self.handle()
        
    def post(self):
        self.handle()        
    
    def handle(self):
        message = Message()
        message.group = self.request.get("group")
        message.content = self.request.get("content")
        message.author = self.request.get("author")
        if (message.valid()):
            message.put()
            self.response.out.write('<html><body>OK</body></html>')
        else:
            self.response.out.write('<html><body>NACK</body></html>')

class ListAll(webapp.RequestHandler):
    
    def get(self):
        self.response.headers['Content-Type'] = 'text/xml; charset=utf-8'
        
        messages = db.GqlQuery("SELECT * FROM Message ORDER BY date DESC LIMIT 100")

        self.response.out.write(render(messages, 'messages.tpl.xml'))

class List(webapp.RequestHandler):
    
    def get(self):
        self.response.headers['Content-Type'] = 'text/xml; charset=utf-8'
        groups = self.request.get_all("groups[]")
        
        
        messages = db.GqlQuery("SELECT * FROM Message ORDER BY date DESC LIMIT 100")

        def f(x):
            return x.group in groups
        messages = filter(f, messages)

        self.response.out.write(render(messages, 'messages.tpl.xml'))        

application = webapp.WSGIApplication(
                                     [('/msg/post', Post),
                                      ('/msg/list', List),
                                      ('/msg/list/all', ListAll)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()