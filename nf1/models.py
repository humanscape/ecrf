from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime, date
from django.utils.safestring import mark_safe
from django.core.validators import FileExtensionValidator
from django.forms import SelectMultiple
from django.contrib.postgres.fields import ArrayField

from encrypted_fields.fields import *

from .assets import CALCULATE_AGE_FIELDS
from common.utils import calculate_age

# TODO: 코드 중복이므로 합쳐야함..... deprecated 예정이라 이렇게 둠
class ArraySelectMultiple(SelectMultiple):

    def value_omitted_from_data(self, data, files, name):
        return False


class ChoiceArrayField(ArrayField):
    """
    A field that allows us to store an array of choices.

    Uses Django 1.9's postgres ArrayField
    and a MultipleChoiceField for its formfield.

    Usage:

        choices = ChoiceArrayField(models.CharField(max_length=...,
                                                    choices=(...,)),
                                   default=[...])
    """

    def formfield(self, **kwargs):
        defaults = {
            'form_class': forms.TypedMultipleChoiceField,
            'choices': self.base_field.choices,
            'widget': forms.CheckboxSelectMultiple,

        }
        defaults.update(kwargs)

        # Skip our parent's formfield implementation completely as we don't
        # care for it.
        # pylint:disable=bad-super-call
        return super(ArrayField, self).formfield(**defaults)

    def validate(self, value, model_instance):
        if not self.editable:
            # Skip validation for non-editable fields.
            return

        if self.choices is not None and value not in self.empty_values:
            if set(value).issubset({option_key for option_key, _ in self.choices}):
                return
            raise exceptions.ValidationError(
                self.error_messages["invalid_choice"],
                code="invalid_choice",
                params={"value": value},
            )

        if value is None and not self.null:
            raise exceptions.ValidationError(self.error_messages["null"], code="null")

        if not self.blank and value in self.empty_values:
            raise exceptions.ValidationError(self.error_messages["blank"], code="blank")


class Crf(models.Model):
    patient_number = models.PositiveIntegerField('Patient No.', null=True, blank=True, help_text='환자 번호')
    icf_date = models.DateField('ICF date', null=True, blank=True, help_text='연구 동의서 취득일')
    birth_year_and_month = EncryptedDateField('Birth year and month', null=True, blank=True,
                                              help_text='생년월일<br/>입력시 오늘 날짜 기준으로 나이가 입력됩니다.')
    # AUTO
    age = models.IntegerField('Age', null=True, blank=True, help_text='나이')

    date_at_dx = models.DateField('Date at Dx.', null=True, blank=True, help_text='진단 받은 날짜<br/>입력시 진단시의 나이가 입력됩니다.')

    # AUTO
    age_at_dx = models.IntegerField('Age at Dx.', null=True, blank=True, help_text='진단시 나이')

    sex = models.IntegerField('Sex', choices=[(i, i) for i in range(4)], null=True, blank=True,
                              help_text='성별<br/>0 : 남자<br/>1 : 여자<br/>2 : 전부<br/>3 : 모름')

    family_hx = models.IntegerField('Family Hx.', choices=[(i, i) for i in range(3)], null=True, blank=True,
                                    help_text='가족 병력<br/>0: 없음<br/>1: 있음<br/>2: 모름')
    familyhistory_diagnosis = models.IntegerField('familyhistory_diagnosis', choices=[(i, i) for i in range(4)], null=True, blank=True,
                                    help_text='0: 부<br/>1: 모<br/>2: 형제<br/>3: 자녀')


    date_at_evaluation = models.DateField('Date at evaluation ', null=True, blank=True,
                                          help_text='유전자 검사 날짜<br/>입력시 유전자 검사시의 나이가 입력됩니다.')
    # AUTO
    age_at_evaluation = models.IntegerField('Age at evaluation', null=True, blank=True, help_text='유전자 검사시 나이')

    nf1_mutation = models.IntegerField('NF1 mutation', choices=[(i, i) for i in range(2)], null=True, blank=True,
                                       help_text='NF1 돌연변이<br/>0 : 없음<br/>1 : 있음')
    dna = models.CharField('DNA', max_length=200, null=True, blank=True, help_text='유전자 변이 (DNA)<br/>예제 c.7126G>C')
    protein = models.CharField('Protein', max_length=200, null=True, blank=True, help_text='유전자 변이 (Protein)<br/>예제 p.Gly2376Arg')
    domain = models.IntegerField('Domain', choices=[(i, i) for i in range(1, 7)], null=True, blank=True,
                                 help_text='도메인<br/>1 : Cysteine/serine rich domain with three cystein pairs (CSRD)<br/>- ATP binding, cAMP- dependent protein kinase (PKA) recognition site<br/>- exon 11-17,<br/>- p. 543-909<br/><br/>2 : Tub<br/> - p. 1095-1176<br/><br/>3 : GTPase- activating protein (GAP) related domain (GRD)<br/> - catalytic RasGAP activity<br/> - exon20-27a, <br/>-  p. 1198-1530<br/><br/>4 : Sec14-line lipid binding domain<br/> - p. 1560 – 1698<br/><br/>5 : Pleckstin homology(PH) like domain<br/> - p. 1713 – 1816<br/><br/>6 : Syn<br/> - p. 2619 – 2719')
    mutation_type = models.IntegerField('Mutation type', choices=[(i, i) for i in range(1, 6)], null=True, blank=True,
                                        help_text='돌연변이 유형<br/>1 : Missense<br/>2 : Nonsense<br/>3 : Frameshift<br/>4 : Splicing<br/>5 : Large deletion')
    inframe_deletion_or_insertion = models.IntegerField('Inframe deletion or insertion',
                                                        choices=[(i, i) for i in range(3)], null=True, blank=True,
                                                        help_text='인프레임 삭제 또는 삽입 (유전자 전사와 번역 과정이 중지되지 않음)<br/>0 : 없음<br/>1 : 있음<br/>2 : 모름')
    nf1_haploinsufficiency_type = models.IntegerField('NF1 haploinsufficiency type', choices=[(i, i) for i in range(3)],
                                                      null=True, blank=True,
                                                      help_text='반수체 부족 유형<br/>0 : 없음<br/>1 : 있음<br/>2 : 모름')
    novel_mutation = models.IntegerField('Novel mutation', choices=[(i, i) for i in range(3)], null=True, blank=True,
                                         help_text='드 노보 유전자 돌연변이 (유전성이 아닌 돌연변이)<br/>0 : 없음<br/>1 : 있음<br/>2 : 모름')
    clinical_findings = models.TextField('Clinical Findings', null=True, blank=True, help_text='임상 소견')
    cafe_au_lait_spots = models.IntegerField(mark_safe('Café au lait spots [ >6 and >(0.5 cm or 1.5 cm)]'),
                                             choices=[(i, i) for i in range(3)], null=True, blank=True,
                                             help_text='커피색의 반점<br/>0 : 없음<br/>1 : 있음<br/>2 : 모름')
    axillary_freckling = models.IntegerField('Axillary Freckling', choices=[(i, i) for i in range(3)], null=True,
                                             blank=True,
                                             help_text='겨드랑이 부위 주근깨 (임상학적 진단)<br/>0 : 없음<br/>1 : 있음<br/>2 : 모름')
    cutaneous_neurofibromas = models.IntegerField('Cutaneous neurofibromas', choices=[(i, i) for i in range(3)],
                                                  null=True, blank=True,
                                                  help_text='피부신경섬유종 (피부표면에 나타나는 종양; 임상학적 진단)<br/>0 : 없음<br/>1 : 있음<br/>2 : 모름')
    wide_spread_diffuse_cutaneous_neurofibroma = models.IntegerField('Wide spread diffuse cutaneous neurofibroma',
                                                                     choices=[(i, i) for i in range(3)], null=True,
                                                                     blank=True,
                                                                     help_text='피하신경섬유종 (진피와 지방층 사이에 나타나는 종양; 임상학적 진단)<br/>0 : 없음<br/>1 : 있음<br/>2 : 모름')
    relative_macrocephaly = models.IntegerField('Relative macrocephaly', choices=[(i, i) for i in range(3)], null=True,
                                                blank=True,
                                                help_text='상대적 대두증 (성조숙증으로 인한 평균 이상의 머리둘레; 신체적 평가)<br/>0 : 없음<br/>1 : 있음<br/>2 : 모름')
    lish_nodules = models.IntegerField('Lish nodules', choices=[(i, i) for i in range(3)], null=True, blank=True,
                                       help_text='홍채에 작고 색조를 띈 과오종인 리쉬결절 (안과적 평가)<br/>0 : 없음<br/>1 : 있음<br/>2 : 모름')
    height_at_dx = models.PositiveIntegerField('Height at Dx', null=True, blank=True,
                                               help_text='진단시 환자의 키 (신체적 평가)<br/>단위 cm')
    height_sds = models.DecimalField('Height (SDS)', max_digits=10, decimal_places=2, null=True, blank=True,
                                     help_text='상대적 키 (신체적 평가, SD score)')
    learning_difficulty = models.IntegerField('Learning difficulty', choices=[(i, i) for i in range(3)], null=True,
                                              blank=True, help_text='학습장애 (심리학적 평가)<br/>0 : 없음<br/>1 : 있음<br/>2 : 모름')
    adhd = models.IntegerField('ADHD', choices=[(i, i) for i in range(3)], null=True, blank=True,
                               help_text='주의력결핍 과잉행동장애 (심리학적 평가)<br/>0 : 없음<br/>1 : 있음<br/>2 : 모름')
    autism = models.IntegerField('Autism', choices=[(i, i) for i in range(3)], null=True, blank=True,
                                 help_text='자폐증 (임상학적 평가)<br/>0 : 없음<br/>1 : 있음<br/>2 : 모름')
    seizure = models.IntegerField('Seizure', choices=[(i, i) for i in range(3)], null=True, blank=True,
                                  help_text='발작 (임상학적 평가)<br/>0 : 없음<br/>1 : 있음<br/>2 : 모름')
    hypertension = models.IntegerField('Hypertension', choices=[(i, i) for i in range(3)], null=True, blank=True,
                                       help_text='고혈압 (임상학적 평가)<br/>0 : 없음<br/>1 : 있음<br/>2 : 모름')
    cardiac_arrhythmia = models.IntegerField('Cardiac arrhythmia', choices=[(i, i) for i in range(3)], null=True,
                                             blank=True, help_text='심장 부정맥 (임상학적 평가)<br/>0 : 없음<br/>1 : 있음<br/>2 : 모름')
    arrhythmia_treatment = models.TextField('Arrhythmia treatment', null=True, blank=True,
                                                help_text='부정맥 치료에 사용된 의료 시술/기술')

    cardiac_myopathy = models.IntegerField('Cardiac myopathy', choices=[(i, i) for i in range(3)], null=True,
                                           blank=True, help_text='심장 근병증 (영상학적 소견)<br/>0 : 없음<br/>1 : 있음<br/>2 : 모름')
    cardiac_myopathy_findings = models.TextField('Cardiac myopathy Findings', null=True, blank=True, help_text='이상 소견')

    oh_25_vitamin_d = models.IntegerField('25-OH vitamin D 시행여부', choices=[(i, i) for i in range(2)], null=True,
                                          blank=True, help_text='25-하이드록시 비타민 D 검사 시행 여부<br/>0 : 미시행<br/>1 : 시행')
    oh_25_vitamin_d_1 = models.DecimalField('25-OH vitamin D', max_digits=10, decimal_places=2, null=True,
                                          blank=True, help_text='25-하이드록시 비타민 D 검사 수치<br/>단위 ng/mL')

    hearing_difficulty = models.IntegerField('Hearing difficulty', choices=[(i, i) for i in range(3)], null=True,
                                             blank=True, help_text='청력 장애 (신경학적 판단)<br/>0 : 없음<br/>1 : 있음<br/>2 : 모름')
    other = models.TextField('Other', null=True, blank=True, help_text='기타')

    brain_mr = models.IntegerField('Brain MR 시행 여부', choices=[(i, i) for i in range(2)], null=True,
                                           blank=True, help_text='Brain MR 시행 여부<br/>0 : 미시행<br/>1 : 시행')
    brain_mr_date = models.DateField('Date at Brain MR ', null=True, blank=True,
                                     help_text='뇌 MR 촬영 날짜<br/>입력시 뇌 MR 촬영시 나이가 입력됩니다.')
    # AUTO
    age_at_brain_mr = models.IntegerField('Age at Brain MR', null=True, blank=True, help_text='뇌 MR 촬영시 나이')
    mr_findings = models.TextField('Brain MR Findings', null=True, blank=True, help_text='뇌 MR 스캔 결과 기술 (영상학적 판단)')

    fasi = models.IntegerField('FASI (focal areas of signal intensity)', choices=[(i, i) for i in range(3)], null=True,
                               blank=True,
                               help_text='고음영 병변 (unidentified bright objects, UBO; 임상적 판단)<br/>0 : 없음<br/>1 : 있음<br/>2 : 모름')
    fasi_findings = models.CharField('FASI Findings', max_length=200, null=True, blank=True, help_text='FASI  발견 부위 (영상학적 판단)')
    optic_pathway_glioma = models.IntegerField('Optic pathway glioma', choices=[(i, i) for i in range(3)], null=True,
                                               blank=True, help_text='시신경교종 (안과적 진단)<br/>0 : 없음<br/>1 : 있음<br/>2 : 모름')
    vascular_anomaly = models.IntegerField('Vascular anomaly', choices=[(i, i) for i in range(3)], null=True,
                                           blank=True,
                                           help_text='혈관 이상 (영상학적/흉부외과적 진단)<br/>0 : 없음<br/>1 : 있음<br/>2 : 모름')

    spine_mr = models.IntegerField('Spine MR 시행여부', choices=[(i, i) for i in range(2)], null=True,
                                   blank=True, help_text='척추 MR 시행 여부<br/>0 : 미시행<br/>1 : 시행')

    spine_mr_date = models.DateField('Data at Spine MR ', null=True, blank=True,
                                     help_text='척추 MR 스캔 촬영 날짜<br/>입력시 척추 MR 촬영시 나이가 입력됩니다.')
    # AUTO
    age_at_spine_mr = models.IntegerField('Age at Spine MR', null=True, blank=True, help_text='척추 MR 촬영시 나이')
    age_at_spine_mr_findings = models.TextField('Spine MR Findings', null=True, blank=True,
                                                help_text='척추 MR 스캔 결과 기술 (영상학적 판단)')

    whole_body_mr = models.IntegerField('Whole body MR', choices=[(i, i) for i in range(2)], null=True,
                                   blank=True, help_text='Whole body MR 시행 여부<br/>0 : 미시행<br/>1 : 시행')

    whole_body_mr_date = models.DateField('Data at Whole body MR ', null=True, blank=True,
                                          help_text='전신 MR 촬영 날짜<br/>입력시 전신 MR 촬영시 나이가 입력됩니다.')
    # AUTO
    age_at_whole_body_mr = models.IntegerField('Age at Whole body MR', null=True, blank=True,
                                                       help_text='전신 MR 촬영시 나이')
    age_at_whole_body_mr_findings = models.TextField('Whole body MR findings', null=True, blank=True,
                                                      help_text='전신 MR 촬영 결과 기술 (영상학적 판단)')
    plexiform_neurofibromas = models.IntegerField('Plexiform neurofibromas', choices=[(i, i) for i in range(3)],
                                                  null=True, blank=True,
                                                  help_text='총상신경섬유종 (임상학적 진단)<br/>0 : 없음<br/>1 : 있음<br/>2 : 모름')
    plexiform_neurofibromas_3 = models.IntegerField('Plexiform neurofibromas (>=3cm)',
                                                    choices=[(i, i) for i in range(3)], null=True, blank=True,
                                                    help_text='총상신경섬유종 (3cm 이상; 임상학적 진단)<br/>0 : 없음<br/>1 : 있음<br/>2 : 모름')
    disfigurement = models.IntegerField('Disfigurement', choices=[(i, i) for i in range(3)], null=True, blank=True,
                                        help_text='이형성증<br/>0 : 없음<br/>1 : 있음<br/>2 : 모름')
    aorta_bone_disruption_malignancy = models.IntegerField('위험한 부위(aorta, bone disruption, malignancy) 침범 여부',
                                                           choices=[(i, i) for i in range(3)], null=True, blank=True,
                                                           help_text='위험한 부위의 이형성증<br/>0 : 없음<br/>1 : 있음<br/>2 : 모름')
    painful_accompanying = models.IntegerField('통증 동반', choices=[(i, i) for i in range(3)], null=True, blank=True,
                                               help_text='통증 동반<br/>0 : 없음<br/>1 : 있음<br/>2 : 모름')
    malignancy = models.IntegerField('Malignancy', choices=[(i, i) for i in range(3)], null=True, blank=True,
                                     help_text='악성 종양<br/>0 : 없음<br/>1 : 있음<br/>2 : 모름')
    brain_tumor = models.IntegerField('Brain tumor', choices=[(i, i) for i in range(3)], null=True, blank=True,
                                      help_text='뇌종양<br/>0 : 없음<br/>1 : 있음<br/>2 : 모름')
    nerve_root_tumor = models.IntegerField('Nerve root tumor', choices=[(i, i) for i in range(3)], null=True,
                                           blank=True, help_text='신경근 종양 <br/>0 : 없음<br/>1 : 있음<br/>2 : 모름')
    malignant_peripheral_nerve_sheath_tumor = models.IntegerField('Malignant peripheral nerve sheath tumor',
                                                                  choices=[(i, i) for i in range(3)], null=True,
                                                                  blank=True,
                                                                  help_text='악성 말초신경 수초 종양<br/>0 : 없음<br/>1 : 있음<br/>2 : 모름')
    moyamoya_disease = models.IntegerField('Moyamoya disease', choices=[(i, i) for i in range(3)], null=True,
                                           blank=True, help_text='모야모야 진단 (합병증)<br/>0 : 없음<br/>1 : 있음<br/>2 : 모름')

    bmd = models.IntegerField('BMD 시행여부', choices=[(i, i) for i in range(2)], null=True, blank=True,
                                               help_text='골밀도<br/>0 : 미시행<br/>1 : 시행')
    bmd_1 = models.IntegerField('BMD', choices=[(i, i) for i in range(3)], null=True, blank=True,
                                     help_text='골밀도(정형외과적 판단)<br/>0 : 정상<br/>1 : 골감소증<br/>2 : 골다공증')

    spine_z_score = models.DecimalField('Spine (z score)', max_digits=10, decimal_places=2, null=True, blank=True,
                                        help_text='척추 (통계학적 수치)')
    femur_z_score = models.DecimalField('Femur (z score)', max_digits=10, decimal_places=2, null=True, blank=True,
                                        help_text='대퇴골 (통계학적 수치)')
    dysplasia_of_long_bone = models.IntegerField('Dysplasia of long bone', choices=[(i, i) for i in range(3)],
                                                 null=True, blank=True,
                                                 help_text='경골의 이형성증<br/>0 : 없음<br/>1 : 있음<br/>2 : 모름')
    dysplasia_of_long_bone_location = models.CharField('Dysplasia of long bone location', max_length=200, null=True, blank=True,
                                                       help_text='관찰 부위')
    sphenoid_wing_dysplaisa = models.IntegerField('Sphenoid wing dysplaisa', choices=[(i, i) for i in range(3)],
                                                  null=True, blank=True,
                                                  help_text='접형골의 비정상적인 발달 및 형성부전<br/>0 : 없음<br/>1 : 있음<br/>2 : 모름')
    vertebral_dysplasia = models.IntegerField('Vertebral dysplasia', choices=[(i, i) for i in range(3)], null=True,
                                              blank=True, help_text='척추 이형서증 (신체적 평가)<br/>0 : 없음<br/>1 : 있음<br/>2 : 모름')
    dural_ectasia = models.IntegerField('Dural ectasia', choices=[(i, i) for i in range(3)], null=True, blank=True,
                                        help_text='경막 확장증<br/>0 : 없음<br/>1 : 있음<br/>2 : 모름')
    scoliosis = models.IntegerField('Scoliosis', choices=[(i, i) for i in range(3)], null=True, blank=True,
                                    help_text='척추측만증 (신체적 평가)<br/>0 : 없음<br/>1 : 있음<br/>2 : 모름')
    breast_examination = models.IntegerField('Breast examination', choices=[(i, i) for i in range(2)], null=True,
                                             blank=True, help_text='유방 초음파 검사<br/>0 : 미시행<br/>1 : 시행')
    date_at_breast_usg = models.DateField('Date at breast USG', null=True, blank=True,
                                          help_text='유방 초음파 검사 날짜<br/>입력시 유방 초음파 검사시 나이가 입력됩니다.')
    # AUTO
    age_at_breast_usg = models.IntegerField('Age at breast USG', null=True, blank=True,
                                                    help_text='유방 초음파 검사시 나이')
    birads_i_ii_iii_iv = models.IntegerField('BIRADS I/II/III/IV', choices=[(i, i) for i in range(1, 5)], null=True,
                                             blank=True,
                                             help_text='질환 경과  단계<br/>1 : BIRADS I<br/>2 : BIRADS II<br/>3 ; BIRADS III<br/>4 : BIRADS IV')
    breast_usg_findings = models.TextField('Breast USG Findings', null=True, blank=True,
                                           help_text='유방 검사 결과 기술 (외과학적/영상학적 판단)')
    biopsy = models.IntegerField('Biopsy', choices=[(i, i) for i in range(2)], null=True, blank=True,
                                 help_text='조직검사 <br/>0 : 미시행<br/>1 : 시행')
    biopsy_findings = models.TextField('Biopsy Findings', null=True, blank=True, help_text='조직검사 결과')
    operation = models.IntegerField('Operation', choices=[(i, i) for i in range(3)], null=True, blank=True,
                                    help_text='수술 유무<br/>0 : 없음<br/>1 : 있음<br/>2 : 모름')
    number_of_operations = models.PositiveIntegerField('Number of operations', null=True, blank=True, help_text='수술 횟수')

    last_fu_date = models.DateField('Date at last f/u ', null=True, blank=True,
                                    help_text='최근 재진/팔로업 날짜<br/>최근 재진/팔로업 날짜 입력시 최근 재진/팔로업시 나이가 입력됩니다.')
    # AUTO
    last_fu_age = models.IntegerField('Age at last f/u ', null=True, blank=True, help_text='최근 재진/팔로업시 나이')

    updated_at = models.DateTimeField(auto_now=True, blank=True)  # 업데이트 시각
    created_at = models.DateTimeField(auto_now_add=True, blank=True)  # 생성 시각

    def save(self, *args, **kwargs):
        fields = self._meta.get_fields()
        for field in fields:
            if field.name in CALCULATE_AGE_FIELDS['crf'].keys():
                if field.name == 'age':
                    setattr(self, field.name, calculate_age(datetime.now(), self.birth_year_and_month))
                else:
                    setattr(self, field.name, calculate_age(getattr(self, CALCULATE_AGE_FIELDS['crf'][field.name]), self.birth_year_and_month))
        super(Crf, self).save(*args, **kwargs)


class CrfOperations(models.Model):
    crf = models.ForeignKey('Crf', related_name='crfOperations', on_delete=models.CASCADE)
    no = models.PositiveIntegerField('수술 번호', null=True, blank=True, help_text='수술 번호')
    date = models.DateField('수술 시기', null=True, blank=True, help_text='수술 시기<br/>수술시기 입력시 나이가 입력됩니다.')
    age = models.IntegerField('수술 나이', null=True, blank=True, help_text='수술 나이')
    status = models.CharField('수술 부위', max_length=200, null=True, blank=True, help_text='수술 부위')
    reason = models.TextField('수술 이유', null=True, blank=True, help_text='수술 이유')
    method = models.CharField('완전절제/부분절제', max_length=200, null=True, blank=True, help_text='완전절제/부분절제')

    def save(self, *args, **kwargs):
        self.age = calculate_age(self.date, self.crf.birth_year_and_month)

        super(CrfOperations, self).save(*args, **kwargs)


    class Meta:
        verbose_name = "Operations"
        verbose_name_plural = "Operations"