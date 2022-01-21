RADIO_FIELDS={
    'ird': (
        'sex', 'sortation',
    ),
    'ird_history': (
        'sex', 'myodesopsia', 'cystoid_macular_edema_od', 'sector_rp_od', 'retinitis_punctata_albescens_od',
        'cystoid_macular_edema_os', 'sector_rp_os', 'retinitis_punctata_albescens_os',
        'familyhistory_diagnosis1', 'familyhistory_diagnosis2', 'other_diagnosis',
        'night_blindness', 'peripheral_vision', 'central_vision', 'read', 'eyeglasses_lens', 
        'object_recognition', 'cataract', 'glaucoma', 'retinal_detachment', 'dark_adaptation', 
        'photopsia', 'color_sense', 'best_night_blindness',
        'best_photopsia', 'best_cataract', 'best_hearing_defect', 'best_pedigree',
        'first_night_blindness', 'first_photopsia',
        'first_cataract', 'first_hearing_defect', 'first_pedigree', 'current_night_blindness', 'current_photopsia', 'current_cataract',
        'current_hearing_defect', 'current_pedigree',
    )
}

CALCULATE_AGE_FIELDS={
    'ird_history': {
        'age': 'birthdate'
    }
}
