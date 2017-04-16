from mongoengine import *
from django.views import generic

from .models import Artist, Performance

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'somnium/index.html'
    context_object_name = 'artists_list'

    def get_queryset(self):
        return Artist.objects.order_by('name')
