# coding: UTF-8
### TODO: 写一个函数，该函数将图像的路径作为输入
### 然后返回此模型所预测的狗的品种
import cv2
from glob import glob
import numpy as np
import os

from static.train_model.extract_bottleneck_features import extract_Resnet50
from static.train_model.dog_detector import dog_detector, path_to_tensor
from static.train_model.dog_dict import dog_dict
from keras.models import Sequential, model_from_json
from keras.layers import Conv2D, MaxPooling2D, GlobalAveragePooling2D, Dense

current_path = os.path.dirname(__file__)
parent_path = os.path.dirname(current_path)
project_dir = os.path.dirname(parent_path)

Resnet50_model = Sequential()
Resnet50_model.add(GlobalAveragePooling2D(input_shape=(1, 1, 2048)))    # train_Resnet50.shape[1:]
Resnet50_model.add(Dense(133, activation='softmax'))
Resnet50_model.load_weights(current_path + '/saved_models/weights.best.Resnet50.hdf5', by_name=True)
# json_string = Resnet50_model.to_json()
# Resnet50_model = model_from_json(json_string)

# 加载狗品种列表
dog_names = [item[60:-1] for item in sorted(glob("D:/PyCharm/cn-deep-learning/dog-project/dogImages/train/*/"))]


def Resnet50_predict_breed(img_path):
    # 提取bottleneck特征
    bottleneck_feature = extract_Resnet50(path_to_tensor(img_path))
    # 获取预测向量
    predicted_vector = Resnet50_model.predict(bottleneck_feature)
    # 返回此模型预测的狗的品种
    return dog_names[np.argmax(predicted_vector)]


def LastPredict(img_path, must_get=False):
    # img = cv2.imread(img_path)
    # # 将BGR图像转变为RGB图像以打印
    # cv_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # plt.imshow(cv_rgb)
    # plt.show()
    if must_get is True:
        return Resnet50_predict_breed(img_path)
    if dog_detector(img_path) == True:  # numpy的bool值只能用==来比较
        return Resnet50_predict_breed(img_path)
    else:
        return 'this is not a dog'


def get_result(image_paths: list, must_get=False):
    res = []
    for path in image_paths:
        predict_result = LastPredict(project_dir + path, must_get)
        print(predict_result)
        if predict_result != 'this is not a dog':
            real_dog_name = predict_result.replace("_", " ")
            res.append("这应该是一条{}({})".format(real_dog_name, dog_dict[real_dog_name]))
        else:
            res.append("这好像不是一条狗~")

    return res


if __name__ == '__main__':
    # path = r"dogImages\test\005.Alaskan_malamute\*g"
    path = r"D:\PyCharm\SuzhouTasks\finally\DogImages\testData\Siberian Husky\*g"
    files_path = glob(path)
    for file_path in files_path:
        # print(file_path)
        print(LastPredict(file_path))
