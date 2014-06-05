from django.contrib import admin

from webapp.models import Contributor, Reviewer
from webapp.models import Class, Subject
from webapp.models import Contact, Faq


admin.site.register(Contributor)
admin.site.register(Reviewer)
admin.site.register(Class)
admin.site.register(Subject)
admin.site.register(Contact)
admin.site.register(Faq)
