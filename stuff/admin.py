from django.contrib import admin
from stuff.models import Companion, MainRune, SubRune, Skill
from django.utils.safestring import mark_safe
# from django import forms


class CompanionAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display = (
        "name",
        "slug",
        "rarity",
        "base_mp",
        "display_types",
        "affected_skill_name",
    )
    filter_horizontal = ("types",)
    ordering = ("id",)

    def affected_skill_name(self, obj):
        return obj.affected_skill.name if obj.affected_skill else '-'
    affected_skill_name.short_description = 'Affected Skill'

    def display_types(self, obj):
        return ", ".join([type.slug for type in obj.types.all()])
    display_types.short_description = 'Types'


admin.site.register(Companion, CompanionAdmin)


class SkillAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display = (
        "name",
        "slug",
        "rarity",
        "description",
        "cooldown",
        "display_types"
    )
    filter_horizontal = ("types",)
    ordering = ("id",)

    def display_types(self, obj):
        return ", ".join([type.slug for type in obj.types.all()])
    display_types.short_description = 'Types'


admin.site.register(Skill, SkillAdmin)


# class RuneAdminForm(forms.ModelForm):
#     class Meta:
#         model = SubRune
#         fields = '__all__'
#         widgets = {
#             'values': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
#         }

#     def __init__(self, *args, **kwargs):
#         super(RuneAdminForm, self).__init__(*args, **kwargs)
#         self.fields['values'].help_text = mark_safe("""
#         <div>
#             <p>Be sure to include the right values :</p>
#             <ul>
#                 <li>'increase_crit_percent': ["percentage"],</li>
#                 <li>'atk_boost': ["percentage"],</li>
#                 <li>'fish_dmg_boost': ["percentage"],</li>
#                 <li>'boss_dmg': ["percentage"],</li>
#                 <li>'crit_dmg_boost': ["percentage"],</li>
#                 <li>'triple_shot': ["percentage"],</li>
#                 <li>'double_shot': ["percentage"],</li>
#                 <li>'increase_all_dmg_per_companion_type': ["percentage", "companion_type"],</li>
#                 <li>'increase_skill_type_dmg_per_companion_type': ["percentage", "type"],</li>
#                 <li>'reduce_mp_for_companion_type_and_rarity': ["mp_reduction", "type", "rarity"],</li>
#                 <li>'increase_skill_rarity_dmg_per_companion_rarity': ["percentage", "skill_rarity", "companion_rarity"],</li>
#                 <li>'increase_final_dmg_after_skill': ["percentage", "duration", "skill_type"],</li>
#                 <li>'increase_deal_ratio_per_companion_type': ["percentage", "type"],</li>
#                 <li>'increase_crit_dmg_boost_per_companion_type': ["percentage", "type"],</li>
#                 <li>'increase_crit_dmg_per_companion_type': ["percentage", "type"],</li>
#                 <li>'increase_max_mp': ["mp_increase"]</li>
#             </ul>
#         </div>
#         """)

class MainRuneAdmin(admin.ModelAdmin):
    # form = RuneAdminForm
    search_fields = ["name"]
    list_display = (
        "name",
        "slug",
        "rarity",
        "description",
        # "display_types",
        # "values",
    )

    ordering = ("id",)

    def display_types(self, obj):
        """Retourne une représentation des types liés à ce compagnon."""
        return ", ".join([type_.name for type_ in obj.types.all()[:5]]) + ('...' if obj.types.count() > 5 else '')
    display_types.short_description = 'Types'


admin.site.register(MainRune, MainRuneAdmin)


class SubRuneAdmin(admin.ModelAdmin):
    # form = RuneAdminForm
    search_fields = ["name"]
    list_display = (
        "name",
        "slug",
        "rarity",
        "description",
        "type",
        "values",
    )

    ordering = ("id",)


admin.site.register(SubRune, SubRuneAdmin)
