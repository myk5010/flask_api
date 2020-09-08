from flask_restplus import Namespace, Resource, fields

ns = Namespace('account', description='Accounts')

success_model = ns.model('Success', {
  'message': fields.String
})


@ns.route('', endpoint='index')
class IndexPage(Resource):

    @ns.marshal_with(success_model)
    def get(self):
      return {'message': '1234'}