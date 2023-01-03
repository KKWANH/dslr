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

def normalize(x):
    x_max = np.max(x)
    x_min = np.min(x)
    return (x - x_min) / (x_max - x_min)

def standardize(x):
    ave = np.average(x)
    std = np.std(x)
    return (x - ave) / std

# -- 순전파 --
def forward_propagation(x):
    #middle_layer_1.forward(x)
    #middle_layer_2.forward(middle_layer_1.y)
    output_layer.forward(x)

# -- 역전파 --
def backpropagation(t):
    output_layer.backward(t)
    #middle_layer_2.backward(output_layer.grad_x)
    #middle_layer_1.backward(middle_layer_2.grad_x)

# -- 가중치와 편향 수정 --
def uppdate_wb():
    #middle_layer_1.update(eta)
    #middle_layer_2.update(eta)
    output_layer.update(eta)

# -- 오차 계산 --
# https://towardsdatascience.com/understanding-sigmoid-logistic-softmax-functions-and-cross-entropy-loss-log-loss-dbbbe0a17efb#3f76
def get_error(t, batch_size):
    return -np.sum(t * np.log(output_layer.y + 1e-7)) / batch_size  # cross entropy error

def addLabelColumn(df):

  label = "Hogwarts House"
  labels = df[label].unique()
  #print(labels)

  #하우스 컬럼을 label 컬럼으로, 각 하우스 이름 문자열에서 0, 1, 2, 3 숫자로
  ##Categories (4, object): ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']
  df[label] = pd.Categorical(df[label])
  df['label'] = df[label].cat.codes
  #print(df['label'].unique())

  return df


def preprocessing2(df, printMode = True):
  #필요없는 컬럼들 삭제후, 모델링에 사용할 독립변수 X만 컬럼들과 종속변수 y (label)컬럼만 존재하는 데이터 프레임 생성
  #print(df.info())
  df2 = df.drop(columns=['Index', 'First Name', 'Last Name', 'Birthday', 'Best Hand', 'Hogwarts House'])
  if printMode:
    print(df2.info())

  #분포가 겹치는 3개의 컬럼 삭제 (0, 9, 10)
  #분포가 겹치는 3+6=9개의 컬럼 삭제 (0, 9, 10) + (4, 5, 7, 8, 11, 12)
  df3 = df2.drop(columns=['Arithmancy', 'Potions', 'Care of Magical Creatures'])
  df3 = df3.drop(columns=['Divination', 'Muggle Studies', 'History of Magic', 'Transfiguration', 'Charms', 'Flying'])
  if printMode:
    print(df3.info())

  #https://thebook.io/080223/ch04/01/03/
  #NaN value 핸들링
  #컬럼 별 누락된 값은 해당 컬럼의 평균값으로 대체
  #imr = SimpleImputer(missing_values=np.nan, strategy='mean')
  #imr = imr.fit(df5.values)

  #컬럼 별 누락된 값은 해당 컬럼의 평균값으로 대체
  if printMode:
    print(df3.mean())
  df4=df3.fillna(df3.mean())

  #or 컬럼 별 누락된 값은 해당 컬럼의 최빈값으로 대체
  #print(df3.mode())
  #df4=df3.fillna(df3.mode())

  #or 컬럼 별 누락된 값이 있는 row 제거
  #df4 = df3.dropna()
  if printMode:
    print(df4.info())

  return df4


def getInputData(df4, printMode = True):

  # 필드 정보를 뺀 데이터의 값들만 추출
  raw_data = df4.values
  #np.random.shuffle(raw_data)  # 인덱스 임의 섞기
  #print(raw_data[1599])

  n_data = len(raw_data)  # 샘플 수 1600
  if printMode:
    print(n_data)

  # 데이터 X값 분리(data_0 ~ data_3)
  # -- 입력 데이터 표준화 --
  input_data = raw_data[:, 0:4]
  ave_input = np.average(input_data, axis=0)
  std_input = np.std(input_data, axis=0)
  input_data = (input_data - ave_input) / std_input
  if printMode:
    print(input_data[0])

  return raw_data, n_data, input_data

def getCorrectData(raw_data, n_data, printMode = True):
  # 레이블 Y값 분리 ##Categories (4, object): ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']
  correct = raw_data[:, -1]
  correct = correct.astype(int)
  if printMode:
    print(correct)

  # -- 정답을 원-핫 인코딩으로 변경 --
  correct_data = np.zeros((n_data, 4))
  for i in range(n_data):
    correct_data[i, correct[i]] = 1.0
  if printMode:
    print(correct_data)

  return correct, correct_data

def splitInputData(input_data, correct_data, n_data, printMode = True):

  # -- 훈련 데이터와 테스트 데이터 --
  index = np.arange(n_data)

  index_train = index[index%2 != 0]
  index_test = index[index%2 == 0]

  input_train = input_data[index_train, :]  # 훈련데이터 입력
  correct_train = correct_data[index_train, :]  # 훈련데이터 정답
  input_test = input_data[index_test, :]  # 테스트데이터 입력
  correct_test = correct_data[index_test, :]  # 테스트데이터 정답

  n_train = input_train.shape[0]  # 훈련데이터 샘플 수
  n_test = input_test.shape[0]  # 테스트데이터 샘플 수
  if printMode:
    print(n_train, n_test, input_data.shape)

  return input_train, input_test, correct_train, correct_test, n_train, n_test

def logreg(n_train, n_test, eta, epoch, batch_size, interval, output_layer, input_train, correct_train, input_test, correct_test):
  # -- 오차 기록용 --
  train_error_x = []
  train_error_y = []
  test_error_x = []
  test_error_y = []

  # -- 학습과 경과 기록 --
  # 확률적 경사하강법 https://gooopy.tistory.com/69
  n_batch = n_train // batch_size  # 1에포크 당 배치 수
  print(n_batch, n_train, batch_size) #100 800 8
  for i in range(epoch):

      # -- 오차 계측 --
      forward_propagation(input_train)
      error_train = get_error(correct_train, n_train)
      forward_propagation(input_test)
      error_test = get_error(correct_test, n_test)

      # -- 오차 기록 --
      test_error_x.append(i)
      test_error_y.append(error_test)
      train_error_x.append(i)
      train_error_y.append(error_train)

      # -- 경과 표시 --
      if i%interval == 0:
          print("Epoch:" + str(i) + "/" + str(epoch),
                "Error_train:" + str(error_train),
                "Error_test:" + str(error_test))

      # -- 학습 --
      index_random = np.arange(n_train)
      np.random.shuffle(index_random)  # 인덱스 임의 섞기
      for j in range(n_batch):

          # 미니배치 샘플 추출
          mb_index = index_random[j*batch_size : (j+1)*batch_size]
          x = input_train[mb_index, :]
          t = correct_train[mb_index, :]

          # 순전파와 역전파
          forward_propagation(x)
          backpropagation(t)

          # 가중치와 편향 수정
          uppdate_wb()


  return output_layer, train_error_x, train_error_y, test_error_x, test_error_y

def writeWB(wbFname):
  print("############################")
  print("######## w b ###############")
  print("############################")
  import sys
  original_stdout = sys.stdout
  f = open(wbFname, 'w')

  print("############################")
  print("o-w", output_layer.w.shape)
  print(output_layer.w)
  print("o-b", output_layer.b.shape)
  print(output_layer.b)
  print("############################")
  sys.stdout = f
  print(output_layer.w.shape[0], output_layer.w.shape[1])
  #print(output_layer.w)
  print(*output_layer.w.flatten(), sep=" ")
  print(output_layer.b.shape[0])
  #print(output_layer.b)
  print(*output_layer.b, sep=" ")
  sys.stdout = original_stdout
  print("############################")

# ------------------------------------------------------------------------------
# main
if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument("file_name", type=str)
  args = parser.parse_args()

  # 데이터 불러오기
  #location = "./datasets/dataset_train.csv"
  fname = args.file_name

  path = Path(fname)
  if (not path.is_file()):
    print("check if your file exists")
    exit(1)

  df = pd.read_csv(args.file_name, header=0)
  #print(df.head())
  #print(df.info())

  df = addLabelColumn(df)
  df4 = preprocessing2(df)
  raw_data, n_data, input_data = getInputData(df4)
  correct, correct_data = getCorrectData(raw_data, n_data)

  input_train, input_test, correct_train, correct_test, n_train, n_test = splitInputData(input_data, correct_data, n_data)


  # -- 각 설정 값 --
  n_in = 4  # 입력층 뉴런 수
  #n_mid = 25  # 은닉층 뉴런 수
  n_out = 4  # 출력층 뉴런 수

  wb_width = 0.1  # 가중치와 편향 설정을 위한 정규분포 표준편차
  eta = 0.001  # 학습률
  epoch = 1001
  batch_size = 8 #8
  interval = 100  # 경과 표시 간격

  # -- 각 층의 초기화 --
  #middle_layer_1 = MiddleLayer(wb_width, n_in, n_mid)
  #middle_layer_2 = MiddleLayer(wb_width, n_mid, n_mid)
  output_layer = OutputLayer(wb_width, n_in, n_out)

  output_layer, train_error_x, train_error_y, test_error_x, test_error_y = logreg(n_train, n_test, eta, epoch, batch_size, interval, output_layer, input_train, correct_train, input_test, correct_test)

  # -- 기록된 오차를 그래프로 표시 --
  plt.plot(train_error_x, train_error_y, label="Train")
  plt.plot(test_error_x, test_error_y, label="Test")
  plt.legend()

  plt.xlabel("Epochs")
  plt.ylabel("Error")
  plt.ylim(0, 1)
  plt.show()

  # -- 정답률 측정 --
  forward_propagation(input_train)
  count_train = np.sum(np.argmax(output_layer.y, axis=1) == np.argmax(correct_train, axis=1))

  forward_propagation(input_test)
  count_test = np.sum(np.argmax(output_layer.y, axis=1) == np.argmax(correct_test, axis=1))

  print("Accuracy Train:", str(count_train/n_train*100) + "%",
        "Accuracy Test:", str(count_test/n_test*100) + "%")

######################

  writeWB("wb.dat")
