from django.shortcuts import render

def mgrammar(request):
    return render(request, 'mgrammar/grammar.html')


def mgrammar_eng(request):
    return render(request, 'mgrammar/grammar_eng.html')