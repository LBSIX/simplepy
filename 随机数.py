import random
def main():
    print('1、数字\n2、字母\n3、汉字\n4、数字、字母\n5、数字、汉字\n6、字母、汉字\n7、数字、字母、汉字\n')
    i=int(input('输入分类对应的数字：\n'))
    n1=int(input('随机数个数='))
    n2=int(input('随机数长度='))
    if i==1:
        while True:
            name=''.join(random.choice(snum) for _ in range(n2))
            if name not in l:
                print(name)
                l.append(name)
                if len(l)==n1:
                    break
    elif i==2:
        while True:
            name=''.join(random.choice(slet) for _ in range(n2))
            if name not in l:
                print(name)
                l.append(name)
                if len(l)==n1:
                    break
    elif i==3:
        while True:
            name=random.choice(xing)+''.join(random.choice(ming) for i in range(n2-1))
            if name not in l:
                print(name)
                l.append(name)
                if len(l)==n1:
                    break
    elif i==4:
        while True:
            name=''.join(random.choice(snl) for _ in range(n2))
            if name not in l:
                print(name)
                l.append(name)
                if len(l)==n1:
                    break
    elif i==5:
        while True:
            xm=random.choice(xing)+''.join(random.choice(ming) for i in range(random.randint(1,2)))
            tmp=list(''.join(random.choice(snum) for _ in range(n2-len(xm))))
            xm=xm.split()
            xm.extend(tmp)
            random.shuffle(xm)
            name=''.join(xm)
            if name not in l:
                print(name)
                l.append(name)
                if len(l)==n1:
                    break
    elif i==6:
        while True:
            xm=random.choice(xing)+''.join(random.choice(ming) for i in range(random.randint(1,2)))
            tmp=list(''.join(random.choice(slet) for _ in range(n2-len(xm))))
            xm=xm.split()
            xm.extend(tmp)
            random.shuffle(xm)
            name=''.join(xm)
            if name not in l:
                print(name)
                l.append(name)
                if len(l)==n1:
                    break
    elif i==7:
        while True:
            xm=random.choice(xing)+''.join(random.choice(ming) for i in range(random.randint(1,2)))
            tmp=list(''.join(random.choice(snl) for _ in range(n2-len(xm))))
            xm=xm.split()
            xm.extend(tmp)
            random.shuffle(xm)
            name=''.join(xm)
            if name not in l:
                print(name)
                l.append(name)
                if len(l)==n1:
                    break
l=[]
snum='0123456789'
slet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
snl='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
xing='赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛'\
    '奚范彭郎鲁韦昌马苗凤花方俞任袁柳酆鲍史唐费廉岑薛雷贺倪汤滕殷罗毕郝邬安常乐于时傅皮卞齐康'\
    '伍余元卜顾孟平黄和穆萧尹姚邵湛汪祁毛禹狄米贝明臧计伏成戴谈宋茅庞熊纪舒屈项祝董梁杜阮蓝闵'\
    '席季麻强贾路娄危江童颜郭梅盛林刁钟徐邱骆高夏蔡田樊胡凌霍虞万支柯昝管卢莫经房裘缪干解应宗'\
    '丁宣贲邓郁单杭洪包诸左石崔吉钮龚程嵇邢滑裴陆荣翁荀羊於惠甄曲家封芮羿储靳汲邴糜松井段富巫'\
    '乌焦巴弓牧隗山谷车侯宓蓬全郗班仰秋仲伊宫宁仇栾暴甘钭厉戎祖武符刘景詹束龙叶幸司韶郜黎蓟薄'\
    '印宿白怀蒲邰从鄂索咸籍赖卓蔺屠蒙池乔阴鬱胥能苍双闻莘党翟谭贡劳逄姬申扶堵冉宰郦雍卻璩桑桂'\
    '濮牛寿通边扈燕冀郏浦尚农温别庄晏柴瞿阎充慕连茹习宦艾鱼容向古易慎戈廖庾终暨居衡步都耿满弘'\
    '匡国文寇广禄阙东欧殳沃利蔚越夔隆师巩厍聂晁勾敖融冷訾辛阚那简饶空曾毋沙乜养鞠须丰巢关蒯相'\
    '查后荆红游竺权逯盖益桓公万俟司马上官欧阳夏侯诸葛闻人东方赫连皇甫尉迟公羊澹台公冶宗政濮阳'\
    '淳于单于太叔申屠公孙仲孙轩辕令狐钟离宇文长孙慕容鲜于闾丘司徒司空丌官司寇仉督子车颛孙端木'\
    '巫马公西漆雕乐正壤驷公良拓跋夹谷宰父谷梁晋楚闫法汝鄢涂钦段干百里东郭南门呼延归海羊舌微生'\
    '岳帅缑亢况郈有琴梁丘左丘东门西门商牟佘佴伯赏南宫墨哈谯笪年爱阳佟第五言福'
ming='伟刚勇毅俊峰强军平保东文辉力明永健世广志义兴良海山仁波宁贵福生龙元全国胜学祥才发武新利清'\
    '飞彬富顺信子杰涛昌成康星光天达安岩中茂进林有坚和彪博诚先敬震振壮会思群豪心邦承乐绍功松善'\
    '厚庆磊民友裕河哲江超浩亮政谦亨奇固之轮翰朗伯宏言若鸣朋斌梁栋维启克伦翔旭鹏泽晨辰士以建家'\
    '致树炎德行时泰盛秀娟英华慧巧美娜静淑惠珠翠雅芝玉萍红娥玲芬芳燕彩春菊兰凤洁梅琳素云莲真环'\
    '雪荣爱妹霞香月莺媛艳瑞凡佳嘉琼勤珍贞莉桂娣叶璧璐娅琦晶妍茜秋珊莎锦黛青倩婷姣婉娴瑾颖露瑶'\
    '怡婵雁蓓纨仪荷丹蓉眉君琴蕊薇菁梦岚苑筠柔竹霭凝晓欢霄枫芸菲寒欣滢伊亚宜可姬舒影荔枝思丽秀'\
    '飘育馥琦晶妍茜秋珊莎锦黛青倩婷宁蓓纨苑婕馨瑗琰韵融园艺咏卿聪澜纯毓悦昭冰爽琬茗羽希'
main()
while True:
    i=input('是否继续？q：退出，其它：继续\n')
    if i=='q':
        break
    else:
        l=[]
        main()