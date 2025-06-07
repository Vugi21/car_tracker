from django.shortcuts import render, redirect, get_object_or_404
from .models import Car, Maintenance
from .forms import CarForm, CarColorForm, MaintenanceForm

def car_list(request):
    cars = Car.objects.all()
    return render(request, 'cars/car_list.html', {'cars': cars})

def car_detail(request, pk):
    car = get_object_or_404(Car, pk=pk)
    maintenances = car.maintenance_records.all()
    if request.method == 'POST':
        form = MaintenanceForm(request.POST)
        if form.is_valid():
            maintenance = form.save(commit=False)
            maintenance.car = car
            maintenance.save()
            return redirect('car_detail', pk=car.pk)
    else:
        form = MaintenanceForm()
    return render(request, 'cars/car_detail.html', {
        'car': car,
        'maintenances': maintenances,
        'form': form,
    })

def add_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            car = form.save()
            return redirect('car_list')
    else:
        form = CarForm()
    return render(request, 'cars/add_car.html', {'form': form})

def edit_car(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if request.method == 'POST':
        form = CarColorForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('car_detail', pk=car.pk)
    else:
        form = CarColorForm(instance=car)
    return render(request, 'cars/edit_car.html', {
        'form': form,
        'car': car,
    })

