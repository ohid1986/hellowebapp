from django.forms import ModelForm
from collection.models import Thing

# create Thing form
class ThingForm(ModelForm):
    
    class Meta:
        model = Thing
        fields = ('name', 'description', )