from main import ma
from api.models import Company


class CompanySchema(ma.SQLAlchemySchema):
    class Meta:
        model = Company

    id = ma.auto_field(dump_only=True)
    external_id = ma.auto_field(required=True)
    name = ma.auto_field(required=True)
    phone = ma.auto_field()
    address = ma.auto_field()


company_schema = CompanySchema()
companies_schema = CompanySchema(many=True)
