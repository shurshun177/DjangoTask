from django.shortcuts import render
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.utils import timezone
from .models import Expense, Note
from .forms import ExpenseForm, NoteForm
from django.shortcuts import render, get_object_or_404

# Create your views here.
def expense_list(request):
    expenses = Expense.objects.order_by('-date')
    return render(request, 'MyExpenses/expense_list.html', {'expenses': expenses})

class ExpenseDelete(DeleteView):
    model = Expense
    success_url = reverse_lazy('expense_list')

def expense_detail(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    return render(request, 'MyExpenses/expense_detail.html', {'expense': expense})

def expense_new(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.date = timezone.now()
            expense.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm()
    return render(request, 'MyExpenses/expense_edit.html', {'form': form})

def expense_edit(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    if request.method == "POST":
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.author = request.user
            expense.date = timezone.now()
            expense.save()
            return redirect('expense_detail', pk=expense.pk)
    else:
        form = ExpenseForm(instance=expense)
    return render(request, 'MyExpenses/expense_edit.html', {'form': form})

def note_new(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.date = timezone.now()
            note.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm()
    return render(request, 'MyExpenses/note_edit.html', {'form': form})