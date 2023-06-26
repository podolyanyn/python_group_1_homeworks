from django.shortcuts import render


def index(request):
    notes = [
        {'title': 'Місяць 1', 'content': 'Початок курсів був доволі лячним, але не таким страшним як я очікував.'},
        {'title': 'Місяць 2', 'content':
            'Відчуваю певну важкість при виконанні курсів, однак все ще непогано справляюсь!'},
        {'title': 'Місяць 3', 'content': 'Все ще важко, але ми не здаємось! Хоча деколи втрачаю наснагу...'},
    ]
    return render(request, 'notes/index.html', {'notes': notes})
