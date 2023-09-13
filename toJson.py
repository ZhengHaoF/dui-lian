# coding=utf-8
with open('上联.txt', 'r',encoding='utf-8') as fa:  # 读取需要拼接的前面那个TXT
    with open('下联.txt', 'r',encoding='utf-8') as fb:  # 读取需要拼接的后面那个TXT
        with open('完整对联.json', 'w',encoding='utf-8') as fc:  # 写入新的TXT
            fc.write("[")
            fc.write('\n')
            for line in fa:
                fc.write("{\"last\":\"")
                fc.write(line.strip('\r\n').replace(" ",""))  # 用于移除字符串头尾指定的字符
                fc.write("\",\"next\":\"")
                fc.write(fb.readline().strip('\r\n').replace(" ",""))
                fc.write("\"},")  
                fc.write('\n')
            fc.write('\n')
            fc.write("]")