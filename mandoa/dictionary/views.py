from django.shortcuts import render
from django.http import HttpResponse
from .models import Dictionary #, Phrasebook
from .forms import SearchFormRus
from .forms import SearchFormEng


def index(request):
    form = SearchFormRus(request.POST or None)
    if form.is_valid():
        data_form = form.cleaned_data
        if data_form.get('lang') == 'mandoa':
            words = Dictionary.objects.filter(mandoa__contains=data_form.get("ptrn"))
        elif data_form.get('lang') == 'russian':
            words = Dictionary.objects.filter(russian__contains=data_form.get("ptrn"))
    else:
        words = Dictionary.objects.all()

    context = {'form': form, "words": words}
    return render(request, 'dictionary/index.html', context)


def index_eng(request):

    form = SearchFormEng(request.POST or None)
    if form.is_valid():
        data_form = form.cleaned_data
        if data_form.get('lang') == 'mandoa':
            words = Dictionary.objects.filter(mandoa__contains=data_form.get("ptrn"))
        elif data_form.get('lang') == 'english':
            words = Dictionary.objects.filter(english__contains=data_form.get("ptrn"))
    else:
        words = Dictionary.objects.all()

    context = {'form': form, "words": words}
    return render(request, 'dictionary/index_eng.html', context)


'''
def phrasebook(request):
    phrases = Phrasebook.objects.all()
    context = {"phrases": phrases}
    return render(request, 'dictionary/phrasebook.html', context)


def phrasebook_eng(request):
    return render(request, 'dictionary/phrasebook_eng.html')
'''


def grammar_rules(request):
    return render(request, 'dictionary/grammar_rules.html')


def grammar_rules_eng(request):
    return render(request, 'dictionary/grammar_rules_eng.html')


def about_us(request):
    return render(request, 'dictionary/about_us.html')


def about_us_eng(request):
    return render(request, 'dictionary/about_us_eng.html')

