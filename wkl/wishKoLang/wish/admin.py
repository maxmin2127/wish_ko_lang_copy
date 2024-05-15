from django.contrib import admin
from . models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Wishlist)
admin.site.register(Item)
admin.site.register(Group)
admin.site.register(Pair)
admin.site.register(Membership)
admin.site.register(Organization)
admin.site.register(Organization_Member)