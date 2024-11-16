from django.shortcuts import render
from django.http import HttpResponse
from .forms import TransactionForms
import weasyprint
from django.template.loader import render_to_string
from django.utils import timezone
from datetime import datetime


def handle_weasy_form(request):
    form = TransactionForms(request.POST or None)
    if request.method == "POST" and form.is_valid():
        print("POST data:", request.POST)
        mode = form.cleaned_data['type_field']
        branch = form.cleaned_data['branch_field']
        remittance = form.cleaned_data['remittance_field']
        correspondant = form.cleaned_data['correspondant_field']
        refnumber = form.cleaned_data['fieldtxnrefnumber']
        civilid = str(form.cleaned_data['civilidnumber'])
        remittername = form.cleaned_data['remittername']
        static_url = request.build_absolute_uri('/static/')

        current_datetime = timezone.localtime(timezone.now())

        formatted_date = current_datetime.strftime('%d/%m/%Y')

        context = {
            'mode': mode,
            'branch': branch,
            'remittance': remittance,
            'correspondant': correspondant,
            'refnumber': refnumber,
            'civilid': civilid,
            'remittername': remittername,
            'static_url': static_url,
            'current_datetime': current_datetime,
            'formatted_date': formatted_date,
        }

        if mode == 'Recall Of Funds':
            localcurrencyfield = form.cleaned_data['localcurrencyfield']
            context['localcurrencyfield']=localcurrencyfield
            foriegncurrencyfield = form.cleaned_data['foriegncurrencyfield']
            context['foriegncurrencyfield']=foriegncurrencyfield
            recall_reason = form.cleaned_data['recall_field']
            context['recall_reason'] = recall_reason
            template_name = 'Recallform.html'
        elif mode == 'Amendment':
            amendment_field = form.cleaned_data['amendment_field']
            print('i reached here and amendment field was ', amendment_field)
            context['amendment_field'] = amendment_field
            newly_amended = form.cleaned_data['newly_amended']
            context['newly_amended'] = newly_amended
            template_name = 'AmendmentForm.html'
        elif mode == 'Stop Payment':
            localcurrencyfield = form.cleaned_data['localcurrencyfield']
            context['localcurrencyfield']=localcurrencyfield
            foriegncurrencyfield = form.cleaned_data['foriegncurrencyfield']
            context['foriegncurrencyfield']=foriegncurrencyfield
            stop_reason = form.cleaned_data['stp_field']
            context['stop_reason'] = stop_reason
            reissue_yn = form.cleaned_data['reissue_field']
            context['reissue_yn'] = reissue_yn
            template_name = 'StopPaymentform.html'

        # Configure WeasyPrint CSS for better date formatting
        css_string = '''
            @page { 
                size: A4; 
                margin: 15mm 10mm; 
                @top-center {
                    content: "";
                }
            }
            .date-field {
                font-family: 'Book Antiqua', Palatino, serif;
            }
        '''

        html_string = render_to_string(template_name, context)
        html_string = html_string.replace('/static/', static_url)

        pdf_file = weasyprint.HTML(
            string=html_string,
            base_url=request.build_absolute_uri('/')
        ).write_pdf(
            stylesheets=[weasyprint.CSS(string=css_string)],
            presentational_hints=True
        )

        response = HttpResponse(pdf_file, content_type='application/pdf')
        filename = f"{mode}_{refnumber}.pdf"
        response['Content-Disposition'] = f'attachment; filename="{filename}"'
        return response

    return render(request, 'normal.html', {'form': form})