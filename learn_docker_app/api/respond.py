from flask_restx import fields, Namespace, Resource

respond_namespace = Namespace(
    'respond', 
    description='Provides operations that generate a simple response.'
)

copy_cat_model = respond_namespace.model('Respond', {
        'response': fields.String(required=True, description='The string provided.')
    }
)

@respond_namespace.route('/<string>')
class SimpleResponse(Resource):
    @respond_namespace.marshal_with(copy_cat_model)
    def get(self, string: str):
        return {
            'response': string,
        }