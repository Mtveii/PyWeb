from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render
from django.template import loader
from .forms.demo_form import DemoForm
from .forms.styled_form import StyledForm
from .forms.delivery_form import DeliveryForm
from .forms.signup_form import SignupForm
from .forms.product_form import ProductForm
from datetime import datetime
from .forms.form_user import form_user as FormUser
from .helper import * 
from .models import *

# технічно представлення - це функції, які приймають
# запит (request) та формують відповідь (response)

def clonning(request) :
    template = loader.get_template('clonning.html')
    return HttpResponse( template.render() )


def form_delivery(request) :
    template = loader.get_template('form_delivery.html')
    if request.method == 'GET' :
        context = {
            'form': DeliveryForm()
        }
    elif request.method == 'POST' :
        form = DeliveryForm(request.POST)
        context = {
            'form': form
        }
    return HttpResponse( template.render(context=context, request=request) )


def form_styled(request) :
    template = loader.get_template('form_styled.html')
    if request.method == 'GET' :
        context = {
            'form': StyledForm()
        }
    elif request.method == 'POST' :
        form = StyledForm(request.POST)
        context = {
            'form': form
        }
    return HttpResponse( template.render(context=context, request=request) )


def forms(request) :
    if request.method == 'GET' :
        template = loader.get_template('forms.html')
        context = {
            'form': DemoForm()
        }
    elif request.method == 'POST' :
        form = DemoForm(request.POST)
        context = {
            'form': form
        }
        template = loader.get_template('form_ok.html' if form.is_valid() else 'forms.html')
    else :
        return HttpResponseNotAllowed()
    
    return HttpResponse( template.render(context=context, request=request) )


def hello(request) :
    return HttpResponse("Hello, world!")


def home(request) :
    template = loader.get_template('home.html')
    context = {
        'x': 10,
        'y': 20,
        'page_title': 'Домашня',
        'page_header': 'Розробка вебдодатків з використанням Python',
        'now': datetime.now().strftime("%H:%M:%S %d.%m.%Y")
    }
    return HttpResponse( template.render(context, request) )


def layouting(request) :
    template = loader.get_template('layouting.html')
    return HttpResponse( template.render() )


def models(request) :
    template = loader.get_template('models.html')
    return HttpResponse( template.render(request=request) )


def params(request) :    
    context = {
        'params': str(request.GET),
        'user': request.GET.get('user', 'Немає даних'),
        'q': request.GET.get('q', 'Немає даних'),
    }
    about = request.GET.get('about', None)
    if about == 'GET' :
        context['about_get'] = " (метод не має тіла і вживається як запит на читання)"
    elif about == 'POST' :
        context['about_post'] = " (метод може мати тіло і вживається як запит на створення)"
    '''Д.З. Створити посилання-підказки для НТТР-методів PUT, PATCH, DELETE
    (аналогічно створеним на занятті для методів GET, POST).
    До звіту додавати скріншоти'''
    template = loader.get_template('params.html')
    return HttpResponse( template.render(context, request) )


def signup(request) :
    template = loader.get_template('signup.html')
    if request.method == 'GET' :
        context = {
            'form': SignupForm()
        }
    elif request.method == 'POST' :
        form = SignupForm(request.POST)
        context = {
            'form': form,
            'is_ok': form.is_valid()
        }
        if form.is_valid() :
            form_data = form.cleaned_data
            _salt = salt()
            _dk = dk(form_data['password'], _salt)
            
            user = User()
            user.first_name = form_data['first_name']
            user.last_name  = form_data['last_name']
            user.email      = form_data['email']
            user.phone      = form_data['phone']
            user.birthdate  = form_data['birthdate']
            user.save()

            # Отримуємо або створюємо роль "Self registered" якщо її немає
            role, created = Role.objects.get_or_create(
                name="Self registered",
                defaults={
                    'create_level': 0,
                    'read_level': 0,
                    'update_level': 0,
                    'delete_level': 0
                }
            )
            
            user_access = Access()
            user_access.user  = user
            user_access.role  = role
            user_access.login = form_data['login']
            user_access.salt  = _salt
            user_access.dk    = _dk
            user_access.save()

            context['user'] = user
            context['user_access'] = user_access

    # context['salt'] = salt()    
    # context['dk'] = dk("123", "456")    
    return HttpResponse( template.render(request=request, context=context) )


def statics(request) :
    template = loader.get_template('statics.html')
    return HttpResponse( template.render() )


def product_form(request):
    if request.method == 'GET':
        template = loader.get_template('product_form.html')
        context = {'form': ProductForm()}
    elif request.method == 'POST':
        form = ProductForm(request.POST)
        context = {'form': form}
        template = loader.get_template('product_form_success.html' if form.is_valid() else 'product_form.html')
    else:
        return HttpResponseNotAllowed()
    return HttpResponse(template.render(context=context, request=request))


def form_user(request):

    template = loader.get_template('form_user.html')
    if request.method == 'GET' :
        context = {
            'form': FormUser()
        }
    elif request.method == 'POST' :
        form = FormUser(request.POST)
        context = {
            'form': form
        }
    return HttpResponse( template.render(context=context, request=request) )