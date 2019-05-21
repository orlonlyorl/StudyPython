'''
  @功能：根据身高体重计算BMI的值
  @作者：吴雅林
  @时间：2019-05-20
  @修改：测试pep8规范
'''
#输入您的身高和体重
height=float(input("请输入您的身高："))
print("您的身高为："+str(height)+"米")

weight=float(input("请输入您的体重："))
print("您的体重为："+str(weight)+"千克")

#请计算BMI的值 BMI=体重/身高*身高
BMI=weight/(height*height)
#print("您的BMI值为："+str(BMI))

#判断
if BMI<18.5:
    print("您的BMI值为：" + str(BMI))#代码块内要统一缩进，4个空格
    print("您的体重过轻 ~@_@~")
if BMI>=18.5 and (BMI
                  <24.9):               #代码可采用括号换行的方式
    print("您的BMI值为：" + str(BMI))  # 代码块内要统一缩进，4个空格
    print("正常范围，注意保持 (-_-)")
if BMI>=24.9 and BMI<29.9:
    print("您的体重过重 ~@_@~")
if BMI>=29.9:
    print("您的BMI值为：" + str(BMI))  # 代码块内要统一缩进，4个空格
    print("肥胖 ^@_@^")