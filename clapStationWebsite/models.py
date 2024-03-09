from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from PIL import Image
from django.contrib.auth.models import User
# Create your models here.




def validate_image_dimensions(value):
    max_height = 360
    max_width = 800

    with Image.open(value) as img:
        width, height = img.size

    if width > max_width or height > max_height:
        raise ValidationError(f"Image dimensions must be at most {max_width}x{max_height} pixels.")


class posts(models.Model):
    img = models.ImageField(upload_to= "posts/image", default="", help_text=" ClapStation upload image | height: 360px | width: 640px"
                            , validators=[validate_image_dimensions])
    about = models.CharField(max_length = 250 )
    liked =models.ManyToManyField(User,default=None,blank=True,related_name='liked')
    updated=models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add = True)
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='author')
    
    def __str__(self):
        return f'{self.img} -{self.about}'


    @property
    def num_likes(self):
        return self.liked.all().count()



LIKE_CHOICES = (
    ('Like','Like'),
    ('Unlike','Unlike'),
)
class Like(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(posts,on_delete=models.CASCADE)
    value=models.CharField(choices=LIKE_CHOICES,default='Like',max_length=10)

    def __str__(self):
        return str(self.post)
    
# CommentSection

class BlogComment(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(posts,on_delete=models.CASCADE)
    post_date=models.DateTimeField(auto_now_add = True)
    desc=models.CharField(max_length=150)

    def _str_(self):
        return f'{self.author.username} : {self.desc[:30]}'


class advertisements(models.Model):
    img = models.ImageField(upload_to="advertisement/image",default="")
    created_at = models.DateTimeField(auto_now_add = True )

class upComingEvents(models.Model):
    img = models.ImageField(upload_to="upcoming/image", default="")
    phone= models.CharField(max_length=10)
    email= models.EmailField(max_length=50)
    address=models.TextField(max_length=50)
    created_at = models.DateTimeField(auto_now_add = True )




# create bands
class Create_bands(models.Model):
    bandname = models.CharField(max_length=20)
    bandbudget = models.DecimalField(max_digits=10, decimal_places=2)
    bandaddress = models.TextField()
    bandimage = models.ImageField(upload_to="createband/image",default="no image",null=True, blank=True)
    banddescription = models.TextField()
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return str(self.bandname)


class Bandbooking(models.Model): 
    bands = models.ForeignKey(Create_bands, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(default="",max_length=100)
    phoneNo = models.TextField(max_length=10)
    numOfcandidate = models.IntegerField()
    category = models.CharField(max_length=100)
    address = models.TextField(max_length=300)
    hour = models.IntegerField()
    date = models.DateField()
    time = models.DateTimeField() 
    
    def _str_(self):
        return str(self.name)

#eventpage
class Event(models.Model):
    event_author=models.ForeignKey(User,on_delete=models.CASCADE)
    event_title = models.CharField(max_length=200)
    description=models.TextField(max_length=600)
    category=models.CharField(max_length=100)
    duration=models.IntegerField()
    venue=models.CharField(max_length=400)
    city=models.CharField(max_length=30)
    state=models.CharField(max_length=30)
    date=models.DateField()
    ticket_price=models.IntegerField()
    poster=models.ImageField(upload_to='event_images/posters',blank=True,null=True)
    images=models.FileField(upload_to='event_images',blank=True,null=True)
    
    def _str_(self):
        return str(self.event_title)

class EventImage(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    image = models.FileField(upload_to='event_images/')

class Eventbooking(models.Model): 
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(default="",max_length=100)
    phoneNo = models.TextField(max_length=10)
    numOfcandidate = models.IntegerField()
    category = models.CharField(max_length=100)
    address = models.TextField(max_length=300)
    time = models.DateTimeField() 
    
    def _str_(self):
        return str(self.name)

#about page
class About_page(models.Model):
    title=models.CharField(max_length = 250 )
    description = models.TextField()



    def __str__(self):
        return str(self.title)

class About_service_page(models.Model):
    title=models.CharField(max_length = 250 )
    description = models.TextField()
    image = models.ImageField(upload_to='about_images/' )


    def __str__(self):
        return str(self.title)

class About_team_page(models.Model):
    member=models.CharField(max_length = 250 )
    occuption=models.CharField(max_length = 250 )
    image = models.ImageField(upload_to='about_images/' )


    def __str__(self):
        return str(self.member)


class About_our_mission(models.Model):
    title=models.CharField(max_length = 250 )
    description = models.TextField()
    image = models.ImageField(upload_to='our_mission/' )

    def __str__(self):
        return str(self.title)



#signup page
class Signup(models.Model):
    profile_image=models.ImageField(upload_to="profile" , default='')
    user= models.ForeignKey(User, on_delete=models.CASCADE) 
    First_name = models.CharField(max_length=100)
    Last_name = models.CharField(max_length=100)
    mobile_email = models.CharField( max_length=50,unique=True)
    day= models.IntegerField()
    month= models.CharField(max_length=20)
    year= models.IntegerField()
    role = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
     
    def __str__(self):
        return self.First_name + "--- " + self.user.username


#contactus page
class Contact_us(models.Model):
    First_N = models.CharField(max_length=50)
    Last_N = models.CharField(max_length=50)
    mobileno = models.IntegerField()
    emailid = models.CharField(max_length=50)
    address = models.TextField()

    def __str__(self)->str:
        return f"{self.First_N} - {self.Last_N} - {self.emailid}"

class Contact_info(models.Model):
    address=models.CharField(max_length=100)
    email=models.EmailField()
    mobile=models.CharField(max_length=15)
    insta=models.URLField()
    facebook=models.URLField()
    twitter=models.URLField()
    linkedin=models.URLField()
    
    def str(self):
        return self.address

class Profilephoto(models.Model):
    image = models.ImageField(upload_to="profilephoto/image",default="",null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile_photos')

    def __str__(self):
        return f'{self.image}'


class Profilevideo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile_videos')

    title=models.CharField(max_length=50)
    video = models.FileField(upload_to="profilephoto/video",default="",null=True, blank=True)
    def __str__(self):
        return f'{self.title}'



