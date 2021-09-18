import xlrd

wd = xlrd.open_workbook(filename=r"F:\SQLyog任务\2020年每个月的销售情况.xlsx") #打开2020年每个月的销售情况表

sum = 0

a = 0
sum1 = 0

b = 0
sum2 = 0

c = 0
sum3 = 0

d = 0
sum4 = 0

e = 0
sum5 = 0

f = 0
sum6 = 0

g = 0
sum7 = 0

h = 0
sum8 = 0

j = 0
sum9 = 0

k = 0
sum10 = 0

l = 0
sum11 = 0

m = 0
sum12 = 0

n = 0
sum13 = 0

xiaoliang = 0

for i in range(0,12):
    sheet = wd.sheet_by_index(i)
    cols = sheet.ncols
    rows = sheet.nrows

    for x in range(1,rows):                 # 让i进行1到行数的遍历 从索引为1的地方开始
        data = sheet.row_values(x)
        sum = sum + data[2] * data[4]
        xiaoliang = xiaoliang + data[4]
        if data[1] == '羽绒服':
            a = a + data[4]                     #销量
            sum1 = sum1 + data[2] * data[4]       #销售额
        if data[1] == '牛仔裤':
            b = b + data[4]
            sum2 = sum2 + data[2] * data[4]
        if data[1] == '风衣':
            c = c + data[4]
            sum3 = sum3 + data[2] * data[4]
        if data[1] == '皮草':
            d = d + data[4]
            sum4 = sum4 + data[2] * data[4]
        if data[1] == 'T血':
            e = e + data[4]
            sum5 = sum5 + data[2] * data[4]
        if data[1] == '马甲':
            f = f + data[4]
            sum6 = sum6 + data[2] * data[4]
        if data[1] == '小西装':
            g = g + data[4]
            sum7 = sum7 + data[2] * data[4]
        if data[1] == '皮衣':
            h = h + data[4]
            sum8 = sum8 + data[2] * data[4]
        if data[1] == '休闲裤':
            j = j + data[4]
            sum9 = sum9 +data[2] * data[4]
        if data[1] == '衬衫':
            k = k + data[4]
            sum10 = sum10 + data[2] * data[4]
        if data[1] == '卫衣':
            l = l + data[4]
            sum11 = sum11 + data[2] * data[4]
        if data[1] == '棉衣':
            m = m+data[4]
            sum12 = sum12 + data[2] * data[4]
        if data[1] == '铅笔裤':
            n = n + data[4]
            sum13 = sum13 + data[2] * data[4]

print("全年销售总额：￥",round(sum,2))
print("羽绒服全年销售量占比：",str(round(a / xiaoliang * 100,2))+'%')
print('羽绒服全年销售额占比:',str(round(sum1 / sum * 100,2))+'%')
print('牛仔裤全年销售量占比:',str(round(b / xiaoliang * 100 ,2))+'%')
print('牛仔裤全年销售额占比:',str(round(sum2 / sum * 100,2))+'%')
print('风衣全年销售量占比:',str(round(c / xiaoliang * 100,2))+'%')
print('风衣全年销售额占比:',str(round(sum3 / sum * 100,2 ))+'%')
print('皮草全年销售量占比:',str(round(d / xiaoliang * 100,2))+'%')
print('皮草全年销售额占比:',str(round(sum4 / sum * 100,2))+'%')
print('T血全年销售量占比:',str(round(e / xiaoliang * 100,2))+'%')
print('T血全年销售额占比:',str(round(sum5 / sum * 100,2))+'%')
print('马甲全年销售量占比:',str(round(f / xiaoliang * 100,2))+'%')
print('马甲全年销售额占比:',str(round(sum6 / sum * 100 ,2))+'%')
print('小西装全年销售量占比:',str(round(g / xiaoliang * 100,2))+'%')
print('小西装全年销售额占比:',str(round(sum7 /sum * 100,2))+'%')
print('皮衣全年销售量占比:',str(round(h / xiaoliang * 100,2))+'%')
print('皮衣全年销售额占比:',str(round(sum8 / sum * 100,2))+'%')
print('休闲裤全年销售量占比:',str(round(j / xiaoliang * 100,2))+'%')
print('休闲裤全年销售额占比:',str(round(sum9 / sum * 100,2))+'%')
print('衬衫全年销售量占比:',str(round(k / xiaoliang * 100,2))+'%')
print('衬衫全年销售额占比:',str(round(sum10 / sum * 100,2))+'%')
print('卫衣全年销售量占比:',str(round(l / xiaoliang * 100,2))+'%')
print('卫衣全年销售额占比:',str(round(sum11 /sum * 100,2))+'%')
print('棉衣全年销售量占比:',str(round(m / xiaoliang * 100,2))+'%')
print('棉衣全年销售额占比:',str(round(sum12 / sum * 100,2))+'%')
print('铅笔裤全年销售量占比:',str(round(n / xiaoliang * 100,2))+'%')
print('铅笔裤全年销售额占比:',str(round(sum13 / sum * 100,2))+'%')









