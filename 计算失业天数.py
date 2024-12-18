import time 

# 失业日期
loss_date = time.strptime("2024-11-12", "%Y-%m-%d")

# 当前日期
current_date = time.strptime(time.strftime("%Y-%m-%d", time.localtime()), "%Y-%m-%d")

# 将struct_time转换为时间戳
loss_timestamp = time.mktime(loss_date)
current_timestamp = time.mktime(current_date)

# 计算时间差并转换为天数
loss_days = int((current_timestamp - loss_timestamp) / (24 * 60 * 60))
print(f"已经失业: {loss_days}天了:<")