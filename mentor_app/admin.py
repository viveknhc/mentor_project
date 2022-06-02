from django.contrib import admin
from mentor_app.models import Catagory,Trainer,Course,Testimonial,Contact
from mentor_app.views import courses
# Register your models here.
admin.site.register(Catagory)
admin.site.register(Trainer)
admin.site.register(Course)
admin.site.register(Testimonial)
admin.site.register(Contact)