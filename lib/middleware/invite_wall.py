import os
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


class InviteWall(object):

    def process_request(self, request):

        if 'invited' in request.session and request.session['invited'] is True:
            return

        if request.path in ['/invite']:
            return

        if 'ENVIRONMENT' in os.environ and os.environ['ENVIRONMENT'] == 'PROD':
            return HttpResponseRedirect(reverse('invite'))
