from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import FormView
from django.views.generic.detail import SingleObjectMixin

from .forms import ItemForm, ExistingListItemForm, NewListForm
from .models import Item, List

User = get_user_model()


class HomePageView(FormView):
    template_name = 'home.html'
    form_class = ItemForm


def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    form = ExistingListItemForm(for_list=list_)
    if request.method == 'POST':
        form = ExistingListItemForm(for_list=list_, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(list_)
    return render(request, 'list.html', {'list': list_, "form": form})


class ViewAndAddToList(CreateView, SingleObjectMixin):
    model = List
    template_name = 'list.html'
    form_class = ExistingListItemForm

    def get_form(self, form_class=None):
        if not form_class:
            form_class = self.get_form_class()
        self.object = self.get_object()
        return form_class(for_list=self.object, data=self.request.POST)


class NewListView(CreateView, HomePageView):
    form_class = NewListForm

    def form_valid(self, form):
        list_ = form.save(owner=self.request.user)
        return redirect(list_)


def new_list(request):
    form = NewListForm(data=request.POST)
    if form.is_valid():
        list_ = form.save(owner=request.user)
        return redirect(list_)
    return render(request, 'home.html', {'form': form})


def my_lists(request, email):
    owner = User.objects.get(email=email)
    return render(request, 'my_lists.html', {'owner': owner})


def share_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    if request.POST.get('email'):
        list_.shared_with.add(request.POST['email'])
    return redirect(list_)
