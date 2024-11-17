from django import forms
from .validator import validate_12_digit_integer

class TransactionForms(forms.Form):
    type_options = [('Recall Of Funds', 'Recall Of Funds'), ('Amendment', 'Amendment'), ('Stop Payment', 'Stop Payment') ]
    type_field = forms.ChoiceField(label = 'Type', choices = type_options, required = True)
    branch_options = [('Abdali', 'Abdali'), ('Fahaheel', 'Fahaheel'), ('Farwaniya', 'Farwaniya'),('Hawally', 'Hawally'),('Jleeb1', 'Jleeb1'),('Jleeb2', 'Jleeb2'),('Mahboula', 'Mahboula'),('Mobile1', 'Mobile1'),
                      ('Mobile2', 'Mobile2'),('Qibla', 'Qibla'),('Safat', 'Safat')]
    branch_field = forms.ChoiceField(choices = branch_options, required = True)
    tt_express_options = [('TT', 'TT'), ('Transfast','Transfast'), ('Himal Remit', 'Himal Remit'), ('Western Union', 'Western Union')]
    remittance_field = forms.ChoiceField(choices = tt_express_options, required = True)
    correspondant_options = [
        ('Agrani Bank', 'Agrani Bank'), ('Banco De Oro', 'Banco De Oro'), ('Bank Of Ceylon', 'Bank Of Ceylon'), ('Bank of Philippine Islands', 'Bank of Philippine Islands'),
        ('Banque Du Caire', 'Banque Du Caire'), ('Banque Misr', 'Banque Misr'), ('Commercial Bank Of Ceylon', 'Commercial Bank Of Ceylon'), ('Eastern Bank', 'Eastern Bank'),
        ('HDFC Bank', 'HDFC Bank'), ('Himalayan Bank', 'Himalayan Bank'), ('ICICI Bank', 'ICICI Bank'), ('IBBL', 'IBBL'),('Janata Bank', 'Janata Bank'), ('Land Bank of Philippines', 'Land Bank of Philippines'), ('NIUM', 'NIUM'),
        ('Peoples Bank', 'Peoples Bank'), ('Philippines National Bank', 'Philippines National Bank'), ('Pubali Bank', 'Pubali Bank'),('Rupali Bank', 'Rupali Bank'), ('Sonali Bank', 'Sonali Bank'),
        ('Transfast', 'Transfast'), ('Trust Bank', 'Trust Bank'), ('UCB Bank', 'UCB Bank'),('Uttara Bank', 'Uttara Bank'),('Warba Bank', 'Warba Bank'), ('Western Union', 'Western Union')
    ]

    correspondant_field = forms.ChoiceField(choices = correspondant_options, required = True)
    fieldtxnrefnumber = forms.CharField(label = "Transaction Reference Number", max_length = 16, required = True)
    civilidnumber = forms.IntegerField(label = "Customer CIVIL ID",validators=[validate_12_digit_integer], required=True )
    localcurrencyfield = forms.DecimalField(label = "Local Currency", required=False , widget=forms.NumberInput(attrs={'placeholder': 'Enter FC amount'}) )
    foriegncurrencyfield = forms.DecimalField(label = "Foriegn Currency", required=False , widget=forms.NumberInput(attrs={'placeholder': 'Enter FC amount'}))
    remittername = forms.CharField(label = "Remitter Name", required = True)
    amendment_options = [('Beneficiary name change','Beneficiary name change'), ('Beneficiary account change','Beneficiary account change'), ('Beneficiary bank details change','Beneficiary bank details change'),
                         ('Beneficiary branch name change','Beneficiary branch name change'),
                         ('Payment mode change','Payment mode change'),('Reprocess','Reprocess'), ('Other','Other')]
    amendment_field = forms.ChoiceField(label = "What type of amendment do you want? ", choices = amendment_options, required = False)
    newly_amended = forms.CharField(label="Amendment Details", required=False)
    stp_options = [('Upload Reject', 'Upload Reject'),('Bank Returned Funds', 'Bank Returned Funds'),('Other', 'Other')]
    stp_field = forms.ChoiceField(label = "Stop Payment Reason", choices = stp_options, required = False)
    reissue = [('Yes', 'Yes'), ('No', 'No')]
    reissue_field = forms.ChoiceField(label = "Reissue", choices = reissue, required = False)
    recall_options = [('Invalid Account details', 'Invalid Account details'),('Invalid Amount','Invalid Amount')]
    recall_field = forms.ChoiceField(label = "Recall Funds Reason", choices = recall_options, required = False)
