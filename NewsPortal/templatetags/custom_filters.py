from django import template
from NewsPortal.config import CENS_WORDS, wordcensor, wordcensor_notisalpha

register = template.Library()

@register.filter()
def censor(value:str):
    if type(value) is str:   #try
        val = value.split()
        for i in range(len(val)):
            if not val[i].isalpha(): val[i] = wordcensor_notisalpha(val[i])
            if val[i] in CENS_WORDS:
                val[i] = wordcensor(val[i])
        return ' '.join(val)
    else:                   #except
        raise TypeError('Переменная должна быть типа str')




