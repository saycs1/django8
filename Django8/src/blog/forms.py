'''
Created on 2018. 9. 1.

@author: kgitbank404
'''
from django.forms.models import ModelForm
from .models import *

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields=['type', 'headline', 'content']
        
        def __init__(self, *args,**kwargs):
            super().__init__(self,*args,**kwargs)
            
            self.fields['type'].empty_label=None
            self.fields['type'].label='글 종류'