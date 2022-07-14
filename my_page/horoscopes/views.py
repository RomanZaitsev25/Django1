# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, \
    HttpResponseRedirect
from django.template.loader import render_to_string
from django.urls import reverse

# Create your views here.
zodiac_dict = {
    'aries': 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
    'taurus': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
    'gemini': 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
    'cancer': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
    'leo': ' Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).',
    'virgo': 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
    'libra': 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
    'scorpio': 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
    'sagittarius': 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
    'capricorn': 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
    'aquarius': 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
    'pisces': 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).',
}


def index(request):
    zodiacs = list(zodiac_dict)
    li_elements = ''
    for sign in zodiacs:
        redirect_path = reverse('horoscope-name', args=[sign, ])
        li_elements += f"<li><a href='{redirect_path}'>{sign.title()}</a></li>"
    response = f'''
    <ol>
        {li_elements}
    </ol>
    '''
    return HttpResponse(response)
    # response = '<br>'.join(zodiacs)


# def get_info_about_sign_zodiac(request, sign_zodiac: str):
#     description = zodiac_dict.get(sign_zodiac, None)
#     # response = render_to_string('horoscope/info_zodiac.html')
#     if description:
#         return HttpResponse(f'<h2>{description}</h2>')
#     # if sign_zodiac == 'leo':
#     #     return HttpResponse(
#     #         'Лев-пятый знак зодиака, солнце(с 23 июля по 21 августа)')
#     # if sign_zodiac == 'scorpio':
#     #     return HttpResponse(
#     #         'Скорпион-восьмой знак зодиака, солнце(с 24 октября по 22 ноября)')
#     # if sign_zodiac == 'taurus':
#     #     return HttpResponse(
#     #         'Овен-первый знак зодиака, солнце(с 21 марта по 20 апреля)')
#     else:
#         return HttpResponseNotFound(f'Неизвестный знак зодиака-{sign_zodiac}')

def get_info_about_sign_zodiac(request, sign_zodiac: str):
    # response = render_to_string('horoscopes/info_zodiac.html')
    # return HttpResponse(response)
    return render(request, 'horoscopes/info_zodiac.html')


def get_info_about_sign_zodiac_by_number(request, sign_zodiac: int):
    zodiacs = list(zodiac_dict)
    if sign_zodiac > len(zodiacs):
        return HttpResponseNotFound(
            f'Неправильный порядковый номер знака зодиака - {sign_zodiac}')
    name_zodiac = zodiacs[sign_zodiac - 1]
    redirect_url = reverse('horoscope-name', args=(name_zodiac,))
    return HttpResponseRedirect(redirect_url)
    # return HttpResponseRedirect(f'/horoscope/{name_zodiac}')
