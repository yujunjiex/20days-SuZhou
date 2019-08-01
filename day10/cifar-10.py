# coding: UTF-8
import numpy as np
import pickle
import os
from PIL import Image
import matplotlib.pyplot as plt


class KNearestNeighbor(object):
    def __init__(self):
        pass

    def train(self, X, y):
        """ X is N x D where each row is an example. Y is 1-dimension of size N """
        # the nearest neighbor classifier simply remembers all the training
        # data
        self.Xtr = X
        self.ytr = y

    def predict(self, X, k=1):
        """ X is N x D where each row is an example we wish to predict label for """
        """ k is the number of nearest neighbors that vote for the predicted labels."""
        num_test = X.shape[0]
        # lets make sure that the output type matches the input type
        Ypred = np.zeros(num_test, dtype=self.ytr.dtype)
        # loop over all test rows
        for i in range(num_test):
            # using the L1 distance (sum of absolute value differences)
            distances = np.sum(np.abs(self.Xtr - X[i, :]), axis=1)
            print(distances)
            # L2 distance:
            # distances = np.sqrt(np.sum(np.square(self.Xtr - X[i, :]), axis=1))
            myImg = X[i].reshape(32, 32, 3).astype("uint8")
            newImg = Image.fromarray(myImg)
            newImg.save("testImg_" + str(i) + " .png")
            plt.subplot(1, 10, 1)
            plt.imshow(newImg)
            plt.pause(0.3)

            indexes = np.argsort(distances)
            Yclosest = self.ytr[indexes[:k]]
            cnt = np.bincount(Yclosest)
            Ypred[i] = np.argmax(cnt)

            disImgs = self.Xtr[indexes[:k]]
            location = 2
            for disImg in disImgs:
                disImg = disImg.reshape(32, 32, 3).astype("uint8")
                disImg = Image.fromarray(disImg)
                plt.subplot(1, 10, location)
                plt.imshow(disImg)
                plt.pause(0.3)
                location += 1
        plt.show()
        return Ypred


def load_CIFAR_batch(file):
    """ load single batch of cifar """
    with open(file, 'rb') as f:
        datadict = pickle.load(f, encoding='latin1')
        X = datadict['data']
        Y = datadict['labels']
        X = X.reshape(10000, 3, 32, 32).transpose(0, 2, 3, 1).astype("float")
        image_index = 0
        # for imgArr in X:
        #     imgNewArr = imgArr.astype("uint8")
        #     newImg = Image.fromarray(imgNewArr)
        #     newImg.save("images/" + str(image_index) + ".png")
        #     image_index += 1
        Y = np.array(Y)
    return X, Y


def load_CIFAR10(ROOT):
    """ load all of cifar """
    xs = []
    ys = []
    for b in range(1, 6):
        f = os.path.join(ROOT, 'data_batch_%d' % (b, ))
        X, Y = load_CIFAR_batch(f)
        xs.append(X)
        ys.append(Y)
    Xtr = np.concatenate(xs)  # 使变成行向量
    Ytr = np.concatenate(ys)
    del X, Y
    Xte, Yte = load_CIFAR_batch(os.path.join(ROOT, 'test_batch'))
    return Xtr, Ytr, Xte, Yte


Xtr, Ytr, Xte, Yte = load_CIFAR10(
    'cifar-10-batches-py/')  # a magic function we provide
# flatten out all images to be one-dimensional
# Xtr_rows becomes 50000 x 3072
Xtr_rows = Xtr.reshape(Xtr.shape[0], 32 * 32 * 3)
# Xte_rows becomes 10000 x 3072
Xte_rows = Xte.reshape(Xte.shape[0], 32 * 32 * 3)
# assume we have Xtr_rows, Ytr, Xte_rows, Yte as before
# recall Xtr_rows is 50,000 x 3072 matrix
Xval_rows = Xtr_rows[:1000, :]  # take first 1000 for validation
Yval = Ytr[:1000]
Xtr_rows = Xtr_rows[1000:, :]  # keep last 49,000 for train
Ytr = Ytr[1000:]
# find hyperparameters that work best on the validation set
validation_accuracies = []
for k in [9, 20, 50, 100]:
    # use a particular value of k and evaluation on validation data
    nn = KNearestNeighbor()
    nn.train(Xtr_rows, Ytr)
    # here we assume a modified NearestNeighbor class that can take a k as
    # input
    Yval_predict = nn.predict(Xval_rows, k=k)
    acc = np.mean(Yval_predict == Yval)
    print('accuracy: %f' % (acc,))
    # keep track of what works on the validation set
    validation_accuracies.append((k, acc))
