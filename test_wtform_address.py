from wtforms.form import Form
from wtform_address import get_states, CountrySelectField, StateSelectField


def test_get_states():
    assert get_states("US")[0][1] == "Alabama"


class TestForm(Form):
    country = CountrySelectField()
    state = StateSelectField()


def test_country_and_state_field_defaults_to_us():
    form = TestForm(default="US")
    assert form.country.choices[0][1] == 'Afghanistan'
    assert form.state.choices[0][1] == 'Alabama'
