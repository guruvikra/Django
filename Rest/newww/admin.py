from django.contrib import admin
from newww.models import Data,Review
# Register your models here.
admin.site.register(Data)
admin.site.register(Review)




# another way
# class DataAdmin(admin.ModelAdmin):
#     list_display=("the thing we want to give to  admin to do curd operaation")

# admin.site.register(DataAdmin,Data)

