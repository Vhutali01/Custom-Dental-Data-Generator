import numpy as np

class Dental:
    """Class for dental data structure, age needs to be specified"""



    def __init__(self, age):
        self.age = age

    caregiver_treatment = lambda: "yes" if np.random.binomial(1, p=0.65) == 1 else "no"

    sa_citizen = lambda: "yes" if np.random.binomial(1, p=0.5) == 1 else "no"

    special_needs = lambda: "yes" if np.random.binomial(1, p=0.08) == 1 else "no"

    plaque = lambda: "yes" if np.random.binomial(1, p=0.4) == 1 else "no"

    dry_mouth = lambda: "yes" if np.random.binomial(1, p=0.2) == 1 else "no"

    enamel_defects = lambda: "yes" if np.random.binomial(1, p=0.4) == 1 else "no"

    appliance = lambda: "yes" if np.random.binomial(1, p=0.5) == 1 else "no"

    fluoride_water = lambda: "yes" if np.random.binomial(1, p=0.65) == 1 else "no"

    fluoride_toothpaste = lambda: "yes" if np.random.binomial(1, p=0.8) == 1 else "no"

    topical_fluoride = lambda: "yes" if np.random.binomial(1, p=0.6) == 1 else "no"

    regular_checkups = lambda: "yes" if np.random.binomial(1, p=0.7) == 1 else "no"

    sealed_pits = lambda: "yes" if np.random.binomial(1, p=0.6) == 1 else "no"

    restorative_procedures = lambda: "yes" if np.random.binomial(1, p=0.4) == 1 else "no"

    enamel_change = lambda: "yes" if np.random.binomial(1, p=0.35) == 1 else "no"

    dentin_discoloration = lambda: "yes" if np.random.binomial(1, p=0.35) == 1 else "no"

    white_spot_lesions = lambda: "yes" if np.random.binomial(1, p=0.4) == 1 else "no"

    cavitated_lesions = lambda: "yes" if np.random.binomial(1, p=0.3) == 1 else "no"

    multiple_restorations = lambda: "yes" if np.random.binomial(1, p=0.3) == 1 else "no"

    missing_teeth = lambda: "yes" if np.random.binomial(1, p=0.3) == 1 else "no"
