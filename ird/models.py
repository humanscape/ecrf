from django.db import models
from django.core.validators import FileExtensionValidator
from datetime import datetime
from django import forms
from django.forms import SelectMultiple
from encrypted_fields.fields import *
from django.contrib.postgres.fields import ArrayField
from .assets import CALCULATE_AGE_FIELDS
from common.utils import calculate_age
from django.core import exceptions

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

class Ird(models.Model):
    SEX_TYPE = ((1, 'Male'), (2, 'Female'), (3, 'All'))
    SORTATION_TYPE = ((1,1), (2,2))

    case_no = models.PositiveIntegerField('차트번호', null=True, blank=True)
    name = EncryptedCharField('성명', max_length=20, null=True, blank=True)
    birth_year_and_month = EncryptedDateField('생년월일', null=True, blank=True)
    sex = models.PositiveIntegerField('SEX', choices=SEX_TYPE, null=True, blank=True)
    finding = models.TextField('특이사항', null=True, blank=True)
    sortation = models.PositiveIntegerField('구분', choices=SORTATION_TYPE, null=True, blank=True)
    
    ARK_SPH = models.DecimalField('ARK_SPH', max_digits=10, decimal_places=2, null=True, blank=True)
    ARK_CYL = models.DecimalField('ARK_CYL', max_digits=10, decimal_places=2, null=True, blank=True)
    ARK_AXIS = models.DecimalField('ARK_AXIS', max_digits=10, decimal_places=2, null=True, blank=True)
    ARK_K1 = models.DecimalField('ARK_K1', max_digits=10, decimal_places=2, null=True, blank=True)
    ARK_K2 = models.DecimalField('ARK_K2', max_digits=10, decimal_places=2, null=True, blank=True)
    ARK_KM = models.DecimalField('ARK_KM', max_digits=10, decimal_places=2, null=True, blank=True)
    ARK_K_cyl = models.DecimalField('ARK_K(cyl)', max_digits=10, decimal_places=2, null=True, blank=True)
    ARK_K_Axis = models.DecimalField('ARK_K(Axis)', max_digits=10, decimal_places=2, null=True, blank=True)
    UDVA = models.DecimalField('UDVA', max_digits=10, decimal_places=2, null=True, blank=True)
    UNVA = models.DecimalField('UNVA', max_digits=10, decimal_places=2, null=True, blank=True)
    CDVA = models.DecimalField('CDVA', max_digits=10, decimal_places=2, null=True, blank=True)
    CNVA = models.DecimalField('CNVA', max_digits=10, decimal_places=2, null=True, blank=True)
    IOP = models.DecimalField('IOP', max_digits=10, decimal_places=2, null=True, blank=True)
    OCT_CST = models.DecimalField('OCT_CST', max_digits=10, decimal_places=2, null=True, blank=True)
    Cones_a = models.DecimalField('Cones_a', max_digits=10, decimal_places=2, null=True, blank=True)
    Cones_b = models.DecimalField('Cones_b', max_digits=10, decimal_places=2, null=True, blank=True)
    Flicker = models.DecimalField('Flicker', max_digits=10, decimal_places=2, null=True, blank=True)
    Pattern_N35_mono = models.DecimalField('Pattern_N35(단안)', max_digits=10, decimal_places=2, null=True, blank=True)
    Pattern_P50_mono = models.DecimalField('Pattern_P50(단안)', max_digits=10, decimal_places=2, null=True, blank=True)
    Pattern_N95_mono = models.DecimalField('Pattern_N95(단안)', max_digits=10, decimal_places=2, null=True, blank=True)
    Pattern_N35_bi = models.DecimalField('Pattern_N35(양안)', max_digits=10, decimal_places=2, null=True, blank=True)
    Pattern_P50_bi = models.DecimalField('Pattern_P50(양안)', max_digits=10, decimal_places=2, null=True, blank=True)
    Pattern_N95_bi = models.DecimalField('Pattern_N95(양안)', max_digits=10, decimal_places=2, null=True, blank=True)
    Rods_a = models.DecimalField('Rods_a', max_digits=10, decimal_places=2, null=True, blank=True)
    Rods_b = models.DecimalField('Rods_b', max_digits=10, decimal_places=2, null=True, blank=True)
    Maximal_a = models.DecimalField('Maximal_a', max_digits=10, decimal_places=2, null=True, blank=True)
    Maximal_b = models.DecimalField('Maximal_b', max_digits=10, decimal_places=2, null=True, blank=True)
    Maximal_c = models.DecimalField('Maximal_c', max_digits=10, decimal_places=2, null=True, blank=True)
    VEP_N75 = models.DecimalField('VEP_N75', max_digits=10, decimal_places=2, null=True, blank=True)
    VEP_P100 = models.DecimalField('VEP_P100', max_digits=10, decimal_places=2, null=True, blank=True)
    VEP_N145 = models.DecimalField('VEP_N145', max_digits=10, decimal_places=2, null=True, blank=True)
    VEP_P1 = models.DecimalField('VEP_P1', max_digits=10, decimal_places=2, null=True, blank=True)
    VEP_P2 = models.DecimalField('VEP_P2', max_digits=10, decimal_places=2, null=True, blank=True)

    updated_at = models.DateTimeField(auto_now=True, blank=True)  # 업데이트 시각
    created_at = models.DateTimeField(auto_now_add=True, blank=True)  # 생성 시각


class IrdHistory(models.Model):
    SEX_CHOICES = ((1, 'Male'), (2, 'Female'))
    OD_OS_CHOICES = ((1, 'OD'), (2, 'OS'))
    YES_NO_DN_CHOICES = ((1, '네'), (2, '아니오'), (3, '모름'))
    EXISTENCE_DN_CHOICES = ((1, '유'), (2, '무'), (3, '모름'))
    EXISTENCE_DN_CHOICES2 = ((1, '있음'), (2, '없음'), (3, '잘모르겠음'))
    EXISTENCE_CHOICES = ((0, '없음'), (1, '있음'))
    EXISTENCE_CHOICES2 = ((1, '있음'), (2, '없음'))
    LP_CHOICES = ((1, 'LP+'), (2, 'LP'), (3, '모름'))
    AVAILABLE_CHOICES = ((1, '가능'), (2, '불가능'))

    FAMILY_HISTORY_CHOICES = ((0, "없음"),
                              (1, "잘 모르겠음"),
                              (2, "자녀 및 손자/손녀"),
                              (3, "형제자매"),
                              (4, "모계 직계(어머니, 외할아버지/할머니)"),
                              (5, "부계 직계(아버지, 할아버지/할머니)"),
                              (6, "모계 4촌 이내(외숙부/이모, 사촌 형제자매)"),
                              (7, "부계 4촌 이내(백부/숙부/고모, 사촌 형제자매)"))

    UNDERLYING_DISEASE_CHOICES = ((0, "없음"),
                                  (1, "청각장애"),
                                  (2, "당뇨"),
                                  (3, "평형감각 이상"),
                                  (4, "지적장애"),
                                  (5, "비뇨기계 이상"),
                                  (6, "다지증"),
                                  (7, "매독"),
                                  (8, "바이러스 질환"),
                                  (9, "악성종양"),
                                  (10, "포도막염"))

    RETINAL_CHOICES = ((1, "오른쪽 눈"),
                       (2, "왼쪽 눈"),
                       (3, "수술하지 않음"))

    register_date = models.DateField('동의서 취득 날짜', null=True, blank=True, help_text='동의서 취득 날짜')
    subject_id = models.PositiveIntegerField('Subject ID', null=True, blank=True)

    name = EncryptedCharField('이름', max_length=444, null=True, blank=True, help_text='성명')
    birthdate = EncryptedDateField('생년월일', null=True, blank=True, help_text='생년월일')
    age = models.PositiveIntegerField('나이', null=True, blank=True, help_text='나이')
    sex = models.IntegerField('성별', choices=[(i, i) for i in range(1, 3)], null=True, blank=True, help_text='성별 (1:남자  2:여자)')
    address = EncryptedTextField('주소', null=True, blank=True, help_text='도/시')
    job = models.TextField('직업', null=True, blank=True, help_text='어떤 일을 하고 계신가요?')
    diagnosis = models.TextField('진단명', null=True, blank=True, help_text='진단명')

    # (참고) 카이안과 작성부분

    # od
    sph_od = models.DecimalField('ARK_SPH', max_digits=10, decimal_places=2, null=True, blank=True, help_text='원/근시')
    cyl_od = models.DecimalField('ARK_CYL', max_digits=10, decimal_places=2, null=True, blank=True, help_text='난시')
    km_od = models.DecimalField('ARK_KM', max_digits=10, decimal_places=2, null=True, blank=True, help_text='각막난시')
    k_cyl_od = models.DecimalField('ARK_K(Cyl)', max_digits=10, decimal_places=2, null=True, blank=True,
                                   help_text='각막난시량')
    k_axis_od = models.PositiveIntegerField('ARK_K(Axis)', null=True, blank=True, help_text='각막난시축')
    udva_od = models.DecimalField('UDVA', max_digits=10, decimal_places=2, null=True, blank=True, help_text='원거리나안시력')
    unva_od = models.DecimalField('UNVA', max_digits=10, decimal_places=2, null=True, blank=True, help_text='근거리나안시력')
    cdva_od = models.DecimalField('CDVA', max_digits=10, decimal_places=2, null=True, blank=True, help_text='원거리교정시력')
    cnva_od = models.DecimalField('CNVA', max_digits=10, decimal_places=2, null=True, blank=True, help_text='근거리교정시력')
    iop_od = models.DecimalField('IOP', max_digits=10, decimal_places=2, null=True, blank=True, help_text='안압')
    cst_od = models.PositiveIntegerField('HOCT_CST', null=True, blank=True, help_text='중심망막 두께')
    vfi_od_full = models.PositiveIntegerField('VF_VFI_full', null=True, blank=True, help_text='중심시야 대비감도 전체')
    vfi_od_part = models.PositiveIntegerField('VF_VFI_part', null=True, blank=True, help_text='중심시야 대비감도 부분')
    cones_a_od = models.DecimalField('ERG_Cones_a', max_digits=10, decimal_places=2, null=True, blank=True,
                                     help_text='망막전위도검사')
    cones_b_od = models.DecimalField('ERG_Cones_b', max_digits=10, decimal_places=2, null=True, blank=True,
                                     help_text='망막전위도검사')
    flicker_od = models.DecimalField('ERG_Flicker', max_digits=10, decimal_places=2, null=True, blank=True,
                                     help_text='망막전위도검사')
    pattern_n35_mono_od = models.DecimalField('ERG_Pattern_n35_mono', max_digits=10, decimal_places=2, null=True,
                                              blank=True, help_text='망막전위도검사')
    pattern_p50_mono_od = models.DecimalField('ERG_Pattern_p50_mono', max_digits=10, decimal_places=2, null=True,
                                              blank=True, help_text='망막전위도검사')
    pattern_n95_mono_od = models.DecimalField('ERG_Pattern_n95_mono', max_digits=10, decimal_places=2, null=True,
                                              blank=True, help_text='망막전위도검사')
    pattern_n35_bi_od = models.DecimalField('ERG_Pattern_n35_bi', max_digits=10, decimal_places=2, null=True,
                                            blank=True, help_text='망막전위도검사')
    pattern_p50_bi_od = models.DecimalField('ERG_Pattern_p50_bi', max_digits=10, decimal_places=2, null=True,
                                            blank=True, help_text='망막전위도검사')
    pattern_n95_bi_od = models.DecimalField('ERG_Pattern_n95_bi', max_digits=10, decimal_places=2, null=True,
                                            blank=True, help_text='망막전위도검사')
    rods_a_od = models.DecimalField('ERG_Rods_a', max_digits=10, decimal_places=2, null=True, blank=True,
                                    help_text='망막전위도검사')
    rods_b_od = models.DecimalField('ERG_Rods_b', max_digits=10, decimal_places=2, null=True, blank=True,
                                    help_text='망막전위도검사')
    maximal_a_od = models.DecimalField('ERG_Maximal_a', max_digits=10, decimal_places=2, null=True, blank=True,
                                       help_text='망막전위도검사')
    maximal_b_od = models.DecimalField('ERG_Maximal_b', max_digits=10, decimal_places=2, null=True, blank=True,
                                       help_text='망막전위도검사')
    maximal_c_od = models.DecimalField('ERG_Maximal_c', max_digits=10, decimal_places=2, null=True, blank=True,
                                       help_text='망막전위도검사')
    cystoid_macular_edema_od = models.IntegerField('CME', choices=[(i, i) for i in range(2)], null=True, blank=True,
                                                   help_text='황반 부음')
    sector_rp_od = models.IntegerField('sector_RP', choices=[(i, i) for i in range(2)], null=True, blank=True,
                                       help_text='부채형 RP')
    retinitis_punctata_albescens_od = models.IntegerField('retinitis_punctata_albescens',
                                                          choices=[(i, i) for i in range(2)], null=True, blank=True,
                                                          help_text='백점상망막염')

    # os
    sph_os = models.DecimalField('ARK_SPH', max_digits=10, decimal_places=2, null=True, blank=True, help_text='원/근시')
    cyl_os = models.DecimalField('ARK_CYL', max_digits=10, decimal_places=2, null=True, blank=True, help_text='난시')
    km_os = models.DecimalField('ARK_KM', max_digits=10, decimal_places=2, null=True, blank=True, help_text='각막난시')
    k_cyl_os = models.DecimalField('ARK_K(Cyl)', max_digits=10, decimal_places=2, null=True, blank=True,
                                   help_text='각막난시량')
    k_axis_os = models.PositiveIntegerField('ARK_K(Axis)', null=True, blank=True, help_text='각막난시축')
    udva_os = models.DecimalField('UDVA', max_digits=10, decimal_places=2, null=True, blank=True, help_text='원거리나안시력')
    unva_os = models.DecimalField('UNVA', max_digits=10, decimal_places=2, null=True, blank=True, help_text='근거리나안시력')
    cdva_os = models.DecimalField('CDVA', max_digits=10, decimal_places=2, null=True, blank=True, help_text='원거리교정시력')
    cnva_os = models.DecimalField('CNVA', max_digits=10, decimal_places=2, null=True, blank=True, help_text='근거리교정시력')
    iop_os = models.DecimalField('IOP', max_digits=10, decimal_places=2, null=True, blank=True, help_text='안압')
    cst_os = models.PositiveIntegerField('HOCT_CST', null=True, blank=True, help_text='중심망막 두께')
    vfi_os_full = models.PositiveIntegerField('VF_VFI_full', null=True, blank=True, help_text='중심시야 대비감도 전체')
    vfi_os_part = models.PositiveIntegerField('VF_VFI_part', null=True, blank=True, help_text='중심시야 대비감도 부분')
    cones_a_os = models.DecimalField('ERG_Cones_a', max_digits=10, decimal_places=2, null=True, blank=True,
                                     help_text='망막전위도검사')
    cones_b_os = models.DecimalField('ERG_Cones_b', max_digits=10, decimal_places=2, null=True, blank=True,
                                     help_text='망막전위도검사')
    flicker_os = models.DecimalField('ERG_Flicker', max_digits=10, decimal_places=2, null=True, blank=True,
                                     help_text='망막전위도검사')
    pattern_n35_mono_os = models.DecimalField('ERG_Pattern_n35_mono', max_digits=10, decimal_places=2, null=True,
                                              blank=True, help_text='망막전위도검사')
    pattern_p50_mono_os = models.DecimalField('ERG_Pattern_p50_mono', max_digits=10, decimal_places=2, null=True,
                                              blank=True, help_text='망막전위도검사')
    pattern_n95_mono_os = models.DecimalField('ERG_Pattern_n95_mono', max_digits=10, decimal_places=2, null=True,
                                              blank=True, help_text='망막전위도검사')
    pattern_n35_bi_os = models.DecimalField('ERG_Pattern_n35_bi', max_digits=10, decimal_places=2, null=True,
                                            blank=True, help_text='망막전위도검사')
    pattern_p50_bi_os = models.DecimalField('ERG_Pattern_p50_bi', max_digits=10, decimal_places=2, null=True,
                                            blank=True, help_text='망막전위도검사')
    pattern_n95_bi_os = models.DecimalField('ERG_Pattern_n95_bi', max_digits=10, decimal_places=2, null=True,
                                            blank=True, help_text='망막전위도검사')
    rods_a_os = models.DecimalField('ERG_Rods_a', max_digits=10, decimal_places=2, null=True, blank=True,
                                    help_text='망막전위도검사')
    rods_b_os = models.DecimalField('ERG_Rods_b', max_digits=10, decimal_places=2, null=True, blank=True,
                                    help_text='망막전위도검사')
    maximal_a_os = models.DecimalField('ERG_Maximal_a', max_digits=10, decimal_places=2, null=True, blank=True,
                                       help_text='망막전위도검사')
    maximal_b_os = models.DecimalField('ERG_Maximal_b', max_digits=10, decimal_places=2, null=True, blank=True,
                                       help_text='망막전위도검사')
    maximal_c_os = models.DecimalField('ERG_Maximal_c', max_digits=10, decimal_places=2, null=True, blank=True,
                                       help_text='망막전위도검사')
    cystoid_macular_edema_os = models.IntegerField('CME', choices=[(i, i) for i in range(3)], null=True, blank=True,
                                                   help_text='황반 부음')
    sector_rp_os = models.IntegerField('sector_RP', choices=[(i, i) for i in range(3)], null=True, blank=True,
                                       help_text='부채형 RP')
    retinitis_punctata_albescens_os = models.IntegerField('retinitis_punctata_albescens',
                                                          choices=[(i, i) for i in range(3)], null=True, blank=True,
                                                          help_text='백점상망막염')
    # (참고) 휴먼스케이프 작성부분

    mutation_list = models.FileField('IRD 관련 유젼자 변이', upload_to="ird/mutation/%Y/%m/%d",
                                     null=True, blank=True,
                                     validators=[FileExtensionValidator(allowed_extensions=['csv'])])
    case_history = models.ImageField('실퇴본_병력청취', upload_to="ird/history/%Y/%m/%d", null=True, blank=True,
                                     help_text='실퇴본에서 조사한 병력청취 기록입니다.<br/>이미지 삽입 (스캔된 PDF파일 업로드)')

    first_symptom_reason = models.TextField('진단 계기', null=True, blank=True, help_text='어떤 계기로 진단을 받게 되었나요?')
    first_symptom_age = models.TextField('첫 증상 나이', null=True, blank=True, help_text='처음 눈에 증상이 나타난 나이는 언제인가요?')
    first_diagnosis_age = models.TextField('첫 진단 나이', null=True, blank=True,
                                           help_text='진단을 처음 받았던 때는 언제였나요?')
    first_diagnosis_hospital = models.TextField('첫 진단 병원', null=True, blank=True, help_text='진단을 처음 받았던 병원은 어디인가요?')
    current_hospital = models.TextField('현재 다니는 병원', null=True, blank=True, help_text='현재 다니는 병원은 어디인가요?')

    pedigree = models.ImageField('가계도', upload_to="ird/pedigree/%Y/%m/%d", null=True, blank=True,
                                 help_text='가족 구성원이 어떻게 되시나요?')


    familyhistory_diagnosis1 = ChoiceArrayField(models.CharField(max_length=200, choices=FAMILY_HISTORY_CHOICES,
                                                                     null=True, blank=True),
                                                verbose_name='같은 종류 진단 받은 가족',
                                                help_text='가족 중 같은 종류의 유전성 망막질환을 진단받은 사람이 있나요? 모두 선택해주세요',
                                                null=True, blank=True)
    familyhistory_diagnosis2 = models.IntegerField('다른 종류 진단 받은 가족', choices=EXISTENCE_DN_CHOICES2, null=True,
                                                   blank=True, help_text='가족 중 다른 종류의 유전성 망막질환을 진단받은 사람이 있나요?')
    familyhistory_diagnosis3 = ChoiceArrayField(models.CharField(max_length=200,choices=FAMILY_HISTORY_CHOICES,
                                                                     null=True, blank=True),
                                                verbose_name='다른 종류 진단 받은 가족 선택',
                                                help_text='가족 중 다른 종류의 유전성 망막질환을 진단받은 사람을 모두 선택해주세요',
                                                null=True, blank=True)
    familyhistory_diagnosis_name = models.TextField('가족 다른 종류 진단명', null=True, blank=True,
                                                    help_text='가족 중 다른 종류의 유전성 망막질환을 진단받은 사람이 있다면, 그 질환은 무엇인가요?')

    underlying_disease1 = ChoiceArrayField(
        models.CharField(max_length=200, choices=UNDERLYING_DISEASE_CHOICES, null=True, blank=True),
        verbose_name='기저질환',
        help_text='과거 앓았거나 현재 앓고 있는 질환이 있나요? 모두 선택해주세요',
        null=True, blank=True)
    underlying_disease2 = models.TextField('기타 기저질환', null=True, blank=True, help_text='그외 기타 질환 적어주세요')

    drug = models.IntegerField('12주 이내 복용한 약물', choices=EXISTENCE_DN_CHOICES2, null=True, blank=True,
                               help_text='최근 12주 이내에 복용한 약물이 있나요? ')
    drug_name = models.TextField('약물명', null=True, blank=True, help_text='약물명을 적어주세요')
    myodesopsia = models.IntegerField('비문증', choices=EXISTENCE_CHOICES2, null=True, blank=True,
                                      help_text='비문증을 경험한 적이 있나요?')
    myodesopsia_age = models.PositiveIntegerField('비문증 경험 나이', null=True, blank=True,
                                                  help_text='비문증 증상이 처음 나타났던 나이를 적어주세요 ')
    night_blindness = models.IntegerField('야맹증', choices=EXISTENCE_CHOICES2, null=True, blank=True,
                                          help_text='야맹증을 경험한 적이 있나요?')
    night_blindness_age = models.PositiveIntegerField('야맹증 나이', null=True, blank=True,
                                                      help_text='야맹증 증상이 처음 나타났던 나이를 적어주세요 ')
    peripheral_vision = models.IntegerField('주변(측면)시력', choices=EXISTENCE_CHOICES2, null=True, blank=True,
                                            help_text='시야가 좁아진다고 느낀 적이 있나요?')
    peripheral_vision_age = models.PositiveIntegerField('주변(측면)시력 나이', null=True, blank=True,
                                                        help_text='시야 좁은 증상이 처음 나타났던 나이를 적어주세요 ')
    central_vision = models.IntegerField('중심시력', choices=EXISTENCE_CHOICES2, null=True, blank=True,
                                         help_text='중심 시력에 이상이 있다고 느낀 적이 있나요?')
    central_vision_age = models.PositiveIntegerField('중심시력 나이', null=True, blank=True,
                                                     help_text='중심 시력 이상 증상이 처음 나타났던 나이를 적어주세요 ')
    read = models.IntegerField('읽기', choices=AVAILABLE_CHOICES, null=True, blank=True,
                               help_text='책이나 컴퓨터 화면 등 가까이 있는 물체를 볼 수 있나요?')
    object_recognition = models.IntegerField('물체 확인', choices=AVAILABLE_CHOICES, null=True, blank=True,
                                             help_text='멀리 있는 물체를 볼 수 있나요?')

    cataract = models.IntegerField('백내장', choices=EXISTENCE_CHOICES2, null=True, blank=True,
                                   help_text='백내장을 경험한 적이 있나요? ')
    cataract_op = ChoiceArrayField(models.CharField(max_length=200, choices=RETINAL_CHOICES, null=True, blank=True),
                                   verbose_name='백내장 수술',
                                   help_text='백내장 수술을 받은 적이 있나요?',
                                   null=True, blank=True)

    cataract_op_history = models.TextField('백내장 수술 이력', null=True, blank=True, help_text='수술 이력을 자세히 적어주세요')
    glaucoma = models.IntegerField('녹내장', choices=EXISTENCE_CHOICES2, null=True, blank=True,
                                   help_text='녹내장을 경험한 적이 있나요?')
    glaucoma_op = ChoiceArrayField(models.CharField(max_length=200, choices=RETINAL_CHOICES, null=True, blank=True),
                                   verbose_name='녹내장 수술',
                                   help_text='녹내장 수술을 받은 적이 있나요?',
                                   null=True, blank=True)
    glaucoma_op_history = models.TextField('녹내장 수술 이력', null=True, blank=True, help_text='수술 이력을 자세히 적어주세요')
    retinal_detachment = models.IntegerField('망막박리', choices=EXISTENCE_CHOICES2, null=True, blank=True,
                                             help_text='망막 박리를 경험한 적이 있나요?')
    retinal_detachment_op = ChoiceArrayField(
        models.CharField(max_length=200, choices=RETINAL_CHOICES, null=True, blank=True),
        verbose_name='망막박리 수술',
        help_text='망막 박리 수술을 받은 적이 있나요?',
        null=True, blank=True)
    retinal_detachment_op_history = models.TextField('망막박리 수술 이력', null=True, blank=True, help_text='수술 이력을 자세히 적어주세요')

    dark_adaptation = models.IntegerField('암순응', choices=EXISTENCE_CHOICES2, null=True, blank=True,
                                          help_text='암순응에 이상이 있다고 느낀 적이 있나요?')
    dark_adaptation_age = models.PositiveIntegerField('암순응 나이', null=True, blank=True,
                                                      help_text='암순응 이상 증상이 처음 나타났던 나이를 적어주세요 ')
    photopsia = models.IntegerField('광시증', choices=EXISTENCE_CHOICES2, null=True, blank=True,
                                    help_text='광시증을 경험한 적이 있나요?')
    photopsia_age = models.PositiveIntegerField('광시증 나이', null=True, blank=True, help_text='광시증 증상이 처음 나타났던 나이를 적어주세요 ')
    color_sense = models.IntegerField('색각', choices=EXISTENCE_CHOICES2, null=True, blank=True,
                                      help_text='색각에 이상이 있다고 느낀 적이 있나요?')
    color_sense_age = models.PositiveIntegerField('색각 나이', null=True, blank=True,
                                                  help_text='색각 이상 증상이 처음 나타났던 나이를 적어주세요 ')
    dazzling = models.IntegerField('눈부심', choices=EXISTENCE_CHOICES2, null=True, blank=True,
                                    help_text='눈부심을 경험한 적이 있나요')
    dazzling_age = models.PositiveIntegerField('눈부심 나이', null=True, blank=True, help_text='눈부심 증상이 처음 나타났던 나이를 적어주세요 ')
    hearing_defect = models.IntegerField('청력', choices=EXISTENCE_CHOICES2, null=True, blank=True,
                                         help_text='청력에 이상이 있나요?')
    hearing_defect_age = models.PositiveIntegerField('쳥력 첫 증상 나이', null=True, blank=True,
                                                     help_text='청력 이상 증상이 처음 나타났던 나이를 적어주세요')

    best_age = models.TextField('가장 좋았을 때 시력 나이', null=True, blank=True, help_text='시력이 가장 좋았던 때는 언제인가요?')
    best_va_lt = models.TextField('가장 좋았을 때 시력 좌', null=True, blank=True, help_text='가장 좋았던 좌측 시력은 얼마였나요?')
    best_va_rt = models.TextField('가장 좋았을 때 시력 우', null=True, blank=True, help_text='가장 좋았던 우측 시력은 얼마였나요?')
    best_vfi_lt = models.TextField('가장 좋았을 때 시야 좌', null=True, blank=True, help_text='가장 좋았던 좌측 시야는 얼마였나요?')
    best_vfi_rt = models.TextField('가장 좋았을 때 시야 우', null=True, blank=True, help_text='가장 좋았던 우측 시야는 얼마였나요?')
    first_va_lt = models.TextField('최초 진단시 시력 좌', null=True, blank=True, help_text='진단을 처음 받았던 때의 좌측 시력은 얼마였나요?')
    first_va_rt = models.TextField('최초 진단시 시력 우', null=True, blank=True, help_text='진단을 처음 받았던 때의 우측 시력은 얼마였나요?')
    first_vfi_lt = models.TextField('최초 진단시 시야 좌', null=True, blank=True, help_text='진단을 처음 받았던 때의 좌측 시야는 얼마였나요?')
    first_vfi_rt = models.TextField('최초 진단시 시야 우', null=True, blank=True, help_text='진단을 처음 받았던 때의 우측 시야는 얼마였나요?')
    current_va_lt = models.TextField('현재 시력 좌', null=True, blank=True, help_text='현재 좌측 시력은 얼마인가요?')
    current_va_rt = models.TextField('현재 시력 우', null=True, blank=True, help_text='현재 우측 시력은 얼마인가요?')
    current_vfi_lt = models.TextField('현재 시야 좌', null=True, blank=True, help_text='현재 좌측 시야는 얼마인가요?')
    current_vfi_rt = models.TextField('현재 시야 우', null=True, blank=True, help_text='현재 우측 시야는 얼마인가요?')

    comment = models.TextField('기타 세부 내용', null=True, blank=True)

    def save(self, *args, **kwargs):
        fields = self._meta.get_fields()
        for field in fields:
            if field.name in CALCULATE_AGE_FIELDS['ird_history'].keys():
                if field.name == 'age':
                    setattr(self, field.name, calculate_age(datetime.now(), self.birthdate))
                else:
                    setattr(self, field.name, calculate_age(getattr(self, CALCULATE_AGE_FIELDS['ird_history'][field.name]), self.birthdate))
        super(IrdHistory, self).save(*args, **kwargs)


    class Meta:
        verbose_name = "ird_병력청취"
        verbose_name_plural = "ird_병력청취"
