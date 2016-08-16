from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Count
from persons.models import Person, Beruf, Todesart

DATA = {"status": "ok",
        "query": "api:graph",
        "timestamp": "2016-07-21T09:56:36.803Z",
        "items": "7",
        "title": "LASK4EVER",
        "subtitle": "This is just a test to check if everythin works as expected.",
        "legendx": "Club",
        "legendy": "# of Victories",
        "measuredObject": "Victories",
        "payload": [
            ["LASK", 10],
            ["Real Madrid", 4],
            ["Rapid Wien", 0],
            ["Blau Weiß Linz", -10]
        ]
        }

DATA_PIECHART = {
    "items": "2",
    "title": "LASK4EVER",
    "subtitle": "This is just a test.",
    "measuredObject": "# of Victories",
    "payload": [
        ["LASK", 9], ["Blau Weiß Linz", 1]
    ]
}


def death_by_profession(request):
    persons = Person.objects.values('beruf').annotate(total=Count('beruf_id')).order_by('-total')
    payload = []
    for x in persons:
        temp_beruf = Beruf.objects.get(id=int(x['beruf']))
        entry = [temp_beruf.name.title(), x['total']]
        payload.append(entry)

    data = {"items": len(Person.objects.all()),
            "title": "Gefallene nach Berufsgruppe",
            "subtitle": "Gefallene nach Berufsgruppe",
            "legendx": "Berufsgruppe",
            "legendy": "Anzahl der Gefallenen",
            "measuredObject": "Gefallene",
            "payload": payload
            }
    return JsonResponse(data)


def death_by_death(request):
    persons = Person.objects.values('todesart').annotate(total=Count('todesart_id')).order_by('-total')
    payload = []
    for x in persons:
        temp_death = Todesart.objects.get(id=int(x['todesart']))
        entry = [temp_death.name, x['total']]
        payload.append(entry)

    data = {"items": len(Person.objects.all()),
            "title": "Gefallene nach Todesart",
            "subtitle": "Gefallene nach Todesart",
            "legendx": "Todesart",
            "legendy": "Anzahl der Gefallenen",
            "measuredObject": "Gefallene",
            "payload": payload
            }
    return JsonResponse(data)


def barcharts_view(request):
    context = {"test": "test"}
    return render(request, 'charts/bar_charts.html', context)


def piecharts_view(request):
    context = {"test": "test"}
    return render(request, 'charts/pie_charts.html', context)


def test_json(request):
    data = DATA
    return JsonResponse(data)


def test_json_pie(request):
    data = DATA_PIECHART
    return JsonResponse(data)
