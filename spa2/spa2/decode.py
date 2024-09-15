import hashlib
import base64
import time


def generate_signature(*args):
    # 获取当前时间的Unix时间戳（秒为单位）
    timestamp = '1725962153'
    # 将所有传入的参数和时间戳连接成一个字符串
    data = ",".join(args + (timestamp,))

    # 使用SHA1哈希算法对数据进行哈希
    sha1_hash = hashlib.sha1(data.encode('utf-8')).hexdigest()

    # 将哈希值和时间戳再次连接，并转换为Base64格式
    base64_encoded = base64.b64encode(f"{sha1_hash},{timestamp}".encode('utf-8')).decode('utf-8')

    return base64_encoded


s = 'ef34#teuq0btua#(-57w1q5o5--j@98xygimlyfxs*-!i-0-mb'
detail = base64.b64encode((s + str(1)).encode()).decode()
print(detail)
print(generate_signature('/api/movie/' + detail))
