from django.contrib import admin
from .models import Homes,Branch,Gallery,Blog,Package,Enquery,Appointment,Contact,Testi
# Register your models here.
class HomesAdmin(admin.ModelAdmin):
    list_display=['name','image']
admin.site.register(Homes,HomesAdmin)

class TestiAdmin(admin.ModelAdmin):
    list_display=['name','detail','place']
admin.site.register(Testi,TestiAdmin)

class EnqueryAdmin(admin.ModelAdmin):
    list_display=['names','email','number','message']
admin.site.register(Enquery,EnqueryAdmin)   

class AppointmentAdmin(admin.ModelAdmin):
    list_display=['name','email','phone','date','time','age','gender','address','message']
admin.site.register(Appointment,AppointmentAdmin) 

class ContactAdmin(admin.ModelAdmin):
    list_display=['name','email','phone','subject','message']
admin.site.register(Contact,ContactAdmin) 

class BranchAdmin(admin.ModelAdmin):
    list_display=['image','name']
admin.site.register(Branch,BranchAdmin)

class GalleryAdmin(admin.ModelAdmin):
    list_display=['image']
admin.site.register(Gallery,GalleryAdmin)

class BlogAdmin(admin.ModelAdmin):
    list_display=['image','name']
admin.site.register(Blog,BlogAdmin)

class PackageAdmin(admin.ModelAdmin):
    list_display=['image','price','name','cont1','cont2','cont3','cont4','cont5','cont6','cont7','cont8','cont9','cont10','cont11','cont12','cont13']
admin.site.register(Package,PackageAdmin)
