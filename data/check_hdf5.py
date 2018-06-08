import tables
import numpy as np
import matplotlib.pyplot as plt

# Reading the file.
fileh = tables.open_file('development_sample_dataset_speaker.hdf5', mode='r')

# Dimentionality of the data structure.
print(fileh.root.utterance_test.shape)
print(fileh.root.utterance_train[:])
print(fileh.root.utterance_test[:])
print(fileh.root.utterance_train.shape)
print(fileh.root.label_train.shape)
print(fileh.root.label_train[:])
print(fileh.root.label_test.shape)
print(fileh.root.label_test[:])


