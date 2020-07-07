from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views import View

from .form import PaymentForm
from .models import Payment


def index(request):
    payments = Payment.objects.all()
    return render(request, 'payments/index.html', context={'payments': payments})


class PaymentCreate(View):
    form_model = PaymentForm
    template = 'payments/create_payment.html'

    def get(self, request):
        form = self.form_model()
        return render(request, self.template, context={'form': form})

    def post(self,request):
        bound_form = self.form_model(request.POST or None)

        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(reverse('index'))
        else:
            return render(request, self.template, context={'form': bound_form})


class PaymentUpdate(View):
    model = Payment
    template = 'payments/update.html'
    form_model = PaymentForm

    def get(self, request, id):
        payment = self.model.objects.get(id=id)
        bound_form = self.form_model(instance=payment)
        return render(request, self.template, context={'form': bound_form, 'payment': payment})

    def post(self, request, id):
        obj = self.model.objects.get(id=id)
        bound_form = self.form_model(request.POST, instance=obj)

        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(reverse('index'))
        else:
            return render(request, self.template, context={'form': bound_form, 'payment': obj})


class PaymentDelete(View):

    def get(self, request,id):
        payment = Payment.objects.get(id=id)
        return render(request, 'payments/delete.html', context={'payment': payment})

    def post(self, request, id):
        payment = Payment.objects.get(id=id)
        payment.delete()
        return redirect(reverse('index'))