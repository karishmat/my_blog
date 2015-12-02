from django.shortcuts import render,render_to_response,RequestContext,HttpResponseRedirect
from .forms import SignUpForm,SignUp,CommentForm,PostForm
from .models import Post,Comment
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def home(request):
    form=SignUpForm(request.POST or None)   #form attributes store in form variable when click on submit button
    print form
    if form.is_valid():
        save_it=form.save(commit=False)
        save_it.save()
        messages.success(request,'Thank you for joining')
        return HttpResponseRedirect('/blog/')
    else:
        form=SignUpForm()  #display empty form
    return render_to_response("signup.html",
                              locals(),
                              context_instance=RequestContext(request))

def userdata(request):
    users=SignUp.objects.all()
    # Publisher.objects.filter(id=52).update(name='Apress Publishing')----------filter and update in same line
    print users
    return render_to_response('signup.html',{'users':users})
    # return render_to_response("signup.html",{'post':Post.objects.get(id=post_id)})

    #post_id will be taken from function parametr

    #return render_to_response('/blog/%s' % post_id)----------this is dynamic routing

def sendpost(request):
    recposts=Post.objects.filter()[0:5]
    form=PostForm(request.POST or None)
    if form.is_valid():
        title=form.cleaned_data['title']
        body=form.cleaned_data['body']
        user=form.cleaned_data['user']
        post=Post(title=title,body=body,user=user)
        post.save()
        print "post save"
        return HttpResponseRedirect('/blog/')
    else:
        form=PostForm()  #display empty form
    #return render_to_response("sendpost.html",
     #                         locals(),
      #                        context_instance=RequestContext(request))
    return render_to_response("sendpost.html", {'recposts': recposts, 'form': form}, context_instance=RequestContext(request))

def like(request, postid):
    post= Post.objects.get(id=int(postid))
    post.like = post.like + 1
    post.save()
    posts=Post.objects.all()
    return render_to_response("blog.html", {'object_list': posts}, context_instance=RequestContext(request))


def comment(request, pk):
    form=CommentForm(request.POST or None)
    post=Post.objects.get(id=pk)
    recposts=Post.objects.filter()[0:5]
    comments=Comment.objects.filter(post_id=pk)
    count=Comment.objects.filter(post_id=pk).count()

    if form.is_valid():
        print "after valid"
        comnt= form.cleaned_data['comment']
        comnter= form.cleaned_data['commenter']
        email= form.cleaned_data['email']
        c=Comment(comment=comnt, post_id=pk, commenter=comnter, email=email)
        c.save()
        return HttpResponseRedirect('')
    else:
        form=CommentForm()  #display empty form
    return render_to_response("post.html", {'post': post, 'form': form, 'comments': comments,'count': count,'recposts': recposts}, context_instance=RequestContext(request))

def search(request):
    if request.method == 'POST':
        text=(request.POST['search'])
        search=Post.objects.filter(body__contains=text)
        if search:
            return render_to_response("blog.html", {'object_list': search}, context_instance=RequestContext(request))
        else:
            msg="Requested post not found"
            return render_to_response("blog.html", {'msg': msg}, context_instance=RequestContext(request))

