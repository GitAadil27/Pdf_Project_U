# views.py
from django.shortcuts import render
from django.http import HttpResponse
from .forms import TransactionForms
from .reject_validations import process_amendment, process_recall, process_stp
from datetime import datetime

def handle_txn_form(request):
    if request.method == "POST":
        form = TransactionForms(request.POST)
        if form.is_valid():
            # Common data extraction
            mode = form.cleaned_data['type_field']
            branch = form.cleaned_data['branch_field']
            remittance = form.cleaned_data['remittance_field']
            correspondant = form.cleaned_data['correspondant_field']
            refnumber = form.cleaned_data['fieldtxnrefnumber']
            civilid = form.cleaned_data['civilidnumber']
            remittername = form.cleaned_data['remittername']

            response = HttpResponse(content_type='application/pdf')
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{mode}_{refnumber}_{timestamp}.pdf"
            response['Content-Disposition'] = f'attachment; filename="{filename}"'

            try:
                if mode == 'Recall Of Funds':
                    recall_reason = form.cleaned_data.get('recall_field', '')
                    process_recall(response, mode, branch, remittance, correspondant,
                                 refnumber, civilid, remittername, recall_reason)

                elif mode == 'Amendment':
                    amendment_field = form.cleaned_data.get('amendment_field', '')
                    process_amendment(response, mode, branch, remittance, correspondant,
                                   refnumber, civilid, remittername, amendment_field)

                elif mode == 'Stop Payment':
                    stp_reason = form.cleaned_data.get('stp_field', '')
                    reissue_yn = form.cleaned_data.get('reissue_field', '')
                    process_stp(response, mode, branch, remittance, correspondant,
                              refnumber, civilid, remittername, stp_reason, reissue_yn)

                return response

            except Exception as e:
                print(f"Error generating PDF: {str(e)}")
                return HttpResponse("Error generating PDF", status=500)

    else:
        form = TransactionForms()

    return render(request, 'index.html', {'form': form})