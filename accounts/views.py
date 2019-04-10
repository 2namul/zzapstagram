from django.shortcuts import render
from .forms import RegisterForm

def register(request):

    if request.method == 'POST': # 회원가입 정보가 서버로 전달됐다. form 태그의 메소드가 post->서버로 자료를 전달하는 메서드
        user_form = RegisterForm(request.POST)#유효성검사실행
        if user_form.is_valid():
            new_user = user_form.save(commit=False) #폼 객체의 지정된 모델 확인 후 객체 만듦,commit=False 이므로 DB가 아닌 메모리에만 저장
            new_user.set_password(user_form.cleaned_data['password'])#password 암호화
            new_user.save()#실제 db에 저장
            return render(request, 'registration/register_done.html', {'new_user':new_user})#register_done템플릿을 랜더링해 보여줌
        #이상이 없으면 데이터 베이스에 저장
    else:
        user_form = RegisterForm()

    return render(request, 'registration/register.html',{'form':user_form})