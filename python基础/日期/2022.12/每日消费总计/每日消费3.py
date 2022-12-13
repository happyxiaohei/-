"""
每日消费3 -

Date: 2022/12/9

"""
import datetime
import pandas as pd

# 初始化 DataFrame
expenses = pd.DataFrame(columns=["amount", "description"])

# 定义一个变量来控制循环
enter_more = True

# 使用 while 循环来重复提示用户输入消费信息
while enter_more:
  # 提示用户输入消费金额和描述
  amount = input("请输入消费金额：")
  description = input("请输入消费描述：")

  # 将用户输入的数据添加到 DataFrame 中
  expenses = pd.concat([expenses, pd.DataFrame(
      [{"amount": pd.to_numeric(amount), "description": description}])], ignore_index=True)

  # 提示用户是否继续输入消费信息
  enter_more_input = input("是否继续输入消费信息？输入 y 继续，其他任意键退出。")
  if enter_more_input.lower() != "y":
    enter_more = False

# 使用当前日期和时间作为文件名的一部分
timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
filename = f"每日消费_{timestamp}.xlsx"

# 保存 DataFrame 到 Excel 文件
expenses.to_excel(filename)


# 让这个程序再提取execl文件中的消费金额和消费描述,再重新创建一个execl文件,
# 用来记录年消费记录,并且只创建一次年消费记录