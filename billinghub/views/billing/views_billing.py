from django.shortcuts import render
from .forms import BillForm
from ...models import Bill
from django.db.models import Sum
from django.db.models import F


def bill_new(request):
    form = BillForm()
    if request.method == "POST":
        if request.POST.get('bill_date') == "":
            return render(request, 'generic_form.html', {'form': form, 'title_form': "Crear un nuevo cliente", 'saved': True, 'date': True, 'message': "La fecha esta vacia", 'type': "error"})
            
        form = BillForm(request.POST)
        if form.is_valid():
            bill = form.save(commit=False)
            bill.bill_date = request.POST.get('bill_date')
            bill.save()
            return render(request, 'generic_form.html', {'form': form, 'title_form': "Crear un nuevo cliente", 'saved': True,'date': True,'message': "Venta registrada", 'type': "success", 'last_date': request.POST.get('bill_date')})
        else:
            return render(request, 'generic_form.html', {'form': form, 'title_form': "Crear un nuevo cliente", 'saved': True, 'date': True, 'message': "No se registro la venta", 'type': "error"})
        
    return render(request, 'generic_form.html', {'form': form, 'title_form': "Crear una nueva venta",'saved': False, 'message': "", 'date': True, 'last_date': request.POST.get('bill_date')})


def registro_ventas(request):
    if request.method == "POST" and request.POST.get('start_date') != "":
        bills = Bill.objects.filter(bill_date__range=[request.POST.get('start_date'), request.POST.get('end_date')])
        if len(bills) == 0:
            return render(request, 'generic_form_table.html', {'bills': {}, 'title_form': "Registro de ventas",'saved': True,'message': "No hay registro en este rango de fechas", 'type':"warning"})
        print(bills)
        descripcion =  "Consultado desde: %s Hasta %s" %(request.POST.get('start_date'), request.POST.get('end_date'))
        return render(request, 'generic_form_table.html', {'bills': bills, 'title_form': "Registro de ventas",'saved': True,'type': "success", 'message': "Todo salio bien!", 'type':"success", 'table_description': descripcion})
        
    return render(request, 'generic_form_table.html', {'bills': {}, 'title_form': "Registro de ventas",'saved': False, 'message': ""})

def cuenta_final(request):
    if request.method == "POST" and request.POST.get('start_date') != "":
        bills = Bill.objects.values('client').order_by('client').annotate(total_price=Sum('price')).filter(bill_date__range=[request.POST.get('start_date'), request.POST.get('end_date')]).values(last_name=F('client__last_name'), first_name=F('client__first_name'),document=F('client__document'), price=F('total_price'))
    
        # objects.filter(bill_date__range=[request.POST.get('start_date'), request.POST.get('end_date')])
        if len(bills) == 0:
            return render(request, 'generic_form_table_list.html', {'bills': {}, 'title_form': "Cuenta final",'saved': True,'message': "No hay registro en este rango de fechas", 'type':"warning"})
        print(bills)
        descripcion =  "Consultado desde: %s Hasta %s" %(request.POST.get('start_date'), request.POST.get('end_date'))
        return render(request, 'generic_form_table_list.html', {'bills': bills, 'title_form': "Cuenta final",'saved': True,'type': "success", 'message': "Todo salio bien!", 'type':"success", 'table_description': descripcion})
        
    return render(request, 'generic_form_table_list.html', {'bills': {}, 'title_form': "Cuenta final",'saved': False, 'message': ""})

        