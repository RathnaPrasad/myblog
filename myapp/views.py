from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from myapp.models import Blog,Comment
from django.views.generic.edit import CreateView,UpdateView
from myapp.forms import CommentForm
from django.urls import reverse


# Create your views here.
def index(request):
    # process data from db (OOPS)
    blogs = Blog.objects.all()
    context = {'blogs':blogs}
    return render(request,'index.html',context)


def detail(request,pk):
    blog = Blog.objects.get(pk = pk)
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CommentForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            comment = form.cleaned_data['comment']
            print(comment)
            obj = Comment(blog = blog,comment = comment)
            obj.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('myapp:detail',kwargs = {'pk':pk}))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CommentForm()

    context = {'blog':blog,'form': form}

    return render(request, 'detail.html', context)

class CreateBlog(CreateView):
    model = Blog
    fields = ['title','description','image']
    template_name = 'create.html'
    success_url = '/'

class UpdateBlog(UpdateView):
    model = Blog
    fields = ['title','description','image']
    template_name = 'create.html'
    success_url = '/'

def like(request):
    #print(request)
    blog_id=request.GET.get('blog_id')
    likes=request.GET.get('likes')
    #process
    blog = Blog.objects.get(id=blog_id)
    blog.likes +=1
    blog.save()
    data={'likes':blog.likes}
    return JsonResponse(data)


    
    
