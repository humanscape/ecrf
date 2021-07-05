from django.db import models

class Crf(models.Model):
    SEX_TYPE = ((1, 'Male'), (2, 'Female'), (3, 'All'))
    R_SEX_TYPE = {
        'Male': 1,
        'Female': 2,
        'All': 3,
        '남성(Male)': 1,
        '여성(Female)': 2,
        '둘다(Both)': 3,
    }

    date_at_evaluation = models.DateTimeField(auto_now=True, blank=True)
    patient_number = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=20, unique=True, blank=True)
    case_no = models.IntegerField(null=True, blank=True)
    family_no = models.IntegerField(null=True, blank=True)
    family_hx = models.IntegerField(null=True, blank=True)
    sex = models.IntegerField(choices=SEX_TYPE, null=True, blank=True)
    birth_date = models.DateField(auto_now=True, blank=True)
    date_at_dx = models.DateField(auto_now=True, blank=True)
    age_at_dx = models.IntegerField(null=True, blank=True)
    date_at_evaluation = models.DateField(auto_now=True, blank=True)
    age_at_evaluation = models.IntegerField(null=True, blank=True)

    dna = models.CharField(max_length=200, unique=True, blank=True)
    protein = models.CharField(max_length=200, unique=True, blank=True)
    domain = models.CharField(max_length=20, unique=True, blank=True)

    mutation_type = models.IntegerField(null=True, blank=True)
    inframe_deletion_or_insertion = models.IntegerField(null=True, blank=True)
    nf1_haploinsufficiency_type = models.IntegerField(null=True, blank=True)

    novel_mutation = models.BooleanField(default=False)

    cafe_au_lait_spots = models.IntegerField(null=True, blank=True)
    axillary_freckling = models.IntegerField(null=True, blank=True)
    cutaneous_neurofibromas = models.IntegerField(null=True, blank=True)
    wide_spread_diffuse_cutaneous_neurofibroma = models.IntegerField(null=True, blank=True)
    relative_macrocephaly = models.IntegerField(null=True, blank=True)
    lish_nodules = models.IntegerField(null=True, blank=True)

    height_at_dx = models.FloatField(null=True, blank=True)
    height_SDS = models.FloatField(null=True, blank=True)

    learning_difficulty = models.IntegerField(null=True, blank=True)
    adhd = models.IntegerField(null=True, blank=True)
    autism = models.IntegerField(null=True, blank=True)
    seizure = models.IntegerField(null=True, blank=True)
    hypertension = models.IntegerField(null=True, blank=True)
    cardiac_arrhthmia = models.IntegerField(null=True, blank=True)
    cardiac_myopathy = models.IntegerField(null=True, blank=True)

    _25_OH_vitamin_D = models.FloatField(null=True, blank=True)
    HEARING = models.IntegerField(null=True, blank=True)
    OTHER = models.IntegerField(null=True, blank=True)
    BRAIN_MR_DATE = models.IntegerField(null=True, blank=True)
    BRAIN_age_at_evaluation = models.IntegerField(null=True, blank=True)
    BRAIN_FINDINGS = models.TextField(null=True, blank=True)
    FASI = models.IntegerField(null=True, blank=True)

    plexiform_neurofibromas = models.IntegerField(null=True, blank=True)
    _3cm_above = models.IntegerField(null=True, blank=True)

    disfigurement = models.IntegerField(null=True, blank=True)
    aorta_bone_disruption_malignancy = models.IntegerField(null=True, blank=True)
    malignancy = models.IntegerField(null=True, blank=True)
    brain_tumor = models.IntegerField(null=True, blank=True)
    nerve_root_tumor = models.IntegerField(null=True, blank=True)
    malignant_peripheral_nerve_sheath_tumor = models.IntegerField(null=True, blank=True)
    moyamoya_ds = models.IntegerField(null=True, blank=True)
    osteopenia = models.IntegerField(null=True, blank=True)

    dysplasia_of_long_bone = models.IntegerField(null=True, blank=True)

    sphenoid_wing_dysplaisa = models.IntegerField(null=True, blank=True)
    vertebral_dysplasia = models.IntegerField(null=True, blank=True)

    dural_ectasia = models.IntegerField(null=True, blank=True)
    scoliosis = models.IntegerField(null=True, blank=True)

    breast_examination = models.IntegerField(null=True, blank=True)
    operation = models.IntegerField(null=True, blank=True)

    last_follow_up_date = models.IntegerField(null=True, blank=True)
    last_follow_up_age = models.FloatField(null=True, blank=True)

    updated_at = models.DateTimeField(auto_now=True, blank=True)  # 업데이트 시각
    created_at = models.DateTimeField(auto_now_add=True, blank=True)  # 생성 시각

