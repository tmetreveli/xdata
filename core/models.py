from django.db import models

class Client(models.Model):
    username = models.CharField(max_length=255, unique=True)
    tts_enabled = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class Site(models.Model):
    sitename = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.sitename
    

class FilterWords(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, blank=True, null=True)
    word = models.CharField(max_length=255, blank=True, null=True)
    wordAlias = models.CharField(max_length=255, blank=True, null=True)
    subwordalias = models.CharField(max_length=255, blank=True, null=True)
    stopword = models.CharField(max_length=255, blank=True, null=True)
    

class Notification(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    sms = models.CharField(max_length=20, blank=True, null=True)
    telegram = models.CharField(max_length=255, blank=True, null=True)
    whatsapp = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    

class Article(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    insert_date = models.DateTimeField(auto_now_add=True)
    article_date = models.DateTimeField()

