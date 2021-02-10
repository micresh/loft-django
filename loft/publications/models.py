from django.db import models


# todo modificate meta to more userfriendly admin panel in all classes
class Tag(models.Model):
    ''' Tag model'''
    text = models.CharField(max_length=100)

    def __str__(self):
        return self.text

    class Meta:
        pass


class Publication(models.Model):
    '''Publication model'''
    title = models.CharField(max_length=300)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

    class Meta:
        pass


class Comment(models.Model):
    '''Comment model'''
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return self.author

    class Meta:
        pass
