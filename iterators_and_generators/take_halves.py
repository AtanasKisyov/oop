def solution():

    def integers():
        num = 1
        while True:
            yield num
            num += 1

    def halves():
        for i in integers():
            yield i / 2

    def take(n, seq):
        res = []
        for i in range(n):
            res.append(next(seq))
        return res

    return take, halves, integers


t = solution()[0]
h = solution()[1]
print(t(5, h()))
