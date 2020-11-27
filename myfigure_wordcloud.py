from wordcloud import WordCloud
path ='/Users/xzero/Library/Fonts/NanumGothic.ttf'

wordcloud = WordCloud(
    font_path = path,    # 맥에선 한글폰트 설정 잘해야함.
    background_color='white',                             # 배경 색깔 정하기
    # colormap = 'Accent_r',                                # 폰트 색깔 정하기
    width = 800,
    height = 800
)
ratio = [5, 25, 10, 5,15,15,20,5]
labels = ['크기', '인공지능', '시각화', '자료','학교','교육',"로봇","성분"]
words =dict(zip(labels,ratio))
wc = wordcloud.generate_from_frequencies(words)

wc.to_file('ke.png')