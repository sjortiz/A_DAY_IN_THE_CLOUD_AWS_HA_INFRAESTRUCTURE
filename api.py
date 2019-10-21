import requests
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
instance_metadata_url = (
    "http://169.254.169.254/latest/meta-data/local-hostname"
)


class HelloWorld(Resource):

    def get(self):
        return {
                'hello': 'world',
                'from': f'{requests.get(instance_metadata_url)}'
            }


api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
