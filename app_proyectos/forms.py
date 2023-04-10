from django import forms

class CreacionProyectoForm(forms.Form):
    titulo = forms.CharField(max_length=30)
    tipologia = forms.CharField(max_length=30)
    superficie = forms.FloatField()
    plantas = forms.IntegerField()
    dormitorios = forms.IntegerField()
    baños = forms.IntegerField()

    

class BuscarProyectoForm(forms.Form):
    titulo = forms.CharField(max_length=30, required=False)
    tipologia = forms.CharField(max_length=30, required=False)
