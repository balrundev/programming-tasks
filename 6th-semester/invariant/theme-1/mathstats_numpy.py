'''
1.2 Осуществить рефакторинг (модификация) скрипта,
вычисляющего статистические показатели для данных, считанных из CSV,
с использованием библиотеки научных вычислений numpy.
'''

import csv
import numpy as np

def read_values(filename='data.csv', column='quantity'):
    data = []

    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for _r in reader:
            data.append(float(_r['quantity']))
            
    return data


def main():
    data = read_values()
    print('Mean:', np.mean(data))
    print('Variance:', np.var(data))
    print('Standard deviation:', np.std(data))
    
if __name__ == '__main__':
    main()