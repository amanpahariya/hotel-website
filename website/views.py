from django.shortcuts import render

from website.models import contactform, Booking, Book, creditcard , Customer_Data


def home(request):
    return render(request, 'home.html')


def contact(request):
    if request.method == 'POST':
        str1 = str(request.POST.get("cell"))
        if len(str1) > 10:
            return render(request, 'contact.html', {'message': 'your cell number is more than 10 digit'})
        elif len(str1) < 10:
            return render(request, 'contact.html', {'message': 'Sorry you missed some values in your cell number'})
        elif len(str1) == 10:
            name = request.POST.get("name")
            email = request.POST.get("email")
            cell = request.POST.get("cell")
            info = request.POST.get("info")
            o_ref = contactform(name=name, email=email, cell=cell, info=info)
            o_ref.save()
            return render(request, 'contact.html',
                          {'message': 'Your Query is Successfully Submitted we contact you soon'})
        else:
            return render(request, 'contact.html',
                          {'message': 'your enter wrong value please correct them and then submit'})
    else:
        return render(request, 'contact.html')


def rooms(request):
    dests = Booking.objects.all()
    return render(request, 'booking.html', {'dests': dests})


def index(request):
    dests = Booking.objects.all()
    li = Book()
    li.check1 = None
    li.id1 = None
    li.check2 = None
    li.rooms = None
    li.mem = None
    id1 = request.POST.get('id')
    li.check1 = request.POST.get('Check-in')
    li.check2 = request.POST.get('Check-out')
    li.mem1 = request.POST.get('member')
    li.rooms = request.POST.get('rooms')
    print(li.check1)
    if li.mem1 is None and id1 is None and li.check1 is None:
        return render(request, 'booking.html', {'dests': dests})

    else:
        li.mem = int(request.POST['member'])
        li.rooms = int(request.POST['rooms'])
        price1 = Booking.objects.filter(id=id1).values_list('price')
        li.price = price1[0][0]
        li.total = li.rooms * li.price + 0.18 * li.price
        dests = Booking.objects.all()
        if li.mem % 2 == 0:
            if li.rooms * 2 >= li.mem:
                print("cnf")
                return render(request, 'index.html', {'list': li})
            else:
                print('no')
                return render(request, 'booking.html', {'message': 'Sorry You need more rooms only 2 members are allowed in single room' , 'dests': dests})
        else:
            if li.rooms * 2 >= li.mem:
                print("cnf")

                return render(request, 'index.html', {'list': li})
            else:
                print('no')
                return render(request, 'booking.html', {'message': 'Sorry You need more rooms only 2 members are allowed in single room' , 'dests': dests})

def cnfbooking(request):
    dests = Booking.objects.all()
    id = None
    cvv = None
    exp  = None
    if id is None and cvv is None and exp is None:
        return render(request, 'booking.html', {'dests': dests})
    else:
        id = request.POST['cardnumber']
        exp = request.POST['expiry']
        if len(str(request.POST.get('cell'))) > 10:
            return render(request, 'index.html', {'message1': ' * your entered cell number is wrong'})
        elif len(str(request.POST.get('cell'))) < 10:
            return render(request, 'index.html', {'message1': ' * your entered cell number is wrong'})
        else:
            id = request.POST['cardnumber']
            cvv = request.POST.get('cvv')
            bool = False
            details = creditcard.objects.all()
            for d1 in  details:
                if  id == str(d1):
                    details = creditcard.objects.filter(cardnumber=d1).values_list('cvv', 'MM_YY')
                    print(details[0])
                    if cvv == str(details[0][0]) and exp == str(details[0][1]):
                        bool = True

            if(bool):
                if request.method == 'POST':
                    prefix = request.POST.get('prefix')
                    first_name = request.POST.get('fname')
                    last_name = request.POST.get('lname')
                    email = request.POST.get('email')
                    cell_number = request.POST.get('cell')
                    country = request.POST.get('country')
                    add1 = request.POST.get('add1')
                    add2 = request.POST.get('add2')
                    city = request.POST.get('city')
                    zip_or_postal = request.POST.get('zip')
                    check1  = request.POST.get('check-in')
                    check2 = request.POST.get('check-out')
                    total = request.POST.get('total')
                    mem = request.POST.get('mem')
                    rooms = request.POST.get('rooms')
                    o_ref = Customer_Data(prefix = prefix, first_name = first_name, last_name = last_name, email = email, cell_number = cell_number, country = country, add1 = add1, add2 = add2, city = city, zip_or_postal = zip_or_postal, check1 = check1, check2 = check2, total = total, mem = mem, rooms = rooms)
                    o_ref.save()
                    return render(request, 'index1.html')
            else:
               return render(request,'index.html',{'message': ' * your entered card details are wrong'})

