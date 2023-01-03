import numpy as np

# -- 각 층의 부모 클래스 생성 --
class BaseLayer:
    def __init__(self, wb_width, n_upper, n):
        self.w = wb_width * np.random.randn(n_upper, n)  # 가중치
        self.b = wb_width * np.random.randn(n)  # 편향

    def update(self, eta):
        self.w -= eta * self.grad_w
        self.b -= eta * self.grad_b
