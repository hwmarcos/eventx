from django.shortcuts import render, get_object_or_404

from eventx.core.models import Speaker, Talk


def home(request):
    speakers = Speaker.objects.all()
    return render(request, 'index.html', {'speakers':speakers})

def speaker_detail(request, slug):
    speaker = get_object_or_404(Speaker, slug=slug)
    context = {
        'speaker':speaker
    }
    return render(request, 'core/speaker_detail.html', context)

def talk_list(request):

    teste1 = Talk.objects.filter(start__lt='12:00')
    teste2 = Talk.objects.filter(start__gte='12:00')

    context = {
        'morning_talks': teste1,
        'afternoon_talks': teste2,
    }
    return render(request, 'core/talk_list.html', context)