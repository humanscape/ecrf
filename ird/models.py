from django.db import models
from django.core.validators import FileExtensionValidator

from encrypted_fields.fields import *

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
    SEX_CHOICES = ((1, 'Male'), (2, 'Female'), (3, 'All'))
    OD_OS_CHOICES = ((1, 'OD'), (2, 'OS'))
    YES_NO_DN_CHOICES = ((1, '네'), (2, '아니오'), (3, '모름'))
    EXISTENCE_CHOICES = ((1, '유'), (2, '무'), (3, '모름'))
    LP_CHOICES = ((1, 'LP+'), (2, 'LP'), (3, '모름'))

    name = EncryptedCharField('이름', max_length=20, null=True, blank=True, help_text='성명')
    birthdate = EncryptedDateField('생년월일', null=True, blank=True, help_text='생년월일')
    sex = models.IntegerField('성별', choices=SEX_CHOICES, null=True, blank=True, help_text='성별')
    address = EncryptedTextField('주소', null=True, blank=True, help_text='도/시')
    age = models.PositiveIntegerField('나이', null=True, blank=True, help_text='나이')

    od_os = models.IntegerField('구분', choices=OD_OS_CHOICES, null=True, blank=True, help_text='OD/OS')
    sph = models.DecimalField('ARK_SPH', max_digits=10, decimal_places=2, null=True, blank=True, help_text='원/근시')
    cyl = models.DecimalField('ARK_CYL', max_digits=10, decimal_places=2, null=True, blank=True, help_text='난시')
    km = models.DecimalField('ARK_KM', max_digits=10, decimal_places=2, null=True, blank=True, help_text='각막난시')
    k_cyl = models.DecimalField('ARK_K(Cyl)', max_digits=10, decimal_places=2, null=True, blank=True, help_text='각막난시량')
    k_axis = models.PositiveIntegerField('ARK_K(Axis)', null=True, blank=True, help_text='각막난시축')
    udva = models.DecimalField('UDVA', max_digits=10, decimal_places=1, null=True, blank=True, help_text='원거리나안시력')
    unva = models.DecimalField('UNVA', max_digits=10, decimal_places=1, null=True, blank=True, help_text='근거리나안시력')
    cdva = models.DecimalField('CDVA', max_digits=10, decimal_places=1, null=True, blank=True, help_text='원거리교정시력')
    cnva = models.DecimalField('CNVA', max_digits=10, decimal_places=1, null=True, blank=True, help_text='근거리교정시력')
    iop = models.DecimalField('IOP', max_digits=10, decimal_places=1, null=True, blank=True, help_text='안압')
    cst = models.PositiveIntegerField('HOCT_CST', null=True, blank=True, help_text='중심망막 두께')
    vfi = models.PositiveIntegerField('VF_VFI', null=True, blank=True, help_text='중심시야 대비감도')

    cones_a = models.DecimalField('ERG_Cones_a', max_digits=10, decimal_places=1, null=True, blank=True,
                                  help_text='망막전위도검사')
    cones_b = models.DecimalField('ERG_Cones_b', max_digits=10, decimal_places=1, null=True, blank=True,
                                  help_text='망막전위도검사')
    flicker = models.DecimalField('ERG_Flicker', max_digits=10, decimal_places=1, null=True, blank=True,
                                  help_text='망막전위도검사')
    pattern_n35_mono = models.DecimalField('ERG_Pattern_n35_mono', max_digits=10, decimal_places=1, null=True,
                                           blank=True, help_text='망막전위도검사')
    pattern_p50_mono = models.DecimalField('ERG_Pattern_p50_mono', max_digits=10, decimal_places=1, null=True,
                                           blank=True, help_text='망막전위도검사')
    pattern_n95_mono = models.DecimalField('ERG_Pattern_n95_mono', max_digits=10, decimal_places=1, null=True,
                                           blank=True, help_text='망막전위도검사')
    pattern_n35_bi = models.DecimalField('ERG_Pattern_n35_bi', max_digits=10, decimal_places=1, null=True, blank=True,
                                         help_text='망막전위도검사')
    pattern_p50_bi = models.DecimalField('ERG_Pattern_p50_bi', max_digits=10, decimal_places=1, null=True, blank=True,
                                         help_text='망막전위도검사')
    pattern_n95_bi = models.DecimalField('ERG_Pattern_n95_bi', max_digits=10, decimal_places=1, null=True, blank=True,
                                         help_text='망막전위도검사')
    rods_a = models.DecimalField('ERG_Rods_a', max_digits=10, decimal_places=1, null=True, blank=True,
                                 help_text='망막전위도검사')
    rods_b = models.DecimalField('ERG_Rods_b', max_digits=10, decimal_places=1, null=True, blank=True,
                                 help_text='망막전위도검사')
    maximal_a = models.DecimalField('ERG_Maximal_a', max_digits=10, decimal_places=1, null=True, blank=True,
                                    help_text='망막전위도검사')
    maximal_b = models.DecimalField('ERG_Maximal_b', max_digits=10, decimal_places=1, null=True, blank=True,
                                    help_text='망막전위도검사')
    maximal_c = models.DecimalField('ERG_Maximal_c', max_digits=10, decimal_places=1, null=True, blank=True,
                                    help_text='망막전위도검사')

    first_symptom_age = models.PositiveIntegerField('첫 증상 나이', null=True, blank=True,
                                                    help_text='처음 눈에 증상이 나타난 나이는 언제인가요?')
    first_symptom_year = models.PositiveIntegerField('첫 증상 연도', null=True, blank=True,
                                                     help_text='처음 눈에 증상이 나타난 연도는 언제인가요?')
    first_diagnosis_age = models.PositiveIntegerField('첫 진단 나이', null=True, blank=True,
                                                      help_text='병원을 통해 처음 질환을 진단 받았던 나이는 언제인가요?')
    first_diagnosis_year = models.PositiveIntegerField('첫 진단 연도', null=True, blank=True,
                                                       help_text='병원을 통해 처음 질환을 진단 받았던 연도는 언제인가요?')

    pedigree = models.ImageField('가계도', upload_to="ird/pedigree/%Y/%m/%d", null=True, blank=True, help_text='가족 구성원이 어떻게 되시나요?')

    familyhistory_diagnosis1 = models.IntegerField('가족 같은 종류 진단', choices=YES_NO_DN_CHOICES, null=True, blank=True,
                                                   help_text='가족 중에서 같은 종류의 유전성 망막질환을 진단받은 사람이 있으신가요?')
    familyhistory_diagnosis2 = models.IntegerField('가족 다른 종류 진단', choices=YES_NO_DN_CHOICES, null=True, blank=True,
                                                   help_text='가족 중에서 다른 종류의 유전성 망막질환을 진단받은 사람이 있으신가요? ')
    familyhistory_diagnosis_name = models.CharField('가족 다른 종류 진단 명', max_length=255, null=True, blank=True,
                                                    help_text='가족중에서 다른 종류의 유전성 망막질환이 있는 경우 그분의 질병은 무엇인가요?')
    other_diagnosis = models.IntegerField('그외 다른 질환', choices=YES_NO_DN_CHOICES, null=True, blank=True,
                                          help_text='그외 다른 질환이 있나요?')
    night_blindness = models.IntegerField('야맹증', choices=YES_NO_DN_CHOICES, null=True, blank=True, help_text='야맹증이 있으신가요?')
    peripheral_vision = models.IntegerField('주변(측면) 시력', choices=YES_NO_DN_CHOICES, null=True, blank=True,
                                            help_text='주변(측력) 시력이 떨어지고 있나요?')
    central_vision = models.IntegerField('중심 시력', choices=YES_NO_DN_CHOICES, null=True, blank=True,
                                         help_text='중심 시력이 조금이라도 떨어졌나요?')
    read = models.IntegerField('읽기', choices=YES_NO_DN_CHOICES, null=True, blank=True, help_text='책이나 컴퓨터 화면 등을 읽을 수 있으신가요?')
    eyeglasses_lens = models.IntegerField('안경, 콘택트 렌즈', choices=YES_NO_DN_CHOICES, null=True, blank=True,
                                          help_text='처방받은 안경이나 콘택트 렌즈를 사용하시나요?')
    object_recognition = models.IntegerField('물체 확인', choices=YES_NO_DN_CHOICES, null=True, blank=True,
                                             help_text='멀리 떨어져 있는 물체를 볼 수 있으신가요?')
    cataract = models.IntegerField('백내장', choices=YES_NO_DN_CHOICES, null=True, blank=True, help_text='백내장이 있으신가요?')
    glaucoma = models.IntegerField('녹내장', choices=YES_NO_DN_CHOICES, null=True, blank=True, help_text='녹내장이 있으신가요?')
    retinal_detachment = models.IntegerField('망막박리', choices=YES_NO_DN_CHOICES, null=True, blank=True, help_text='망막박리가 있으신가요?')
    retinal_detachment_age = models.PositiveIntegerField('망막박리 발생 나이', null=True, blank=True,
                                                         help_text='몇 살 때, 망막박리가 나타났나요?')
    dark_adaptation = models.IntegerField('암순응', choices=YES_NO_DN_CHOICES, null=True, blank=True,
                                          help_text='현재 암순응(밝은 곳에서 어두운 곳으로 들어갈 때 적응하는 상태)에 문제가 있으신가요?')
    dark_adaptation_age = models.PositiveIntegerField('암순응 인지 나이', null=True, blank=True,
                                                      help_text='몇 살 때, 암순응에 문제가 있다고 처음 인지하셨나요?')
    photopsia = models.IntegerField('광시증', choices=YES_NO_DN_CHOICES, null=True, blank=True,
                                    help_text='광시증(갑자기 눈앞이 번쩍거리는 증상)이 있으신가요?')
    photopsia_age = models.PositiveIntegerField('광시증 경험 나이', null=True, blank=True, help_text='몇 살 때, 광시증을 처음 경험하셨나요?')
    color_sense = models.IntegerField('색각', choices=YES_NO_DN_CHOICES, null=True, blank=True, help_text='색각(색채 구별)에 문제가 있으신가요?')

    best_year = models.PositiveIntegerField('가장 좋았을때 년도', null=True, blank=True)
    best_age = models.PositiveIntegerField('가장 좋았을때 나이', null=True, blank=True)
    best_va = models.IntegerField('가장 좋았을때 시력측정 가능 여부', choices=YES_NO_DN_CHOICES, null=True, blank=True)
    best_lp_lt = models.IntegerField('가장 좋았을때 시력측정 불가할 경우 빛인지_좌', choices=LP_CHOICES, null=True, blank=True)
    best_lp_rt = models.IntegerField('가장 좋았을때 시력측정 불가할 경우 빛인지_우', choices=LP_CHOICES, null=True, blank=True)
    best_va_lt = models.DecimalField('가장 좋았을때 시력 좌', max_digits=10, decimal_places=2, null=True, blank=True)
    best_va_rt = models.DecimalField('가장 좋았을때 시력 우', max_digits=10, decimal_places=2, null=True, blank=True)
    best_vfi_lt = models.PositiveIntegerField('가장 좋았을때 시야 좌', null=True, blank=True)
    best_vfi_rt = models.PositiveIntegerField('가장 좋았을때 시야 우', null=True, blank=True)
    best_night_blindness = models.IntegerField('가장 좋았을때 야맹증', choices=EXISTENCE_CHOICES, null=True, blank=True)
    best_photopsia = models.IntegerField('가장 좋았을때 눈부심', choices=EXISTENCE_CHOICES, null=True, blank=True)
    best_cataract = models.IntegerField('가장 좋았을때 백내장', choices=EXISTENCE_CHOICES, null=True, blank=True)
    best_hearing_defect = models.IntegerField('가장 좋았을때 청각장애', choices=EXISTENCE_CHOICES, null=True, blank=True)
    best_pedigree = models.IntegerField('가장 좋았을때 가족력', choices=EXISTENCE_CHOICES, null=True, blank=True)
    first_year = models.PositiveIntegerField('최초 진단시 년도', null=True, blank=True)
    first_age = models.PositiveIntegerField('최초_진단시 나이', null=True, blank=True)
    first_va = models.IntegerField('최초 진단시 시력측정 가능 여부', choices=YES_NO_DN_CHOICES, null=True, blank=True)
    first_lp_lt = models.IntegerField('최초 진단시 시력측정 불가할 경우 빛인지_좌', choices=LP_CHOICES, null=True, blank=True)
    first_lp_rt = models.IntegerField('최초 진단시 시력측정 불가할 경우 빛인지_우', choices=LP_CHOICES, null=True, blank=True)
    first_va_lt = models.TextField('최초 진단시 시력 좌', null=True, blank=True)
    first_va_rt = models.TextField('최초 진단시 시력 우', null=True, blank=True)
    first_vfi_lt = models.PositiveIntegerField('최초 진단시 시야 좌', null=True, blank=True)
    first_vfi_rt = models.PositiveIntegerField('최초 진단시 시야 우', null=True, blank=True)
    first_night_blindness = models.IntegerField('최초 진단시 야맹증', choices=EXISTENCE_CHOICES, null=True, blank=True)
    first_photopsia = models.IntegerField('최초 진단시 눈부심', choices=EXISTENCE_CHOICES, null=True, blank=True)
    first_cataract = models.IntegerField('최초 진단시 백내장', choices=EXISTENCE_CHOICES, null=True, blank=True)
    first_hearing_defect = models.IntegerField('최초 진단시 청각장애', choices=EXISTENCE_CHOICES, null=True, blank=True)
    first_pedigree = models.IntegerField('최초 진단시 가족력', choices=EXISTENCE_CHOICES, null=True, blank=True)

    current_year = models.PositiveIntegerField('현재 년도', null=True, blank=True)
    current_age = models.PositiveIntegerField('현재 나이', null=True, blank=True)
    current_va = models.IntegerField('현재 시력측정 가능 여부', choices=YES_NO_DN_CHOICES, null=True, blank=True)
    current_lp_lt = models.IntegerField('현재 시력측정 불가할 경우 빛인지_좌', choices=LP_CHOICES, null=True, blank=True)
    current_p_rt = models.IntegerField('현재 시력측정 불가할 경우 빛인지_우', choices=LP_CHOICES, null=True, blank=True)
    current_va_lt = models.TextField('현재 시력 좌', null=True, blank=True)
    current_va_rt = models.TextField('현재 시력 우', null=True, blank=True)
    current_vfi_lt = models.PositiveIntegerField('현재 시야 좌', null=True, blank=True)
    current_vfi_rt = models.PositiveIntegerField('현재 시야 우', null=True, blank=True)
    current_night_blindness = models.IntegerField('현재_야맹증', choices=EXISTENCE_CHOICES, null=True, blank=True)
    current_photopsia = models.IntegerField('현재 눈부심', choices=EXISTENCE_CHOICES, null=True, blank=True)
    current_cataract = models.IntegerField('현재 백내장', choices=EXISTENCE_CHOICES, null=True, blank=True)
    current_hearing_defect = models.IntegerField('현재 청각장애', choices=EXISTENCE_CHOICES, null=True, blank=True)
    current_pedigree = models.IntegerField('현재의 상태 가족력', choices=EXISTENCE_CHOICES, null=True, blank=True)

    mutation_list = models.FileField('IRD 관련 유젼자 변이', upload_to="ird/mutation/%Y/%m/%d", 
                                    null=True, blank=True, validators=[FileExtensionValidator(allowed_extensions=['csv'])])

    class Meta:
        verbose_name = "ird_병력청취"
        verbose_name_plural = "ird_병력청취"
