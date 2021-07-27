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

    date_at_evaluation = models.DateTimeField('Date at evaluation', auto_now=True, blank=True, help_text='진단을 받은 날짜')
    patient_number = models.IntegerField('Patient number', null=True, blank=True, help_text='환자 번호')
    name = models.CharField('Name', max_length=20, unique=True, blank=True, help_text='환자 이름')
    case_no = models.IntegerField('Case no.', null=True, blank=True, help_text='사건/차트 번호')
    family_no = models.IntegerField('Family no.', null=True, blank=True, help_text='가족 번호')
    family_hx = models.IntegerField('Family Hx', null=True, blank=True, help_text='가족 병력')
    sex = models.IntegerField('SEX', choices=SEX_TYPE, null=True, blank=True, help_text='성별')
    birth_date = models.DateField('Birth year and month', auto_now=True, blank=True, help_text='생년월일')
    date_at_dx = models.DateField('Date at Dx', auto_now=True, blank=True, help_text='진단 받은 날짜')
    age_at_dx = models.IntegerField('Age at Dx', null=True, blank=True, help_text='진단시 연령')
    date_at_evaluation = models.DateField('Date at evaluation', auto_now=True, blank=True, help_text='유전자 검사 날짜')
    age_at_evaluation = models.IntegerField('Age at evaluation', null=True, blank=True, help_text='유전자 검사시 연령')

    NF1_genotype = models.CharField('NF1 genotype', max_length=200, unique=True, blank=True, help_text='연관 유전자 자위')
    dna = models.CharField('DNA', max_length=200, unique=True, blank=True, help_text='유전자 변이 (DNA)')
    protein = models.CharField('Protein', max_length=200, unique=True, blank=True, help_text='유전자 변이 (protein)')
    domain = models.CharField('Domain', max_length=20, unique=True, blank=True, help_text='유전자 도메인')

    mutation_type = models.IntegerField('Mutation type', null=True, blank=True, help_text='돌연변이 종류<br/>1:missense<br/>2:nonsense<br/>3:frameshift<br/>4:splicing<br/>5:large deletion')
    inframe_deletion_or_insertion = models.IntegerField('Inframe deletion or insertion', null=True, blank=True, help_text='인델 돌연변이(유무; 유전자 인프레임 삭제 또는 삽입; 유전자 전사와 번역 과정이 중지되지 않음)')
    nf1_haploinsufficiency_type = models.IntegerField('NF1 haploinsufficiency type', null=True, blank=True, help_text='반수체 부족 유형')

    novel_mutation = models.BooleanField('Novel mutation', default=False, help_text='드 노보 유전자 돌연변이 (유무; 유전성이 아닌 돌연변이)')
    Clinical_FINDINGS = models.TextField('Clinical FINDINGS', null=True, blank=True, help_text='임상 소견')

    cafe_au_lait_spots = models.IntegerField('Café au lait spots [ >6 and >(0.5 cm or 1.5 cm)]', null=True, blank=True, help_text='커피색의 반점')
    axillary_freckling = models.IntegerField('Axillary Freckling', null=True, blank=True, help_text='겨드랑이 부위 주근깨 (임상학적 진단)')
    cutaneous_neurofibromas = models.IntegerField('Cutaneous neurofibromas', null=True, blank=True, help_text='피부신경섬유종 (피부표면에 나타나는 종양; 임상학적 진단)')
    wide_spread_diffuse_cutaneous_neurofibroma = models.IntegerField('Wide spread diffuse cutaneous neurofibroma', null=True, blank=True, help_text='피하신경섬유종 (진피와 지방층 사이에 나타나는 종양; 임상학적 진단)')
    relative_macrocephaly = models.IntegerField('Relative macrocephaly', null=True, blank=True, help_text='상대적 대두증 (성조숙증으로 인한 평균 이상의 머리둘레; 신체적 평가)')
    lish_nodules = models.IntegerField('Lish nodules', null=True, blank=True, help_text='홍채에 작고 색조를 띈 과오종인 리쉬결절 (안과적 평가)')

    height_at_dx = models.FloatField('Height at Dx', null=True, blank=True, help_text='진단시 환자의 키 (신체적 평가)')
    height_SDS = models.FloatField('Height (SDS)', null=True, blank=True, help_text='상대적 키 (신체적 평가, SD score)')

    learning_difficulty = models.IntegerField('Learning difficulty', null=True, blank=True, help_text='학습장애 (심리학적 평가)')
    adhd = models.IntegerField('ADHD', null=True, blank=True, help_text='주의력결핍 과잉행동장애 (심리학적 평가)')
    autism = models.IntegerField('Autism', null=True, blank=True, help_text='자폐증 (임상학적 평가)')
    seizure = models.IntegerField('Seizure', null=True, blank=True, help_text='발작 (유무; 임상학적 평가)')
    hypertension = models.IntegerField('Hypertension', null=True, blank=True, help_text='고혈압 (유무; 임상학적 평가)')

    cardiac_arrhthmia = models.IntegerField('Cardiac arrhythmia', null=True, blank=True, help_text='심장 부정맥 (유무; 임상학적 평가)')
    Age_at_brain_MR_FINDINGS = models.IntegerField('Age at brain MR FINDINGS', null=True, blank=True, help_text='부정맥 치료에 사용된 의료 시술/기술')
    cardiac_myopathy = models.IntegerField('Cardiac myopathy', null=True, blank=True, help_text='심장 근병증 (유무; 영상학적 소견)')
    Cardiac_myopathy_FINDINGS = models.TextField('Cardiac myopathy FINDINGS', null=True, blank=True, help_text='이상 소견')

    _25_OH_vitamin_D = models.FloatField('25-OH vitamin D', null=True, blank=True, help_text='25-하이드록시 비타민 D 검사 수치')
    HEARING = models.IntegerField('Hearing difficulty', null=True, blank=True, help_text='청력 장애 (유무; 신경학적 판단)')
    OTHER = models.IntegerField('Other', null=True, blank=True, help_text='기타')

    BRAIN_MR_DATE = models.DateField('BRAIN MR DATE', null=True, blank=True, help_text='뇌 MR 촬영 날짜')
    BRAIN_age_at_evaluation = models.IntegerField('Age at brain MR', null=True, blank=True, help_text='뇌 MR 촬영시 연령')
    BRAIN_FINDINGS = models.TextField('MR FINDINGS', null=True, blank=True, help_text='뇌 MR 스캔 결과 기술 (영상학적 판단)')

    FASI = models.IntegerField('FASI(focal areas of signal intensity)', null=True, blank=True, help_text='고음영 병변 (유무; unidentified bright objects, UBO; 임상적 판단)')
    FASI_FINDINGS = models.TextField('FASI FINDINGS', null=True, blank=True, help_text='FASI  발견 부위 (영상학적 판단)')

    optic_pathway_glioma = models.IntegerField('Optic pathway glioma', null=True, blank=True, help_text='시신경교종 (유무; 안과적 진단)')
    Vascular_anomaly = models.IntegerField('Vascular anomaly', null=True, blank=True, help_text='혈관 이상 (유무; 영상학적/흉부외과적 진단)')
    SPINE_MR_DATE = models.DateField('SPINE MR DATE', auto_now=True, blank=True, help_text='척추 MR 스캔 촬영 날짜')
    Age_at_Spine_MR = models.IntegerField('Age at Spine MR', null=True, blank=True,
                                           help_text='척추 MR 촬영시 연령')
    Age_at_Spine_MR_FINDINGS = models.TextField('Age at Spine MR FINDINGS', null=True, blank=True, help_text='척추 MR 스캔 결과 기술 (영상학적 판단)')
    Whole_body_MR_DATE = models.DateField('Whole body MR DATE', auto_now=True, blank=True, help_text='전신 MR 촬영 날짜')
    Age_at_Whole_body_MR = models.TextField('Age at Whole body MR', null=True, blank=True,
                                                help_text='전신 MR 촬영시 나이')
    Age_at_Whole_body_MR_FINDINGS = models.TextField('Age at Whole body MR FINDINGS', null=True, blank=True,
                                                help_text='전신 MR 촬영 결과 기술 (영상학적 판단)')

    # Age at Whole body MR	숫자	전신 MR 촬영시 나이


    plexiform_neurofibromas = models.IntegerField('Plexiform neurofibromas', null=True, blank=True, help_text='총상신경섬유종 (유무; 임상학적 진단)')
    plexiform_neurofibromas_3cm_above = models.IntegerField('Plexiform neurofibromas(>=3cm)', null=True, blank=True, help_text='총상신경섬유종 (3cm 이상; 임상학적 진단)')

    disfigurement = models.IntegerField('Disfigurement', null=True, blank=True, help_text='이형성증')
    aorta_bone_disruption_malignancy = models.IntegerField('위험한 부위(aorta, bone disruption, malignancy) 침범 여부', null=True, blank=True, help_text='위험한 부위의 이형성증')
    with_pain = models.IntegerField('통증 동반', null=True, blank=True, help_text='통증 동반 (유무)')

    malignancy = models.IntegerField('Malignancy', null=True, blank=True, help_text='악성 종양 (유무)')
    brain_tumor = models.IntegerField('Brain tumor', null=True, blank=True, help_text='뇌종양 (유무)')
    nerve_root_tumor = models.IntegerField('Nerve root tumor', null=True, blank=True, help_text='신경근 종양 (유무)')
    malignant_peripheral_nerve_sheath_tumor = models.IntegerField('Malignant peripheral nerve sheath tumor', null=True, blank=True, help_text='악성 말초신경 수초 종양 (유무)')
    moyamoya_ds = models.IntegerField('Moyamoya disease', null=True, blank=True, help_text='모야모야 진단 (합병증 유무)')
    osteopenia = models.IntegerField('Osteopenia', null=True, blank=True, help_text='골감소증 (유무; 정형외과적 판단)')
    Spine_z_score = models.IntegerField('Spine (z score)', null=True, blank=True, help_text='척추 (통계학적 수치)')
    Femur_z_score = models.IntegerField('Femur (z score)', null=True, blank=True, help_text='대퇴골 (통계학적 수치)')

    dysplasia_of_long_bone = models.IntegerField('Dysplasia of long bone', null=True, blank=True, help_text='경골의 이형성증')
    dysplasia_of_long_bone_location = models.CharField('Dysplasia of long bone location', max_length=200, null=True, blank=True, help_text='관찰 부위')

    sphenoid_wing_dysplaisa = models.IntegerField('Sphenoid wing dysplaisa', null=True, blank=True, help_text='접형골의 비정상적인 발달 및 형성부전')
    vertebral_dysplasia = models.IntegerField('Vertebral dysplasia', null=True, blank=True, help_text='척추 이형서증 (유무; 신체적 평가)')

    dural_ectasia = models.IntegerField('Dural ectasia', null=True, blank=True, help_text='경막 확장증 (유무)')
    scoliosis = models.IntegerField('Scoliosis', null=True, blank=True, help_text='척추측만증 (유무; 신체적 평가)')

    breast_examination = models.IntegerField('Breast examination', null=True, blank=True, help_text='유방 초음파 검사 (유무)')
    age_at_breast_USG = models.IntegerField('Age at breast USG', null=True, blank=True, help_text='유방 초음파 검사시 연령')
    BIRADS_I_II_III_IV = models.CharField('BIRADS I/II/III/IV', max_length=200, null=True, blank=True, help_text='질환 경과 단계')
    Breast_USG_FINDINGS = models.TextField('Breast USG FINDINGS', null=True, blank=True, help_text='유방 검사 결과 기술 (외과학적/영상학적 판단)')

    biopsy = models.IntegerField('biopsy', null=True, blank=True, help_text='조직검사 (유무)')
    biopsy_FINDINGS = models.TextField('biopsy FINDINGS', null=True, blank=True, help_text='조직검사 결과')

    operation = models.IntegerField('OPERATION', null=True, blank=True, help_text='수술 유무 (유무)')

    last_follow_up_date = models.IntegerField('last f/u date', null=True, blank=True, help_text='최근 재진/팔로업 날짜')
    last_follow_up_age = models.FloatField('last f/u age', null=True, blank=True, help_text='최근 재진/팔로업시 연령')

    updated_at = models.DateTimeField(auto_now=True, blank=True)  # 업데이트 시각
    created_at = models.DateTimeField(auto_now_add=True, blank=True)  # 생성 시각

