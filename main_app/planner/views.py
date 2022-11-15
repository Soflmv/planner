from django.shortcuts import render


def main(request):
    data = {
        'data': 'Hello!'
    }
    return render(request, 'planner/home.html', {'data': data})
