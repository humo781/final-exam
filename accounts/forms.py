from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField(
        max_length=50,
        label='Foydalanuvchi emaili',
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)