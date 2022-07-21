from django.db import models
from django.contrib.postgres.fields import ArrayField
from django import forms
from django.core import exceptions


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


class Ks(models.Model):
    SEX_CHOICES = ((1, '남자'), (2, '여자'))
    EXISTENCE_DN_CHOICES = ((1, '있음'), (2, '없음'), (3, '모름'))

    YES_NO_CHOICES = ((1, '네'), (2, '아니오'))

    DISABILITY_GRADE_1_CHOICES = ((1, '1급'), (2, '2급'), (3, '3급'), (4, '4급'), (5, '5급'), (6, '6급'), (7, '등급 외(장애 정도)'))
    DISABILITY_GRADE_2_CHOICES = ((1, '장애 정도가 심한 장애인(중증)'), (2, '장애 정도가 심하지 않은 장애인(경증)'), (3, '장애 정도 미해당'))

    patient_number = models.PositiveIntegerField('대상자 번호', null=True, blank=True, help_text='대상자 번호')
    icf_date = models.DateField('연구 동의 날짜', null=True, blank=True, help_text='연구 동의 날짜')
    sex = models.IntegerField('성별', choices=SEX_CHOICES, null=True, blank=True, help_text='성별')
    birthdate = models.DateField('생년월일', null=True, blank=True, help_text='생년월일')
    diagnosis_age = models.DateField('진단 받은 날짜', null=True, blank=True, help_text='가부키 증후군 진단 받은 날짜')
    familyhistory_1 = models.IntegerField('가족 병력', choices=EXISTENCE_DN_CHOICES, null=True, blank=True,
                                          help_text='가족 병력<br/>')

    FAMILY_HISTORY_CHOICES = ((0, '-'), (1, '부'), (2, '모'), (3, '형제'), (4, '자녀'))
    familyhistory_2 = models.IntegerField('가족 병력 관계', choices=FAMILY_HISTORY_CHOICES, null=True, blank=True,
                                          help_text='가족 병력 관계<br/>')
    familyhistory_2_multiple = ChoiceArrayField(models.CharField(max_length=200, choices=FAMILY_HISTORY_CHOICES,
                                                                 null=True, blank=True),
                                                verbose_name='가족 병력 관계',
                                                help_text='가족 병력 관계<br/>',
                                                null=True, blank=True)
    birth_weight = models.DecimalField('출생시 체중', max_digits=10, decimal_places=2, null=True, blank=True,
                                       help_text='출생시 체중')
    gestational_age = models.TextField('출생시 재태주수', null=True, blank=True, help_text='출생시 재태주수')
    height = models.DecimalField('현재 키', max_digits=10, decimal_places=2, null=True, blank=True, help_text='현재 키')
    weight = models.DecimalField('현재 체중', max_digits=10, decimal_places=2, null=True, blank=True, help_text='현재 체중')
    disability_grade_1 = models.IntegerField('지적장애 등급', choices=DISABILITY_GRADE_1_CHOICES, null=True, blank=True,
                                             help_text='지적장애 등급')
    disability_grade_2 = models.IntegerField('지적장애 정도', choices=DISABILITY_GRADE_2_CHOICES, null=True, blank=True,
                                             help_text='지적장애 정도')

    GROWTH_CHOICES = ((0, 'N'),
                      (1, 'Short stature'),
                      (2, 'Failure to thrive'),
                      (3, 'Obesity'))
    growth = ChoiceArrayField(models.CharField(max_length=200, choices=GROWTH_CHOICES,
                                               null=True, blank=True),
                              verbose_name='성장 이상 소견',
                              help_text='성장 이상 소견',
                              null=True, blank=True)

    growth_hormone_1 = models.IntegerField('성장호르몬결핍증 유무', choices=YES_NO_CHOICES, null=True, blank=True,
                                           help_text='성장호르몬결핍증 유무')
    growth_hormone_2 = models.IntegerField('성장 호르몬(IGF-1)검사 시행', choices=YES_NO_CHOICES, null=True,
                                           blank=True, help_text='성장 호르몬(IGF-1)검사 시행')
    growth_hormone_3 = models.DecimalField('성장호르몬(IGF-1)수치', max_digits=10, decimal_places=2, null=True, blank=True,
                                           help_text='가장 최근 성장호르몬 수치')
    precocious_puberty = models.IntegerField('성조숙증진단', choices=YES_NO_CHOICES, null=True, blank=True,
                                             help_text='성조숙증진단')
    EAR_CHOICES = ((0, 'N'),
                   (1, 'Sensorineural hearing impairmen'),
                   (2, 'Conductive hearing impairment'),
                   (3, 'Macrotia'),
                   (4, 'Protruding ear'))
    ear = ChoiceArrayField(models.CharField(max_length=200, choices=EAR_CHOICES,
                                            null=True, blank=True),
                           verbose_name='귀 관련 이상 소견',
                           help_text='귀 관련 이상 소견',
                           null=True, blank=True)

    ear_test = models.TextField('귀 관련 검사 소견', null=True, blank=True, help_text='귀 관련 검사 소견')
    EYE_CHOICES = ((0, 'N'),
                   (1, 'Nystagmus'),
                   (2, 'Strabismus'),
                   (3, 'Microcornea'),
                   (4, 'Ptosis'),
                   (5, 'Blue sclerae'),
                   (6, 'Coloboma'))
    eye = ChoiceArrayField(models.CharField(max_length=200, choices=EYE_CHOICES,
                                            null=True, blank=True),
                           verbose_name='안과적 이상 소견',
                           help_text='안과적 이상 소견',
                           null=True, blank=True)
    eye_test = models.TextField('안과적 검사 소견', null=True, blank=True, help_text='안과적 검사 소견')
    HEAD_AND_NECK_CHOICES = ((0, 'N'),
                             (1, 'Abnormality of the dentition'),
                             (2, 'Cleft palate'),
                             (3, 'Eversion of lateral third of lower eyelids'),
                             (4, 'Short columella'),
                             (5, 'Microdontia'),
                             (6, 'Widely spaced teeth'),
                             (7, 'Hypodontia'),
                             (8, 'Mask-like facies'),
                             (9, 'High palate'),
                             (10, 'Oral cleft'),
                             (11, 'Abnormality of dental morphology'))
    head_and_neck = ChoiceArrayField(models.CharField(max_length=200, choices=HEAD_AND_NECK_CHOICES,
                                                      null=True, blank=True),
                                     verbose_name='머리와 목 이상 소견',
                                     help_text='머리와 목 이상 소견',
                                     null=True, blank=True)
    head_and_neck_test = models.TextField('머리와 목 검사 소견', null=True, blank=True, help_text='머리와 목 검사 소견')
    CARDIOVASCULAR_CHOICES = ((1, 'N'),
                              (2, 'Abnormal cardiac septum morphology'),
                              (3, 'Coarctation of aorta'))
    cardiovascular = ChoiceArrayField(models.CharField(max_length=200, choices=CARDIOVASCULAR_CHOICES,
                                                       null=True, blank=True),
                                      verbose_name='심혈관 이상 소견',
                                      help_text='심혈관 이상 소견',
                                      null=True, blank=True)

    models.IntegerField('심혈관 이상 소견', choices=[(i, i) for i in range(3)], null=True, blank=True,
                        help_text='심혈관 이상 소견')
    cardiovascular_test = models.TextField('심혈관 검사 소견', null=True, blank=True, help_text='심혈관 검사 소견')
    digestive_system = models.IntegerField('소화계 이상 소견', choices=YES_NO_CHOICES, null=True, blank=True,
                                           help_text='소화계 이상 소견')
    digestive_system_test = models.TextField('소화계 검사 소견', null=True, blank=True, help_text='소화계 검사 소견')

    GENITOURINARY_SYSTEM_CHOICES = ((0, 'N'),
                                    (1, 'Hypoplasia of penis'),
                                    (2, 'Renal hypoplasia /aplasia'),
                                    (3, 'Duplicated collecting system'),
                                    (4, 'Ureteropelvic junction obstruction'),
                                    (5, 'Hypospadias'),
                                    (6, 'Cryptorchidism'),
                                    (7, 'Hydronephrosis'),
                                    (8, 'Abnormal localization of kidney'),
                                    (9, 'Crossed fused renal ectopia'))
    genitourinary_system = ChoiceArrayField(models.CharField(max_length=200, choices=GENITOURINARY_SYSTEM_CHOICES,
                                                             null=True, blank=True),
                                            verbose_name='비뇨 생식기 이상 유무',
                                            help_text='비뇨 생식기 이상 소견',
                                            null=True, blank=True)
    genitourinary_system_test = models.TextField('비뇨 생식기 이상 관련 검사 소견', null=True, blank=True, help_text='비뇨 생식기 검사 소견')
    IMMUNOLOGY_CHOICES = ((0, 'N'),
                          (1, 'Abnormality of immune system physiology'),
                          (2, 'Recurrent infections'))
    Immunology = ChoiceArrayField(models.CharField(max_length=200, choices=IMMUNOLOGY_CHOICES,
                                                   null=True, blank=True),
                                  verbose_name='면역학 이상 유무',
                                  help_text='면역학 이상 소견',
                                  null=True, blank=True)
    thyroid = models.IntegerField('갑상선기능이상', choices=YES_NO_CHOICES, null=True, blank=True,
                                  help_text='갑상선기능이상')
    thyroid_test = models.IntegerField('갑상선기능 검사 시행', choices=YES_NO_CHOICES, null=True, blank=True,
                                       help_text='갑상선기능 검사 시행')
    tsh = models.DecimalField('TSH', max_digits=10, decimal_places=2, null=True, blank=True, help_text='가장 최근 TSH 수치')
    t3 = models.DecimalField('T3', max_digits=10, decimal_places=2, null=True, blank=True, help_text='가장 최근 T3 수치')
    free_t4 = models.DecimalField('free T4', max_digits=10, decimal_places=2, null=True, blank=True,
                                  help_text='가장 최근 free T4 수치')
    SKELETAL_SYSTEM_CHOICES = ((0, 'N'),
                               (1, 'Scoliosis'),
                               (2, 'Abnormal form of the vertebral bodies'),
                               (3, 'Butterfly vertebrae'),
                               (4, 'Vertebral clefting'),
                               (5, 'Joint hyperflexibility'),
                               (6, 'Hemiverteb'))
    skeletal_system = ChoiceArrayField(models.CharField(max_length=200, choices=SKELETAL_SYSTEM_CHOICES,
                                                        null=True, blank=True),
                                       verbose_name='골격계 이상 소견',
                                       help_text='골격계 이상 소견',
                                       null=True, blank=True)
    skeletal_system_test = models.TextField('골격계 검사 소견', null=True, blank=True, help_text='골격계 검사 소견')
    hypotonia = models.IntegerField('근기능 저하 유무', choices=YES_NO_CHOICES, null=True, blank=True,
                                    help_text='근기능 저하 유무')
    LIMBS_CHOICES = ((0, 'N'),
                     (1, 'Small hand'),
                     (2, 'Short 5th finger'),
                     (4, 'Short middle phalanx of finger'),
                     (5, 'Hip dislocation'))
    limbs = ChoiceArrayField(models.CharField(max_length=200, choices=LIMBS_CHOICES,
                                              null=True, blank=True),
                             verbose_name='사지 이상 소견',
                             help_text='사지 이상 소견',
                             null=True, blank=True)
    limbs_test = models.TextField('사지 검사 소견', null=True, blank=True, help_text='사지 검사 소견')
    congenital_diaphragmatic_hernia = models.IntegerField('선천성 횡경막 탈장 유무', choices=YES_NO_CHOICES,
                                                          null=True, blank=True, help_text='선천성 횡경막 탈장 유무')

    SKIN_HAIR_NAILS_CHOICES = ((0, 'N'),
                               (1, 'Highly arched eyebrow'),
                               (2, 'Abnormal dermatoglyphics'),
                               (3, 'Lip pit'),
                               (4, 'Preauricular skin tag'),
                               (5, 'Sparse lateral eyebrow'),
                               (6, 'Long eyelashes'))
    skin_hair_nails = ChoiceArrayField(models.CharField(max_length=200, choices=SKIN_HAIR_NAILS_CHOICES,
                                                        null=True, blank=True),
                                       verbose_name='피부, 머리카락, 손톱 이상 소견',
                                       help_text='피부, 머리카락, 손톱 이상 소견',
                                       null=True, blank=True)

    skin_hair_nails_test = models.TextField('피부, 머리카락, 손톱 검사 소견', null=True, blank=True, help_text='피부, 머리카락, 손톱 검사 소견')
    NERVOUS_SYSTEM_CHOICES = ((0, 'N'),
                              (1, 'Seizure'),
                              (2, 'Cerebral cortical atrophy'),
                              (3, 'Ventriculomegaly'),
                              (4, 'EEG abnormality'),
                              (5, 'Hydrocephalus'),
                              (6, 'Microcephaly'))
    nervous_system = ChoiceArrayField(models.CharField(max_length=200, choices=NERVOUS_SYSTEM_CHOICES,
                                                       null=True, blank=True),
                                      verbose_name='신경계 이상 소견',
                                      help_text='신경계 이상 유무',
                                      null=True, blank=True)

    nervous_system_test = models.TextField('신경계 검사 소견', null=True, blank=True, help_text='신경계 검사 유무')
    adhd = models.IntegerField('ADHD 유무', choices=YES_NO_CHOICES, null=True, blank=True,
                               help_text='ADHD 유무')
    autism = models.IntegerField('자폐증 유무', choices=YES_NO_CHOICES, null=True, blank=True,
                                 help_text='자폐증 유무')
    diabetes = models.IntegerField('당뇨병 유무', choices=YES_NO_CHOICES, null=True, blank=True,
                                   help_text='당뇨병 유무')
    hba1c = models.IntegerField('HbA1C 검사 시행 ', choices=YES_NO_CHOICES, null=True, blank=True,
                                help_text='HbA1C 검사 시행')
    hba1c_test = models.DecimalField('HbA1C 수치', max_digits=10, decimal_places=2, null=True, blank=True,
                                     help_text='가장 최근 HbA1C 수치')
    tumor_1 = models.IntegerField('종양 유무', choices=YES_NO_CHOICES, null=True, blank=True, help_text='종양 유무')
    TUMOR_2_CHOICES = ((0, '미해당'), (1, '혈액암'), (2, '고형암'))
    tumor_2 = ChoiceArrayField(models.CharField(max_length=200, choices=TUMOR_2_CHOICES,
                                                null=True, blank=True),
                               verbose_name='혈액암 혹은 고형암 진단',
                               help_text='혈액암 혹은 고형암 진단',
                               null=True, blank=True)
    tumor_test = models.TextField('종양 관련 검사 소견', null=True, blank=True, help_text='종양 관련 검사 소견')
    genetic_test = models.IntegerField('유전자 검사 시행 여부', choices=YES_NO_CHOICES, null=True, blank=True,
                                       help_text='유전자 검사 시행 여부')
    mll2 = models.IntegerField('MLL2 유전자 변이 여부', choices=YES_NO_CHOICES, null=True, blank=True,
                               help_text='MLL2 유전자 변이 여부')
    dna = models.CharField('유전자 변이 (DNA)', max_length=444, null=True, blank=True, help_text='유전자 변이 (DNA)')
    protein = models.CharField('유전자 변이 (Protein)', max_length=444, null=True, blank=True, help_text='유전자 변이 (Protein)')
    domain = models.TextField('Domain', null=True, blank=True, help_text='Domain')
    mutation_type = models.TextField('Mutation type', null=True, blank=True, help_text='Mutation type')
    Inframe_deletion_or_insertion = models.TextField('Inframe deletion or insertion', null=True, blank=True,
                                                     help_text='Inframe deletion or insertion')
    haploinsufficiency_type = models.TextField('haploinsufficiency type', null=True, blank=True,
                                               help_text='haploinsufficiency type')
    novel_mutation = models.TextField('Novel mutation', null=True, blank=True, help_text='Novel mutation')
    brain_mr = models.IntegerField('뇌 MR 시행 유무', choices=YES_NO_CHOICES, null=True, blank=True,
                                   help_text='뇌 MR 시행 유무')
    brain_mr_test = models.TextField('뇌 MR 검사 소견', null=True, blank=True, help_text='뇌 MR 검사 소견')
    operation_1 = models.IntegerField('수술 유무', choices=YES_NO_CHOICES, null=True, blank=True,
                                      help_text='수술 유무')
    operation_2 = models.PositiveIntegerField('수술 횟수', null=True, blank=True, help_text='수술 횟수')
    operation_3 = models.TextField('수술 종류', null=True, blank=True, help_text='수술 종류')

    class Meta:
        abstract = True


class Ks_pnuh(Ks):
    class Meta:
        verbose_name = "가부키증후군_양산부산대병원"
        verbose_name_plural = "가부키증후군_양산부산대병원"

class Ks_snuh(Ks):
    class Meta:
        verbose_name = "가부키증후군_서울대학교병원"
        verbose_name_plural = "가부키증후군_서울대학교병원"
