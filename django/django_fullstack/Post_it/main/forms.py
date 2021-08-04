from django import forms

class NoteForm(forms.Form):
    #id
    text = forms.CharField(label='Add a new Post', widget=forms.Textarea)
