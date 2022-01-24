from django.views.generic.edit import FormView
from search.form import PostSearchForm
from django.db.models import Q
from django.shortcuts import render 

class SearchFormView(FormView):
    form_class = PostSearchForm 
    template_name = 'search/sh.html'
    schWord='%s' % self.request.POST['search_word']

    post_list = Post.objects.filter( Q(title__icontains = schWord) | Q(description__icontains=schWord) | Q(content__icontains=schWord) ).distinct()

context={}

context['form'] = form

context['search_term'] = schWord

context['object_list'] = post_list
