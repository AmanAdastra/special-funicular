from django import forms
from .models import Bucket,Article

class BucketForm(forms.ModelForm):
    class Meta:
        model =  Bucket
        fields = ['image','notes']
        
        
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['heading','image','theory']
        