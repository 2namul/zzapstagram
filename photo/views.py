from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Photo
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView

@login_required
def photo_list(request): #함수형 뷰는 기본매개변수를 request로 설정
    photos = Photo.objects.all() #목록으로 출력할 사진객체를 불러오기 ~objects.all로모든 사진을 불러옴
    return render(request,'photo/list.html', {'photos':photos})

class PhotoUploadView(LoginRequiredMixin, CreateView):
    model = Photo
    fields = ['photo','text']
    template_name = 'photo/upload.html' #실제 사용할 템플릿 설정

    def form_valid(self, form): #업로드 끝낸 후 이동할 페이지 호출
        form.instance.author_id = self.request.user.id #작성자 설정
        if form.is_valid():#입력된 값 검증
            form.instance.save()#이상 없을시 db에 저장
            return redirect('/')#그 후 메인페이지로
        else:
            return self.render_to_response({'form':form}) #이상 있을 시 내용을 그대로 페이지에 표시

class PhotoDeleteView(LoginRequiredMixin, DeleteView):
    model = Photo
    success_url = '/'
    template_name = 'photo/delete.html'

class PhotoUpdateView(LoginRequiredMixin, UpdateView):
    model = Photo
    fields = ['photo','text']
    template_name = 'photo/update.html'

class PhotoDetailView(LoginRequiredMixin, DetailView):
    model = Photo
    template_name = 'photo/detail.html'

