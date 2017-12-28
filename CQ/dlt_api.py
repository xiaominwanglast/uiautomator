#coding:utf-8
import requests
import json
import time
url='http://api.icaipiao123.com/api/v7/social/newlist?count=1000&lottery_key=daletou&max_id=0'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',}
rq=requests.get(url=url,headers=headers)
js_rq=json.loads(rq.text)
new_list=[]
image_list=[]
for i in js_rq['data']:
    if time.localtime(int(i['publish_time'])/1000).tm_mday>=26:
        print i['content']
        if i['images']:
            image_list.append(i['images'])
        if i['predict_data']:
            for j in i['predict_data']['data']:
                 new_list.append(j)

for i in image_list:
    print i
print new_list

s1=s2=s3=s4=s5=s6=s7=s8=s9=s10=s11=s12=s13=s14=s15=s16=s17=s18=s19=s20=s21=s22=s23=s24=s25=s26=s27=s28=s29=s30=s31=s32=s33=s34=s35=0
q1=q2=q3=q4=q5=q6=q7=q8=q9=q10=q11=q12=0
for k in new_list:
    if '01' in k[0]:
        s1+=1
    if '02' in k[0]:
        s2+=1
    if '03' in k[0]:
        s3+=1
    if '04' in k[0]:
        s4+=1
    if '05' in k[0]:
        s5+=1
    if '06' in k[0]:
        s6+=1
    if '07' in k[0]:
        s7+=1
    if '08' in k[0]:
        s8+=1
    if '09' in k[0]:
        s9+=1
    if '10' in k[0]:
        s10+=1
    if '11' in k[0]:
        s11+=1
    if '12' in k[0]:
        s12+=1
    if '13' in k[0]:
        s13+=1
    if '14' in k[0]:
        s14+=1
    if '15' in k[0]:
        s15+=1
    if '16' in k[0]:
        s16+=1
    if '17' in k[0]:
        s17+=1
    if '18' in k[0]:
        s18+=1
    if '19' in k[0]:
        s19+=1
    if '20' in k[0]:
        s20+=1
    if '21' in k[0]:
        s21+=1
    if '22' in k[0]:
        s22+=1
    if '23' in k[0]:
        s23+=1
    if '24' in k[0]:
        s24+=1
    if '25' in k[0]:
        s25+=1
    if '26' in k[0]:
        s26+=1
    if '27' in k[0]:
        s27+=1
    if '28' in k[0]:
        s28+=1
    if '29' in k[0]:
        s29+=1
    if '30' in k[0]:
        s30+=1
    if '31' in k[0]:
        s31+=1
    if '32' in k[0]:
        s32+=1
    if '33' in k[0]:
        s33+=1
    if '34' in k[0]:
        s34+=1
    if '35' in k[0]:
        s35+=1
    if '01' in k[1]:
        q1+=1
    if '02' in k[1]:
        q2+=1
    if '03' in k[1]:
        q3+=1
    if '04' in k[1]:
        q4+=1
    if '05' in k[1]:
        q5+=1
    if '06' in k[1]:
        q6+=1
    if '07' in k[1]:
        q7+=1
    if '08' in k[1]:
        q8+=1
    if '09' in k[1]:
        q9+=1
    if '10' in k[1]:
        q10+=1
    if '11' in k[1]:
        q11+=1
    if '12' in k[1]:
        q12+=1


print 1,'show',s1
print 2,'show',s2
print 3,'show',s3
print 4,'show',s4
print 5,'show',s5
print 6,'show',s6
print 7,'show',s7
print 8,'show',s8
print 9,'show',s9
print 10,'show',s10
print 11,'show',s11
print 12 ,'show', s12
print 13 ,'show', s13
print 14 ,'show', s14
print 15 ,'show', s15
print 16 ,'show', s16
print 17 ,'show', s17
print 18 ,'show', s18
print 19 ,'show', s19
print 20 ,'show', s20
print 21 ,'show', s21
print 22 ,'show', s22
print 23 ,'show', s23
print 24 ,'show', s24
print 25 ,'show', s25
print 26 ,'show', s26
print 27 ,'show', s27
print 28 ,'show', s28
print 29 ,'show', s29
print 30 ,'show', s30
print 31 ,'show', s31
print 32 ,'show', s32
print 33 ,'show', s33
print 34 ,'show', s34
print 35 ,'show', s35

print 1 ,'show', q1
print 2 ,'show', q2
print 3 ,'show', q3
print 4 ,'show', q4
print 5 ,'show', q5
print 6 ,'show', q6
print 7 ,'show', q7
print 8 ,'show', q8
print 9 ,'show', q9
print 10 ,'show', q10
print 11 ,'show', q11
print 12 ,'show', q12





