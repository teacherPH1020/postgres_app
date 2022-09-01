from django.forms import ModelForm
from .models import Metadata, Storage

class StorageForm(ModelForm):
    class Meta:
        model = Storage
        fields = "__all__" # ["cell" , "file", "access_date"]

class MetadataForm(ModelForm):
    class Meta:
        model = Metadata
        fields = ["info" , "cell_pk"]