from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    #posts = models.ForeignKey(User, on_delete=models.CASCADE)
    #body = models.TextField()
    body = RichTextUploadingField(default='Add Notice here', blank=False, null=False)
    image = models.ImageField(upload_to='images/', blank=True, null=True)


    def __str__(self):
        #changes the blog title in the admin area from being called blog 1 and blog 1 to the actual blog title
        return self.title

    def summary(self):
        #cap the text to 100
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
