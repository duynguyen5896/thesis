import tables
import numpy as np
import matplotlib.pyplot as plt

# Reading the file.
fileh = tables.open_file('enrollment-evaluation_sample_dataset.hdf5', mode='r')

# Dimentionality of the data structure.
print(fileh.root.utterance_enrollment.shape)
print(fileh.root.utterance_evaluation.shape)
print(fileh.root.label_enrollment[:])
print(fileh.root.label_evaluation[:])


