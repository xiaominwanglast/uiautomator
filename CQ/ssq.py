#coding:utf-8
# import requests
# import json
# url='https://api.icaipiao123.com/api/v6/lottery/trendgroup?lotteryKey=shuangseqiu&trendGroup=dlt-base&amount=500'
# headers={'User-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36'}
# rq=requests.get(url=url,headers=headers)
# rq_json=json.loads(rq.text)
# list_one=rq_json['data']['sub'][1]
# new_list=[]
# for data in list_one['data']:
#     unit_list=[]
#     for i_str in data[0][0].split(','):
#         i_int=int(i_str)
#         unit_list.append(i_int)
#     new_list.append(unit_list)
# print new_list
ssq=[[5, 6, 8, 14, 22, 31, 8], [12, 14, 17, 19, 22, 24, 8], [7, 13, 24, 25, 27, 32, 15], [2, 13, 17, 20, 29, 31, 7], [1, 5, 10, 11, 13, 32, 14], [1, 6, 9, 10, 14, 16, 11], [16, 18, 20, 23, 24, 32, 7], [14, 16, 21, 24, 28, 31, 13], [3, 8, 9, 10, 18, 33, 4], [2, 6, 12, 19, 27, 28, 13], [14, 16, 17, 19, 27, 32, 4], [9, 14, 17, 18, 21, 25, 15], [11, 14, 17, 22, 25, 27, 16], [3, 8, 9, 20, 23, 28, 2], [2, 5, 11, 15, 19, 28, 2], [1, 8, 11, 13, 19, 30, 6], [2, 8, 17, 20, 22, 28, 2], [1, 15, 16, 21, 24, 30, 3], [12, 14, 28, 31, 32, 33, 7], [2, 7, 23, 30, 32, 33, 10], [1, 9, 10, 11, 13, 32, 3], [9, 10, 14, 15, 19, 29, 16], [5, 10, 17, 25, 28, 29, 4], [5, 7, 15, 18, 26, 30, 3], [6, 13, 17, 20, 26, 29, 9], [1, 7, 12, 16, 23, 28, 4], [1, 2, 13, 22, 28, 30, 9], [6, 9, 11, 16, 20, 29, 11], [1, 6, 11, 17, 28, 33, 5], [2, 17, 20, 24, 31, 33, 4], [10, 11, 15, 26, 31, 32, 6], [6, 11, 16, 17, 22, 27, 1], [2, 10, 12, 21, 23, 27, 12], [5, 7, 8, 17, 18, 24, 14], [5, 8, 9, 20, 28, 32, 2], [1, 2, 10, 24, 30, 33, 10], [5, 17, 21, 22, 28, 32, 14], [5, 6, 14, 15, 18, 33, 8], [13, 14, 16, 23, 30, 31, 13], [5, 16, 22, 23, 26, 28, 2], [2, 4, 11, 13, 25, 33, 1], [3, 16, 19, 27, 31, 32, 10], [3, 6, 9, 11, 25, 29, 9], [4, 6, 13, 29, 31, 33, 13], [1, 14, 15, 20, 25, 29, 11], [6, 10, 11, 14, 17, 33, 6], [8, 9, 11, 16, 21, 24, 10], [6, 21, 22, 23, 25, 28, 13], [3, 12, 18, 20, 25, 26, 16], [3, 5, 6, 9, 10, 27, 14], [10, 12, 13, 23, 26, 29, 11], [1, 6, 13, 20, 29, 32, 1], [6, 7, 22, 26, 31, 32, 10], [1, 2, 5, 12, 15, 16, 13], [7, 9, 10, 15, 19, 33, 1], [3, 8, 14, 22, 24, 32, 9], [4, 5, 8, 11, 21, 27, 8], [8, 13, 15, 20, 21, 25, 12], [1, 7, 9, 16, 20, 23, 6], [7, 15, 16, 25, 28, 32, 5], [10, 15, 20, 23, 24, 31, 15], [2, 14, 15, 16, 23, 24, 10], [7, 10, 16, 17, 18, 32, 15], [1, 10, 11, 29, 31, 33, 13], [1, 7, 9, 17, 20, 33, 8], [4, 7, 10, 16, 20, 22, 3], [4, 7, 14, 17, 21, 25, 14], [1, 2, 3, 8, 21, 31, 9], [4, 14, 15, 17, 18, 20, 15], [3, 5, 22, 23, 29, 31, 6], [8, 9, 24, 25, 26, 29, 1], [2, 12, 16, 19, 27, 30, 11], [1, 7, 20, 24, 25, 33, 4], [2, 6, 10, 15, 17, 31, 13], [13, 18, 20, 25, 27, 33, 12], [6, 9, 12, 14, 28, 29, 9], [2, 6, 11, 19, 25, 26, 4], [1, 4, 7, 19, 22, 23, 4], [14, 15, 16, 17, 27, 28, 8], [4, 7, 10, 16, 23, 25, 10], [8, 9, 10, 13, 29, 30, 1], [9, 11, 16, 18, 23, 24, 10], [10, 11, 12, 15, 27, 32, 14], [2, 13, 17, 21, 22, 33, 13], [5, 7, 9, 16, 26, 29, 7], [4, 7, 10, 26, 27, 28, 14], [7, 14, 15, 19, 21, 28, 7], [8, 11, 14, 15, 16, 26, 7], [1, 5, 7, 22, 26, 32, 11], [11, 14, 16, 18, 29, 32, 16], [3, 6, 21, 29, 31, 32, 5], [12, 13, 17, 18, 20, 27, 13], [1, 8, 9, 22, 24, 33, 3], [4, 6, 16, 17, 26, 33, 3], [5, 7, 12, 18, 28, 31, 3], [5, 6, 11, 12, 14, 33, 14], [1, 13, 15, 26, 29, 30, 12], [13, 16, 18, 27, 30, 32, 16], [4, 9, 11, 17, 21, 25, 6], [9, 10, 19, 21, 23, 32, 8], [11, 12, 15, 24, 26, 27, 15], [2, 3, 4, 13, 14, 16, 2], [1, 5, 13, 22, 30, 31, 7], [5, 7, 10, 14, 23, 31, 1], [2, 3, 20, 24, 26, 27, 9], [13, 16, 17, 22, 25, 27, 10], [7, 12, 14, 17, 20, 23, 5], [3, 9, 12, 16, 17, 31, 4], [4, 10, 24, 26, 28, 32, 9], [2, 4, 11, 16, 25, 26, 12], [3, 7, 17, 22, 32, 33, 10], [1, 2, 7, 10, 22, 26, 7], [1, 10, 15, 18, 19, 28, 2], [1, 7, 8, 16, 18, 20, 14], [9, 20, 24, 25, 26, 32, 4], [2, 9, 10, 18, 19, 20, 15], [2, 6, 9, 16, 25, 32, 14], [1, 3, 18, 27, 31, 32, 13], [6, 18, 22, 26, 32, 33, 4], [9, 14, 15, 18, 21, 26, 16], [1, 7, 9, 16, 22, 32, 12], [11, 12, 14, 17, 23, 27, 1], [8, 10, 14, 19, 26, 29, 12], [5, 8, 11, 17, 24, 28, 16], [2, 5, 8, 24, 25, 31, 14], [6, 15, 18, 21, 26, 27, 10], [1, 13, 17, 18, 23, 30, 15], [1, 7, 13, 19, 21, 29, 15], [8, 18, 20, 28, 29, 31, 8], [1, 3, 5, 20, 21, 31, 5], [1, 2, 17, 22, 26, 27, 4], [4, 7, 21, 25, 26, 29, 8], [6, 11, 13, 19, 21, 32, 4], [1, 9, 10, 19, 23, 27, 9], [1, 6, 8, 10, 13, 27, 16], [3, 7, 20, 22, 26, 29, 2], [9, 14, 15, 20, 26, 32, 11], [14, 17, 25, 27, 28, 30, 2], [13, 20, 22, 26, 28, 31, 13], [2, 8, 9, 14, 28, 30, 7], [6, 7, 16, 18, 29, 32, 5], [15, 18, 20, 22, 28, 29, 15], [2, 8, 25, 27, 28, 29, 5], [5, 6, 8, 16, 18, 22, 12], [9, 15, 16, 19, 20, 28, 11], [2, 12, 20, 24, 29, 31, 9], [12, 14, 19, 27, 28, 29, 1], [10, 12, 14, 22, 25, 33, 15], [5, 7, 17, 19, 22, 31, 11], [9, 15, 19, 21, 26, 27, 1], [1, 3, 13, 21, 25, 31, 8], [1, 4, 6, 13, 16, 17, 10], [4, 15, 21, 28, 30, 31, 4], [6, 16, 17, 23, 24, 31, 7], [9, 12, 14, 20, 26, 27, 4], [6, 9, 13, 26, 27, 33, 1], [6, 7, 10, 11, 14, 22, 9], [2, 3, 11, 17, 19, 21, 8], [8, 16, 22, 24, 28, 29, 5], [7, 9, 12, 14, 21, 23, 6], [6, 8, 13, 26, 30, 32, 14], [9, 18, 21, 23, 25, 26, 1], [9, 10, 16, 19, 20, 26, 12], [1, 3, 4, 23, 31, 32, 13], [7, 14, 16, 18, 21, 25, 8], [2, 12, 19, 22, 24, 27, 15], [1, 8, 9, 16, 32, 33, 13], [5, 7, 16, 17, 22, 23, 4], [8, 14, 16, 18, 20, 30, 12], [1, 3, 10, 19, 20, 27, 11], [1, 5, 7, 8, 19, 27, 12], [4, 7, 9, 13, 21, 26, 1], [1, 7, 8, 14, 24, 32, 3], [4, 6, 15, 23, 26, 28, 11], [4, 11, 12, 18, 26, 32, 12], [1, 4, 11, 21, 23, 31, 12], [2, 8, 10, 18, 23, 31, 8], [16, 21, 24, 26, 27, 29, 16], [1, 3, 20, 21, 28, 29, 12], [5, 7, 11, 16, 22, 25, 7], [5, 8, 9, 12, 22, 28, 7], [2, 3, 5, 12, 18, 27, 1], [5, 13, 22, 27, 30, 33, 10], [10, 11, 15, 20, 23, 29, 12], [7, 10, 19, 22, 27, 33, 6], [1, 3, 8, 11, 22, 28, 6], [5, 8, 11, 16, 18, 27, 4], [6, 14, 15, 16, 17, 22, 10], [10, 12, 13, 19, 22, 26, 3], [3, 5, 11, 28, 30, 33, 1], [2, 3, 13, 20, 22, 24, 15], [2, 5, 14, 19, 27, 31, 4], [1, 12, 14, 18, 26, 32, 7], [2, 5, 12, 23, 28, 29, 1], [14, 22, 23, 27, 28, 31, 12], [1, 2, 8, 16, 19, 24, 11], [1, 10, 13, 18, 25, 27, 9], [6, 20, 28, 29, 30, 31, 12], [3, 8, 19, 25, 27, 28, 2], [13, 17, 19, 20, 22, 25, 11], [13, 15, 19, 20, 21, 32, 4], [1, 4, 7, 15, 28, 32, 16], [7, 8, 15, 19, 20, 24, 13], [16, 17, 21, 28, 30, 32, 15], [8, 9, 16, 23, 24, 30, 5], [9, 13, 14, 22, 26, 27, 7], [9, 10, 20, 21, 22, 33, 9], [1, 3, 8, 11, 29, 31, 13], [5, 6, 8, 23, 31, 32, 11], [11, 18, 19, 21, 29, 32, 12], [8, 11, 15, 22, 27, 29, 3], [7, 9, 11, 15, 18, 25, 7], [6, 13, 16, 18, 20, 22, 13], [9, 14, 17, 20, 24, 30, 16], [1, 10, 14, 23, 26, 28, 1], [8, 10, 17, 22, 25, 33, 12], [11, 14, 18, 20, 31, 33, 14], [13, 16, 18, 20, 28, 31, 12], [5, 12, 14, 20, 27, 29, 6], [2, 15, 24, 29, 32, 33, 2], [10, 14, 24, 25, 27, 32, 4], [2, 4, 12, 14, 19, 25, 6], [3, 8, 10, 15, 22, 29, 12], [7, 12, 14, 16, 27, 32, 15], [7, 12, 21, 22, 26, 31, 1], [2, 8, 10, 18, 20, 27, 7], [1, 2, 14, 22, 25, 26, 7], [1, 20, 22, 24, 25, 26, 16], [5, 6, 8, 20, 22, 30, 5], [12, 13, 14, 17, 21, 25, 4], [6, 13, 16, 17, 23, 30, 10], [1, 2, 10, 12, 22, 24, 10], [9, 11, 13, 22, 24, 26, 5], [4, 9, 19, 22, 23, 30, 7], [3, 6, 10, 19, 25, 29, 7], [2, 5, 7, 14, 18, 31, 13], [4, 11, 12, 17, 24, 30, 12], [4, 9, 12, 28, 30, 33, 1], [11, 13, 15, 17, 19, 31, 5], [6, 8, 12, 21, 25, 29, 1], [12, 15, 18, 20, 21, 27, 15], [10, 14, 19, 22, 25, 29, 12], [3, 8, 10, 19, 26, 33, 3], [8, 12, 14, 15, 21, 27, 15], [6, 17, 18, 20, 27, 29, 15], [3, 15, 21, 22, 23, 28, 15], [4, 13, 19, 20, 26, 29, 11], [3, 4, 7, 9, 20, 22, 3], [6, 15, 26, 31, 32, 33, 16], [3, 12, 13, 22, 28, 29, 3], [1, 3, 7, 18, 19, 27, 16], [3, 13, 19, 20, 23, 26, 3], [12, 17, 18, 21, 22, 24, 4], [7, 14, 17, 23, 26, 31, 9], [5, 14, 20, 26, 30, 33, 12], [1, 3, 10, 12, 18, 30, 1], [4, 9, 12, 17, 30, 32, 3], [7, 20, 25, 26, 27, 30, 14], [2, 5, 8, 15, 17, 22, 16], [3, 8, 13, 14, 15, 30, 4], [6, 8, 13, 14, 22, 27, 10], [9, 12, 24, 28, 29, 30, 2], [1, 2, 4, 9, 15, 33, 12], [1, 6, 13, 19, 24, 28, 16], [2, 8, 10, 12, 29, 31, 1], [6, 11, 16, 19, 28, 32, 4], [5, 6, 10, 16, 22, 26, 11], [3, 4, 8, 11, 16, 18, 14], [7, 12, 19, 22, 23, 26, 11], [3, 5, 18, 20, 24, 32, 11], [4, 11, 12, 20, 25, 28, 15], [4, 5, 22, 26, 29, 32, 8], [5, 6, 8, 18, 20, 32, 8], [12, 13, 15, 18, 19, 21, 9], [16, 17, 18, 23, 28, 32, 7], [3, 12, 14, 17, 19, 26, 3], [13, 16, 22, 25, 26, 27, 14], [3, 7, 13, 18, 19, 20, 5], [9, 13, 18, 20, 27, 31, 4], [8, 19, 23, 28, 31, 32, 1], [8, 10, 11, 20, 21, 27, 11], [3, 6, 11, 18, 23, 29, 1], [19, 21, 26, 28, 29, 32, 1], [5, 16, 19, 22, 24, 25, 2], [9, 11, 12, 15, 16, 20, 13], [6, 10, 11, 12, 20, 25, 12], [1, 3, 6, 16, 29, 32, 7], [7, 8, 13, 22, 30, 32, 1], [1, 9, 17, 19, 20, 29, 10], [2, 4, 8, 23, 26, 29, 2], [1, 3, 10, 12, 24, 28, 2], [1, 16, 17, 24, 25, 32, 14], [2, 6, 15, 25, 30, 32, 7], [6, 12, 14, 15, 17, 20, 9], [9, 16, 17, 24, 30, 31, 4], [2, 4, 12, 18, 24, 26, 5], [1, 12, 19, 20, 21, 25, 16], [9, 10, 11, 12, 15, 32, 5], [2, 3, 10, 11, 14, 21, 12], [3, 14, 16, 18, 25, 33, 15], [1, 3, 14, 30, 31, 32, 8], [2, 13, 17, 20, 21, 26, 7], [4, 8, 14, 22, 23, 28, 7], [2, 13, 15, 23, 24, 29, 6], [6, 9, 15, 17, 25, 27, 9], [6, 7, 10, 12, 18, 31, 10], [1, 5, 9, 12, 18, 32, 12], [6, 13, 14, 21, 22, 24, 16], [6, 13, 25, 26, 28, 31, 1], [2, 8, 25, 29, 31, 32, 6], [1, 11, 21, 23, 27, 33, 6], [3, 10, 22, 23, 27, 29, 4], [1, 3, 19, 24, 32, 33, 1], [5, 8, 10, 14, 17, 30, 13], [1, 5, 13, 19, 24, 27, 11], [5, 9, 11, 18, 30, 31, 4], [8, 10, 19, 27, 28, 31, 16], [4, 5, 13, 22, 25, 30, 4], [6, 11, 18, 26, 27, 32, 1], [2, 3, 7, 8, 19, 26, 16], [9, 11, 15, 16, 27, 33, 5], [5, 7, 28, 31, 32, 33, 8], [2, 4, 7, 14, 15, 32, 4], [6, 12, 14, 15, 18, 25, 12], [1, 11, 16, 17, 20, 26, 14], [5, 16, 20, 22, 27, 29, 9], [6, 8, 20, 22, 26, 27, 9], [7, 18, 20, 23, 27, 31, 13], [3, 10, 14, 17, 28, 33, 2], [9, 14, 22, 23, 31, 33, 14], [9, 19, 21, 30, 31, 32, 4], [2, 5, 6, 21, 25, 28, 9], [2, 3, 10, 23, 25, 28, 9], [15, 22, 23, 24, 28, 29, 8], [7, 9, 12, 14, 20, 27, 16], [9, 15, 21, 24, 27, 32, 10], [1, 6, 8, 20, 27, 30, 3], [2, 6, 12, 17, 18, 19, 10], [7, 12, 17, 26, 29, 31, 16], [4, 9, 11, 17, 26, 27, 13], [5, 6, 8, 21, 31, 33, 14], [3, 17, 21, 23, 27, 28, 1], [4, 10, 18, 19, 25, 27, 2], [5, 8, 13, 19, 27, 28, 7], [15, 16, 21, 22, 27, 33, 15], [11, 12, 13, 14, 18, 33, 13], [2, 8, 10, 18, 20, 33, 12], [2, 7, 10, 20, 27, 29, 3], [1, 6, 9, 10, 15, 32, 14], [7, 16, 20, 24, 25, 30, 7], [1, 6, 19, 26, 28, 30, 3], [1, 2, 5, 17, 26, 32, 10], [4, 13, 15, 17, 21, 24, 15], [1, 10, 17, 21, 23, 30, 12], [6, 9, 23, 24, 25, 33, 13], [4, 10, 12, 27, 32, 33, 5], [1, 3, 7, 12, 19, 20, 6], [3, 7, 15, 16, 17, 23, 10], [4, 14, 18, 28, 31, 32, 12], [1, 2, 11, 20, 26, 30, 14], [3, 20, 23, 26, 32, 33, 7], [2, 4, 5, 9, 13, 21, 5], [6, 11, 16, 20, 22, 33, 7], [2, 8, 9, 16, 20, 22, 7], [7, 9, 16, 24, 25, 29, 6], [9, 11, 14, 20, 25, 26, 15], [15, 19, 23, 24, 25, 32, 3], [1, 4, 8, 15, 27, 32, 16], [5, 13, 17, 26, 27, 30, 7], [6, 11, 12, 22, 23, 30, 5], [2, 4, 8, 26, 29, 33, 8], [2, 4, 5, 24, 26, 33, 15], [7, 13, 15, 27, 28, 29, 13], [2, 6, 8, 9, 15, 29, 14], [5, 8, 19, 25, 28, 30, 7], [10, 11, 12, 23, 26, 29, 16], [10, 11, 14, 15, 16, 24, 7], [8, 11, 28, 29, 31, 33, 6], [6, 8, 18, 20, 23, 31, 13], [1, 8, 9, 14, 17, 32, 1], [5, 8, 16, 22, 27, 29, 2], [3, 7, 8, 10, 22, 23, 12], [1, 2, 3, 17, 25, 31, 9], [4, 6, 8, 12, 23, 25, 8], [4, 8, 10, 12, 31, 33, 10], [2, 5, 10, 22, 32, 33, 9], [2, 6, 15, 16, 18, 32, 15], [1, 3, 4, 11, 18, 22, 14], [9, 21, 25, 26, 29, 31, 13], [2, 15, 16, 17, 22, 32, 7], [3, 10, 12, 19, 27, 30, 8], [2, 4, 11, 14, 27, 30, 5], [7, 8, 12, 13, 22, 30, 9], [2, 15, 21, 23, 25, 30, 10], [1, 7, 9, 20, 23, 30, 2], [6, 10, 16, 26, 27, 29, 3], [5, 8, 15, 24, 27, 31, 11], [5, 7, 15, 20, 23, 30, 15], [4, 7, 8, 19, 32, 33, 13], [1, 6, 14, 24, 28, 32, 12], [1, 2, 5, 10, 24, 27, 15], [11, 15, 20, 22, 25, 30, 5], [1, 4, 8, 13, 24, 27, 5], [2, 4, 12, 14, 17, 24, 15], [15, 19, 23, 28, 29, 33, 4], [4, 10, 13, 15, 22, 27, 4], [1, 2, 4, 7, 10, 23, 4], [8, 13, 16, 23, 27, 31, 8], [8, 16, 19, 21, 31, 32, 6], [5, 7, 16, 20, 21, 25, 5], [4, 13, 14, 23, 26, 32, 10], [2, 5, 8, 10, 32, 33, 2], [5, 8, 9, 14, 15, 19, 7], [1, 8, 14, 15, 20, 29, 10], [10, 12, 20, 24, 27, 29, 7], [2, 5, 9, 15, 24, 25, 11], [7, 8, 18, 24, 29, 31, 7], [4, 9, 11, 15, 29, 31, 6], [2, 3, 9, 23, 28, 33, 8], [7, 12, 13, 20, 24, 31, 5], [13, 14, 18, 19, 21, 28, 6], [18, 20, 22, 23, 30, 31, 16], [1, 9, 13, 22, 28, 32, 11], [4, 8, 9, 15, 19, 25, 9], [5, 10, 13, 24, 26, 31, 4], [6, 7, 12, 20, 26, 27, 11], [1, 7, 22, 24, 26, 31, 10], [12, 16, 20, 22, 25, 31, 4], [2, 10, 16, 22, 24, 28, 15], [2, 5, 8, 10, 12, 21, 7], [1, 4, 6, 17, 19, 26, 3], [1, 3, 4, 10, 18, 29, 4], [2, 6, 10, 22, 30, 31, 15], [2, 11, 12, 23, 29, 31, 5], [1, 6, 14, 22, 25, 26, 12], [2, 3, 6, 14, 31, 32, 3], [6, 11, 14, 23, 26, 30, 2], [3, 6, 16, 23, 26, 30, 14], [2, 6, 16, 23, 30, 31, 2], [1, 3, 6, 19, 21, 29, 7], [1, 4, 8, 9, 14, 15, 13], [1, 2, 4, 15, 17, 22, 14], [5, 7, 18, 19, 22, 24, 16], [3, 7, 14, 23, 25, 27, 8], [1, 12, 16, 20, 22, 24, 8], [3, 5, 14, 25, 26, 30, 5], [14, 18, 21, 25, 28, 29, 10], [3, 8, 14, 20, 24, 26, 12], [1, 5, 11, 20, 22, 24, 2], [1, 5, 6, 16, 25, 30, 9], [3, 5, 6, 13, 20, 22, 7], [3, 6, 13, 14, 19, 28, 6], [7, 9, 18, 22, 23, 29, 6], [11, 12, 13, 16, 23, 25, 12], [1, 7, 10, 16, 22, 33, 9], [5, 7, 10, 23, 28, 29, 3], [10, 18, 19, 29, 32, 33, 9], [7, 8, 9, 15, 22, 27, 12], [8, 11, 13, 19, 28, 31, 6], [9, 10, 12, 19, 22, 29, 16], [2, 6, 11, 12, 19, 29, 6], [5, 10, 18, 19, 30, 31, 3], [4, 19, 22, 27, 30, 33, 1], [2, 5, 6, 16, 28, 29, 4], [4, 7, 8, 18, 23, 24, 2], [1, 4, 11, 28, 31, 32, 16], [4, 8, 10, 14, 18, 20, 11], [1, 21, 23, 25, 31, 33, 1], [1, 14, 15, 20, 23, 30, 14], [3, 6, 7, 12, 25, 26, 7], [12, 15, 20, 25, 27, 31, 2], [8, 9, 15, 17, 30, 32, 6], [7, 12, 14, 15, 17, 20, 1], [8, 14, 16, 18, 21, 23, 16], [1, 3, 12, 15, 19, 23, 14], [5, 10, 17, 19, 29, 32, 12], [3, 10, 14, 16, 22, 23, 11], [4, 6, 16, 27, 29, 33, 5], [6, 12, 13, 15, 18, 26, 13], [4, 10, 11, 25, 30, 31, 1], [2, 14, 20, 22, 30, 32, 2], [1, 2, 8, 11, 14, 21, 9], [8, 9, 15, 22, 30, 33, 16], [9, 16, 21, 25, 26, 31, 14], [8, 10, 15, 19, 23, 28, 16], [11, 18, 19, 22, 24, 32, 7], [11, 20, 21, 22, 24, 27, 15], [4, 5, 6, 11, 21, 31, 10], [2, 6, 11, 26, 28, 29, 3], [1, 14, 23, 25, 29, 30, 3], [1, 16, 17, 21, 27, 30, 16], [14, 15, 21, 24, 27, 32, 12], [2, 6, 13, 22, 29, 31, 8], [5, 6, 9, 14, 21, 33, 2], [5, 13, 14, 23, 25, 31, 2], [1, 7, 10, 11, 26, 27, 11], [2, 3, 5, 9, 13, 28, 11], [6, 15, 17, 18, 23, 30, 11], [4, 5, 11, 14, 28, 32, 4], [1, 6, 7, 14, 18, 26, 16],[3,7,10,18,21,24,12],[5,10,20,23,26,31,3],[1,17,24,28,32,33,2],[2,14,20,24,28,32,16],[21,22,25,28,29,30,8],[1,6,7,11,13,15,5],[8,13,14,18,23,33,6],[4,6,9,14,20,29,14],[3,14,16,20,31,32,9],[2,6,12,17,25,28,12],[1,19,25,26,27,33,10],[3,7,20,21,25,31,14],[4,7,11,14,29,32,12],[5,8,15,20,27,30,13],[6,14,19,20,21,23,8],[2,5,7,9,11,27,16],[6,10,23,25,26,29,5]]

#------------------------------------
def TestRuleOne(one):
    Get_List=[]
    sum=one[0]+one[1]+one[2]+one[3]+one[4]+one[5]
    first_D=(sum-one[0])/one[0]
    second_D=(sum-one[1])/one[1]
    third_D=(sum-one[2])/one[2]
    forth_D=(sum-one[3])/one[3]
    fifth_D=(sum-one[4])/one[4]
    sixth_D=(sum-one[5])/one[5]
    for _D in [first_D,second_D,third_D,forth_D,fifth_D,sixth_D]:
        get_list=ruleOne(_D)
        for i in get_list:
            Get_List.append(i)
    for i in Get_List:
        if i==0 or i>33:
            Get_List.remove(i)
    return sorted(list(set(Get_List)))

def ruleOne(data):
    touch_List = []
    touch_List.append(data)
    if data<10:
        tail=data
    else:
        tail=data%10
    for i in range(6):
        if tail<=33:
            touch_List.append(tail)
            tail += 10
        else:
            break
    return list(set(touch_List))

def kill(one):
    data_List=TestRuleOne(one)
    if one[5]-one[0] in data_List:
        data_List.remove(one[5]-one[0])
    return data_List

def TestFirstOne(datas=None):
    first_=[]
    for data in datas[-100:]:
        if data[0]%2==0:
            first_.append('偶')
        else:
            first_.append('奇')
    print str(first_).decode('string_escape')
def TestLastOne(datas=None):
    last_=[]
    for data in datas[-100:]:
        if data[-1]%2==0:
            last_.append('偶')
        else:
            last_.append('奇')
    print str(last_).decode('string_escape')
def run(ssq):
    for i in ssq:
        if i[-2]==30 and i[-3]>=27:
            try:
                print ssq[ssq.index(i)], ssq.index(i)
                print ssq[ssq.index(i) + 1], ssq.index(i)
            except Exception as e:
                pass
            print '*'*30

def rule(ssq):
    for i in ssq:
        if i[-1]==16 and i[0]%2==0 and 27 in i:
            try:
                print ssq[ssq.index(i)], ssq.index(i)
            except Exception as e:
                pass
def rule_quchong(ssq,res=None):
    for i in ssq:
        if i ==res:
            try:
                print ssq[ssq.index(i)], ssq.index(i)
            except Exception as e:
                pass
def rule_test(ssq):
    for i in ssq:
        if  13 ==i[0] and 13==i[-1]:
            try:
                # print ssq[ssq.index(i) -1], ssq.index(i)
                print ssq[ssq.index(i)], ssq.index(i)
                # print ssq[ssq.index(i) + 1], ssq.index(i)
                # if ssq[ssq.index(i) + 1][-1]%2==1:
                #     print ssq[ssq.index(i) + 1][-1]
            except Exception as e:
                pass
            # print '*'*30
def rule_together(ssq):
    l=len(ssq)
    for i in range(1,34):
        for j in range(i,34):
            s = 0
            if i!=j:
                for data in ssq:
                    if i in data and j in data:
                        s+=1
                print i,j,u'Result:'+ '%.2f%%'%(float(s)/l*100)

if __name__=='__main__':
    # print kill(ssq[-1])
    # TestFirstOne(ssq)
    TestLastOne(ssq)
    # rule(ssq)
    # rule_quchong(ssq)
    # rule_test(ssq)
    # rule_together(ssq)