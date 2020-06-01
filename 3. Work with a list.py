house = ['nick', 'kiki', 'layla', 'kawahi', 'huskar'] #我们建立一个列表，列出家里所有的人
for roommate in house: #建立for循环：对于房子里的每个室友
	print(f"{roommate.title()}") #都要python显示每个人的名字
# for every "roommate" in the "house", print each of their names

print()
number = list(range(1,6)) #让python生成一个1-5的数字列表。注意，最后一个数字是5，不是6.
print(number)

some_number = list(range(2, 100, 5))
#在这里，我们让python生成一个2-99的数字列表，每个数之间距离5个数，你也可以想象成每个数字在不停的加5.
print(some_number)

# Let's create a list of square numbers (平方数).
squares = [] #我们创建一个叫平方数的列表
for value in range(1, 11): #生成数字1-10，创建for循环。我们把每个数字称为value。
	square = value ** 2 #定义平方数：一个平方数就是这个数平方之后得到的值
	squares.append(square) # 将新得到的平方数添加到列表中
print(squares)

#我们也可以将上面的代码简化，去掉square这个临时变量
new_squares = []
for zhi in range(11, 21): #生成一个11-20的数字列表
	new_squares.append(zhi ** 2) #直接在append()命令里就可以进行操作
print(new_squares)

#我们可以用一些命令来对列表进行简单的统计操作
print()
print(max(new_squares)) #列表中的最大值
print(min(new_squares)) #列表中的最小值
print(sum(new_squares)) #列表中数值的总和

#同样，上面的平方数也可以仅仅通过一行代码来体现，这样代码就很精简了，我们称之为list comprehension
consice_squares = [new_value**2 for new_value in range(1,11)]
print(consice_squares) 
#首先，新建一个空白列表
#在方括号中，首先写上你要对值做什么操作，然后再写一个for loop，这样python就会按照你的要求来做事情


#切分列表｜Slicing a list
print()
avengers = ['iron man', 'captain america', 'thor', 'black widow', 'hawk eye', 'hulk', 'black panther']
#👆首先我们新建一个复仇者联盟的列表
print(avengers[0:5]) #然后让python显示超级英雄的名字，从第0个开始，到第5个为止（5号不显示）
for avenger in avengers[0:6]: #我们也可以在for loop中使用slicing，比如我们只显示0-5号复仇者
	print(f"{avenger.title()}")
print(f"{avengers[-1].title()} is not a American avenger because he is from Wakanda.")

print()
superheros = avengers[:] #在这里，我们复制刚才复仇者联盟的列表，注意最后需要有方括号
superheros.sort()#将复仇者联盟按顺序排列
for heronames in superheros: #按顺序显示超级英雄的名字
	print(heronames.title())
	
dimensions = (0,50) #我们用圆括号来表示元组。当只需要一个数的时候，依然需要留下逗号
print("\n",dimensions)
dimensions = (100,500)#元组不可以被修改，但是我们可以指派新的值
print("\nLook, the new dimention here is:")
for modified_dimension in dimensions:
	print(modified_dimension)