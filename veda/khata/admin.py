from django.contrib import admin
from .models import User,openaccount,depositetype,applyloan,heroImages

admin.site.register(User)
admin.site.register(openaccount)
admin.site.register(depositetype)
admin.site.register(applyloan)
admin.site.register(heroImages)