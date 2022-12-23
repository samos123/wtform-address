from wtforms import SelectField
import pycountry


class CountrySelectField(SelectField):
    def __init__(self, *args, **kwargs):
        super(CountrySelectField, self).__init__(*args, **kwargs)
        self.choices = [(country.alpha_2, country.name) for country in pycountry.countries]
        self.choices.sort(key=lambda x: x[1])


def get_states(country_code: str):
    states = [(state.code, state.name) for state in pycountry.subdivisions.get(country_code=country_code)]
    states.sort(key=lambda x: x[1])
    return states


class StateSelectField(SelectField):
    def __init__(self, *args, **kwargs):
        country = kwargs.get("country", "US")
        super(StateSelectField, self).__init__(*args, **kwargs)
        self.choices = get_states(country)
