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
    EXISTENCE_DN_CHOICES = ((1, '유'), (2, '무'), (3, '모름'))
    EXISTENCE_CHOICES = ((0, '없음'), (1, '있음'))
    LP_CHOICES = ((1, 'LP+'), (2, 'LP'), (3, '모름'))

    name = EncryptedCharField('이름', max_length=20, null=True, blank=True, help_text='성명')
    birthdate = EncryptedDateField('생년월일', null=True, blank=True, help_text='생년월일')
    sex = models.IntegerField('성별', choices=SEX_CHOICES, null=True, blank=True, help_text='성별')
    address = EncryptedTextField('주소', null=True, blank=True, help_text='도/시')
    age = models.PositiveIntegerField('나이', null=True, blank=True, help_text='나이')

    sph_od = models.DecimalField('ARK_SPH OD', max_digits=10, decimal_places=2, null=True, blank=True, help_text='원/근시')
    cyl_od = models.DecimalField('ARK_CYL OD', max_digits=10, decimal_places=2, null=True, blank=True, help_text='난시')
    km_od = models.DecimalField('ARK_KM OD', max_digits=10, decimal_places=2, null=True, blank=True, help_text='각막난시')
    k_cyl_od = models.DecimalField('ARK_K(Cyl) OD', max_digits=10, decimal_places=2, null=True, blank=True, help_text='각막난시량')
    k_axis_od = models.PositiveIntegerField('ARK_K(Axis) OD', null=True, blank=True, help_text='각막난시축')
    udva_od = models.DecimalField('UDVA OD', max_digits=10, decimal_places=1, null=True, blank=True, help_text='원거리나안시력')
    unva_od = models.DecimalField('UNVA OD', max_digits=10, decimal_places=1, null=True, blank=True, help_text='근거리나안시력')
    cdva_od = models.DecimalField('CDVA OD', max_digits=10, decimal_places=1, null=True, blank=True, help_text='원거리교정시력')
    cnva_od = models.DecimalField('CNVA OD', max_digits=10, decimal_places=1, null=True, blank=True, help_text='근거리교정시력')
    iop_od = models.DecimalField('IOP OD', max_digits=10, decimal_places=1, null=True, blank=True, help_text='안압')
    cst_od = models.PositiveIntegerField('HOCT_CST OD', null=True, blank=True, help_text='중심망막 두께')
    vfi_od_full = models.PositiveIntegerField('VF_VFI_full OD', null=True, blank=True, help_text='중심시야 대비감도 전체')
    vfi_od_part = models.PositiveIntegerField('VF_VFI_part OD', null=True, blank=True, help_text='중심시야 대비감도 부분')

    cones_a_od = models.DecimalField('ERG_Cones_a OD', max_digits=10, decimal_places=1, null=True, blank=True,
                                  help_text='망막전위도검사')
    cones_b_od = models.DecimalField('ERG_Cones_b OD', max_digits=10, decimal_places=1, null=True, blank=True,
                                  help_text='망막전위도검사')
    flicker_od = models.DecimalField('ERG_Flicker OD', max_digits=10, decimal_places=1, null=True, blank=True,
                                  help_text='망막전위도검사')
    pattern_n35_mono_od = models.DecimalField('ERG_Pattern_n35_mono OD', max_digits=10, decimal_places=1, null=True,
                                           blank=True, help_text='망막전위도검사')
    pattern_p50_mono_od = models.DecimalField('ERG_Pattern_p50_mono OD', max_digits=10, decimal_places=1, null=True,
                                           blank=True, help_text='망막전위도검사')
    pattern_n95_mono_od = models.DecimalField('ERG_Pattern_n95_mono OD', max_digits=10, decimal_places=1, null=True,
                                           blank=True, help_text='망막전위도검사')
    pattern_n35_bi_od = models.DecimalField('ERG_Pattern_n35_bi OD', max_digits=10, decimal_places=1, null=True, blank=True,
                                         help_text='망막전위도검사')
    pattern_p50_bi_od = models.DecimalField('ERG_Pattern_p50_bi OD', max_digits=10, decimal_places=1, null=True, blank=True,
                                         help_text='망막전위도검사')
    pattern_n95_bi_od = models.DecimalField('ERG_Pattern_n95_bi OD', max_digits=10, decimal_places=1, null=True, blank=True,
                                         help_text='망막전위도검사')
    rods_a_od = models.DecimalField('ERG_Rods_a OD', max_digits=10, decimal_places=1, null=True, blank=True,
                                 help_text='망막전위도검사')
    rods_b_od = models.DecimalField('ERG_Rods_b OD', max_digits=10, decimal_places=1, null=True, blank=True,
                                 help_text='망막전위도검사')
    maximal_a_od = models.DecimalField('ERG_Maximal_a OD', max_digits=10, decimal_places=1, null=True, blank=True,
                                    help_text='망막전위도검사')
    maximal_b_od = models.DecimalField('ERG_Maximal_b OD', max_digits=10, decimal_places=1, null=True, blank=True,
                                    help_text='망막전위도검사')
    maximal_c_od = models.DecimalField('ERG_Maximal_c OD', max_digits=10, decimal_places=1, null=True, blank=True,
                                    help_text='망막전위도검사')
    cystoid_macular_edema_od = models.IntegerField('CME OD', choices=EXISTENCE_CHOICES, null=True, blank=True, help_text='황반 부음')
    sector_rp_od = models.IntegerField('sector_RP OD', choices=EXISTENCE_CHOICES, null=True, blank=True, help_text='부채형 RP')
    retinitis_punctata_albescens_od = models.IntegerField('retinitis_punctata_albescens OD', choices=EXISTENCE_CHOICES, null=True, blank=True, help_text='백점상망막염')

    sph_os = models.DecimalField('ARK_SPH OS', max_digits=10, decimal_places=2, null=True, blank=True, help_text='원/근시')
    cyl_os = models.DecimalField('ARK_CYL OS', max_digits=10, decimal_places=2, null=True, blank=True, help_text='난시')
    km_os = models.DecimalField('ARK_KM OS', max_digits=10, decimal_places=2, null=True, blank=True, help_text='각막난시')
    k_cyl_os = models.DecimalField('ARK_K(Cyl) OS', max_digits=10, decimal_places=2, null=True, blank=True, help_text='각막난시량')
    k_axis_os = models.PositiveIntegerField('ARK_K(Axis) OS', null=True, blank=True, help_text='각막난시축')
    udva_os = models.DecimalField('UDVA OS', max_digits=10, decimal_places=1, null=True, blank=True, help_text='원거리나안시력')
    unva_os = models.DecimalField('UNVA OS', max_digits=10, decimal_places=1, null=True, blank=True, help_text='근거리나안시력')
    cdva_os = models.DecimalField('CDVA OS', max_digits=10, decimal_places=1, null=True, blank=True, help_text='원거리교정시력')
    cnva_os = models.DecimalField('CNVA OS', max_digits=10, decimal_places=1, null=True, blank=True, help_text='근거리교정시력')
    iop_os = models.DecimalField('IOP OS', max_digits=10, decimal_places=1, null=True, blank=True, help_text='안압')
    cst_os = models.PositiveIntegerField('HOCT_CST OS', null=True, blank=True, help_text='중심망막 두께')
    vfi_os_full = models.PositiveIntegerField('VF_VFI_full OS', null=True, blank=True, help_text='중심시야 대비감도 전체')
    vfi_os_part = models.PositiveIntegerField('VF_VFI_part OS', null=True, blank=True, help_text='중심시야 대비감도 부분')

    cones_a_os = models.DecimalField('ERG_Cones_a OS', max_digits=10, decimal_places=1, null=True, blank=True,
                                  help_text='망막전위도검사')
    cones_b_os = models.DecimalField('ERG_Cones_b OS', max_digits=10, decimal_places=1, null=True, blank=True,
                                  help_text='망막전위도검사')
    flicker_os = models.DecimalField('ERG_Flicker OS', max_digits=10, decimal_places=1, null=True, blank=True,
                                  help_text='망막전위도검사')
    pattern_n35_mono_os = models.DecimalField('ERG_Pattern_n35_mono OS', max_digits=10, decimal_places=1, null=True,
                                           blank=True, help_text='망막전위도검사')
    pattern_p50_mono_os = models.DecimalField('ERG_Pattern_p50_mono OS', max_digits=10, decimal_places=1, null=True,
                                           blank=True, help_text='망막전위도검사')
    pattern_n95_mono_os = models.DecimalField('ERG_Pattern_n95_mono OS', max_digits=10, decimal_places=1, null=True,
                                           blank=True, help_text='망막전위도검사')
    pattern_n35_bi_os = models.DecimalField('ERG_Pattern_n35_bi OS', max_digits=10, decimal_places=1, null=True, blank=True,
                                         help_text='망막전위도검사')
    pattern_p50_bi_os = models.DecimalField('ERG_Pattern_p50_bi OS', max_digits=10, decimal_places=1, null=True, blank=True,
                                         help_text='망막전위도검사')
    pattern_n95_bi_os = models.DecimalField('ERG_Pattern_n95_bi OS', max_digits=10, decimal_places=1, null=True, blank=True,
                                         help_text='망막전위도검사')
    rods_a_os = models.DecimalField('ERG_Rods_a OS', max_digits=10, decimal_places=1, null=True, blank=True,
                                 help_text='망막전위도검사')
    rods_b_os = models.DecimalField('ERG_Rods_b OS', max_digits=10, decimal_places=1, null=True, blank=True,
                                 help_text='망막전위도검사')
    maximal_a_os = models.DecimalField('ERG_Maximal_a OS', max_digits=10, decimal_places=1, null=True, blank=True,
                                    help_text='망막전위도검사')
    maximal_b_os = models.DecimalField('ERG_Maximal_b OS', max_digits=10, decimal_places=1, null=True, blank=True,
                                    help_text='망막전위도검사')
    maximal_c_os = models.DecimalField('ERG_Maximal_c OS', max_digits=10, decimal_places=1, null=True, blank=True,
                                    help_text='망막전위도검사')
    cystoid_macular_edema_os = models.IntegerField('CME OS', choices=EXISTENCE_CHOICES, null=True, blank=True, help_text='황반 부음')
    sector_rp_os = models.IntegerField('sector_RP OS', choices=EXISTENCE_CHOICES, null=True, blank=True, help_text='부채형 RP')
    retinitis_punctata_albescens_os = models.IntegerField('retinitis_punctata_albescens OS', choices=EXISTENCE_CHOICES, null=True, blank=True, help_text='백점상망막염')

    case_history = models.ImageField('실퇴본_병력청취', upload_to="ird/history/%Y/%m/%d", null=True, blank=True, help_text='실퇴본에서 조사한 병력 청취 기록입니다.')
    job = models.CharField('직업', max_length=255, null=True, blank=True, help_text='어떤 일을 하고 계신가요?')

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
    best_night_blindness = models.IntegerField('가장 좋았을때 야맹증', choices=EXISTENCE_DN_CHOICES, null=True, blank=True)
    best_photopsia = models.IntegerField('가장 좋았을때 눈부심', choices=EXISTENCE_DN_CHOICES, null=True, blank=True)
    best_cataract = models.IntegerField('가장 좋았을때 백내장', choices=EXISTENCE_DN_CHOICES, null=True, blank=True)
    best_hearing_defect = models.IntegerField('가장 좋았을때 청각장애', choices=EXISTENCE_DN_CHOICES, null=True, blank=True)
    best_pedigree = models.IntegerField('가장 좋았을때 가족력', choices=EXISTENCE_DN_CHOICES, null=True, blank=True)
    first_year = models.PositiveIntegerField('최초 진단시 년도', null=True, blank=True)
    first_age = models.PositiveIntegerField('최초_진단시 나이', null=True, blank=True)
    first_va = models.IntegerField('최초 진단시 시력측정 가능 여부', choices=YES_NO_DN_CHOICES, null=True, blank=True)
    first_lp_lt = models.IntegerField('최초 진단시 시력측정 불가할 경우 빛인지_좌', choices=LP_CHOICES, null=True, blank=True)
    first_lp_rt = models.IntegerField('최초 진단시 시력측정 불가할 경우 빛인지_우', choices=LP_CHOICES, null=True, blank=True)
    first_va_lt = models.TextField('최초 진단시 시력 좌', null=True, blank=True)
    first_va_rt = models.TextField('최초 진단시 시력 우', null=True, blank=True)
    first_vfi_lt = models.PositiveIntegerField('최초 진단시 시야 좌', null=True, blank=True)
    first_vfi_rt = models.PositiveIntegerField('최초 진단시 시야 우', null=True, blank=True)
    first_night_blindness = models.IntegerField('최초 진단시 야맹증', choices=EXISTENCE_DN_CHOICES, null=True, blank=True)
    first_photopsia = models.IntegerField('최초 진단시 눈부심', choices=EXISTENCE_DN_CHOICES, null=True, blank=True)
    first_cataract = models.IntegerField('최초 진단시 백내장', choices=EXISTENCE_DN_CHOICES, null=True, blank=True)
    first_hearing_defect = models.IntegerField('최초 진단시 청각장애', choices=EXISTENCE_DN_CHOICES, null=True, blank=True)
    first_pedigree = models.IntegerField('최초 진단시 가족력', choices=EXISTENCE_DN_CHOICES, null=True, blank=True)

    current_year = models.PositiveIntegerField('현재 년도', null=True, blank=True)
    current_age = models.PositiveIntegerField('현재 나이', null=True, blank=True)
    current_va = models.IntegerField('현재 시력측정 가능 여부', choices=YES_NO_DN_CHOICES, null=True, blank=True)
    current_lp_lt = models.IntegerField('현재 시력측정 불가할 경우 빛인지_좌', choices=LP_CHOICES, null=True, blank=True)
    current_p_rt = models.IntegerField('현재 시력측정 불가할 경우 빛인지_우', choices=LP_CHOICES, null=True, blank=True)
    current_va_lt = models.TextField('현재 시력 좌', null=True, blank=True)
    current_va_rt = models.TextField('현재 시력 우', null=True, blank=True)
    current_vfi_lt = models.PositiveIntegerField('현재 시야 좌', null=True, blank=True)
    current_vfi_rt = models.PositiveIntegerField('현재 시야 우', null=True, blank=True)
    current_night_blindness = models.IntegerField('현재_야맹증', choices=EXISTENCE_DN_CHOICES, null=True, blank=True)
    current_photopsia = models.IntegerField('현재 눈부심', choices=EXISTENCE_DN_CHOICES, null=True, blank=True)
    current_cataract = models.IntegerField('현재 백내장', choices=EXISTENCE_DN_CHOICES, null=True, blank=True)
    current_hearing_defect = models.IntegerField('현재 청각장애', choices=EXISTENCE_DN_CHOICES, null=True, blank=True)
    current_pedigree = models.IntegerField('현재의 상태 가족력', choices=EXISTENCE_DN_CHOICES, null=True, blank=True)

    mutation_list = models.FileField('IRD 관련 유젼자 변이', upload_to="ird/mutation/%Y/%m/%d", 
                                    null=True, blank=True, validators=[FileExtensionValidator(allowed_extensions=['csv'])])

    class Meta:
        verbose_name = "ird_병력청취"
        verbose_name_plural = "ird_병력청취"
