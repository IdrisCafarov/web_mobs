from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager






# Create your models here.

class MyUserManager(BaseUserManager):
    def create_user(self,email,password=None,is_active=True,is_staff=False,is_superuser=False, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")
        user = self.model(
            email=email,
            **extra_fields
        )
        user.set_password(password)
        user.is_active = is_active
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.save(using=self._db)
        return user

    def create_superuser(self,email,password=None):
        user = self.create_user(
            email=email,
            password=password
        )
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)
        return user



class MyUser(AbstractBaseUser):
    phone_number = models.CharField(max_length=20,verbose_name="Telefon nomresi",null=True, blank=True)
    email = models.EmailField(unique=True,max_length=120, null=True)
    name = models.CharField(max_length=40,verbose_name="Name", blank=True, null=True)
    surname = models.CharField( max_length=40,verbose_name="Surname", blank=True, null=True)
    profile_image = models.ImageField(upload_to="Profile Image",null=True, blank=True)

    about = models.TextField(null=True)
    present_work_space = models.CharField(max_length=100, null=True)
    birthday = models.DateField(null=True)

    rating = models.PositiveIntegerField(default=0)


    meet = models.CharField(max_length=20,null=True)
    slug = models.SlugField(unique=True,null=True)


    password_reset_code = models.CharField(max_length=120,blank=True,null=True)

    timestamp = models.DateTimeField(auto_now_add=True)

   

    is_active = models.BooleanField(default=True)
    is_disable = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)


    objects = MyUserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        ordering = ['-timestamp']
        verbose_name = 'MyUser'
        verbose_name_plural = 'MyUser'


    def __str__(self):
        return f"{self.email}"


    def get_full_name(self):
        if self.surname:
            return '%s %s'%(self.name,self.surname)
        return self.name

    def has_perm(self,perm,obj=None):
        return self.is_superuser

    def has_module_perms(self,app_label):
        return True

    def get_avatar(self):
        if self.profile_image:
            return self.profile_image.url
        else:
            return "/static/static/user.png"

    def save(self, *args, **kwargs):
        from account.utils import create_slug_shortcode
        if not self.slug:
            self.slug = create_slug_shortcode(size=20, model_=MyUser)
        return super(MyUser, self).save(*args,**kwargs)

