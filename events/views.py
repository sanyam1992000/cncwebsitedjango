from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from .certificates import render_to_pdf
# Create your views here.


def events(request):
    return HttpResponse('iucfhroiuhf')


@login_required
def getpdf(request, userid, eventid, *args, **kwargs):
    user = request.user
    if userid == user.username:
        data = {
            'user': user }
        #      'user': datetime.date.today(),
        #      'amount': 39.99,
        #     'customer_name': 'Cooper Mann',
        #     'order_id': 1233434,
        # }
        pdf = render_to_pdf('events/certi.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
    else:
        return render(request, '404.html')
