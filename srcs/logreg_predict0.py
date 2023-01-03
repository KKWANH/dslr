#자주 사용하는 라이브러리 임포트
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import argparse

#소숫점 자리수 표시 방법 지정
pd.options.display.float_format = '{:.5f}'.format

#경고메세지 제거
import warnings
warnings.filterwarnings('ignore')

from pathlib import Path

from MiddleLayer import MiddleLayer
from OutputLayer import OutputLayer

from logreg_train import addLabelColumn
from logreg_train import preprocessing2
from logreg_train import getInputData
from logreg_train import getCorrectData

# -- 순전파 --
def forward_propagation(x):
    #middle_layer_1.forward(x)
    #middle_layer_2.forward(middle_layer_1.y)
    output_layer.forward(x)

def get_wb(printMode = True):
  fname = 'wb.dat'
  path = Path(fname)
  if (not path.is_file()):
    return False
  f = open(fname, 'r')

  #o
  line1 = f.readline()
  owShape =  [int(i) for i in line1.split()]
  if printMode:
    print("owShape=", owShape)
  line2 = f.readline()
  if owShape[0] * owShape[1] != len(line2.split()):
    return False
  ow = np.reshape([float(i) for i in line2.split()], (owShape[0], owShape[1]))
  if printMode:
    print("ow=", ow)
    print(owShape, list(ow.shape))

  line3 = f.readline()
  obShape =  [int(i) for i in line3.split()]
  if printMode:
    print("obShape=", obShape)
  line4 = f.readline()
  ob = np.reshape([float(i) for i in line4.split()], (obShape))
  if obShape[0] != len(ob):
    return False
  if printMode:
    print("ob=", ob)
    print(obShape[0], len(ob))

  return ow, ob

# -- 오차 계산 --
# https://towardsdatascience.com/understanding-sigmoid-logistic-softmax-functions-and-cross-entropy-loss-log-loss-dbbbe0a17efb#3f76
def get_error(t, batch_size):
    return -np.sum(t * np.log(output_layer.y + 1e-7)) / batch_size  # cross entropy error

def evaulate(mylabels, testFname, resultFname, printMode = True):

  print("############################")
  print("############################")
  print("############################")

  df = pd.read_csv(testFname, header=0)

  #print(df.shape) #(1600, 19)
  if (df.shape[1] != 19):
    print("It has to have 19 columns. check your data. stop the processing")
    return

  df = addLabelColumn(df) #training only

  df4 = preprocessing2(df, printMode=False)
  raw_data, n_data, input_data = getInputData(df4, printMode=False)
  correct, correct_data = getCorrectData(raw_data, n_data, printMode=False)

  forward_propagation(input_data)

  error = get_error(correct_data, n_data)
  print(np.argmax(output_layer.y, axis=1) == np.argmax(correct_data, axis=1))
  print(np.argmax(output_layer.y, axis=1))
  print(np.argmax(correct_data, axis=1))

  count = np.sum(np.argmax(output_layer.y, axis=1) == np.argmax(correct_data, axis=1))
  print("Error:" + str(error), "Accuracy:", str(count/n_data*100) + "%")

  #print(mylabels)
  if printMode:
    print("w", output_layer.w.shape)
    print(output_layer.w)
    print("b", output_layer.b.shape)
    print(output_layer.b)
    print("y", output_layer.y.shape)

  # num = 5
  # retdf = df.iloc[0:num, 0:1]
  # y5 = np.around(output_layer.y[0:num, ], decimals=2)

  retdf = df.iloc[0:, 0:1]
  y5 = np.around(output_layer.y[0:, ], decimals=2)

  if printMode:
    print(y5)
    print(y5.argmax(axis=1))
    print(labels)
  ret = y5.argmax(axis=1)
  label = []

  for i in ret:
    label.append(mylabels[i])

  if printMode:
    print(retdf)
    print(label)

  retdf['Hogwarts House'] = label
  retdf.columns = ['Index' ,'Hogwarts House']
  #if printMode:
  print(retdf)

  retdf.to_csv(resultFname, index=False)





# ------------------------------------------------------------------------------
# main
if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument("file_name", type=str)
  args = parser.parse_args()

  wblist = get_wb(False)
  if (type(wblist) == bool and wblist == False):
    print("do training first")
    exit()

  #print(len(wblist))
  ow, ob = wblist
  #print(ow)

  # -- 각 설정 값 --
  n_in = 4  # 입력층 뉴런 수
  #n_mid = 25  # 은닉층 뉴런 수
  n_out = 4  # 출력층 뉴런 수

  wb_width = 0.1  # 가중치와 편향 설정을 위한 정규분포 표준편차
  eta = 0.001  # 학습률
  epoch = 1000
  batch_size = 8 #8
  interval = 100  # 경과 표시 간격

 # -- 각 층의 초기화 --
  #middle_layer_1 = MiddleLayer(wb_width, n_in, n_mid)
  #middle_layer_2 = MiddleLayer(wb_width, n_mid, n_mid)
  output_layer = OutputLayer(wb_width, n_in, n_out)

  output_layer.w = ow
  output_layer.b = ob

  labels = ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']

  #fname = input('enter test filename or just press enter: ')
  #print(fname)
  #if (fname == ''):
  fname = args.file_name
  #print("fname=", fname)

  path = Path(fname)
  if (path.is_file()):
    resultFname = 'houses.csv'
    evaulate(labels, fname, resultFname, False)
    print("check the result in ./"+ resultFname)

  else:
    print("check if your file exists")

