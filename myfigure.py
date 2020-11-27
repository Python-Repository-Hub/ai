import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 그래프에서 마이너스 폰트 깨지는 문제에 대한 대처
mpl.rcParams['axes.unicode_minus'] = False

import numpy as np

print([(f.name, f.fname) for f in fm.fontManager.ttflist if 'Nanum' in f.name])
path ='/Users/xzero/Library/Fonts/NanumGothic.ttf'

font_name = fm.FontProperties(fname=path).get_name()
mpl.rc('font',family=font_name)
ratio = [5, 25, 10, 5,15,15,20,5]
labels = ['크기', '인공지능', '시각화', '자료','학교','교육',"로봇","성분"]

plt.pie(ratio, labels=labels, autopct='%.0f%%')
# plt.show()
plt.savefig('fig1.png', dpi=300)

