from django import forms

class FormularioRegistroEmpleados(forms.Form):

    ZONA=(
        (1, 'COMIDAS'),
        (2, 'ADMINISTRACION'),
        (3, 'LOGISTICA'),
        (4, 'BODEGA'),
    )

    nombreEmpleado=forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control mb-3"}),
        max_length=25,
        required=True,
        label="Nombre"
    )
    funcionEmpleado=forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control mb-3"}),
        max_length=50,
        required=True,
        label="Funcion Empleado"
    )
    edadEmpleado=forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control mb-3"}),
        max_length=2,
        required=True,
        label="Edad Empleado"
    )
    correoEmpleado=forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control mb-3"}),
        required=True,
        label="Correo Empleado"
    )
    zonaEmpleado=forms.ChoiceField(
       widget=forms.Select(attrs={"class":"form-control mb-3"}),
       choices=ZONA,
       label="Zona Empleado"
    )

    