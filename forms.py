# forms.py

from wtforms import Form, StringField, SelectField, validators

class MusicSearchForm(Form):
    print('HERE')
    choices = [('Artist', 'Artist'),
               ('Album', 'Album'),
               ('Price', 'Price')]
    select = SelectField('Search for music:', choices=choices)
    search = StringField('')


class AlbumForm(Form):
    competitors = [('LOWES', 'LOWES'),
                   ('HOME DEPOT', 'HOME DEPOT'),
                   ('ELLIOTS', 'ELLIOTS'),
                   ('PLATT', 'PLATT')
                   ]
    artist = StringField('Artist')
    title = StringField('Title')
    release_date = StringField('Release Date')
    Price = StringField('Price')
    Competitors_name = SelectField('Competitors', choices=competitors)
