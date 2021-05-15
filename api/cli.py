import click
from faker import Faker

from main import db, app
from api.models import Company


@app.cli.command()
@click.argument('qty', nargs=1)
def loadcompanies(qty):
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
