RADIO_FIELDS={
    'ird': (
        'sex', 'sortation',
    ),
    'ird_history': (
        'sex', 'myodesopsia', 'cystoid_macular_edema_od', 'sector_rp_od', 'retinitis_punctata_albescens_od',
        'cystoid_macular_edema_os', 'sector_rp_os', 'retinitis_punctata_albescens_os',
        'night_blindness', 'peripheral_vision', 'central_vision', 'read',
        'object_recognition', 'cataract', 'glaucoma', 'retinal_detachment', 'dark_adaptation', 
        'photopsia', 'color_sense', 'familyhistory_diagnosis2', 'drug', 'myodesopsia',
        'night_blindness', 'peripheral_vision', 'central_vision', 'read',
        'object_recognition', 'cataract', 'glaucoma', 'retinal_detachment',
        'dark_adaptation', 'photopsia', 'color_sense', 'dazzling', 'hearing_defect'
    )
}

CALCULATE_AGE_FIELDS={
    'ird_history': {
        'age': 'birthdate'
    }
}
