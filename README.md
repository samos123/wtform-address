# Wtform address fields: CountrySelectField and StateSelectField
Fields that are helpful when dealing with physical addresses such as a
CountrySelectField and a StateSelectField.

## Install
```shell
pip install wtform_address
```

## Usage
```python
from wtforms import Form
from wtform_address import CountrySelectField, StateSelectField

class MyForm(Form):
    country = CountrySelectField(default="US")
    state = StateSelectField(default="US-CA")
```

## Credits
Credits to [@mekza](https://github.com/mekza) for his initial [gist](https://gist.github.com/mekza/516f172278c328468ea0).

## License
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
