#讀檔案
date = []
count = 0
with open('original.txt','r') as f:
    for line in f:
        date.append(line)
        count = count + 1
        if count % 1000 == 0:
                print(len(date))
print('檔案讀取完了','總共有',len(date),'筆資料')

sum_len = 0
for d in date:
    sum_len = sum_len + len(d)
    print('平均留言長度',sum_len/len(date))
    
