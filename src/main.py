import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()

print 'Content-Type: text/plain'
print ''
print 'Hello, world!'