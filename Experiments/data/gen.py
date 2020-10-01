import pickle
a = [1, 2, 3, 4]
with open('numbers1.in', 'wb') as handle:
    pickle.dump(a, handle)
with open('numbers1.in', 'rb') as handle:
    b = pickle.load(handle)
print(a == b)