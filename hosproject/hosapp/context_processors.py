from .models import Package


def menu_links(req):
    
    pak=Package.objects.all()
    return dict(pak=pak)