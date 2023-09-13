# coding=utf-8
with open('上联.txt', 'r',encoding='utf-8') as fa:  # 读取需要拼接的前面那个TXT
    with open('下联.txt', 'r',encoding='utf-8') as fb:  # 读取需要拼接的后面那个TXT
        with open('完整对联.txt', 'w',encoding='utf-8') as fc:  # 写入新的TXT
            for line in fa:
                fc.write(line.strip('\r\n').replace(" ",""))  # 用于移除字符串头尾指定的字符
                #fc.write(fa.readline())
                fc.write(' ——— ')
                fc.write(fb.readline().replace(" ",""))
                #fc.write('\n')