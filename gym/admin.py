from django.contrib import admin
from .models import MembershipPlan, Member, Trainer, Attendance, Payment

admin.site.register(MembershipPlan)
admin.site.register(Member)
admin.site.register(Trainer)
admin.site.register(Attendance)
admin.site.register(Payment)
