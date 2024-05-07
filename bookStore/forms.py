from django.forms import ModelForm
from .models import BokkStore

class BookForm(ModelForm):
    class Meta:
        model = BokkStore
        fields = ['title', 'desc', 'rate', 'views', 'published']
        