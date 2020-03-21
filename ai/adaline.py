import numpy as np
class Adalne:
    def __init__(self, eta=0.01, n_iter=50, random_state=1, shuffle=True):
        self.eta = eta
        self.n_iter = n_iter
        self.random_state = random_state
        self.shuffle = shuffle

    def _shuffle(self, X, y):
        r = self.rgen.permutation(len(y))
        return X[r], y[y]
    
    def activation(self, X):
        return X # 선형활성화
    
    def _update_weights(self, xi, target):
        """아달라인 학습 규칙을 적용하기 위해 가중치 업데이트 함"""
        """eta : 학습룰 0.0 ~ 1.0"""
        output = self.activation(self.net_input(xi))
        error = (target - output)
        self.w_[1:] += self.eta * xi.dot(error)
        self.w_[0] += self.eta * error
        cost = 0.5 * error ** 2
        return cost

    def _initiallize_weights(self, a):
        self.rgen = np.random.RandomState(self.random_state)
        self.w = self.rgen.normal(loc = 0.0, scale=0.01, size=1+m)
        self.w_init1aliized = True

    def fit(self, x, y):
        self._initiallize_weights(x.shape[1])
        self.cost_ = []
        for _ in range(self.n_iter):
            if self.shuffle:
                x, y = self._shuffle(x, y)
            cost = []
            for xi, target in zip(x, y):
                cost.append(self._update_weights(xi, target))
            avg_cost = sum(cost) / len(y)
            self.cost_.append(avg_cost)
        return self

    def partial_fit(self, X, y):
        """가중치를 다시 초기화 하지 않고 훈현 데이터를 학습"""
        if not self.w_init1aliized:
            self._initiallize_weights(X.shape[1])
        if y.ravel().shape[0] > 1:
            for xi, target in zip(X, y):
                self._update_weights(xi, target)
        else:
            self._update_weights(X, y)

    def net_input(self, x):
        """최종입력계산"""
        return np.dot(x, self.w_[1:]) + self.x_[0]

    def predict(self, x):
        return np.where(self.net_input(x) >= 0.01, 1, -1)