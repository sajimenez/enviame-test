from datetime import datetime
import json
import requests

import click
from faker import Faker

from main import db, app
from api.models import Company
from config import Config


@app.cli.command()
@click.argument('qty', nargs=1, default=1)
def load_companies(qty):
    """Load mock companies into the DB."""
    click.echo('Loading companies...')
    fake = Faker()
    for _ in range(int(qty)):
        company = Company(
            external_id=fake.ssn(),
            name=fake.company(),
            phone=fake.phone_number(),
            address=fake.address(),
        )
        db.session.add(company)
    db.session.commit()
    click.echo('Data load success.')


# Exercise 4
SHIPPING = {
    "shipping_order": {
        "n_packages": "1",
        "content_description": "ORDEN 255826267",
        "imported_id": "255826267",
        "order_price": "24509.0",
        "weight": "0.98",
        "volume": "1.0",
        "type": "delivery"
    },
    "shipping_origin": {
        "warehouse_code": "401"
    },
    "shipping_destination": {
        "customer": {
            "name": "Bernardita Tapia Riquelme",
            "email": "b.tapia@outlook.com",
            "phone": "977623070"
        },
        "delivery_address": {
            "home_address": {
                "place": "Puente Alto",
                "full_address": "SAN HUGO 01324, Puente Alto, Puente Alto"
            }
        }
    },
    "carrier": {
        "carrier_code": "",
        "tracking_number": ""
    }
}


@app.cli.command()
def create_shipping():
    """Create a shipping order in Enviame.io."""
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api-key': Config.ENVIAME_API_KEY,
    }
    url = f'{Config.ENVIAME_API_BASE_URL}/companies/401/deliveries'
    payload = json.dumps(SHIPPING)
    rsp = requests.post(url, data=payload, headers=headers)

    click.echo(rsp.json())

    with open('shipping.log', 'a+') as log:
        log.write(f'{datetime.now()}|{payload}|{rsp.json()}\n')
