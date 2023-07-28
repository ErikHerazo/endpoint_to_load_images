import os
from flask import Blueprint
from flask_restful import Resource
from flask import Flask, request, jsonify
from apps import api
from apps.utils.rename_and_save_photo import renameAndSavePhoto
from config import conn
from dotenv import load_dotenv

user = Blueprint('user', __name__)

folder = os.getenv('folder', 'img')
UPLOAD_FOLDER = folder

class UploadImange(Resource):

    def post(self):
        photo = request.files['photo']
        username = request.form['username']
        new_file_path = renameAndSavePhoto(photo, username, UPLOAD_FOLDER)
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO public.usuario (photo) VALUES ('{new_file_path}')")
        conn.commit()
        cursor.close()
        return jsonify({'message': 'Imagen subida exitosamente'})

api.add_resource(UploadImange, '/upload_photo')