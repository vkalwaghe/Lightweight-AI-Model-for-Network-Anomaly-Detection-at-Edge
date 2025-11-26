# tests/test_features.py
import numpy as np
from src.features import window_features_from_packets

class Dummy:
    def __init__(self, time, length, has_tcp=False, has_udp=False, dport=None):
        self.time = time
        self.length = length
        self.has_tcp = has_tcp
        self.has_udp = has_udp
        self.dport = dport

def test_features_empty():
    arr = window_features_from_packets([])
    assert arr.shape[0] == 6
    assert np.all(arr == 0) or arr[0] == 0.0

def test_features_basic():
    pkts = [Dummy(0.0, 100, True, False, 80), Dummy(0.5, 200, True, False, 80)]
    arr = window_features_from_packets(pkts)
    assert arr[0] > 0
    assert arr[1] > 0
    assert arr[3] == 1
