from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,UpdateView,ListView,DetailView,View,TemplateView,DeleteView
from noting.models import notepad
from django.urls import reverse,reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid

class note_list(LoginRequiredMixin,ListView): 
	context_object_name='notes'
	model= notepad
	
	queryset=notepad.objects.order_by('-saving_date')
	template_name='noting/note_list.html'
    
@login_required
def note_detail(request,slug):
	note=notepad.objects.get(slug=slug)
	return render(request,'noting/note_details.html',context={'note':note})

class edit_blog(LoginRequiredMixin,UpdateView):
		model=notepad
		fields=['note_title','note_content']
		template_name='noting/edit_note.html'
		def get_success_url(self, **kwargs):
			return reverse_lazy('noting:note_detail',kwargs={'slug':self.object.slug})
			#return HttpResponseRedirect(reverse('index'))
			



class CreateNote(LoginRequiredMixin,CreateView):
			
		model=notepad	
		template_name='noting/create_note.html'
		fields=['note_title','note_content','note_image']

		def form_valid(self,form):
			note_obj=form.save(commit=False)
			note_obj.author=self.request.user
			title=note_obj.note_title
			note_obj.slug=title.replace(" ","-")+"-"+str(uuid.uuid4())
			note_obj.save()
			return HttpResponseRedirect(reverse('index'))




# Create your views here.
