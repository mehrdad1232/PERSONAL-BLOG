from django.db import models

class SocialLinks(models.Model):
    platform = models.CharField(max_length=50)
    link = models.URLField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = 'sociallinks'
    
    def __str__(self):
        return self.platform
