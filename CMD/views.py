from django.shortcuts import render, HttpResponse
from django.template import loader
import subprocess
import platform

# Create your views here.
def home(request):
    return render(request=request,template_name='index.html')

def command_injection(request):
    template = loader.get_template('CMD.html')
    context = {}
    os = platform.system()
    if request.method == 'POST':
        cmd_input = request.POST.get('cmd-input','')
        command = 'echo {}'.format(cmd_input)
        
        try:
            if os == 'Windows':
                process = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            else:
                process = subprocess.Popen(["/bin/bash", "-c",command],stdout=subprocess.PIPE,stderr=subprocess.PIPE)

            stdout, stderr = process.communicate()
            
            data = stdout.decode(encoding='iso-8859-1')
            err = stderr.decode(encoding='iso-8859-1')
            output = data + err
        except Exception as e:
            output = 'Ha ocurrido un error inesperado: {}'.format(str(e))
        context['output'] = output


    return HttpResponse(template.render(context,request))