import pandas as pd
import numpy as np


chat_id = 252926140 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    L = x.sum()/(x.size*44)
    return L
