#!/usr/bin/python3
from TinyStatistician import TinyStatistician as tiny
import numpy as np

if __name__ == "__main__":
    ts = tiny()
    mp = 'midpoint'
    data = [1, 42, 300, 10, 59]
    print(f"data -> \t\t{data}")
    print(f"mean -> \t\t{ts.mean(data)}")
    print(f"median -> \t\t{ts.median(data)}")
    print(f"quartile(25) -> \t{ts.quartile(data, 25)}")
    print(f"quartile(75) -> \t{ts.quartile(data, 75)}")
    print(f"variance -> \t\t{ts.var(data)}")
    print(f"std deviation -> \t{ts.std(data)}")
    print(f"\nNUMPY")
    print(f"data -> \t\t{data}")
    print(f"sort -> \t\t{np.sort(data)}")
    print(f"mean -> \t\t{np.mean(data)}")
    print(f"median -> \t\t{np.median(data)}")
    print(f"quartile(25) -> \t{np.percentile(data, 25, interpolation=mp)}")
    print(f"quartile(75) -> \t{np.percentile(data, 75, interpolation=mp)}")
    print(f"variance -> \t\t{np.var(data)}")
    print(f"std deviation -> \t{np.std(data)}")
