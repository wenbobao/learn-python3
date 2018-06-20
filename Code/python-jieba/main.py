#!/usr/bin/python
# coding:utf-8

import jieba

# seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
# print("Default Mode: " + "/ ".join(seg_list))

# seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
# print("Default Mode: " + "/ ".join(seg_list))

# seg_list = jieba.cut("我来到北京清华大学")
# print("Default Mode: " + "/ ".join(seg_list))

seg_list = jieba.cut("花园畈海虾肉酱海鲜酱海虾酱香辣椒酱拌饭拌面酱虾酱海南酱宝特产")
print("Default Mode: " + "/ ".join(seg_list))

seg_list = jieba.cut("半身裙")
print("Default Mode: " + "/ ".join(seg_list))

category = "纸巾-居家,厨房用品-居家,家庭清洁-居家,收纳-居家,家纺-居家,家饰-居家,卫浴-居家,宠物-居家,其他-居家,保健品-美食,粮油副食-美食,休闲零食-美食,坚果蜜饯-美食,奶制品-美食,冲饮-美食,糖果-美食,酒-美食,其他-美食,笔-文体,本子-文体,办公-文体,图书-文体,运动装备-文体,健身器械-文体,户外-文体,汽车用品-文体,其他-文体,手机壳-数码,手机膜-数码,耳机-数码,数据线-数码,电脑配件-数码,智能设备-数码,平板配件-数码,生活电器-数码,其他-数码,童装-母婴,童鞋-母婴,玩具-母婴,孕妇用品-母婴,辅食营养-母婴,喂养-母婴,母婴洗护-母婴,婴童出行-母婴,其他-母婴,面膜-美妆,口红-美妆,洁面-美妆,彩妆-美妆,美妆工具-美妆,护肤-美妆,男士护理-美妆,套装-美妆,其他-美妆,男装-服饰,女装-服饰,内衣-服饰,打底裤-服饰,男袜-服饰,女袜-服饰,裙子-服饰,睡衣-服饰,其他-服饰,男鞋-鞋包,女鞋-鞋包,单肩包-鞋包,腰带-鞋包,钱包-鞋包,行李箱-鞋包,拖鞋-鞋包,帽子-鞋包,其他-鞋包"

cateArr = category.split(",")

def cateGory(title):
    for x in cateArr:
        _temArr = x.split("-")
        _splitWord = jieba.cut(_temArr[0].replace("\n", ""), cut_all=False)
        index = 0
        lens = 0

        for x in _splitWord:
            lens += 1

            if x in title:
                name = _temArr[1].replace("\n", "")
                index += 1
        if index == lens:
            return _temArr[0].replace("\n", ""), name
    else:
        return "其他", "其他"


print(cateGory('花园畈海虾肉酱海鲜酱海虾酱香辣椒酱拌饭拌面酱虾酱海南酱宝特产'))