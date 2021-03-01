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
    # lists = eval(model).objects.all()

    lists = eval(model).objects.all()
    print(lists)
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
        else:
            entity = eval(model).objects.get(pk=id)
            form = eval(modelForm)(instance=entity)

            print(entity, form)
        return render(request, "adminlte/pages/partial/create.html", {'form': form, 'slug': slug})
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


def province_list(request):
    province_list = Province.objects.all()
    header = 'Province'
    context = {'province_list': province_list, 'header': header}
    return render(request, "adminlte/pages/list.html", context)


def province_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = ProvinceForm()
        else:
            province = Province.objects.get(pk=id)
            form = ProvinceForm(instance=province)
        return render(request, "primary_master/province_form.htm", {'form': form})
    else:
        if id == 0:
            form = ProvinceForm(request.POST)
        else:
            province = Province.objects.get(pk=id)
            form = ProvinceForm(request.POST, instance=province)
        if form.is_valid():
            form.save()
        return redirect('../province/list')


def province_delete(request, id):
    province = Province.objects.get(pk=id)
    province.delete()
    return redirect('../province/list')

# View for District


def district_list(request):
    district_list = District.objects.all()
    context = {'district_list': district_list}
    return render(request, "primary_master/district_list.htm", context)


def district_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = DistrictForm()
        else:
            district = District.objects.get(pk=id)
            form = DistrictForm(instance=district)
        return render(request, "primary_master/district_form.htm", {'form': form})
    else:
        if id == 0:
            form = DistrictForm(request.POST)
        else:
            district = District.objects.get(pk=id)
            form = DistrictForm(request.POST, instance=district)
        if form.is_valid():
            form.save()
        return redirect('../district/list')


def district_delete(request, id):
    district = District.objects.get(pk=id)
    district.delete()
    return redirect('../district/list')

# View for Locallevel


def locallevel_list(request):
    locallevel_list = LocalLevel.objects.all()
    context = {'locallevel_list': locallevel_list}
    return render(request, "primary_master/locallevel_list.htm", context)


def locallevel_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = LocalLevelForm()
        else:
            locallevel = LocalLevel.objects.get(pk=id)
            form = LocalLevelForm(instance=locallevel)
        return render(request, "primary_master/locallevel_form.htm", {'form': form})
    else:
        if id == 0:
            form = LocalLevelForm(request.POST)
        else:
            locallevel = LocalLevel.objects.get(pk=id)
            form = LocalLevelForm(request.POST, instance=locallevel)
        if form.is_valid():
            form.save()
        return redirect('../local_level/list')


def locallevel_delete(request, id):
    locallevel = LocalLevel.objects.get(pk=id)
    locallevel.delete()
    return redirect('../local_level/list')

# View for LocalLevel Type


def locallevel_type_list(request):
    locallevel_type_list = LocalLevelType.objects.all()
    context = {'locallevel_type_list': locallevel_type_list}
    return render(request, "primary_master/locallevel_type_list.htm", context)


def locallevel_type_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = LocalLevelTypeForm()
        else:
            locallevel_type = LocalLevelType.objects.get(pk=id)
            form = LocalLevelTypeForm(instance=locallevel_type)
        return render(request, "primary_master/locallevel_type_form.htm", {'form': form})
    else:
        if id == 0:
            form = LocalLevelTypeForm(request.POST)
        else:
            locallevel_type = LocalLevelType.objects.get(pk=id)
            form = LocalLevelTypeForm(request.POST, instance=locallevel_type)
        if form.is_valid():
            form.save()
        return redirect('../local_level_type/list')


def locallevel_type_delete(request, id):
    locallevel_type = LocalLevelType.objects.get(pk=id)
    locallevel_type.delete()
    return redirect('../local_level_type/list')

# View for FiscalYear


def fiscalyear_list(request):
    fiscalyear_list = FiscalYear.objects.all()
    context = {'fiscalyear_list': fiscalyear_list}
    return render(request, "primary_master/fiscalyear_list.htm", context)


def fiscalyear_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = FiscalYearForm()
        else:
            fiscalyear = FiscalYear.objects.get(pk=id)
            form = FiscalYearForm(instance=fiscalyear)
        return render(request, "primary_master/fiscalyear_form.htm", {'form': form})
    else:
        if id == 0:
            form = FiscalYearForm(request.POST)
            print(request.POST)
        else:
            fiscalyear = FiscalYear.objects.get(pk=id)
            form = FiscalYearForm(request.POST, instance=fiscalyear)
        if form.is_valid():
            form.save()
        return redirect('../fiscal_year/list')


def fiscalyear_delete(request, id):
    fiscalyear = FiscalYear.objects.get(pk=id)
    fiscalyear.delete()
    return redirect('../fiscal_year/list')

# View for NepaliMonth


def nepalimonth_list(request):
    nepalimonth_list = NepaliMonth.objects.all()
    context = {'nepalimonth_list': nepalimonth_list}
    return render(request, "primary_master/nepalimonth_list.htm", context)


def nepalimonth_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = NepaliMonthForm()
        else:
            nepalimonth = NepaliMonth.objects.get(pk=id)
            form = NepaliMonthForm(instance=nepalimonth)
        return render(request, "primary_master/nepalimonth_form.htm", {'form': form})
    else:
        if id == 0:
            form = NepaliMonthForm(request.POST)
        else:
            nepalimonth = NepaliMonth.objects.get(pk=id)
            form = NepaliMonthForm(request.POST, instance=nepalimonth)
        if form.is_valid():
            form.save()
        return redirect('../nepali_month/list')


def nepalimonth_delete(request, id):
    nepalimonth = NepaliMonth.objects.get(pk=id)
    nepalimonth.delete()
    return redirect('../nepali_month/list')

# View for Gender


def gender_list(request):
    gender_list = Gender.objects.all()
    context = {'gender_list': gender_list}
    return render(request, "primary_master/gender_list.htm", context)


def gender_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = GenderForm()
        else:
            gender = Gender.objects.get(pk=id)
            form = GenderForm(instance=gender)
        return render(request, "primary_master/gender_form.htm", {'form': form})
    else:
        if id == 0:
            form = GenderForm(request.POST)
        else:
            gender = Gender.objects.get(pk=id)
            form = GenderForm(request.POST, instance=gender)
        if form.is_valid():
            form.save()
        return redirect('../gender/list')


def gender_delete(request, id):
    gender = Gender.objects.get(pk=id)
    gender.delete()
    return redirect('../gender/list')


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
