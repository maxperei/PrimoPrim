from django_mongoengine import mongo_admin as admin
from .models import Artist, Performance

# Register your models here.
# @admin.register(Artist)
class ArtistAdmin(admin.DocumentAdmin):
    pass

# @admin.register(Performance)
class PerformanceAdmin(admin.DocumentAdmin):
    pass
