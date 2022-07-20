DISPLAY_FIELDS={
    'crf': (
        'patient_number',
        'birth_year_and_month', 'age', 'date_at_dx', 'age_at_dx', 'sex', 'family_hx', 'familyhistory_diagnosis',
        'date_at_evaluation', 'age_at_evaluation', 'nf1_mutation', 'dna', 'protein', 'domain', 'mutation_type',
        'inframe_deletion_or_insertion', 'nf1_haploinsufficiency_type', 'novel_mutation',
        'clinical_findings', 'cafe_au_lait_spots', 'axillary_freckling', 'cutaneous_neurofibromas',
        'wide_spread_diffuse_cutaneous_neurofibroma', 'relative_macrocephaly', 'lish_nodules',
        'height_at_dx','height_sds', 'learning_difficulty', 'adhd', 'autism', 'seizure', 'hypertension',
        'cardiac_arrhythmia', 'arrhythmia_treatment', 'cardiac_myopathy', 'cardiac_myopathy_findings',
        'oh_25_vitamin_d', 'oh_25_vitamin_d_1', 'hearing_difficulty', 'other', 'brain_mr', 'brain_mr_date', 'age_at_brain_mr',
        'mr_findings', 'fasi', 'fasi_findings', 'optic_pathway_glioma', 'vascular_anomaly', 'spine_mr', 'spine_mr_date',
        'age_at_spine_mr', 'age_at_spine_mr_findings', 'whole_body_mr', 'whole_body_mr_date', 'age_at_whole_body_mr',
        'age_at_whole_body_mr_findings', 'plexiform_neurofibromas', 'plexiform_neurofibromas_3',
        'disfigurement', 'aorta_bone_disruption_malignancy', 'painful_accompanying', 'malignancy',
        'brain_tumor', 'nerve_root_tumor', 'malignant_peripheral_nerve_sheath_tumor', 'moyamoya_disease', 'bmd', 'bmd_1',
        'spine_z_score', 'femur_z_score', 'dysplasia_of_long_bone',
        'dysplasia_of_long_bone_location', 'sphenoid_wing_dysplaisa', 'vertebral_dysplasia',
        'dural_ectasia', 'scoliosis', 'breast_examination', 'date_at_breast_usg', 'age_at_breast_usg',
        'birads_i_ii_iii_iv', 'breast_usg_findings', 'biopsy', 'biopsy_findings', 'operation',
        'number_of_operations', 'last_fu_date', 'last_fu_age',
    )
}

RADIO_FIELDS={
    'crf': ( 
        'family_hx', 'sex', 'nf1_mutation', 'domain', 'mutation_type', 'inframe_deletion_or_insertion',
        'nf1_haploinsufficiency_type', 'novel_mutation', 'cafe_au_lait_spots', 'axillary_freckling', 'cutaneous_neurofibromas',
        'wide_spread_diffuse_cutaneous_neurofibroma', 'relative_macrocephaly', 'lish_nodules', 'learning_difficulty', 
        'adhd', 'autism', 'lish_nodules', 'seizure', 'hypertension', 'cardiac_arrhythmia', 'cardiac_myopathy',
        'oh_25_vitamin_d', 'hearing_difficulty', 'brain_mr', 'fasi', 'optic_pathway_glioma', 'vascular_anomaly', 'spine_mr',
        'whole_body_mr', 'plexiform_neurofibromas',
        'plexiform_neurofibromas_3', 'disfigurement', 'aorta_bone_disruption_malignancy', 'painful_accompanying', 'malignancy', 
        'brain_tumor', 'nerve_root_tumor', 'malignant_peripheral_nerve_sheath_tumor', 'moyamoya_disease', 'bmd', 'bmd_1',
        'dysplasia_of_long_bone', 'sphenoid_wing_dysplaisa', 'vertebral_dysplasia', 'dural_ectasia', 'scoliosis', 
        'breast_examination', 'birads_i_ii_iii_iv', 'biopsy', 'operation'
    )
}

PREFIX={
    'crf': {
        'dna': 'c.',
        'protein': 'p.'
    }
}

SUFFIX={
    'crf': {
        'height_at_dx': 'cm',
        'oh_25_vitamin_d_1': 'ng/mL'
    }
}

CALCULATE_AGE_FIELDS={
    'crf': {
        'age': 'birth_year_and_month', 
        'age_at_dx': 'date_at_dx',
        'age_at_evaluation': 'date_at_evaluation', 
        'age_at_brain_mr': 'brain_mr_date', 
        'age_at_spine_mr': 'spine_mr_date', 
        'age_at_whole_body_mr': 'whole_body_mr_date', 
        'age_at_breast_usg': 'date_at_breast_usg', 
        'last_fu_age': 'last_fu_date'
    }
}
