data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('檔案讀取完成, 總共有', len(data), '筆資料')

# print('------------------')
# print(data[0])
# print('------------------')
# print(data[1]) 

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print('average is', sum_len/len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('there are', len(new), 'comments which the length is smaller than 100')

# print(new[0])
# print(new[1])

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print(len(good))

# print(good[0])
