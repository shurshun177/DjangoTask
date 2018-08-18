from django import forms

from .models import Expense, Note

class ExpenseForm(forms.ModelForm):

    class Meta:
        model = Expense
        fields = ('title', 'description','date','sum')

class NoteForm(forms.ModelForm):

    class Meta:
        model = Note
        fields = ('note', 'date')