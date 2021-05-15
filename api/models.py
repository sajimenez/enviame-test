from main import db


class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    external_id = db.Column(db.String(64), index=True, unique=True)
    name = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    address = db.Column(db.String(120))

    def __repr__(self):
        return f'<Company {self.external_id} - {self.name}>'
