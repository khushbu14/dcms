from django.contrib import admin
from webapp.models import Contributor, Reviewer, Class, Subject, Contact, Faq

# Register your models here.
admin.site.register(Contributor)
admin.site.register(Reviewer)
admin.site.register(Class)
admin.site.register(Subject)
admin.site.register(Contact)
admin.site.register(Faq)


