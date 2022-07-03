'''
1.1 Разработка скрипта, вычисляющего статистические показатели
(среднее значение, дисперсия, среднее квадратичное отклонение)
для данных, считанных из CSV-файла.
'''


class MathStats:
    
    def __init__(self, filename='data.csv', column='quantity'):
        import csv
        
        self._data = []

        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            
            for _r in reader:
                self._data.append(float(_r['quantity']))
                
                
    @property
    def mean(self):
        return sum(self._data) / len(self._data)
    
    
    @property
    def disp(self):
        mean_sum = 0
        for val in self._data:
            mean_sum += (val - self.mean) ** 2
        return mean_sum / len(self._data)
    
    
    @property
    def sigma_sq(self):
        return self.disp ** (1/2)
    
    
if __name__ == '__main__':
    data = MathStats()
    print('Mean:', data.mean)
    print('Variance:', data.disp)
    print('Standard deviation:', data.sigma_sq)