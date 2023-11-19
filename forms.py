from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class CitySearchForm(FlaskForm):
    cityName = StringField('CIty Name', validators=[DataRequired()])
    submit = SubmitField('Search')

class CountrySearchForm(FlaskForm):
    countryName = StringField('Country Name', validators=[DataRequired()])
    submit = SubmitField('Search')

class CountryCodeSearchForm(FlaskForm):
    countryCode = StringField('Country Code', validators=[DataRequired()])
    submit = SubmitField('Search')
    
class FilterCountryForm(FlaskForm):
    db_countryName = StringField('DB Search Country')
    submit = SubmitField('Search')