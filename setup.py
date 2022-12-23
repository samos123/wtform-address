from setuptools import setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="wtform_address",
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    description="Physical address fields (CountrySelectField, StateSelectField) for wtform",
    author="Sam Stoelinga",
    url="https://github.com/samos123/wtform-address",
    long_description=long_description,
    long_description_content_type='text/markdown',
    py_modules=["wtform_address"],
    license_files=["LICENSE"],
    install_requires=[
        'pycountry',
        'wtform'
    ]
)
