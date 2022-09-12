from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db import connection
from .models import Blog


# Create your views here.
# def home(request):
#     return HttpResponse('<h1>hello world</h1>')

# def home(request):
#     return render(request,'blogapp/home.html')

def about(request):
    return HttpResponse('<h1>Welcome to about page</h1>')

def home(request):
    # cursor=connection.cursor()
    # cursor.execute('select * from posts where softdelete=0')

    # columns = [col[0] for col in cursor.description]
    # posts =  [
    #     dict(zip(columns, row))
    #     for row in cursor.fetchall()
    # ]
    # posts=Blog.objects.all()
    posts=Blog.objects.filter(softDelete=0)
    print(posts)

    context={
        'keyposts':posts
    }

    return render(request,'blogapp/home.html',context)
def create(request):
    return render(request,'blogapp/form.html')

def insert(request):
    title = request.POST['blogTitle']
    content = request.POST['content']

    # cursor = connection.cursor(cursor=cursors.DictCursor)
    # cursor.execute("INSERT INTO posts (`title`,`content`) VALUES ( %s, %s );", (title, content))
    # cursor = connection.cursor()
    # cursor.execute("SELECT * from posts where softdelete = 0")

    blog=Blog(title=title,content=content)
    blog.save()
    return redirect('/blog/home')

def edit(request,pk):
    # cursor=connection.cursor()
    # cursor.execute(f"select * from posts where softdelete=0 and id={pk}")
    # # result=cursor.fetchone()

    # columns = [col[0] for col in cursor.description]
    # posts =  [
    #     dict(zip(columns, row))
    #     for row in cursor.fetchall()
    # ]
    posts=Blog.objects.get(id=pk)
    context={
        'keyposts':posts, #post[0] because we need only the dictionary and not list of dictionary
    }

    # print(result)
    # print(pk)
    print(context)
    return render(request,'blogapp/editForm.html',context)

# data 
def update(request):
    id=request.POST['id']
    title=request.POST['blogTitle']
    content=request.POST['content']
    # cursor=connection.cursor()
    # cursor.execute('update posts set title=%s,content=%s where id=%s',(title,content,id))
    blog=Blog.objects.get(id=id)
    blog.title=title
    blog.content=content
    blog.save()
    return redirect('/blog/home')


def delete(request,pk):
    # cursor=connection.cursor()
    # cursor.execute(f'update posts set softdelete=1 where id={pk}')
    blog=Blog.objects.get(id=pk)
    blog.softDelete=1
    blog.save()
    return redirect('/blog/home')
