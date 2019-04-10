from django.contrib.auth.models import User
from django import forms


class RegisterForm(forms.ModelForm): #forms.ModelForm을 상속, Form 내부의 Meta class를 사용하면 기존에 있는 모델의 입력 폼을 쉽게 만들 수 있음.
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name','last_name', 'email']

    def clean_password2(self): #clean.. 유효성검사나 조작을 하고 싶을때 사용
        cd = self.cleaned_data#해당 필드의 값을 사용할때 꼭 cleaned data를 사용- 처리를 마친 값이기때문
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords not matched!')
        return cd['password2']