#!/usr/bin/python3

def delta(seq):
    #should return the sequence of differences of the successive terms in seq (list)
    if seq == []: return seq
    diff = list()
    for i in range(len(seq) - 1):
        current = seq[i]
        next = seq[i + 1]
        diff.append(current - next)
    return diff

# def dual_seq(seq):
#     #should return the Binomial Transform of seq
#     d = delta(seq)
#     if d == []: return seq
#     y = [seq[0], d[0]]
#     first_time = True
#     for i in range(len(seq) - 2):
#         diff = d[i] - d[i + 1]
#         if first_time:
#             y.append(diff)
#             first_time = False
#         else:
#                       # should be equivalent to y[-1]
#             y.append(y[-1] - diff)
#     return y

# def dual_seq(seq):
#     d = delta(seq)
#     if d == []: return seq
#     y = [seq[0], d[0]]
#     for i in range(1, len(seq) - 1):
#         v = y[-1]
#         y.append(v - d[i])
#     return y

# def dual_seq(seq):
#     for i in range(len(seq)):
#         c = delta(seq[:i])
#         for j in range(len(c)):



























def dual_seq(seq):
    f = []
    d = seq
    while len(d) != 0:
        f.append(d[0])
        d = delta(d)
    return f


def extra_pol(seq, n):  # NB: you can also use a lambda if you prefer to code it in one line :D
    #should return the sequence seq, completed by the n next terms, with respect to the best possible polynomial approximation
    # return dual_seq(seq *[0 for _ in range(n)])
    neew = dual_seq(seq)
    for i in range(n):
        neew.append(0)
    return dual_seq(neew)


print(extra_pol([1], 0))  # returns [1]
print(extra_pol([1], 5))  # returns [1, 1, 1, 1, 1, 1]
print(extra_pol([1,4],5)) #returns [1, 4, 7, 10, 13, 16, 19]
print(extra_pol([1,4,9],5)) #returns [1, 4, 9, 16, 25, 36, 49, 64]
print(extra_pol([4,16,36],5)) #returns [4, 16, 36, 64, 100, 144, 196, 256]
print(extra_pol([216, 125 ,64 ,27],7)) #returns [216, 125, 64, 27, 8, 1, 0, -1, -8, -27, -64]




print(dual_seq([1])) #returns [1]
print(dual_seq([1,2,3,4,5])) #returns [1, -1, 0, 0, 0]
print(dual_seq([1, -1, 1, -1, 1, -1, 1, -1, 1])) #returns [1, 2, 4, 8, 16, 32, 64, 128, 256]
print(dual_seq([1, -1, 0, 0, 0])) #returns [1, 2, 3, 4, 5]
print(dual_seq([2,4,6,8,10])) #returns [2, -2, 0, 0, 0]
