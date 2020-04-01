import platform

from flask import request
from flask_restx import fields, Namespace, Resource

respond_namespace = Namespace(
    'respond',
    description='Provides operations that generate a simple response.'
)

copy_cat_model = respond_namespace.model('Respond', {
    'response': fields.String(description='The string provided.')
})


@respond_namespace.route('<string>')
class Copycat(Resource):
    @respond_namespace.marshal_with(copy_cat_model)
    def get(self, string: str):
        return {
            'response': string,
        }


platform_model = respond_namespace.model('Host', {
    'hostname_or_ip': fields.String(
        description='The computer’s network name (may not be fully qualified!) or its ip address.' \
                    'An empty string is returned if the value cannot be determined.'
    ),
    'system': fields.String(
        description='Returns the system/OS name, such as "Linux", "Darwin", ' \
                    '"Java", "Windows". An empty string is returned if the' \
                    'value cannot be determined.'
    )
})
hostname_model = respond_namespace.model('Hostname', {
    'host': fields.Nested(platform_model, description='Data concerning the API server.'),
    'client': fields.Nested(platform_model, description='Data concerning the requesting client.'),
})


@respond_namespace.route('hostname')
class Hostname(Resource):
    @respond_namespace.marshal_with(hostname_model)
    def get(self):
        return {
            'host': {
                'hostname_or_ip': platform.node(),
                'system': platform.system(),
            },
            'client': {
                'hostname_or_ip': request.remote_addr,
                'system': request.user_agent.platform,
            },
        }
