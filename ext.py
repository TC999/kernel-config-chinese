import os
import json
import re

# 定义要查找的文件名
file_names = ["Kconfig", "Kconfig.debug", "Kernel.binfmt"]

# 定义要提取的关键字
keywords = ["menu", "bool", "help"]

# 定义存储结果的字典
result = {}

# 遍历当前目录及所有子目录
for root, dirs, files in os.walk("."):
    for file_name in file_names:
        if file_name in files:
            file_path = os.path.join(root, file_name)
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                matches = []
                for keyword in keywords:
                    # 使用正则表达式提取关键字后的值
                    matches.extend(re.findall(rf'{keyword}\s+"(.*?)"', content, re.DOTALL))
                if matches:  # 仅在匹配到内容时添加到结果中
                    result[file_path] = matches

# 将结果写入指定的JSON文件，格式："xxx": ""
formatted_result = {file_path: {value: "" for value in values} for file_path, values in result.items()}

# 将结果写入 result.json 文件中
with open('result.json', 'w', encoding='utf-8') as json_file:
    json.dump(formatted_result, json_file, ensure_ascii=False, indent=4)

print("提取完成，结果已保存到 result.json 文件中。")
