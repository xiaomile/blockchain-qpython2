
from django.conf.urls import url
from django.contrib import admin
from django.http import HttpResponse
from blockchaintest import views
import os.path

def webapp_index(request):
    r = '''It works, you can develop this project with <a href='javascript:milib.qedit("%s")'>QPython Editor</a> now.''' % os.path.abspath(__file__)
    return HttpResponse(r)

def webapp_exit(request):
    import os,signal
    os.kill(os.getpid(), signal.SIGKILL)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^__exit', webapp_exit),
    #url(r'^$', webapp_index),
    url(r'^$',views.index),
    url(r'^index/',views.index),
    url(r'^chain/',views.chain),
    url(r'^mine/',views.mine),
    url(r'^transactions/new/',views.new_transactions),
    
]
