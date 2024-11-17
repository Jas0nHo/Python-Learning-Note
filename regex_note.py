import re


# re模块

# 三大查找方法
# re.findall() 以列表的方式返回全部匹配结果
# re.match() 对开头进行匹配,放回第一个结果
# re.search() 返回一个匹配结果

# 其他常用方法
# re.split() 以指定方式分割文本并返回一个列表
# re.sub() 匹配制定内容并替换,可指定替换次数
# group() 返回指定分组的内容

# 匹配模式
# I 不区分大小写
# S 匹配全部字符(.可匹配除换行符外全部字符)


#正则表达式

# 预定义字符
# \d 匹配所有数字 0-9
# \D 匹配所有的非数字 等于 ^\d
# \w 匹配下划线,数字,字母 a-ZA-Z0-9_
# \W 匹配非正常字符,特殊字符
# \s 匹配空自符 制表符 换行符
# \S 匹配空自符 制表符 换行符 等于^\s
# . 匹配除换行符以外的任何单个字符
# \ 转义符

# 元字符
#［］匹配一个字符，括号内的字符是或者的关系
# ^ 取反 \D ^\d
# - 代表区间
# () 代表分组

# 重复匹配
# {n} 前面的字符匹配n次
# {n,m} 前面的字符匹配最少n次,最多m次
# {n,} 前面的字符匹配最少n次,无上限
# ? 前面的字符匹配0次或1次
# + 前面的字符至少匹配一次
# * 前面的字符匹配0次或任意次
# 正则表达式默认进行贪婪匹配,上述符号后加 ? 进行非贪婪匹配


# 例1 匹配html文本中的特定信息
html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>正则表达式匹配练习</title>
</head>
<body>
    <h1>欢迎来到正则表达式匹配练习</h1>
    <p>这是一个段落，包含一些文本和数字：1234567890</p>
    <ul>
        <li>列表项 1</li>
        <li>列表项 2</li>
        <li>列表项 3</li>
    </ul>
    <p>另一个段落，包含一些特殊字符：@#$%^&*()</p>
    <a href="https://www.example.com">这是一个链接</a>
</body>
</html>
'''

pattern_1 = r'<ul>(.+?)</ul>'
result_1 = re.findall(pattern_1, html)
result_1_improved = re.findall(pattern_1, html, re.S)
print('例1 优化前:',result_1)
print('例1 优化后:',result_1_improved)

# 反向引用
# 例2 匹配文本中以固定形式开头和结尾的字符
words = '''
'hello' "hey" 'yo" "lol'
'''

pattern_2 = r'(\'|")(\w+?)(\1)'
result_2 = re.search(pattern_2, words)
print('例2:', result_2.group(2))
# 例3 在匹配内容前后加入特定字符
text = 'the teacher recommend some books to us,including Holes and Dune.They are all my love'
pattern_3 = r'([A-Z]\w+)'#注意小括号
result_3 = re.sub(pattern_3, r'《\1》', text, 2)
print('例3:', result_3)

# 位置匹配
# ^ $用于匹配特定开头和结尾的行
# \b \b用于匹配特定开头和结尾的字符,匹配位置为两个字符或符号之间(中文不行)
# 例4 匹配文本中的手机号码
text_ch = '我的手机号码13812345678，另一个号码是13987654321。如果你需要联系我，可以拨打这两个号码中的任意一个。'
text_en = 'My phone number is 13812345678,another is 13987654321.If you need to contact me,please call one of those.'
# 正则表达式在英文文本和中文文本中匹配结果不同
pattern_4 = r'\b1[3-9]\d{9}\b'
result_ch = re.findall(pattern_4, text_ch)
result_en = re.findall(pattern_4, text_en)
print('例3 pattern修改前中文匹配结果:', result_ch)
print('例3 pattern修改前英文匹配结果:', result_en)
# 解决方法
pattern_4_improved = r'(?<!\d)1[3-9]\d{9}(?!\d)'
result_ch_improved = re.findall(pattern_4_improved, text_ch)
result_en_improved = re.findall(pattern_4_improved, text_en)
print('例3 pattern修改后中文匹配结果:', result_ch_improved)
print('例3 pattern修改后英文匹配结果:', result_en_improved)
