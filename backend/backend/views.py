from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connection
from .models import Countries, Locations


def home(request):
    countries = Countries.objects.all()
    locations = Locations.objects.all()

    context = {'countries': countries, 'locations': locations}
    return render(request, 'home.html', context)

def insert_record_country(request):
    return render(request,"countries.html")

def insert_record(request):
    countries = Countries.objects.all()
    return render(request, "locations.html", {'countries': countries})

def save_location(request):
    if request.method == 'POST':
        location_id = request.POST.get('location_id')
        street_address = request.POST.get('street_address')
        postal_code = request.POST.get('postal_code')
        city = request.POST.get('city')
        state_province = request.POST.get('state_province')
        country_id = request.POST.get('country_id')

        location = Locations(location_id=location_id, street_address=street_address,
                             postal_code=postal_code, city=city, state_province=state_province,
                             country_id=country_id)
        location.save()

        return redirect('home')
    else:
        return HttpResponse("Method Not Allowed")



def get_canada(request):

    # canada = Countries.objects.get(country_name='Canada')
    # locations = Locations.objects.filter(country_id=canada)
    # addresses = [location for location in locations]
    # context = {'addresses': addresses}
    # return render(request, 'canada.html', context)
    sql_query = """
    SELECT *
    FROM backend_locations
    JOIN backend_countries ON backend_locations.country_id = backend_countries.country_id
    WHERE backend_countries.country_name = 'Canada' or backend_locations.country_id='CA' ;
    """

    sql_query_without_join = """
    SELECT *
    FROM backend_locations
    WHERE backend_locations.country_id IN (
        SELECT backend_countries.country_id
        FROM backend_countries
        WHERE backend_countries.country_name = 'Canada'
    );
    """

    with connection.cursor() as cursor:
        cursor.execute(sql_query)
        canada_data = cursor.fetchall()
    print(canada_data)

    with connection.cursor() as cursor:
        cursor.execute(sql_query_without_join)
        canada_data_without_join = cursor.fetchall()
    print(canada_data_without_join)

    context = {'canada_data': canada_data,'canada_data_without_join':canada_data_without_join}
    return render(request, 'canada.html', context)

def save_country(request):
    if request.method == 'POST':
        country_id = request.POST.get('country_id')
        country_name = request.POST.get('country_name')
        region_id = request.POST.get('region_id')

        country = Countries(country_id=country_id, country_name=country_name, region_id=region_id)
        country.save()

        return redirect('home')
    else:
        return HttpResponse("Method Not Allowed")