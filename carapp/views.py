from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, CustomUserCreationForm, \
                   ProfileForm, ProfileFormEditable, \
                   AdvertForm, EmailPriceForm, EmailPriceReminderForm
from .models import Profile, Advert, PriceReminderConnection
from .utils import searchAdverts
from django.core.mail import send_mail


reminder_list = {}


@login_required
def dashboard(request):
    return render(request,
                  'carapp/dashboard.html',
                  {'section': 'dashboard'})


def user_login(request):
    form = LoginForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('main-site')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
        else:
            form = LoginForm()

    context = {'form': form}
    return render(request, 'registration/login.html', context)


def index(request):
    adverts = Advert.objects.all()
    num = len(adverts)
    context = {'num': num, 'adverts': adverts}
    return render(request, 'carapp/index.html', context)


def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            profile = Profile.objects.create(user=user)
            profile.save()

            messages.success(request, "User account was created!")

            login(request, user)
            return redirect('edit-account')

        else:
            return HttpResponse('Error')

    context = {'page': page, 'form': form}
    return render(request, 'registration/register.html', context)


def forgot(request):
    return render(request, 'carapp/forgot.html')


def profile(request, pk):
    page = 'profile'
    profile = Profile.objects.get(id=pk)

    adverts = profile.advert_set.all()

    context = {'profile': profile,
               'page': page,
               'adverts': adverts,
               }
    return render(request, 'carapp/profile.html', context)


@login_required(login_url="login")
def userAccount(request):
    profile = request.user.profile
    username = profile.username
    form = ProfileForm(instance=profile)
    adverts = profile.advert_set.all()

    context = {'profile': profile,
               'form': form,
               'adverts': adverts,
               'username': username}

    return render(request, 'carapp/profile.html', context)


@login_required(login_url="login")
def editAccount(request):
    profile = request.user.profile
    form = ProfileFormEditable(instance=profile)
    username = profile.username
    if request.method == 'POST':
        form = ProfileFormEditable(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('account')

    context = {'form': form, 'profile': profile, 'username': username}
    return render(request, 'carapp/edit_profile.html', context)


@login_required(login_url="login")
def deleteAccount(request):
    if request.method == "POST":
        profile = request.user.profile
        profile.delete()
        messages.success(request, "User account was deleted!")
        return render(request, 'registration/deleted.html')


def adverts_view(request):
    search_query = ""
    adverts = Advert.objects.all()

    # searching
    if request.GET.get('search_query'):
        adverts, search_query = searchAdverts(request)
    elif request.GET.get('first-registration-min'):
        filter_by_year = request.GET.get('first-registration-min')

        if filter_by_year == '2022':
            adverts = Advert.objects.filter(first_registration__gte=2022)
        elif filter_by_year == '2021':
            adverts = Advert.objects.filter(first_registration__gte=2021)
        elif filter_by_year == '2020':
            adverts = Advert.objects.filter(first_registration__gte=2020)
        elif filter_by_year == '2019':
            adverts = Advert.objects.filter(first_registration__gte=2019)
        elif filter_by_year == '2018':
            adverts = Advert.objects.filter(first_registration__gte=2018)
        elif filter_by_year == '2017':
            adverts = Advert.objects.filter(first_registration__gte=2017)
        elif filter_by_year == '2016':
            adverts = Advert.objects.filter(first_registration__gte=2016)
        elif filter_by_year == '2015':
            adverts = Advert.objects.filter(first_registration__gte=2015)
        elif filter_by_year == '2014':
            adverts = Advert.objects.filter(first_registration__gte=2014)
        elif filter_by_year == '2013':
            adverts = Advert.objects.filter(first_registration__gte=2013)
        elif filter_by_year == '2012':
            adverts = Advert.objects.filter(first_registration__gte=2012)
        elif filter_by_year == '2011':
            adverts = Advert.objects.filter(first_registration__gte=2011)
        elif filter_by_year == '2010':
            adverts = Advert.objects.filter(first_registration__gte=2010)
        elif filter_by_year == '2009':
            adverts = Advert.objects.filter(first_registration__gte=2009)
        elif filter_by_year == '2008':
            adverts = Advert.objects.filter(first_registration__gte=2008)
        elif filter_by_year == '2007':
            adverts = Advert.objects.filter(first_registration__gte=2007)
        elif filter_by_year == '2006':
            adverts = Advert.objects.filter(first_registration__gte=2006)
        elif filter_by_year == '2005':
            adverts = Advert.objects.filter(first_registration__gte=2005)
    elif request.GET.get('first-registration-max'):
        filter_by_year_max = request.GET.get('first-registration-max')

        if filter_by_year_max == '2022':
            adverts = Advert.objects.filter(first_registration__lte=2022)
        elif filter_by_year_max == '2021':
            adverts = Advert.objects.filter(first_registration__lte=2021)
        elif filter_by_year_max == '2020':
            adverts = Advert.objects.filter(first_registration__lte=2020)
        elif filter_by_year_max == '2019':
            adverts = Advert.objects.filter(first_registration__lte=2019)
        elif filter_by_year_max == '2018':
            adverts = Advert.objects.filter(first_registration__lte=2018)
        elif filter_by_year_max == '2017':
            adverts = Advert.objects.filter(first_registration__lte=2017)
        elif filter_by_year_max == '2016':
            adverts = Advert.objects.filter(first_registration__lte=2016)
        elif filter_by_year_max == '2015':
            adverts = Advert.objects.filter(first_registration__lte=2015)
        elif filter_by_year_max == '2014':
            adverts = Advert.objects.filter(first_registration__lte=2014)
        elif filter_by_year_max == '2013':
            adverts = Advert.objects.filter(first_registration__lte=2013)
        elif filter_by_year_max == '2012':
            adverts = Advert.objects.filter(first_registration__lte=2012)
        elif filter_by_year_max == '2011':
            adverts = Advert.objects.filter(first_registration__lte=2011)
        elif filter_by_year_max == '2010':
            adverts = Advert.objects.filter(first_registration__lte=2010)
        elif filter_by_year_max == '2009':
            adverts = Advert.objects.filter(first_registration__lte=2009)
        elif filter_by_year_max == '2008':
            adverts = Advert.objects.filter(first_registration__lte=2008)
        elif filter_by_year_max == '2007':
            adverts = Advert.objects.filter(first_registration__lte=2007)
        elif filter_by_year_max == '2006':
            adverts = Advert.objects.filter(first_registration__lte=2006)
        elif filter_by_year_max == '2005':
            adverts = Advert.objects.filter(first_registration__lte=2005)
    elif request.GET.get('distance-min'):
        filter_by_mileage_min = request.GET.get('distance-min')
        if filter_by_mileage_min == '20000':
            adverts = Advert.objects.filter(mileage__gte=20000)
        elif filter_by_mileage_min == '35000':
            adverts = Advert.objects.filter(mileage__gte=35000)
        elif filter_by_mileage_min == '50000':
            adverts = Advert.objects.filter(mileage__gte=50000)
        elif filter_by_mileage_min == '75000':
            adverts = Advert.objects.filter(mileage__gte=75000)
        elif filter_by_mileage_min == '100000':
            adverts = Advert.objects.filter(mileage__gte=100000)
        elif filter_by_mileage_min == '125000':
            adverts = Advert.objects.filter(mileage__gte=125000)
        elif filter_by_mileage_min == '150000':
            adverts = Advert.objects.filter(mileage__gte=150000)
        elif filter_by_mileage_min == '200000':
            adverts = Advert.objects.filter(mileage__gte=200000)
        elif filter_by_mileage_min == '250000':
            adverts = Advert.objects.filter(mileage__gte=250000)
    elif request.GET.get('distance-max'):
        filter_by_mileage_max = request.GET.get('distance-max')
        if filter_by_mileage_max == '20000':
            adverts = Advert.objects.filter(mileage__lte=20000)
        elif filter_by_mileage_max == '35000':
            adverts = Advert.objects.filter(mileage__lte=35000)
        elif filter_by_mileage_max == '50000':
            adverts = Advert.objects.filter(mileage__lte=50000)
        elif filter_by_mileage_max == '75000':
            adverts = Advert.objects.filter(mileage__lte=75000)
        elif filter_by_mileage_max == '100000':
            adverts = Advert.objects.filter(mileage__lte=100000)
        elif filter_by_mileage_max == '125000':
            adverts = Advert.objects.filter(mileage__lte=125000)
        elif filter_by_mileage_max == '150000':
            adverts = Advert.objects.filter(mileage__lte=150000)
        elif filter_by_mileage_max == '200000':
            adverts = Advert.objects.filter(mileage__lte=200000)
        elif filter_by_mileage_max == '250000':
            adverts = Advert.objects.filter(mileage__lte=250000)
    else:
        # sorting
        adverts = Advert.objects.all()
        sort_by = request.GET.get('sort')

        if sort_by == 'new':
            adverts = adverts.order_by('-created')
        elif sort_by == 'old':
            adverts = adverts.order_by('created')
        elif sort_by == 'price_low':
            adverts = adverts.order_by('price')
        elif sort_by == 'price_high':
            adverts = adverts.order_by('-price')
        elif sort_by == 'mileage_low':
            adverts = adverts.order_by('mileage')
        elif sort_by == 'mileage_high':
            adverts = adverts.order_by('-mileage')
        else:
            adverts = adverts.order_by('-created')

    num = len(adverts)
    context = {'adverts': adverts, 'search_query': search_query, 'num':num}
    return render(request, 'carapp/advertsView.html', context)


def advert_view(request, pk):
    page = 'advert'
    advert = Advert.objects.get(id=pk)
    profile = Profile.objects.all()
    context = {'advert': advert, 'profile': profile, 'page': page}
    return render(request, 'carapp/detailsAdvert.html', context)

@login_required(login_url="login")
def add_to_favorite(request, pk):
    profile = request.user.profile
    advert = Advert.objects.get(id=pk)

    
    context = {'advert': advert, 'profile': profile}
    return render(request, 'carapp/detailsAdvert.html', context)


@login_required(login_url="login")
def myAdverts(request):
    profile = request.user.profile
    # adverts = Advert.objects.all()
    adverts = profile.advert_set.all()
    context = {'adverts': adverts, 'profile': profile}
    return render(request, 'carapp/myAdverts.html', context)

@login_required(login_url="login")
def delete_advert(request, pk):
    profile = request.user.profile
    advert = Advert.objects.get(id=pk)
    advert.delete()
    context = {'advert': advert, 'profile': profile}
    return render(request, 'carapp/myAdverts.html', context)


def contact_advert(request, pk):
    advert = Advert.objects.get(id=pk)
    sent = False
    if request.method == 'POST':
        # form was submitted
        form = EmailPriceForm(request.POST)
        if form.is_valid():
            # form fields passed validation
            cd = form.cleaned_data
            # send email
            subject = f"{cd['name']} prosi o kontakt. Ogłoszenie: {advert.title}, {advert.created}"
            if cd['comments']:
                message = f"Adres e-mail do kontaktu: {cd['your_address']}\nNumer telefonu: {cd['your_phone']}\n\nLink do ogłoszenia: localhost:8000/advert/{advert.id}\n" \
                          f"Komentarze do kontaktu: \n {cd['comments']}"
            else:
                message = f"Adres e-mail do kontaktu: {cd['your_address']}\nNumer telefonu: {cd['your_phone']}\n\nLink do ogłoszenia: localhost:8000/advert/{advert.id}\n" \
                          f"Uzytkownik nie dodal komentarza."
            send_mail(subject, message, 'marczak01@o2.pl', [cd['your_address'], advert.owner.email])
            sent = True
        else:
            print('form not valid')
    else:
        print('no post method')
        form = EmailPriceForm()

    context = {'advert': advert, 'form': form, 'sent': sent}
    return render(request, 'carapp/contact_seller.html', context)


@login_required(login_url="login")
def price_reminder(request, pk):
    profile = request.user.profile
    advert = Advert.objects.get(id=pk)
    sent = False
    on_the_list = False

    if request.method == 'POST':
        form = EmailPriceReminderForm(request.POST, profile)
        if form.is_valid():
            # we're cleaning data from form and saving it in 'cd' variable
            cd = form.cleaned_data
            subject = f"Ustawienie powiadomienia przebieglo pomyslnie."
            message = f"Dziękujemy za ustawienie powiadomienia. Gdy tylko cena ogloszenia ulegnie zmianie powiadomimy Ciebie o tym drogą mailową"
            send_mail(subject, message, 'marczak01@o2.pl', [cd['your_address']])
            sent = True

            if sent:
                list_of_emails = PriceReminderConnection.objects.filter(user_address=cd['your_address'], id_of_advert=advert.id)
                print(list_of_emails)
                if list_of_emails:
                    on_the_list = True
                    print('on the list')
                else:
                    price_reminder_list = PriceReminderConnection(user_address=cd['your_address'], id_of_advert=advert.id)
                    price_reminder_list.save()
                    on_the_list = False
                    print(f"Dodano email oraz id ogloszenia do bazy danych {cd['your_address']} oraz id {advert.id}")
        else:
            print('form not valid')
    else:
        form = EmailPriceReminderForm()


    context = {'advert': advert, 'form': form, 'sent': sent, 'profile': profile, 'on_the_list': on_the_list}
    return render(request, 'carapp/price_reminder.html', context)


def other_user_adverts(request, pk):
    profile = Profile.objects.get(id=pk)

    adverts = profile.advert_set.all()
    context = {'adverts': adverts, 'profile': profile}
    return render(request, 'carapp/otherUserAdverts.html', context)


@login_required(login_url="login")
def create_advert(request):
    profile = request.user.profile #aktualnie zalogowany uzytk
    form = AdvertForm()
    created = False
    if request.method == "POST":
        form = AdvertForm(request.POST, request.FILES)
        if form.is_valid():
            #set current user to owner while creating advert
            advert = form.save(commit=False)
            advert.owner = profile
            advert.save()
            created = True
            return redirect('adverts')
        else:
            return redirect('advert_form')
    context = {'form': form, 'created': created}
    return render(request, 'carapp/addAdvert.html', context)


@login_required(login_url="login")
def updateAdvert(request, pk):
    profile = request.user.profile
    advert = profile.advert_set.get(id=pk)
    form = AdvertForm(instance=advert)
    # we're taking actual price before changes
    advert_price = advert.price
    print(f"{advert_price} było")
    if request.method == "POST":
        form = AdvertForm(request.POST, request.FILES, instance=advert)
        if form.is_valid():
            form.save()
            print(f"{advert.price} jest")
            # after we see any price changes in advert
            # then we send a reminder to all addresses connected with this advert
            if advert_price != advert.price:
                print('cena sie zmienila')
                list_of_emails = PriceReminderConnection.objects.filter(id_of_advert=str(advert.id))
                print(list_of_emails)

                subject = f"Uwaga nastąpiła zmiana ceny dla ogłoszenia: {advert.title}"
                message = f"Informujemy, ze cena ogłoszenia uległa zmianie.\n " \
                          f"Poprzenia cena: {advert_price}PLN \nAktualna cena: {advert.price}PLN"
                for i in list_of_emails:
                    send_mail(subject, message, 'marczak01@o2.pl', [i])

            return redirect('adverts')

    context = {'form': form}
    return render(request, 'carapp/addAdvert.html', context)




# @login_required(login_url="login")
# def deleteAdvert(request, pk):
#     profile = request.user.profile
#     advert = profile.advert_set.get(id=pk)
#     if request.method == 'POST':
#         advert.delete()
#         return redirect('adverts')
#     context = {'object': advert}
#     return render(request, 'adverts/delete_template.html', context)
