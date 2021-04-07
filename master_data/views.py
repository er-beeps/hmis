from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest, JsonResponse
from django.shortcuts import redirect, render
from django.template import RequestContext
from django.template.defaulttags import register
from .filters import *
from .forms import *
from .models import *
from pyexcel_xlsx import get_data


global master_models
master_models = ['Province', 'District', 'LocalLevel',
                 'LocalLevelType', 'FiscalYear', 'NepaliMonth', 'Gender']


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
    # pass page header name
    header = model

    # if filter is present
    filterClass = model+'Filter'
    filterFields = eval(filterClass)(
        request.GET, queryset=eval(model).objects.all())

    if model in master_models:
        upload_button = True
    else:
        upload_button = False

    context = {'header': header, 'slug': slug,
               'filterFields': filterFields, 'upload_button': upload_button}
    return render(request, "adminlte/pages/list.html", context)


# Render List Operation partial view
@login_required(login_url="login/")
def filter_crud_list(request, slug):
    # get model name from slug
    model = underscore_to_camelcase(slug)
    # buid form from model
    modelForm = model+'Form'
    # get columns name and label  for list operation
    columns = eval(modelForm)._meta.fields
    labels = eval(modelForm)._meta.labels
    # get all data from table
    lists = eval(model).objects.all()
    # for filter
    if request.GET is not None:
        # if filter is present
        filterClass = model+'Filter'
        filteredLists = eval(filterClass)(request.GET, queryset=lists)
        lists = filteredLists

    context = {'columns': columns, 'labels': labels,
               'lists': lists, 'slug': slug}
    return render(request, "adminlte/pages/partial/datatable.html", context)

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
            return render(request, "adminlte/pages/partial/edit.html", {'form': form, 'slug': slug, 'entry': entity})
    else:
        message = ''
        if id == 0:
            form = eval(modelForm)(request.POST)
        else:
            entity = eval(model).objects.get(pk=id)
            form = eval(modelForm)(request.POST, instance=entity)

        if form.is_valid():
            form.save()
            if id == 0:
                message = 'The item has been added successfully !'
            else:
                message = 'The item has been modified successfully !'

        return JsonResponse({'message': message, 'slug': slug})


@login_required(login_url="login/")
def crud_delete(request, slug, id):
    model = underscore_to_camelcase(slug)
    entity = eval(model).objects.get(pk=id)
    delete_status = entity.delete()
    if(delete_status):
        status = 'success'
        value = 1
    else:
        status = 'error'
        value = 0
    return JsonResponse({'status': status, 'value': value, 'slug': slug})

# file upload


def upload(request, slug):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():
            upload_file = request.FILES['file']
            data = get_data(upload_file)
            for collection in data.items():
                columns = collection[1][0]
                for item in collection[1]:
                    print(item)
        else:
            return HttpResponseBadRequest()
    else:
        form = UploadFileForm()

    context = {'slug': slug}
    return render(request, 'adminlte/pages/partial/upload.html', context)


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
