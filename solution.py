import pandas as pd
import numpy as np


chat_id = 750949272 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    n = 100
    path = np.random.laplace(loc=100, scale=10, size=n)
    mean_path = np.mean(path)
    x = 2 * mean_path / (93 ** 2)
    return x.mean() # Ваш ответ
