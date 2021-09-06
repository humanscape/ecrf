from django.contrib import admin
from rangefilter.filter import DateRangeFilter
from .models import *


class CrfOperationsInline(admin.TabularInline):
    model = CrfOperations
    fields = (
        'crf','no','date','age','status','reason','method'
    )
    readonly_fields = (
        'age',
    )
    extra = 1


@admin.register(Crf)
class CrfAdmin(admin.ModelAdmin):
    inlines = (CrfOperationsInline, )

    list_display = (
        'date_at_evaluation_diagnosis',
        'patient_number',
        'name',
        'case_no',
        'family_no',
        'family_hx',
        'sex',

        'birth_date',
        'age',
        'date_at_dx',
        'age_at_dx',

        'date_at_evaluation_dna',
        'age_at_evaluation',
        'dna',
        'protein',
        'domain',
        'mutation_type',
        'inframe_deletion_or_insertion',
        'nf1_haploinsufficiency_type',
        'novel_mutation',

        'cafe_au_lait_spots',
        'axillary_freckling',
        'cutaneous_neurofibromas',
        'wide_spread_diffuse_cutaneous_neurofibroma',
        'relative_macrocephaly',
        'lish_nodules',

        'height_at_dx',
        'height_SDS',

        'learning_difficulty',
        'adhd',
        'autism',
        'seizure',
        'hypertension',
        'cardiac_arrhthmia',
        'cardiac_myopathy',

        '_25_OH_vitamin_D',
        'HEARING',
        'OTHER',
        'BRAIN_MR_DATE',
        'BRAIN_age_at_evaluation',
        'BRAIN_FINDINGS',
        'FASI',

        'FASI_FINDINGS',
        'optic_pathway_glioma',
        'Vascular_anomaly',
        'SPINE_MR_DATE',
        'Age_at_Spine_MR',
        'Age_at_Spine_MR_FINDINGS',

        'Whole_body_MR_DATE',
        'Age_at_Whole_body_MR',
        'Age_at_Whole_body_MR_FINDINGS',
        
        'plexiform_neurofibromas',
        'plexiform_neurofibromas_3cm_above',

        'disfigurement',
        'aorta_bone_disruption_malignancy',
        'malignancy',
        'brain_tumor',
        'nerve_root_tumor',
        'malignant_peripheral_nerve_sheath_tumor',
        'moyamoya_ds',
        'osteopenia',

        'dysplasia_of_long_bone',

        'sphenoid_wing_dysplaisa',
        'vertebral_dysplasia',

        'dural_ectasia',
        'scoliosis',

        'breast_examination',
        'operation',

        'last_follow_up_date',
        'last_follow_up_age',

        'updated_at',
        'created_at',

    )
    readonly_fields = (
        'age',
        'age_at_dx',
        'age_at_evaluation',
        'BRAIN_age_at_evaluation',
        'Age_at_Spine_MR',
        'Age_at_Whole_body_MR',
        
        'updated_at',
        'created_at',
    )
    fields = list_display
    list_display_links = fields
    list_filter = fields

