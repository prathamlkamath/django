from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Dummy data for pets
PETS = [
    {"id": 1, "name": "Bella", "breed": "Labrador", "age": 3, "description": "Friendly and loves to play fetch."},
    {"id": 2, "name": "Charlie", "breed": "Beagle", "age": 2, "description": "Energetic and great with kids."},
    {"id": 3, "name": "Max", "breed": "German Shepherd", "age": 4, "description": "Loyal and protective."},
]

ADOPTED_PETS = []  # List to store adopted pets


# View for listing pets
def pet_list(request):
    available_pets = [pet for pet in PETS if pet["id"] not in [p["id"] for p in ADOPTED_PETS]]
    return render(request, 'pets/pet_list.html', {"pets": available_pets})


# View for pet details
def pet_detail(request, pet_id):
    pet = next((pet for pet in PETS if pet["id"] == pet_id), None)
    return render(request, 'pets/pet_detail.html', {"pet": pet})


# View for showing adoption form
def adoption_form(request, pet_id):
    pet = next((pet for pet in PETS if pet["id"] == pet_id), None)
    return render(request, 'pets/adoption_form.html', {"pet": pet})


# View to handle adoption submission
@csrf_exempt
def adopt_pet(request, pet_id):
    if request.method == "POST":
        name = request.POST.get("name")
        pet = next((pet for pet in PETS if pet["id"] == pet_id), None)
        if pet:
            ADOPTED_PETS.append(pet)
            return render(request, 'pets/adopt_success.html', {"pet": pet, "owner": name})
    return JsonResponse({"status": "error", "message": "Adoption failed!"})
