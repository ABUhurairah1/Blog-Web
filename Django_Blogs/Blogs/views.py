from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm,BlogForm,CommentForm
from datetime import datetime
from .models import Blog,Comments
from django.http import JsonResponse

# Create your views here.
def Home(request):
    blogs = Blog.objects.all()
    context = {'blogs':blogs}
    return render(request,'index.html',context)

def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = request.user
        user = authenticate(user,username = username , password = password)
        if user != None:
            login(request,user)

        return redirect('Home')

    return render(request,'login_page.html')

def Sign_in(request):    
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Login')

    else : 
        form = SignUpForm()

    context = {'form':form}
    return render(request,'Sign_up.html',context)

def Logout(request):
    logout(request)
    return redirect('Home')



def Blog_page(request,blog_id):
    blog = Blog.objects.get(id = blog_id)
    comments = Comments.objects.filter(blog=blog)
    user = request.user
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            blog_comment = form.save(commit=False)
            blog_comment.host = user
            blog_comment.blog = blog
            blog_comment.created = datetime.now()
            blog_comment.save()

            comment_data = [
                {
                    'text': comment.text,
                    'host': comment.host.username,
                    'id': comment.id,
                    'created': comment.created.strftime('%Y-%m-%d %H:%M:%S'),
                    'is_host': comment.host == user
                }
                for comment in comments
            ]
            return JsonResponse({'status': 'Save', 'comment_data': comment_data})
        else :
            return JsonResponse({'status': 0})
    else : 
        form = CommentForm()

    context = {'blog':blog,'form':form,'comments':comments}
    return render(request,'blog_page.html',context)

def Delete_comment(request,comment_id):
    comment = Comments.objects.get(id = comment_id)
    if request.method == 'POST':
        comment.delete()
        return redirect('Home')
    context = {'comment' : comment}
    return render(request,'delete_blog.html',context)

@login_required(login_url='Login')
def Add_blog(request):

    user = request.user
    if request.method == 'POST':
        form = BlogForm(request.POST,request.FILES)
        if form.is_valid():
            blog_form = form.save(commit=False)
            blog_form.host = user
            blog_form.created = datetime.now()
            blog_form.save()
            return redirect('Home')
    else: 
        form = BlogForm()


    context = {'form':form}
    return render(request,'add_blog.html',context)

def Update_blog(request,blog_id):
    blog = Blog.objects.get(id = blog_id)
    if request.method == 'POST':
        form = BlogForm(request.POST,request.FILES,instance=blog)
        if form.is_valid():
           form.save()
        return redirect('Home')
    else: 
        form = BlogForm(instance=blog)


    context = {'form':form}
    return render(request,'add_blog.html',context)

def Delete_blog(request,blog_id):
    page = "Delete-Blog"
    blog = Blog.objects.get(id = blog_id)
    if request.method == 'POST':
        blog.delete()
        return redirect('Home')

    context = {'blog' : blog,'page':page}
    return render(request,'delete_blog.html',context)

