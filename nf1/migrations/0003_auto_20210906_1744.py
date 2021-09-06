# Generated by Django 3.2.4 on 2021-09-06 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nf1', '0002_auto_20210906_1710'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crf',
            name='NF1_genotype',
        ),
        migrations.AddField(
            model_name='crf',
            name='date_at_breast_USG',
            field=models.DateField(blank=True, help_text='유방 초음파 검사 날짜<br/>입력시 유방 초음파 검사시 나이가 입력됩니다.', null=True, verbose_name='Date at breast USG'),
        ),
        migrations.AddField(
            model_name='crf',
            name='nf1_mutation',
            field=models.IntegerField(blank=True, choices=[(0, '없음'), (1, '있음')], help_text='NF1 돌연변이<br/>0 : 없음<br/>1 : 있음', null=True, verbose_name='NF1 mutation'),
        ),
        migrations.AlterField(
            model_name='crf',
            name='BIRADS_I_II_III_IV',
            field=models.IntegerField(blank=True, choices=[(1, 'BIRADS I'), (2, 'BIRADS II'), (3, 'BIRADS III'), (4, 'BIRADS IV')], help_text='질환 경과 단계', null=True, verbose_name='BIRADS I/II/III/IV'),
        ),
        migrations.AlterField(
            model_name='crf',
            name='BRAIN_MR_DATE',
            field=models.DateField(blank=True, help_text='뇌 MR 촬영 날짜<br/>입력시 뇌 MR 촬영시 나이가 입력됩니다.', null=True, verbose_name='BRAIN MR DATE'),
        ),
        migrations.AlterField(
            model_name='crf',
            name='FASI',
            field=models.IntegerField(blank=True, choices=[(0, '없음'), (1, '있음'), (2, '모름')], help_text='고음영 병변 (유무; unidentified bright objects, UBO; 임상적 판단)', null=True, verbose_name='FASI(focal areas of signal intensity)'),
        ),
        migrations.AlterField(
            model_name='crf',
            name='HEARING',
            field=models.IntegerField(blank=True, choices=[(0, '없음'), (1, '있음'), (2, '모름')], help_text='청력 장애 (유무; 신경학적 판단)', null=True, verbose_name='Hearing difficulty'),
        ),
        migrations.AlterField(
            model_name='crf',
            name='Vascular_anomaly',
            field=models.IntegerField(blank=True, choices=[(0, '없음'), (1, '있음'), (2, '모름')], help_text='혈관 이상 (유무; 영상학적/흉부외과적 진단)', null=True, verbose_name='Vascular anomaly'),
        ),
        migrations.AlterField(
            model_name='crf',
            name='Whole_body_MR_DATE',
            field=models.DateField(blank=True, help_text='전신 MR 촬영 날짜<br/>입력시 전신 MR 촬영시 나이가 입력됩니다.', null=True, verbose_name='Whole body MR DATE'),
        ),
        migrations.AlterField(
            model_name='crf',
            name='_25_OH_vitamin_D',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='25-하이드록시 비타민 D 검사 수치<br/>단위 ng/mL', max_digits=10, null=True, verbose_name='25-OH vitamin D'),
        ),
        migrations.AlterField(
            model_name='crf',
            name='adhd',
            field=models.IntegerField(blank=True, choices=[(0, '없음'), (1, '있음'), (2, '모름')], help_text='주의력결핍 과잉행동장애 (심리학적 평가)', null=True, verbose_name='ADHD'),
        ),
        migrations.AlterField(
            model_name='crf',
            name='age',
            field=models.PositiveIntegerField(blank=True, help_text='(자동 반영)나이', null=True, verbose_name='Age'),
        ),
        migrations.AlterField(
            model_name='crf',
            name='age_at_breast_USG',
            field=models.PositiveIntegerField(blank=True, help_text='유방 초음파 검사시 나이', null=True, verbose_name='Age at breast USG'),
        ),
        migrations.AlterField(
            model_name='crf',
            name='age_at_dx',
            field=models.PositiveIntegerField(blank=True, help_text='(자동 반영)진단시 나이', null=True, verbose_name='Age at Dx'),
        ),
        migrations.AlterField(
            model_name='crf',
            name='age_at_evaluation',
            field=models.PositiveIntegerField(blank=True, help_text='(자동 반영)유전자 검사시 나이', null=True, verbose_name='Age at evaluation'),
        ),
        migrations.AlterField(
            model_name='crf',
            name='aorta_bone_disruption_malignancy',
            field=models.IntegerField(blank=True, choices=[(0, '없음'), (1, '있음'), (2, '모름')], help_text='위험한 부위의 이형성증', null=True, verbose_name='위험한 부위(aorta, bone disruption, malignancy) 침범 여부'),
        ),
        migrations.AlterField(
            model_name='crf',
            name='autism',
            field=models.IntegerField(blank=True, choices=[(0, '없음'), (1, '있음'), (2, '모름')], help_text='자폐증 (임상학적 평가)', null=True, verbose_name='Autism'),
        ),
        migrations.AlterField(
            model_name='crf',
            name='axillary_freckling',
            field=models.IntegerField(blank=True, choices=[(0, '없음'), (1, '있음'), (2, '모름')], help_text='겨드랑이 부위 주근깨 (임상학적 진단)', null=True, verbose_name='Axillary Freckling'),
        ),
        migrations.AlterField(
            model_name='crf',
            name='biopsy',
            field=models.PositiveIntegerField(blank=True, choices=[(0, '없음'), (1, '있음'), (2, '모름')], help_text='조직검사 (유무)', null=True, verbose_name='biopsy'),
        ),
        migrations.AlterField(
            model_name='crf',
            name='brain_tumor',
            field=models.IntegerField(blank=True, choices=[(0, '없음'), (1, '있음'), (2, '모름')], help_text='뇌종양 (유무)', null=True, verbose_name='Brain tumor'),
        ),
        migrations.AlterField(
            model_name='crf',
            name='breast_examination',
            field=models.PositiveIntegerField(blank=True, choices=[(0, '없음'), (1, '있음'), (2, '모름')], help_text='유방 초음파 검사 (유무)', null=True, verbose_name='Breast examination'),
        ),
        migrations.AlterField(
            model_name='crf',
            name='cafe_au_lait_spots',
            field=models.IntegerField(blank=True, choices=[(0, '없음'), (1, '있음'), (2, '모름')], help_text='커피색의 반점', null=True, verbose_name='Café au lait spots [ >6 and >(0.5 cm or 1.5 cm)]'),
        ),
        migrations.AlterField(
            model_name='crf',
            name='cardiac_arrhthmia',
            field=models.IntegerField(blank=True, choices=[(0, '없음'), (1, '있음'), (2, '모름')], help_text='심장 부정맥 (유무; 임상학적 평가)', null=True, verbose_name='Cardiac arrhythmia'),
        ),
        migrations.AlterField(
            model_name='crf',
            name='cardiac_myopathy',
            field=models.IntegerField(blank=True, choices=[(0, '없음'), (1, '있음'), (2, '모름')], help_text='심장 근병증 (유무; 영상학적 소견)', null=True, verbose_name='Cardiac myopathy'),
        ),
        migrations.AlterField(
            model_name='crf',
            name='cutaneous_neurofibromas',
            field=models.IntegerField(blank=True, choices=[(0, '없음'), (1, '있음'), (2, '모름')], help_text='피부신경섬유종 (피부표면에 나타나는 종양; 임상학적 진단)', null=True, verbose_name='Cutaneous neurofibromas'),
        ),
        migrations.AlterField(
            model_name='crf',
            name='date_at_dx',
            field=models.DateField(blank=True, help_text='진단 받은 날짜<br/>입력시 진단시의 나이가 입력됩니다.', null=True, verbose_name='Date at Dx'),
        ),
        migrations.AlterField(
            model_name='crf',
            name='date_at_evaluation_dna',
            field=models.DateField(blank=True, help_text='유전자 검사 날짜<br/>입력시 유전자 검사시의 나이가 입력됩니다.', null=True, verbose_name='Date at evaluation(유전자 검사)'),
        ),
        migrations.AlterField(
            model_name='crf',
            name='disfigurement',
            field=models.IntegerField(blank=True, choices=[(0, '없음'), (1, '있음'), (2, '모름')], help_text='이형성증', null=True, verbose_name='Disfigurement'),
        ),
        migrations.AlterField(
            model_name='crf',
            name='dna',
            field=models.CharField(blank=True, help_text='유전자 변이 (DNA)<br/>예제 c.7126G>C', max_length=200, null=True, verbose_name='DNA'),
        ),
        migrations.AlterField(
            model_name='crf',
            name='domain',
            field=models.CharField(blank=True, help_text='<br>Cysteine/serine rich domain with three cystein pairs (CSRD)<br>- ATP binding, cAMP- dependent protein kinase (PKA) recognition site<br>- exon 11-17,<br>- p. 543-909<br><br>Tub<br> - p. 1095-1176<br><br>GTPase- activating protein (GAP) related domain (GRD)<br> - catalytic RasGAP activity<br> - exon20-27a, <br>-  p. 1198-1530<br><br>Sec14-line lipid binding domain<br> - p. 1560 – 1698<br><br>Pleckstin homology(PH) like domain<br> - p. 1713 – 1816<br><br>Syn<br> - p. 2619 – 2719"<br>    ', max_length=20, null=True, verbose_name='Domain'),
        ),
        migrations.AlterField(
            model_name='crf',
            name='dural_ectasia',
            field=models.IntegerField(blank=True, choices=[(0, '없음'), (1, '있음'), (2, '모름')], help_text='경막 확장증 (유무)', null=True, verbose_name='Dural ectasia'),
        ),
        migrations.AlterField(
            model_name='crf',
            name='dysplasia_of_long_bone',
            field=models.IntegerField(blank=True, choices=[(0, '없음'), (1, '있음'), (2, '모름')], help_text='경골의 이형성증', null=True, verbose_name='Dysplasia of long bone'),
        ),
        migrations.AlterField(
            model_name='crf',
            name='family_hx',
            field=models.PositiveIntegerField(blank=True, choices=[(0, '없음'), (1, '있음')], help_text='가족 병력<br/>(0:없음, 1: 있음, 모름)', null=True, verbose_name='Family Hx'),
        ),
        migrations.AlterField(
            model_name='crf',
            name='height_at_dx',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='진단시 환자의 키 (신체적 평가)<br/>단위 cm', max_digits=10, null=True, verbose_name='Height at Dx'),
        ),
        migrations.AlterField(
            model_name='crf',
            name='hypertension',
            field=models.IntegerField(blank=True, choices=[(0, '없음'), (1, '있음'), (2, '모름')], help_text='고혈압 (유무; 임상학적 평가)', null=True, verbose_name='Hypertension'),
        ),
        migrations.AlterField(
            model_name='crf',
            name='inframe_deletion_or_insertion',
            field=models.IntegerField(blank=True, choices=[(0, '없음'), (1, '있음'), (2, '모름')], help_text='인프레임 삭제 또는 삽입 (유전자 전사와 번역 과정이 중지되지 않음)', null=True, verbose_name='Inframe deletion or insertion'),
        ),
        migrations.AlterField(
            model_name='crf',
            name='learning_difficulty',
            field=models.PositiveIntegerField(blank=True, choices=[(0, '없음'), (1, '있음'), (2, '모름')], help_text='학습장애 (심리학적 평가)', null=True, verbose_name='Learning difficulty'),
        ),
        migrations.AlterField(
            model_name='crf',
            name='lish_nodules',
            field=models.IntegerField(blank=True, choices=[(0, '없음'), (1, '있음'), (2, '모름')], help_text='홍채에 작고 색조를 띈 과오종인 리쉬결절 (안과적 평가)', null=True, verbose_name='Lish nodules'),
        ),
        migrations.AlterField(
            model_name='crf',
            name='malignancy',
            field=models.IntegerField(blank=True, choices=[(0, '없음'), (1, '있음'), (2, '모름')], help_text='악성 종양 (유무)', null=True, verbose_name='Malignancy'),
        ),
        migrations.AlterField(
            model_name='crf',
            name='malignant_peripheral_nerve_sheath_tumor',
            field=models.IntegerField(blank=True, choices=[(0, '없음'), (1, '있음'), (2, '모름')], help_text='악성 말초신경 수초 종양 (유무)', null=True, verbose_name='Malignant peripheral nerve sheath tumor'),
        ),
        migrations.AlterField(
            model_name='crf',
            name='moyamoya_ds',
            field=models.IntegerField(blank=True, choices=[(0, '없음'), (1, '있음'), (2, '모름')], help_text='모야모야 진단 (합병증 유무)', null=True, verbose_name='Moyamoya disease'),
        ),
        migrations.AlterField(
            model_name='crf',
            name='nerve_root_tumor',
            field=models.IntegerField(blank=True, choices=[(0, '없음'), (1, '있음'), (2, '모름')], help_text='신경근 종양 (유무)', null=True, verbose_name='Nerve root tumor'),
        ),
        migrations.AlterField(
            model_name='crf',
            name='nf1_haploinsufficiency_type',
            field=models.IntegerField(blank=True, choices=[(0, '없음'), (1, '있음'), (2, '모름')], help_text='반수체 부족 유형', null=True, verbose_name='NF1 haploinsufficiency type'),
        ),
        migrations.AlterField(
            model_name='crf',
            name='novel_mutation',
            field=models.IntegerField(blank=True, choices=[(0, '없음'), (1, '있음'), (2, '모름')], help_text='드 노보 유전자 돌연변이 (유무; 유전성이 아닌 돌연변이)', null=True, verbose_name='Novel mutation'),
        ),
        migrations.AlterField(
            model_name='crf',
            name='operation',
            field=models.PositiveIntegerField(blank=True, choices=[(0, '없음'), (1, '있음'), (2, '모름')], help_text='수술 유무 (유무)', null=True, verbose_name='OPERATION'),
        ),
        migrations.AlterField(
            model_name='crf',
            name='optic_pathway_glioma',
            field=models.IntegerField(blank=True, choices=[(0, '없음'), (1, '있음'), (2, '모름')], help_text='시신경교종 (유무; 안과적 진단)', null=True, verbose_name='Optic pathway glioma'),
        ),
        migrations.AlterField(
            model_name='crf',
            name='osteopenia',
            field=models.IntegerField(blank=True, choices=[(0, '없음'), (1, '있음'), (2, '모름')], help_text='골감소증 (유무; 정형외과적 판단)', null=True, verbose_name='Osteopenia'),
        ),
        migrations.AlterField(
            model_name='crf',
            name='plexiform_neurofibromas',
            field=models.IntegerField(blank=True, choices=[(0, '없음'), (1, '있음'), (2, '모름')], help_text='총상신경섬유종 (유무; 임상학적 진단)', null=True, verbose_name='Plexiform neurofibromas'),
        ),
        migrations.AlterField(
            model_name='crf',
            name='plexiform_neurofibromas_3cm_above',
            field=models.IntegerField(blank=True, choices=[(0, '없음'), (1, '있음'), (2, '모름')], help_text='총상신경섬유종 (3cm 이상; 임상학적 진단)', null=True, verbose_name='Plexiform neurofibromas(>=3cm)'),
        ),
        migrations.AlterField(
            model_name='crf',
            name='protein',
            field=models.CharField(blank=True, help_text='유전자 변이 (protein)<br/>예제 p.Gly2376Arg', max_length=200, null=True, verbose_name='Protein'),
        ),
        migrations.AlterField(
            model_name='crf',
            name='relative_macrocephaly',
            field=models.IntegerField(blank=True, choices=[(0, '없음'), (1, '있음'), (2, '모름')], help_text='상대적 대두증 (성조숙증으로 인한 평균 이상의 머리둘레; 신체적 평가)', null=True, verbose_name='Relative macrocephaly'),
        ),
        migrations.AlterField(
            model_name='crf',
            name='scoliosis',
            field=models.IntegerField(blank=True, choices=[(0, '없음'), (1, '있음'), (2, '모름')], help_text='척추측만증 (유무; 신체적 평가)', null=True, verbose_name='Scoliosis'),
        ),
        migrations.AlterField(
            model_name='crf',
            name='seizure',
            field=models.IntegerField(blank=True, choices=[(0, '없음'), (1, '있음'), (2, '모름')], help_text='발작 (유무; 임상학적 평가)', null=True, verbose_name='Seizure'),
        ),
        migrations.AlterField(
            model_name='crf',
            name='sphenoid_wing_dysplaisa',
            field=models.IntegerField(blank=True, choices=[(0, '없음'), (1, '있음'), (2, '모름')], help_text='접형골의 비정상적인 발달 및 형성부전', null=True, verbose_name='Sphenoid wing dysplaisa'),
        ),
        migrations.AlterField(
            model_name='crf',
            name='vertebral_dysplasia',
            field=models.IntegerField(blank=True, choices=[(0, '없음'), (1, '있음'), (2, '모름')], help_text='척추 이형서증 (유무; 신체적 평가)', null=True, verbose_name='Vertebral dysplasia'),
        ),
        migrations.AlterField(
            model_name='crf',
            name='wide_spread_diffuse_cutaneous_neurofibroma',
            field=models.IntegerField(blank=True, choices=[(0, '없음'), (1, '있음'), (2, '모름')], help_text='피하신경섬유종 (진피와 지방층 사이에 나타나는 종양; 임상학적 진단)', null=True, verbose_name='Wide spread diffuse cutaneous neurofibroma'),
        ),
        migrations.AlterField(
            model_name='crf',
            name='with_pain',
            field=models.IntegerField(blank=True, choices=[(0, '없음'), (1, '있음'), (2, '모름')], help_text='통증 동반 (유무)', null=True, verbose_name='통증 동반'),
        ),
        migrations.AlterField(
            model_name='crfoperations',
            name='date',
            field=models.DateField(blank=True, help_text='수술 시기<br/>수술시기 입력시 나이가 입력됩니다.', null=True, verbose_name='수술 시기'),
        ),
    ]
