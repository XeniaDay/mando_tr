from django import forms


class SearchFormRus(forms.Form):
    choices_lang = [
        ('mandoa', "Мандо'а"),
        ('russian', 'Русский'),
    ]
    lang = forms.ChoiceField(label='Выбрать язык',
                             choices=choices_lang,
                             widget=forms.RadioSelect(choices=choices_lang,
                                                      attrs={"class":"radioselect"}),
                             initial='mandoa')
    ptrn = forms.CharField(max_length=100,
                           label="",
                           required=False,
                           widget=forms.TextInput(attrs={"class":"searcharea"}))


class SearchFormEng(forms.Form):
    choices_lang = [
        ('mandoa', "Mando'a"),
        ('english', 'English')
    ]
    lang = forms.ChoiceField(label='Choose language',
                             choices=choices_lang,
                             widget=forms.RadioSelect(choices=choices_lang,
                                                      attrs={"class":"radioselect"}),
                             initial='mandoa')
    ptrn = forms.CharField(max_length=100,
                           label="",
                           required=False,
                           widget=forms.TextInput(attrs={"class":"searcharea"}))