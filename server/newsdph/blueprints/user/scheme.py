from webargs import fields

profile = {
    # name, sex, age, age_gt, age_lt, age_gte, age_lte, birday,
    # birday_gt, birday_lt, birday_gte, birday_lte, email, username, address,
    # phone, register_time_gt, register_time_lt, register_time_gte,
    # register_time_lte, login_time_gt, login_time_lt, login_time_gte,
    # login_time_lte, confirmed, locked, active, role, order, desc
    "name": fields.Str(),
    "sex": fields.Str(),
    "age": fields.Int(),
    "age_gte": fields.Int(),
    "age_lte": fields.Int(),
    "birday_gte": fields.Date(),
    "birday_lte": fields.Date(),
    "email": fields.Str(),
    "page": fields.Integer(),
    "page_size": fields.Integer()
}
