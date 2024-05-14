import numpy as np
import pandas as pd

Daten = pd.read_csv('Datensatz 1.csv',
                    index_col=0,
                    sep= ';')

# Create the index
index_ = ['Row_1', 'Row_2', 'Row_3', 'Row_4', 'Row_5', 'Row_2', 'Row_3', 'Row_4', 'Row_5', 'Row_6', 'Row_7', 'Row_8',
          'Row_9', 'Row_10', 'Row_11', 'Row_12', 'Row_13', 'Row_14', 'Row_15', 'Row_16', 'Row_17']

# Set the index
Daten.index = index_

hallo = Daten.loc['packet_nr', 'Row_2']

print(hallo)