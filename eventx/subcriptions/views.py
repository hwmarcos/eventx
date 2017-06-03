from django.shortcuts import render

from eventx.subcriptions.forms import SubscriptionForm


def subscribe(request):
    context = {'form': SubscriptionForm()}
    return render(request, 'subscriptions/subscription_form.html', context)