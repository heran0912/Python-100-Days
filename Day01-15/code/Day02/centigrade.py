"""
将华氏温度转换为摄氏温度
F = 1.8C + 32

Version: 0.1
Author: 骆昊
Date: 2018-02-27
"""

f = float(input('请您输入华氏度: '))
c = (f - 32) / 1.8   
print('%.1f华氏度 = %.2f摄氏度' % (f, c))
