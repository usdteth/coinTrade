import random
import string

def write_text(file_name,record_text):
    with open(file_name, 'a') as file:
        file.write(record_text + '\n')

# 随机数生成
def generate_random_string(length):
    letters = string.ascii_letters + string.digits  # 包含大小写字母和数字
    return ''.join(random.choice(letters) for _ in range(length))