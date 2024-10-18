import os
def batch_rename(folder_path, prefix):
    # 檢查資料夾是否存在
    if not os.path.exists(folder_path):
        print(f"路徑{folder_path}不存在")
        return

    for index, filename in enumerate(os.listdir(folder_path)):
        old_file = os.path.join(folder_path, filename)
        new_file = os.path.join(folder_path, f"{prefix}_{index}{os.path.splitext(filename)[1]}")
        try:
            os.rename(old_file,new_file)
        except OSError as e:
            print(f"無法重新命名{old_file}為{new_file}：{e}")
    
    print("批量改名完成!")

# 用戶輸入，使用 r 來處理路徑中的空格
folder_path = input("請輸入資料夾路徑：")
folder_path = r"{}".format(folder_path) # 將輸入路徑處理為原始字串
prefix = input("請輸入新檔名的前綴：")

batch_rename(folder_path, prefix)

help(os)