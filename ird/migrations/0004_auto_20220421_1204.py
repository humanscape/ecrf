# Generated by Django 3.2.4 on 2022-04-21 03:04

from django.db import migrations, models
import ird.models


class Migration(migrations.Migration):

    dependencies = [
        ('ird', '0003_auto_20220413_2207'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='irdhistory',
            name='first_symptom_year',
        ),
        migrations.AddField(
            model_name='irdhistory',
            name='comment',
            field=models.TextField(blank=True, null=True, verbose_name='기타 세부 내용'),
        ),
        migrations.AddField(
            model_name='irdhistory',
            name='dazzling',
            field=models.IntegerField(blank=True, choices=[(1, '있음'), (2, '없음')], help_text='눈부심을 경험한 적이 있나요', null=True, verbose_name='눈부심'),
        ),
        migrations.AddField(
            model_name='irdhistory',
            name='dazzling_age',
            field=models.PositiveIntegerField(blank=True, help_text='눈부심 증상이 처음 나타났던 나이를 적어주세요 ', null=True, verbose_name='눈부심 나이'),
        ),
        migrations.AlterField(
            model_name='irdhistory',
            name='cataract_op',
            field=ird.models.ChoiceArrayField(base_field=models.CharField(blank=True, choices=[(1, '있음'), (2, '없음')], max_length=200, null=True), blank=True, help_text='백내장 수술을 받은 적이 있나요?', null=True, size=None, verbose_name='백내장 수술'),
        ),
        migrations.AlterField(
            model_name='irdhistory',
            name='cystoid_macular_edema_od',
            field=models.IntegerField(blank=True, choices=[(0, 0), (1, 1)], help_text='황반 부음', null=True, verbose_name='CME'),
        ),
        migrations.AlterField(
            model_name='irdhistory',
            name='familyhistory_diagnosis1',
            field=ird.models.ChoiceArrayField(base_field=models.CharField(blank=True, choices=[(0, '없음'), (1, '잘 모르겠음'), (2, '자녀 및 손자/손녀'), (3, '모계 직계(어머니, 외할아버지/할머니)'), (4, '부계 직계(아버지, 할아버지/할머니)'), (5, '모계 4촌 이내(외숙부/이모, 사촌 형제자매)'), (6, '부계 4촌 이내(백부/숙부/고모, 사촌 형제자매)')], max_length=200, null=True), blank=True, help_text='가족 중 같은 종류의 유전성 망막질환을 진단받은 사람이 있나요? 모두 선택해주세요', null=True, size=None, verbose_name='같은 종류 진단 받은 가족'),
        ),
        migrations.AlterField(
            model_name='irdhistory',
            name='familyhistory_diagnosis3',
            field=ird.models.ChoiceArrayField(base_field=models.CharField(blank=True, choices=[(0, '없음'), (1, '잘 모르겠음'), (2, '자녀 및 손자/손녀'), (3, '모계 직계(어머니, 외할아버지/할머니)'), (4, '부계 직계(아버지, 할아버지/할머니)'), (5, '모계 4촌 이내(외숙부/이모, 사촌 형제자매)'), (6, '부계 4촌 이내(백부/숙부/고모, 사촌 형제자매)')], max_length=200, null=True), blank=True, help_text='가족 중 다른 종류의 유전성 망막질환을 진단받은 사람을 모두 선택해주세요', null=True, size=None, verbose_name='다른 종류 진단 받은 가족 선택'),
        ),
        migrations.AlterField(
            model_name='irdhistory',
            name='first_diagnosis_age',
            field=models.TextField(blank=True, help_text='진단을 처음 받았던 때는 언제였나요?', null=True, verbose_name='첫 진단 나이'),
        ),
        migrations.AlterField(
            model_name='irdhistory',
            name='glaucoma_op',
            field=ird.models.ChoiceArrayField(base_field=models.CharField(blank=True, choices=[(1, '오른쪽 눈'), (2, '왼쪽 눈'), (3, '수술하지 않음')], max_length=200, null=True), blank=True, help_text='녹내장 수술을 받은 적이 있나요?', null=True, size=None, verbose_name='녹내장 수술'),
        ),
        migrations.AlterField(
            model_name='irdhistory',
            name='photopsia',
            field=models.IntegerField(blank=True, choices=[(1, '있음'), (2, '없음')], help_text='광시증을 경험한 적이 있나요?', null=True, verbose_name='광시증'),
        ),
        migrations.AlterField(
            model_name='irdhistory',
            name='photopsia_age',
            field=models.PositiveIntegerField(blank=True, help_text='광시증 증상이 처음 나타났던 나이를 적어주세요 ', null=True, verbose_name='광시증 나이'),
        ),
        migrations.AlterField(
            model_name='irdhistory',
            name='retinal_detachment_op',
            field=ird.models.ChoiceArrayField(base_field=models.CharField(blank=True, choices=[(1, '오른쪽 눈'), (2, '왼쪽 눈'), (3, '수술하지 않음')], max_length=200, null=True), blank=True, help_text='망막 박리 수술을 받은 적이 있나요?', null=True, size=None, verbose_name='망막박리 수술'),
        ),
        migrations.AlterField(
            model_name='irdhistory',
            name='retinitis_punctata_albescens_od',
            field=models.IntegerField(blank=True, choices=[(0, 0), (1, 1)], help_text='백점상망막염', null=True, verbose_name='retinitis_punctata_albescens'),
        ),
        migrations.AlterField(
            model_name='irdhistory',
            name='sector_rp_od',
            field=models.IntegerField(blank=True, choices=[(0, 0), (1, 1)], help_text='부채형 RP', null=True, verbose_name='sector_RP'),
        ),
        migrations.AlterField(
            model_name='irdhistory',
            name='sex',
            field=models.IntegerField(blank=True, choices=[(1, 1), (2, 2)], help_text='성별 (1:남자  2:여자)', null=True, verbose_name='성별'),
        ),
        migrations.AlterField(
            model_name='irdhistory',
            name='underlying_disease1',
            field=ird.models.ChoiceArrayField(base_field=models.CharField(blank=True, choices=[(0, '없음'), (1, '청각장애'), (2, '당뇨'), (3, '평형감각 이상'), (4, '지적장애'), (5, '비뇨기계 이상'), (6, '다지증'), (7, '매독'), (8, '바이러스 질환'), (9, '악성종양'), (10, '포도막염')], max_length=200, null=True), blank=True, help_text='과거 앓았거나 현재 앓고 있는 질환이 있나요? 모두 선택해주세요', null=True, size=None, verbose_name='기저질환'),
        ),
    ]