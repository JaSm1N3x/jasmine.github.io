# 初始化成绩和学分列表
scores = []
credits = []


for i in range(1, 3):
    while True:
        try:
            score = float(input(f"请输入第{i}门课程的百分制成绩: "))
            if 0 <= score <= 100:
                scores.append(score)
                break
            else:
                print("成绩必须在0-100之间，请重新输入")
        except ValueError:
            print("输入无效，请输入数字")
    
    while True:
        try:
            credit = float(input(f"请输入第{i}门课程的学分: "))
            if credit > 0:
                credits.append(credit)
                break
            else:
                print("学分必须为正数，请重新输入")
        except ValueError:
            print("输入无效，请输入数字")


总学分= sum(credits)
学期学习平均成绩= sum(s * c for s, c in zip(scores, credits)) / 总学分  if 总学分 > 0 else 0

print(f"学期学习平均成绩: {学期学习平均成绩:.2f}") 
学期综合素质测得分=float(input("学期综合素质测得分"))
学期综合成绩=float(学期学习平均成绩*0.85+学期综合素质测得分*0.15)
print(学期综合成绩)