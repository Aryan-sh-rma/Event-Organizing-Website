from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(advertisements)
admin.site.register(upComingEvents)

class PostAdmin(admin.ModelAdmin):
  list_display = ("author", "about", "img",)
admin.site.register(posts,PostAdmin)

admin.site.register(Like)

class CommentAdmin(admin.ModelAdmin):
  list_display = ("author", "desc", "post")
admin.site.register(BlogComment,CommentAdmin)




class EventAdmin(admin.ModelAdmin):
  list_display = ("event_author", "event_title", "category",)
admin.site.register(Event,EventAdmin)

class EventImageAdmin(admin.ModelAdmin):
  list_display = ["image", "get_event_title"]
  def get_event_title(self, obj):
      return obj.event.event_title
  get_event_title.short_description = 'event Title'
admin.site.register(EventImage,EventImageAdmin)


class EventbookingAdmin(admin.ModelAdmin):
  list_display = ("get_event_title","name", "email", "phoneNo",)
  def get_event_title(self, obj):
      return obj.event.event_title
  get_event_title.short_description = 'event Title'
admin.site.register(Eventbooking,EventbookingAdmin)






class Create_bandsAdmin(admin.ModelAdmin):
  list_display = ("bandname", "bandaddress", "author",)
admin.site.register(Create_bands,Create_bandsAdmin)

class BandbookingAdmin(admin.ModelAdmin):
  list_display = ("get_bandname","name", "email", "phoneNo",)
  def get_bandname(self, obj):
      return obj.bands.bandname
  get_bandname.short_description = 'Band name'
admin.site.register(Bandbooking,BandbookingAdmin)


class SignupAdmin(admin.ModelAdmin):
  list_display = ("First_name", "Last_name", "mobile_email",)
admin.site.register(Signup,SignupAdmin)

class Contact_usAdmin(admin.ModelAdmin):
  list_display = ("First_N", "mobileno", "emailid",)
admin.site.register(Contact_us,Contact_usAdmin)

class Contact_infoAdmin(admin.ModelAdmin):
  list_display = ("address", "email", "mobile",)
admin.site.register(Contact_info,Contact_infoAdmin)



class ProfilephotoAdmin(admin.ModelAdmin):
  list_display = ("author","image")
admin.site.register(Profilephoto,ProfilephotoAdmin)

class ProfilevideoAdmin(admin.ModelAdmin):
  list_display = ("author", "title", "video",)
admin.site.register(Profilevideo,ProfilevideoAdmin)

class About_pageAdmin(admin.ModelAdmin):
  list_display = ("title",)
admin.site.register(About_page,About_pageAdmin)

class About_service_pageAdmin(admin.ModelAdmin):
  list_display = ("title",)
admin.site.register(About_service_page,About_service_pageAdmin)

class About_team_pageAdmin(admin.ModelAdmin):
  list_display = ("member", "occuption")
admin.site.register(About_team_page,About_team_pageAdmin)

class About_our_missionAdmin(admin.ModelAdmin):
  list_display = ("title",)
admin.site.register(About_our_mission,About_our_missionAdmin)







