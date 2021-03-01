from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.template.defaulttags import register
from .models import *
from .forms import *


@login_required(login_url="login/")
def homepage(request):
    return render(request, 'layouts/dashboard.html')


@login_required(login_url="login/")
def redirect_to_dashboard(request):
    return redirect('/master/dashboard')


# List Operation
@login_required(login_url="login/")
def crud_list(request, slug):
    # get model name from slug
    model = underscore_to_camelcase(slug)
    # buid form from model
    modelForm = model+'Form'
    # get columns name and label  for list operation
    columns = eval(modelForm)._meta.fields
    labels = eval(modelForm)._meta.labels
    # get all data from table
    lists = eval(model).objects.all()
    # pass page header name
    header = model

    context = {'columns': columns, 'labels': labels, 'lists': lists,
               'header': header, 'slug': slug}
    return render(request, "adminlte/pages/list.html", context)

# Create or Update Operation
@login_required(login_url="login/")
def crud_create_or_update(request, slug, id=0):
    model = underscore_to_camelcase(slug)
    modelForm = model+'Form'
    if request.method == "GET":
        if id == 0:
            form = eval(modelForm)()
            return render(request, "adminlte/pages/partial/create.html", {'form': form, 'slug': slug})
        else:
            entity = eval(model).objects.get(pk=id)
            form = eval(modelForm)(instance=entity)
            return render(request, "adminlte/pages/partial/edit.html", {'form': form, 'slug': slug,'entry':entity})
    else:
        if id == 0:
            form = eval(modelForm)(request.POST)
        else:
            entity = eval(model).objects.get(pk=id)
            form = eval(modelForm)(request.POST, instance=entity)
        if form.is_valid():
            form.save()
        return redirect('crud_list', slug=slug)


@login_required(login_url="login/")
def crud_delete(request, slug, id):
    model = underscore_to_camelcase(slug)
    entity = eval(model).objects.get(pk=id)
    entity.delete()
    return redirect('crud_list', slug=slug)


def underscore_to_camelcase(value):
    output = ""
    first_word_passed = False
    for word in value.split("_"):
        if not word:
            output += "_"
            continue
        if first_word_passed:
            output += word.capitalize()
        else:
            output += word.capitalize()
        first_word_passed = True
    return output

# for getting column label
@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

# for getting value from db using column key
@register.filter
def get_item_value(item, column):
    value = 'item.'+column
    return eval(value)
