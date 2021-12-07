from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from .models import *

data = {
    'app_name': 'ajax app',
}
def load_data():
    data['user_data'] = UserProfile.objects.all()[::-1]

def index(request):
    load_data()
    return render(request, 'index.html', data)

# Update data
def update_data(request, pk):
    if request.method == 'POST':
        user = UserProfile.objects.get(pk=pk)
        
        user.Name = request.POST['fullname']
        user.Email = request.POST['email']
        user.Mobile = request.POST['mobile']

        user.save()

        return redirect(index)
    else:
        pass

# delete data
def delete_data(request, pk):
    UserProfile.objects.get(pk=pk).delete()
    return redirect(index)

# Add New Data
def add_new(request):
    if request.method == 'POST':
        print('ajax form data: ', request.POST)
        UserProfile.objects.create(
            Name = request.POST.get('fullname'),
            Email = request.POST.get('email'),
            Mobile = request.POST.get('mobile'),
        )
        load_data()
        
        l = []
        for user_data in data['user_data']:
            d = dict()
            for key,value in user_data.__dict__.items():
                if not key.startswith('_'):
                    d.setdefault(key, value)
            l.append(d)
        data['user_data'] = l
        
        return JsonResponse(data)
    else:
        pass