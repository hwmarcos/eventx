from django.shortcuts import render, get_object_or_404

from eventx.subcriptions.forms import SubscriptionForm
from eventx.subcriptions.mixins import EmailCreateView
from eventx.subcriptions.models import Subscription

new = EmailCreateView.as_view(
    model = Subscription,
    template_name = 'subscriptions/subscription_form.html',
    form_class = SubscriptionForm,
    email_subject = 'Confirmação de inscrição'
)

# detail = DetailView.as_view(model=Subscription)

def detail(request, pk):
    subscription = get_object_or_404(Subscription, pk=pk)
    return render(request, 'subscriptions/subscription_detail.html', {'subscription': subscription})