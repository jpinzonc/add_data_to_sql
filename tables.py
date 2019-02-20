from flask_table import Table, Col, LinkCol

class Results(Table):
    id = Col('Id', show=False)
    artist = Col('Artist')
    title = Col('Title')
    release_date = Col('Release Date')
    Price = Col('Price')
    Competitors_name = Col('Competitors_name')
    edit = LinkCol('Edit', 'edit', url_kwargs=dict(id='id'))
