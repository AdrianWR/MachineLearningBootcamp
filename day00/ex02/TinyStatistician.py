import math


class TinyStatistician:

    @staticmethod
    def mean(x):
        if not len(x):
            return None
        return sum(x) / len(x)

    @staticmethod
    def median(x):
        if not len(x):
            return None
        return TinyStatistician.quartile(x, 50)

    @staticmethod
    def quartile(x, percentile):
        if not len(x):
            return None
        data = TinyStatistician.__sort(x)
        n = len(data)
        index = percentile * n / 100
        floor = math.floor(index)
        if index == floor:
            return float((data[floor] + data[floor - 1]) / 2)
        return float(data[floor])

    @staticmethod
    def var(x):
        n = len(x)
        if not n:
            return None
        mu = TinyStatistician.mean(x)
        sqd = 0         # sum of square deviations
        for i in x:
            sqd += (i - mu) ** 2
        return sqd / n

    @staticmethod
    def std(x):
        if not len(x):
            return None
        return math.sqrt(TinyStatistician.var(x))

    @staticmethod
    def __sort(array):
        x = array.copy()
        for i in range(1, len(x)):
            key = x[i]
            j = i
            while j > 0 and key < x[j - 1]:
                x[j] = x[j - 1]
                j -= 1
            x[j] = key
        return x
