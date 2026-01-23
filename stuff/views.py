import json
import csv
import zipfile
import io
from django.http import JsonResponse, HttpResponse
from django.views import View
from builds.models import BuildModel
from stuff.business import calculate_mp, get_list_data, return_all_data, get_base_mp
from stuff.models import Companion, Skill, Type, RuneType, SubRune, MainRune


class GetMPInfo(View):
    def post(self, request):
        try:
            equipment_data = json.loads(request.body)
        except (ValueError, KeyError):
            return JsonResponse({'error': 'Invalid request'}, status=400)

        return self.build_response(equipment_data)

    def build_response(self, equipment_data):
        companions_list, _, _, sub_rune_list = get_list_data(equipment_data)
        baseMp = get_base_mp(equipment_data)
        mp, maxMp = calculate_mp(companions_list, sub_rune_list, baseMp)
        response_data = {
            'mp': mp,
            'maxMp': maxMp
        }
        return JsonResponse(response_data)


class GetAllStuffData(View):
    def get(self, request):
        return JsonResponse(return_all_data())


class GetBuildInfo(View):
    def get(self, request, build_id):
        try:
            build = BuildModel.objects.get(pk=build_id)
        except BuildModel.DoesNotExist:
            return JsonResponse({"error": "Build does not exist"})
        return self.build_response(build)

    def build_response(self, build):
        equipment = build.build["equipment"]
        print(equipment)
        companions_list, skill_list, main_rune_list, sub_rune_list = get_list_data(equipment)
        baseMp = get_base_mp(equipment)
        mp, maxMp = calculate_mp(companions_list, sub_rune_list, baseMp)
        response_data = {
            'companions': companions_list,
            'skills': skill_list,
            'mainRunes': main_rune_list,
            'subRunes': sub_rune_list,
            'mp': mp,
            'maxMp': maxMp,
            'shoe': True if equipment.get("additionalMp", 0) > 0 else False
        }
        return JsonResponse(response_data)


def export_companions_csv(request):
    '''
    Exporte tous les compagnons en CSV
    '''
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="companions.csv"'
    
    writer = csv.writer(response)
    writer.writerow(['id', 'name', 'slug', 'rarity', 'base_mp', 'types', 'affected_skill'])
    
    for companion in Companion.objects.all().prefetch_related('types', 'affected_skill'):
        types_str = ', '.join([t.slug for t in companion.types.all()])
        affected_skill = companion.affected_skill.name if companion.affected_skill else ''
        writer.writerow([
            companion.id,
            companion.name,
            companion.slug,
            companion.rarity,
            companion.base_mp,
            types_str,
            affected_skill
        ])
    
    return response


def export_skills_csv(request):
    '''
    Exporte toutes les compétences en CSV
    '''
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="skills.csv"'
    
    writer = csv.writer(response)
    writer.writerow(['id', 'name', 'slug', 'rarity', 'description', 'cooldown', 'types'])
    
    for skill in Skill.objects.all().prefetch_related('types'):
        types_str = ', '.join([t.slug for t in skill.types.all()])
        writer.writerow([
            skill.id,
            skill.name,
            skill.slug,
            skill.rarity,
            skill.description,
            skill.cooldown,
            types_str
        ])
    
    return response


def export_types_csv(request):
    '''
    Exporte tous les types en CSV
    '''
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="types.csv"'
    
    writer = csv.writer(response)
    writer.writerow(['id', 'slug'])
    
    for type_obj in Type.objects.all():
        writer.writerow([
            type_obj.id,
            type_obj.slug
        ])
    
    return response


def export_runetypes_csv(request):
    '''
    Exporte tous les types de runes en CSV
    '''
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="runetypes.csv"'
    
    writer = csv.writer(response)
    writer.writerow(['id', 'name', 'values_required'])
    
    for rune_type in RuneType.objects.all():
        values_str = ', '.join(rune_type.values_required) if rune_type.values_required else ''
        writer.writerow([
            rune_type.id,
            rune_type.name,
            values_str
        ])
    
    return response


def export_subrunes_csv(request):
    '''
    Exporte toutes les sous-runes en CSV
    '''
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="subrunes.csv"'
    
    writer = csv.writer(response)
    writer.writerow(['id', 'name', 'slug', 'rarity', 'description', 'type', 'values'])
    
    for subrune in SubRune.objects.all().select_related('type'):
        type_name = subrune.type.name if subrune.type else ''
        values_str = ', '.join(subrune.values) if subrune.values else ''
        writer.writerow([
            subrune.id,
            subrune.name,
            subrune.slug,
            subrune.rarity,
            subrune.description,
            type_name,
            values_str
        ])
    
    return response


def export_mainrunes_csv(request):
    '''
    Exporte toutes les runes principales en CSV
    '''
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="mainrunes.csv"'
    
    writer = csv.writer(response)
    writer.writerow(['id', 'name', 'slug', 'rarity', 'description'])
    
    for mainrune in MainRune.objects.all():
        writer.writerow([
            mainrune.id,
            mainrune.name,
            mainrune.slug,
            mainrune.rarity,
            mainrune.description
        ])
    
    return response


def export_all_csv(request):
    '''
    Exporte tous les modèles de stuff dans un fichier ZIP
    '''
    zip_buffer = io.BytesIO()
    
    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        companions_buffer = io.StringIO()
        writer = csv.writer(companions_buffer)
        writer.writerow(['id', 'name', 'slug', 'rarity', 'base_mp', 'types', 'affected_skill'])
        for companion in Companion.objects.all().prefetch_related('types', 'affected_skill'):
            types_str = ', '.join([t.slug for t in companion.types.all()])
            affected_skill = companion.affected_skill.name if companion.affected_skill else ''
            writer.writerow([companion.id, companion.name, companion.slug, companion.rarity, companion.base_mp, types_str, affected_skill])
        zip_file.writestr('companions.csv', companions_buffer.getvalue())
        
        skills_buffer = io.StringIO()
        writer = csv.writer(skills_buffer)
        writer.writerow(['id', 'name', 'slug', 'rarity', 'description', 'cooldown', 'types'])
        for skill in Skill.objects.all().prefetch_related('types'):
            types_str = ', '.join([t.slug for t in skill.types.all()])
            writer.writerow([skill.id, skill.name, skill.slug, skill.rarity, skill.description, skill.cooldown, types_str])
        zip_file.writestr('skills.csv', skills_buffer.getvalue())
        
        types_buffer = io.StringIO()
        writer = csv.writer(types_buffer)
        writer.writerow(['id', 'slug'])
        for type_obj in Type.objects.all():
            writer.writerow([type_obj.id, type_obj.slug])
        zip_file.writestr('types.csv', types_buffer.getvalue())
        
        runetypes_buffer = io.StringIO()
        writer = csv.writer(runetypes_buffer)
        writer.writerow(['id', 'name', 'values_required'])
        for rune_type in RuneType.objects.all():
            values_str = ', '.join(rune_type.values_required) if rune_type.values_required else ''
            writer.writerow([rune_type.id, rune_type.name, values_str])
        zip_file.writestr('runetypes.csv', runetypes_buffer.getvalue())
        
        subrunes_buffer = io.StringIO()
        writer = csv.writer(subrunes_buffer)
        writer.writerow(['id', 'name', 'slug', 'rarity', 'description', 'type', 'values'])
        for subrune in SubRune.objects.all().select_related('type'):
            type_name = subrune.type.name if subrune.type else ''
            values_str = ', '.join(subrune.values) if subrune.values else ''
            writer.writerow([subrune.id, subrune.name, subrune.slug, subrune.rarity, subrune.description, type_name, values_str])
        zip_file.writestr('subrunes.csv', subrunes_buffer.getvalue())
        
        mainrunes_buffer = io.StringIO()
        writer = csv.writer(mainrunes_buffer)
        writer.writerow(['id', 'name', 'slug', 'rarity', 'description'])
        for mainrune in MainRune.objects.all():
            writer.writerow([mainrune.id, mainrune.name, mainrune.slug, mainrune.rarity, mainrune.description])
        zip_file.writestr('mainrunes.csv', mainrunes_buffer.getvalue())
    
    zip_buffer.seek(0)
    response = HttpResponse(zip_buffer.read(), content_type='application/zip')
    response['Content-Disposition'] = 'attachment; filename="stuff_export.zip"'
    return response
