from flask_restful import fields
CategorySerilizer= {
    'id': fields.Integer,
    'cateoryName': fields.String,
}



postserilizer= {
    'id':fields.Integer,
    'title' :fields.String,
    'body': fields.String,
    'description':fields.String,
    'category': fields.Nested(CategorySerilizer)
}