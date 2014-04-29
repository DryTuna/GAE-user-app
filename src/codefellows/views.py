'''
Created on Apr 28, 2014

@author: Duy Tran
'''
from django.views.generic.simple import direct_to_template
from django.http import HttpResponseRedirect
from django.core.cache import cache

from codefellows.models import People
from codefellows.forms import CreatePeopleForm

MEMCACHE_PEOPLE = 'people'

def main_page(request):
    people = cache.get(MEMCACHE_PEOPLE)
    return direct_to_template(request, 'main_page.html', 
                              {'people': people, 'form': CreatePeopleForm()})
    '''
    person_name = request.GET.get('people_name', 'default_codefellows')
    person_key = People.get_key_from_name(person_name)
    person_query = People.all().ancestor(person_key)
    person = person_query.fetch(10)
    template_values = {
        'person': person,
        'person_name': person_name,
    }
    return direct_to_template(request, 'main_page.html', template_values)
    '''
def submit_data(request):
    if request.method == 'POST':
        person = People()
        person.first_name = request.POST.get('first_name')
        person.last_name = request.POST.get('last_name')
        person.email = request.POST.get('email')
        person.save()
        return HttpResponseRedirect('main_page.html')
    
    return HttpResponseRedirect('main_page.html')