from django.shortcuts import render

# Create your views here.
# lr 14
def home(request):
    return render(request, 'shop/home.html')

def about(request):
    return render(request, 'shop/about.html')

def author(request):
    return render(request, 'shop/author.html')

# lr 15
from django.http import JsonResponse
import json

def format_skill(skill_data):
    # форматируем данные для красивого вывода
    return {
        'ID': skill_data['pk'],
        'Код специальности': skill_data['fields']['code'],
        'Название': skill_data['fields']['title'],
        'Специальность': skill_data['fields']['specialty'],
        'Описание': skill_data['fields'].get('desc', 'Нет описания')
    }

def all_skills(request):
    # Список всех специальностей (/spec/)
    with open('dump.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        skills = [
            {
                'ID': item['pk'],
                'Код': item['fields']['code'],
                'Специальность': item['fields']['title'],
                'Ссылка': f"http://{request.get_host()}/spec/{item['pk']}/"
            } 
            for item in data if item['model'] == 'data.skill'
        ]
    return JsonResponse({'специальности': skills}, json_dumps_params={'ensure_ascii': False, 'indent': 4})

def skill_detail(request, id):
    # Детали специальности (/spec/<id>/)
    with open('dump.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        skill = next((item for item in data if item['model'] == 'data.skill' and item['pk'] == id), None)
    
    if skill:
        response_data = format_skill(skill)
        return JsonResponse(response_data, json_dumps_params={'ensure_ascii': False, 'indent': 4})
    return JsonResponse({'ошибка': 'Специальность не найдена'}, status=404)