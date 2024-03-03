from django import forms
from . models import *

    

class Bookingforms(forms.ModelForm):
    class Meta:
        model=appo
        fields='__all__'



        labels = {
            'pname':'Patient Name',
            'email':'Email Address',
            'phone':'Contact Id',
            'depp':'Department',
            'date':'Date',
        }




        



class doctersBookingforms(forms.ModelForm):
    
    class Meta:

        model=docters_booking
        fields='__all__'


        labels = {
            'pname':'Patient Name',
    
              'age':'Age',
            'phone':'Contact Id',
            'email':'Email Address',
            'date':'Date'

        }
    