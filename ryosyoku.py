# coding: utf-8
import datetime

date_now = datetime.datetime.now()    #今日の情報を取得
w_now = date_now.strftime('%w')    #今週の月曜を把握するため曜日番号を取得
youbi = {'0':'日', '1':'月', '2':'火', '3':'水', '4':'木', '5':'金', '6':'土'}    #曜日番号と曜日を変換する辞書

f = open('ryosyoku.txt', 'w')

for i in range(5):    #月-金で繰り返す
    date = date_now - datetime.timedelta(days=(int(w_now)-1)) + datetime.timedelta(days=i)
    #右辺第2項は今週の月曜から始めるための調整

    m = date.strftime('%m').lstrip('0')
    d = date.strftime('%d').lstrip('0')
    y = youbi[date.strftime('%w')]

    f.write('{0}/{1} ({2}) 昼\n\n{0}/{1} ({2}) 夕\n\n'.format(m, d, y))

f.close()
