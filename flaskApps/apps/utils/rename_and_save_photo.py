import os

def renameAndSavePhoto(photo, username, UPLOAD_FOLDER):
    name_photo = photo.filename
    field_name, extension = os.path.splitext(name_photo)
    username = str(username)
    name_photo = f"{username}{extension}"
    photo.save(os.path.join(UPLOAD_FOLDER, name_photo))
    new_file_path = f"{UPLOAD_FOLDER}/{name_photo}"
    return new_file_path