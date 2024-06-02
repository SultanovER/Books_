from django.shortcuts import render
from .models import Cloth, TagCloth

def all_cloth(request):
    all_cloth = Cloth.objects.all()
    tags = TagCloth.objects.all()
    return render(request, 'cloth/all_cloth.html', {'all_cloth': all_cloth, 'tags': tags})

def filtered_cloth(request, tag_id):
    tag = TagCloth.objects.get(id=tag_id)
    filtered_cloth = Cloth.objects.filter(tag=tag)
    tags = TagCloth.objects.all()
    return render(request, 'cloth/filtered_cloth.html', {'filtered_cloth': filtered_cloth, 'tags': tags})
