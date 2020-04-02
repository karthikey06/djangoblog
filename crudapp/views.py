from django.shortcuts import render,redirect,get_object_or_404
from .models import Post
from rest_framework import viewsets
from .forms import PostForm
from .serializers import PostSerializer
from django.views.generic import ListView,DetailView



#home view for the posts,to see in the list view
class IndexView(ListView):
	template_name = 'crudapp/index.html'
	context_object_name = 'post_list'
	def get_queryset(self):
		return Post.objects.all()

#DETAIL VIEW TO THE POST
class PostDetailView(DetailView):
	model = Post
	template_name = 'crudapp/post-detail.html'

#new post views(create new post)
def postview(request):
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('index')
	form = PostForm()
	return render(request,'crudapp/post.html',{'form':form})

#edit a post
def edit(request,pk,template_name='crudapp/edit.html'):
	post = get_object_or_404(Post,pk=pk)
	form = PostForm(request.POST or None, instance =post)
	if form.is_valid():
		form.save()
		return redirect('index')
	return render(request,template_name,{'form':form})

#delete a post
def delete(request,pk,template_name='crudapp/delete.html'):
	post = get_object_or_404(Post,pk=pk)
	if request.method == "POST":
		post.delete()
		return redirect('index')
	return render(request,template_name,{'object':post})


#serializers method 
class PostView(viewsets.ModelViewSet):       
	serializer_class = PostSerializer          
	queryset = Post.objects.all() 


