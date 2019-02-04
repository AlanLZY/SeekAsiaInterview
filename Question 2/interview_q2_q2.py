import pandas as pd
import numpy as np

data_explore = pd.read_csv('test.csv')
before_drop = len(data_explore)
data_explore.drop_duplicates(keep=False, inplace=True)
after_drop = len(data_explore)
assert before_drop == after_drop

# Levenshtein is used to calculate the action needed to change the word to match the other string.
# A lower score indicates lesser action/moves required to the compared string.
# In this case, more similar.
#


def measure_levenshtein(x, y):
    if len(x) < len(y):
        x, y = y, x

    if len(y) == 0:
        return len(x)

    prev_row = range(len(y) + 1)
    for i, c1 in enumerate(x):
        curr_row = [i + 1]
        for j, c2 in enumerate(y):
            add = prev_row[j + 1] + 1
            remove = curr_row[j] + 1
            sub = prev_row[j] + (c1 != c2)
            curr_row.append(min(add, remove, sub))
        prev_row = curr_row

    return prev_row[-1] / float(len(x))


vect = np.vectorize(measure_levenshtein)

data_explore['score'] = vect(
    data_explore.description_x, data_explore.description_y)
print(data_explore.head())
