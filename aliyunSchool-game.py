print('----欢迎-----')
#身份选择 A 和 B
print('\t请选择A或B：')
print('\t1.A ','2.B ')
choice = int(input('请选择：'))
if choice == 1:
	print('欢迎选择的是A')
elif choice == 2:
	print('还是分到选择的是A')
else :
	print('选择错误，还是分到选择的是A')

#显示玩家信息（攻击，生命），要创建变量保存
pattack = 9
plive = 9
#创建变量，保存BOSS攻击和生命1

battack = 10
blive = 20

#显示玩家信息
print(f'身份A攻击:{pattack},生命:{plive}')

# 游戏显示选项是循环的
while True:
	#显示游戏选项
	print('\t选择操作：\n \t1.练级 2.打怪 3.逃跑')
	num = int(input('请选择:'))
	#处理用户选择
	if num == 1:
		pattack = pattack + 2
		plive = plive + 2
		print(f'已升级！身份A现在的attack:{pattack},生命:{plive}')

	elif num ==2:
		#玩家攻击BOSS,减去BOSS生命值
		blive = blive - pattack

		print('A攻击了BOSS')
		#检查BOSS生命值是否为0
		if blive <= 0:
			#boss消亡，玩家胜利
			print(f'BOSS受到了{pattack}点伤害，已消灭BOSS')
			#游戏结束
			break

		#BOSS反击玩家
		#减去玩家生命值
		print('BOSS攻击了A')
		plive = plive - battack
		#检查玩家是否生命值为0
		if plive <= 0:
			print(f'玩家受到了{battack}点伤害，游戏结束')
			break

	elif num == 3:
		print('跑了，游戏结束')
		break
	else :
		print('重新输入')






#       print('欢迎选择的是A,attack:',attack,'live:',live)
# 		print('选择操作：\n 1.练级 2.打怪 3.逃跑')
# 		c4 = int(input('请选择:'))
# 		if c4 == 1:
# 			attack = attack + num
# 			live = live + num
# 			print('现在A的attack:',attack,'live:',live)
# 		elif c4 == 2:
# 			pass
# 		elif c4 == 3:
# 			pass
# 		else :
# 			print('输入有误')
