from django.shortcuts import render
from .forms import PizzaForm,MultiplePizzaForm # form class
from django.forms import formset_factory
from .models import Pizza

# Create your views here.
def homepage(request):
    return render(request,'pizza/home.html')
def order(request):
    multiple_pizza_form=MultiplePizzaForm()#call, instance create
    created_pizza_pk=None
    if request.method=='POST':
        filled_form=PizzaForm(request.POST)
        if filled_form.is_valid():

            filled_form.save()
            note = "Thanks for your order %s,%s,%s size pizza placed successfully!" % (
            filled_form.cleaned_data['topping1'], filled_form.cleaned_data['topping2'],
            filled_form.cleaned_data['size'])
            created_pizza=filled_form.save()
            created_pizza_pk=created_pizza.id
        else:
            note="Order not placed. please try again"
        new_form=PizzaForm()
        return render(request,'pizza/order.html',{"note":note,"multiple_pizza_form":multiple_pizza_form,'created_pizza_pk':created_pizza_pk})
    else:
        form=PizzaForm()
        return render(request,'pizza/order.html',{'pizzaform':form,"multiple_pizza_form":multiple_pizza_form})
def pizzas (request):
    no_of_pizzas=2
    if request.method=="GET":
        filled_multiple_pizza_form=MultiplePizzaForm(request.GET)
        if filled_multiple_pizza_form.is_valid():
            no_of_pizzas=filled_multiple_pizza_form.cleaned_data['number']
    PizzaFormset=formset_factory(PizzaForm,extra=no_of_pizzas)
    formset=PizzaFormset()
    if request.method=="POST":
        filled_formset=PizzaFormset(request.POST)
        if filled_formset.is_valid():
            for form in filled_formset:
                form.save()
            note="Thanks your order placed successfully!"
        else:
            note="Sorry, order not placed yet please try again"
        return render(request, 'pizza/pizzas.html', {"submitted":True,"note":note})


    return render(request,'pizza/pizzas.html',{"formset":formset})
def edit(request,pk):
    note= ''
    pizza = Pizza.objects.get(pk = pk) #save order model
    form = PizzaForm(instance=pizza) #placed order
    if request.method== 'POST':
        edited_form=PizzaForm(request.POST,instance=pizza)
        if edited_form.is_valid():
            edited_form.save()
            note='Order edited successfully'
        else:
            note='Sorry please try again'

    return render(request,'pizza/edit.html',{'pizzaform':form,'pk':pk,'note':note})
