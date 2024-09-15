# 具体编码步骤
# 第一步，将待转换的字符串每三个字节分为一组，每个字节占8bit，那么共有24个二进制位。
# 第二步，将上面的24个二进制位每6个一组，共分为4组。
# 第三步，在每组前面添加两个0，每组由6个变为8个二进制位，总共32个二进制位，即四个字节。
# 第四步，根据Base64编码对照表（见下图）获得对应的值。
# 第五步，填充字符的处理: Base64 编码在原始数据长度不是 3 的倍数时，需要在编码后的字符串末尾添加等号 (=) 作为填充。
import base64


def base64_encode(data: str):
    # 将字符串转换为字节串，然后进行Base64编码
    data = data.encode('utf-8')
    # 使用base64.b64encode()函数进行Base64编码
    encoded_bytes = base64.b64encode(data)
    # 将编码后的字节串转换回字符串
    return encoded_bytes.decode('utf-8')


def base64_decode(data: str):
    # 将字符串转换为字节串，然后进行Base64解码
    data = data.encode('utf-8')
    # 使用base64.b64decode()函数进行Base64解码
    decoded_bytes = base64.b64decode(data)
    # 将解码后的字节串转换回字符串
    return decoded_bytes.decode('utf-8')
