from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse, Http404
from .models import Todo
# Create your views here.
from django.views.generic import DeleteView,  UpdateView


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


    
@login_required
def index(request):
	# request.user = todo.user
	# todo = Todo.objects.all()[:10]

	todo = Todo.objects.filter(user=request.user.id)
	context = {
		'todo':todo
	}
	template='index.html'
	return render(request, 'index.html', context)
	
def details(request, pk):
	todo = Todo.objects.get(pk=pk)
	context = {
		'todo':todo
	}
	template='details.html'
	return render(request, 'details.html', context)

def add(request):
	if not request.user.is_authenticated():
		raise Http404
	if(request.method == 'POST'):

		title = request.POST['title']
		priority = request.POST.get('priority', 'select')
		# The get method used above for choices is of the general form 
		#my_var = dict.get(<key>, <default>)
		text = request.POST['text']

		todo = Todo(title=title, priority=priority, text=text)
		todo.user = request.user
		todo.save()
		return redirect ('/')

	else:
		return render(request, 'add.html')

class edit(UpdateView):
    model = Todo
    fields= ['title','priority','text']
    def get_success_url(self):
         return reverse('details', kwargs={
             'pk': self.object.pk,
         })

class delete(DeleteView):
    model = Todo
    success_url = '/'