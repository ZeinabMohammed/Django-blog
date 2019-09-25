from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from .models import *
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView,TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# from .forms import CommentForm
from django.http import HttpResponseRedirect
from .forms import CommentForm
from blog.models import Post

def comment_posted(request):
    if request.POST.get(['c']):
        comment_id, post_id  = request.GET['c'].split( ':' )
        post = Post.objects.get( pk=post_id )

        if post:
            return HttpResponseRedirect( post.get_absolute_url() )

    return HttpResponseRedirect( "/" )

def home(request):
	context={
	'posts':Post.objects.all()
	}
	return render(request, 'blog/home.html', context)


class PostListView(ListView):
	model = Post
	template_name = 'blog/home.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']
	paginate_by = 7

class UserPostListView(ListView):
	model = Post
	template_name = 'blog/user_post.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']
	paginate_by = 7
	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Post.objects.filter(author = user).order_by('-date_posted')


def add_comment(request, pk):
	
	post = get_object_or_404(Post, pk=pk)

	if request.method == 'POST':
		form = CommentForm(request.POST, None)
		if form.is_valid:

			comment = form.save(commit=False)
			comment.post = post
			comment.user=request.user
			comment.save()
			return redirect(request.META.get('HTTP_REFERER','post-detail.html'))
	
	form = CommentForm()

	template = 'blog/comment_form.html'
	context  = {'form': form,
					'post':post}
	return HttpResponseRedirect("")
class PostDetailView(DetailView):
	model = Post
	
	template_name = 'blog/post_detail.html'
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['form'] = CommentForm

		return context

	def post(self, request, *args, **kwargs):
		form = CommentForm(request.POST)

		if form.is_valid():
			comment = form.save(commit=False)
			comment.user = request.user
			comment.post = self.get_object()
			comment.save()
			self.object = self.get_object()
			context = context = super().get_context_data(**kwargs)
			context['form'] = CommentForm

			return self.render_to_response(context=context)

		else:
			self.object = self.get_object()
			context = super().get_context_data(**kwargs)
			context['form'] = CommentForm

			return self.render_to_response(context=context)


class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['title', 'content']
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	# def test_func(self):
	# 	post= self.get_object(pk=pk)
	# 	if request.user == post.author:
	# 		return True
	# 	return False
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['title', 'content']
	def test_func(self):
		post= self.get_object()
		if self.request.user == post.author:
			return True
		return False

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
	model = Post
	success_url = '/'
	def test_func(self):
		post= self.get_object()
		if self.request.user == post.author:
			return True
		return False
def about(request):
	return render(request, 'blog/about.html', {"title": 'About'})

class Postdetail(DetailView):
	model = Post
	template_name = 'blog/post_detail.html'

	def get(self, request, **kwargs):
		form = CommentForm()
		return render(request, self.template_name, {"form": form,})

	def post(self, request, **kwargs):
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.post = post
			comment.user=request.user
			comment.save()
		return render(request, self.template_name, {"form": form})
# def comment_posted(request):
# 	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
# class CommentCreateView(LoginRequiredMixin, CreateView):
# 	model = Comment
# 	success_url= reverse_lazy("blog:post-detail")
# 	fields = [ 'content']
# 	def form_valid(self, form):
# 		form.instance.user = self.request.user

# 		return super().form_valid(form)

# 	def test_func(self):
# 		comment= self.get_object()
# 		if request.user == comment.user:
# 			return True
# 		return False
# 	