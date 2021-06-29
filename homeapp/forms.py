from django import forms
from .models import Bucket,Article,Project

class BucketForm(forms.ModelForm):
    class Meta:
        model =  Bucket
        fields = ['image','notes']

class ProjectForm(forms.ModelForm):
    class Meta:
        model =  Project
        fields = ['image','notes']
        
        
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['heading','image','theory']
        widgets = {
            'heading':forms.TextInput(attrs={'class':'form-control'}),
            'image':forms.FileInput(attrs={'class':'form-control'}),
            'theory':forms.Textarea(attrs={'class':'form-control'}),
        }
        