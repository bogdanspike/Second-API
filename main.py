from pprint import pprint

from flask import Flask, request
from flask_restful import Resource, Api

from Base_model import session, File

app = Flask(__name__)
api = Api(app)


class Upload(Resource):
    def get(self):
        return 'This message Popp(y)ed up as you tried to execute the GET method on Upload route.'

    def post(self):
        f = request.files['file']
        filename = f.filename
        f.save(filename)
        with open(filename, "r") as file:
            file_text = file.read()
        try:
            test_file = File(filename=filename, file_text=file_text)
            session.add(test_file)
            session.commit()
        except:
            pprint('Error occured!')


class DeleteFile(Resource):
    def get(self):
        return 'Same goes for this one but on Delete route.'

    def delete(self):
        id_to_delete = request.form.get('id')
        try:
            session.query(File).filter_by(id=id_to_delete).delete()
            session.commit()
        except:
            print('Error occured!')


class Update(Resource):
    def get(self):
        return 'And another one on Update route.'

    def patch(self):
        given_id = request.form.get('id')
        updated_file = request.form.get('text')
        try:
            updating = session.query(File).get(given_id)
            updating.file_text = updated_file
            session.commit()
        except:
            print('Error occured!')


api.add_resource(Upload, '/upload-file')
api.add_resource(DeleteFile, '/delete-file')
api.add_resource(Update, '/update-file-text')

if __name__ == '__main__':
    app.run(debug=True)
