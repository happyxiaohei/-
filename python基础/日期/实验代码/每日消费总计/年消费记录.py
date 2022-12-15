"""
年消费记录 -

Date: 2022/12/9

"""
import datetime
import csv


def main():
  # 获取当前日期
  today = datetime.datetime.now()
  # 获取当前年份
  year = today.year

  # 创建消费记录列表
  records = []

  # 打开年消费记录文件
  with open(f"{year}消费记录.csv", "a", newline="") as csvfile:
    # 创建 CSV 文件写入器
    writer = csv.writer(csvfile)

    while True:
      # 获取消费金额
      amount = float(input("请输入消费金额（输入 0 退出程序）："))
      if amount == 0:
        break

      # 写入表头
      writer.writerow(["日期", "消费金额", "消费月份"])

      # 写入消费记录
      writer.writerow([today.strftime("%Y-%m-%d"), amount, today.strftime("%Y-%m")])

      # 将消费金额和日期添加到消费记录列表
      records.append((amount, today.strftime("%Y-%m-%d")))


if __name__ == "__main__":
  main()
