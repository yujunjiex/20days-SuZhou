from flask import Flask, render_template, request, redirect, url_for, make_response, jsonify, flash
from werkzeug.utils import secure_filename
from datetime import timedelta
import os
import random
from static.train_model import predict
import json

# 设置允许的文件格式
ALLOWED_EXTENSIONS = {'png', 'jpg', 'JPG', 'PNG'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


app = Flask(__name__)
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = timedelta(seconds=10)  # 将缓存时间设置为10s
app.config['SECRET_KEY'] = '123456'  # 设置SECRET_KEY
app.config['UPLOAD_FOLDER'] = 'static/images'   # 设置图片上传路径


@app.route('/dogname/', methods=['GET'])
def get_dog_names():
    from static.train_model.dog_dict import dog_dict
    return jsonify(status='200', dog_names=dog_dict)


@app.route('/identify/', methods=['POST'])
def identify():
    """返回图像识别的结果"""
    json_res = request.json

    # TODO: 进行图像识别处理
    results = predict.get_result(list(json_res.values()))

    return jsonify(status='200', results=results)


@app.route('/upload/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'images' not in request.files:
            flash('No file part')
            return redirect(request.url)
        files = request.files.getlist('images')
        print("files=", files)

        res = {}
        for file in files:
            # Check if the file is one of the allowed types/extensions
            if file and allowed_file(file.filename):
                # TODO:Make the filename safe, remove unsupported chars
                filename = file.filename
                # Move the file form the temporal folder to the upload
                # folder we setup
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                image_url = os.path.join(os.path.join('/static', 'images'), filename)
                res[filename.split(".")[0]] = image_url
            # return jsonify(code=status_code.OK, image_urls=res)
        return jsonify(code='200', imageUrls=res)
    return ''


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
