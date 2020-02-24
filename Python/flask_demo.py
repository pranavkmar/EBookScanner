import flask
import werkzeug
import time
import os

app = flask.Flask(__name__)

save_path = 'my_images'
if not os.path.exists(save_path):
    os.makedirs(save_path)


@app.route('/', methods=['GET', 'POST'])
def handle_request():
    files_ids = list(flask.request.files)
    print("\nNumber of Received Images : ", len(files_ids))
    image_num = 1
    for file_id in files_ids:
        print("\nSaving Image ", str(image_num), "/", len(files_ids))
        imageFile = flask.request.files[file_id]
        filename = werkzeug.utils.secure_filename(imageFile.filename)
        print("Image Filename : " + imageFile.filename)
        timestr = time.strftime("%Y%m%d-%H%M%S")
        imageFile.save(save_path+'/'+timestr + '_' + filename)
        image_num = image_num + 1
    print("\n")
    return str(len(files_ids)) + " Image(s) Uploaded Successfully. Come Back Soon."


app.run(host="0.0.0.0", port=5000, debug=True)
