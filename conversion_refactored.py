class ConversionNotPossible(Exception):
    pass


BASE_UNITS = {
    "celsius":    ("temp", lambda c: c + 273.15, lambda k: k - 273.15),
    "fahrenheit": ("temp", lambda f: (f + 459.67) * 5/9, lambda k: k * 9/5 - 459.67),
    "kelvin":     ("temp", lambda k: k, lambda k: k),
    "meter":      ("dist", lambda m: m, lambda m: m),
    "mile":       ("dist", lambda mi: mi * 1609.344, lambda m: m / 1609.344),
    "yard":       ("dist", lambda y: y * 0.9144, lambda m: m / 0.9144),
}

#plurals
UNITS = {}
for name, data in BASE_UNITS.items():
    UNITS[name] = data
    UNITS[name + "s"] = data

def convert(value, from_unit, to_unit):
    # Clean up strings: lowercase and remove extra spaces
    f_unit = from_unit.lower().strip()
    t_unit = to_unit.lower().strip()

    if f_unit not in UNITS or t_unit not in UNITS:
        raise ConversionNotPossible(f"Unknown unit: {from_unit} or {to_unit}")

    from_cat, to_base_func, _ = UNITS[f_unit]
    to_cat, _, from_base_func = UNITS[t_unit]

    if from_cat != to_cat:
        raise ConversionNotPossible(f"Cannot convert {from_cat} to {to_cat}")


    return from_base_func(to_base_func(float(value)))
