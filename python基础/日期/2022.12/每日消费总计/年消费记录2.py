"""
年消费记录2 -

Date: 2022/12/10

"""
# 导入 datetime 和 csv 模块
import datetime
import csv

def main():
  # 获取当前日期
  today = datetime.datetime.now()
  # 获取当前年份
  year = today.year

  # 创建消费记录列表
  records = []

  # 检查文件是否存在
  file_exists = False
  try:
    # 尝试打开文件。如果它存在，将file_exists设置为True
    with open(f"{year}_consumption_records.csv", "r", newline="") as csvfile:
      file_exists = True
  except:
    pass

  # 打开文件
  with open(f"{year}_consumption_records.csv", "a", newline="") as csvfile:
    # 创建一个CSV文件写入器
    writer = csv.writer(csvfile)

    # 如果文件不存在，写入标题
    if not file_exists:
      writer.writerow(["date", "consumption_amount", "consumption_month"])

    # 初始化每月和每年的消费总量
    monthly_total = 0
    yearly_total = 0

    while True:
      # 获取消费量
      amount = float(input("请输入消费量（输入0退出）："))
      if amount == 0:
        break

      # 写入消费记录
      writer.writerow([today.strftime("%Y-%m-%d"), amount, today.strftime("%Y-%m")])




      # 将消费量和日期添加到记录列表中
      records.append((amount, today.strftime("%Y-%m-%d")))

      # 更新每月和每年的消费总量
      monthly_total += amount
      yearly_total += amount

    def print_totals():
      # Print the monthly and yearly totals for consumption
      print(f"每月消耗总量: {monthly_total}")
      print(f"每年消耗总量: {yearly_total}")

    # Call the function
    print_totals()

    # 再次打印每月和每年的消耗总量
    print(f"Monthly total for consumption: {monthly_total}")
    print(f"Yearly total for consumption: {yearly_total}")


if __name__ == "__main__":
  main()

