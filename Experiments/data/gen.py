import pickle


def write_nums(nums, filename):
    with open(filename + '.in', 'wb') as handle:
        pickle.dump(nums, handle)
    with open(filename + '.in', 'rb') as handle:
        b = pickle.load(handle)
    print(nums == b)


write_nums([1, 2, 3, 4], 'numbers1')
write_nums([4, 3, 2, 1], 'numbers2')
