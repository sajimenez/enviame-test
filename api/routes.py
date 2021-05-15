from flask import Blueprint, request
from flask.json import jsonify

from api.schema import company_schema, companies_schema
from api.models import Company
from main import db

api_bp = Blueprint('api', __name__)


@api_bp.get('/companies/')
def get_companies():
    qs = Company.query.all()
    companies = companies_schema.dump(qs)
    return jsonify(companies)


@api_bp.get('/companies/<int:id>/')
def get_company(id):
    qs = Company.query.get_or_404(id)
    company = company_schema.dump(qs)
    return jsonify(company)


@api_bp.post('/companies/')
def add_company():
    data = company_schema.load(request.json)
    company = Company(**data)
    db.session.add(company)
    db.session.commit()
    return jsonify(company_schema.dump(company)), 201


@api_bp.put('/companies/<int:id>/')
def update_company(id):
    company = Company.query.get_or_404(id)
    data = company_schema.load(request.json)
    for key, item in data.items():
        setattr(company, key, item)
    db.session.add(company)
    db.session.commit()
    return jsonify(company_schema.dump(company))


@api_bp.delete('/companies/<int:id>/')
def delete_company(id):
    company = Company.query.get_or_404(id)
    db.session.delete(company)
    db.session.commit()
    return ('', 204)
