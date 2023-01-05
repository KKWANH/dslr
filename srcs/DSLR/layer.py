# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    layer.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kkim <kkim@student.42.fr>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/01/04 14:19:03 by kkim              #+#    #+#              #
#    Updated: 2023/01/04 14:23:02 by kkim             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# ------------------------------------------------------------------------------
# import : library
import numpy

# ------------------------------------------------------------------------------
# Layer: BaseLayer
#   각 층의 부모 클래스 생성
class BaseLayer:
    def __init__(self, wb_width, n_upper, n):
        self.w = wb_width * numpy.random.randn(n_upper, n)  # 가중치
        self.b = wb_width * numpy.random.randn(n)  # 편향

    def update(self, eta):
        self.w -= eta * self.grad_w
        self.b -= eta * self.grad_b

# ------------------------------------------------------------------------------
# Layer: MiddleLayer
#   Hidden Layer
class MiddleLayer(BaseLayer):
    def forward(self, x):
        self.x = x
        self.u = numpy.dot(x, self.w) + self.b
        self.y = numpy.where(self.u <= 0, 0, self.u) # ReLU

    def backward(self, grad_y):
        delta = grad_y * numpy.where(self.u <= 0, 0, 1)  # ReLU 미분

        self.grad_w = numpy.dot(self.x.T, delta)
        self.grad_b = numpy.sum(delta, axis=0)

        self.grad_x = numpy.dot(delta, self.w.T)

# ------------------------------------------------------------------------------
# Layer: OutputLayer
#   출력층
class OutputLayer(BaseLayer):
    def forward(self, x):
        self.x = x
        u = numpy.dot(x, self.w) + self.b
        self.y = numpy.exp(u)/numpy.sum(numpy.exp(u), axis=1, keepdims=True)  # 소프트맥스 함수

    def backward(self, t):
        delta = self.y - t

        self.grad_w = numpy.dot(self.x.T, delta)
        self.grad_b = numpy.sum(delta, axis=0)

        self.grad_x = numpy.dot(delta, self.w.T)
