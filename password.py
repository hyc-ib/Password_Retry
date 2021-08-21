# 密碼: a123456
password = 'a123456'
# 剩餘機會
count = 3

# 讓使用者輸入密碼，最多三次
while count > 0:
	count = count - 1
	p = input('請輸入密碼: ')
	if p == password:
		print('登入成功!')
		break
	else:
		print('密碼錯誤!')
		if count > 0:
			print('還有', count, '次機會')
		else:
			print('請重新設定密碼')