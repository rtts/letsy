from flask import Flask, render_template
import datetime

app = Flask(__name__)

def is_positive(value):
    if (value > 0):
        return True
    else:
        return False
app.jinja_env.filters['is_positive'] = is_positive

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<anything>/')
def balance(**void):
    transactions = [
    {'date': datetime.datetime.now() - datetime.timedelta(hours=1),
     'description': 'Bedankt voor het terugzetten van de container!',
     'other': 'jolanda@r2src.com',
     'debit': -10
    },
    {'date': datetime.datetime.now() - datetime.timedelta(hours=5),
     'description': 'Lekker koffie gezet hmmm!',
     'other': 'jolanda@r2src.com',
     'debit': -15
    },
    {'date': datetime.datetime.now() - datetime.timedelta(hours=13),
     'description': 'Ontwerpen van een kleurenschema',
     'other': 'Fictieve klant',
     'debit': 50
    },
    {'date': datetime.datetime.now() - datetime.timedelta(days=1, hours=5),
     'description': 'Paadje opnieuw betegeld',
     'other': 'heymans@rosmalen.nl',
     'debit': -90
    },
    {'date': datetime.datetime.now() - datetime.timedelta(days=1, hours=12),
     'description': 'Rock Crawler 9398',
     'other': 'kassa@macro.nl',
     'debit': -133
    },
    {'date': datetime.datetime.now() - datetime.timedelta(days=4),
     'description': 'Loon over maand december',
     'other': 'Fred Vermaat',
     'debit': 300
    },
    {'date': datetime.datetime.now() - datetime.timedelta(days=8),
     'description': 'Voor de geweldige hulp!',
     'other': 'iemand@ergens.com',
     'debit': 30
    },
    {'date': datetime.datetime.now() - datetime.timedelta(weeks=4, days=4),
     'description': 'Jij bent de eerste aan wie ik op deze wijze een betaling doe. Ik snap eigenlijk niet helemaal hoe het werkt. Hoe kan ik nou "geld" overmaken als ik helemaal geen saldo heb?!',
     'other': 'noob@hotmail.com',
     'debit': 1
    }
    ]
    return render_template('balance.html', transactions=transactions)
