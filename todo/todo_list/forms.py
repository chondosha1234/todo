from django.forms import ModelForm
from django import forms
from todo_list.models import Task


class TaskForm(forms.ModelForm):
    #status = forms.BooleanField()
   """
    def __init__(self, id=None, complete=False, description=None):
        #self.task_id = kwargs.pop('task_id')
        self.id = id
        self.complete = complete
        self.description = description
        #super(CompleteForm, self).__init__(id, complete, description)
        if self.complete == True:
            self.status = forms.BooleanField(label="", widget=forms.CheckboxInput(attrs={'onclick':'this.form.submit();'}), required=False)
            #self.fields['status'].widget = forms.BooleanField(label="", widget=forms.CheckboxInput(attrs={'onclick':'this.form.submit();'}), required=False)
        else:
            self.status = forms.BooleanField(label="", widget=forms.CheckboxInput(attrs={'onclick':'this.form.submit();'}), required=False)
            #self.fields['status'].widget = forms.BooleanField(label="", widget=forms.CheckboxInput(attrs={'onclick':'this.form.submit();'}), required=False)
            #set the box to be checked or unchecked based on passed arguments from associated task
        super(CompleteForm, self).__init__(id, complete, description)
   """
   class Meta:
       model = Task
       fields = ['complete']

   def __init__(self, *args, **kwargs):
       self.description = kwargs.pop('description')
       self.id = kwargs.pop('id')
       self.complete = kwargs.pop('complete')
       super(TaskForm, self).__init__(*args, **kwargs)
       self.fields['complete'] = forms.BooleanField(label="", widget=forms.CheckboxInput(attrs={'onclick':'this.form.submit();'}), required=False)
       if (self.complete):
           self.fields['complete'].initial = True
       else:
           self.fields['complete'].initial = False
