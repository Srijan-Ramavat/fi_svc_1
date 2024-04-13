from django.shortcuts import render, redirect
from .forms import TransactionForm
from .models import Transaction
from django.db import models
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TransactionSerializer



__all__ = ['input_transaction','insights', 'insights_detail', 'create_transaction']


def input_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('insights')
    else:
        form = TransactionForm()
    return render(request, 'finance/input_transaction.html', {'form': form})


def insights(request):
    categories = Transaction.objects.values_list('category', flat=True).distinct()
    transactions_per_category = Transaction.objects.values('category').annotate(total=models.Sum('amount'))
    context = {
        'categories': categories,
        'transactions_per_category': transactions_per_category,
    }
    return render(request, 'finance/insights.html', context)


@api_view(['GET'])
def insights_detail(request):
    categories = Transaction.objects.values_list('category', flat=True).distinct()
    transactions_per_category = Transaction.objects.values('category').annotate(total=models.Sum('amount'))
    date_wise_spends_per_category = Transaction.objects.values('date', 'category').annotate(total=models.Sum('amount')).order_by('date', 'category')
    data = {
        'categories': categories,
        'transactions_per_category': transactions_per_category,
        'date_wise_spends_per_category': date_wise_spends_per_category
    }
    return Response(data, status=200)


@api_view(['Post'])
def create_transaction(request):
    if request.method == 'POST':
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("created", status=201)
        else:
            return Response("Error", status=400)
    else:
        return Response("Bad Request", status=400)