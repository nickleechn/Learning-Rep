zzymark = []
rcmark = []
zytmark = []
lxymark = []
roundnumber = []

def calcualte_mark():
	roundnumber.append(1)
	roundsum = sum(roundnumber)
	print(":::正在填写分数 REGISTERING MARKS:::")
	print()
	print(f"- ⚠️ 可以填写3、2、1或0分")
	zzyinput = int(input(f"🐵 请输入祝子扬分数："))
	zzymark.append(zzyinput)
	rcinput = int(input(f"🐵 请输入任晨分数："))
	rcmark.append(rcinput)
	zytinput = int(input(f"🐵 请输入朱奕潼分数："))
	zytmark.append(zytinput)
	lxyinput = int(input(f"🐵 请输入厉修远分数："))
	lxymark.append(lxyinput)
	print(f"\t⏰ 这已经是第{roundsum}局")
	print(f"💅 记录完成，请开始下一局或显示分数")
	invite()
	
def showmark():
	zzysum = sum(zzymark)
	rcsum = sum(rcmark)
	lxysum = sum(lxymark)
	zytsum = sum(zytmark)
	finalsum = sum(roundnumber)
	totalsum = zzysum + rcsum + lxysum + zytsum
	zzywin = zzysum / totalsum
	rcwin = rcsum / totalsum
	zytwin = zytsum / totalsum
	lxywin = lxysum / totalsum
	zzypercent = "{:.0%}".format(zzywin)
	rcpercent = "{:.0%}".format(rcwin)
	zytpercent = "{:.0%}".format(zytwin)
	lxypercent = "{:.0%}".format(lxywin)
	
	print("")
	print("====🏆对战结果  RESULTS🏆====")
	print("")
	print(f"- 我们一共进行了{finalsum}局UNO，总分为{totalsum}")
	print("")
	print(f"祝子扬{zzysum}分，胜率{zzypercent}\n任晨{rcsum}分，胜率{rcpercent}\n朱奕潼{zytsum}分，胜率{zytpercent}\n厉修远{lxysum}分，胜率{lxypercent}")
	print("")

def invite():
	print("请进行选择 MAKE A SELECTION")
	userinput = int(input("\n1. 🥁 计算分数 \n2. 👀 显示分数 "))
	if userinput == 1:
		calcualte_mark()
	elif userinput ==2:
		showmark()
	else:
		print("输入错误，请重新输入")
		invite()

print(f":::UNO Calculator v1.2:::")
print()
print(f"- 🎉请开始第一局")

invite()