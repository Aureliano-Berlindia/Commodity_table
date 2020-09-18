# 🛠爬虫商品展示初版
   *Commodity Table Demo*

## 📊展示一列商品。

---
<img src="https://raw.githubusercontent.com/Aureliano-Berlindia/Commodity_table/master/demo_gif.gif" align="right">


1.  *jupyterLab* 环境编写，生产环境内请使用[commodity.py](https://github.com/Aureliano-Berlindia/Commodity_table/blob/master/commodity.py)

2.  数据源在Excel文件内，**保持格式不变**。 `后续视实际数据更新代码`

3.  网页展示效果请访问 [Demo](http://wberlin.cn:9999)  `更新可能不及时`

---

## 💎目前功能

* 通过`Brand`筛选`Country`选项列表，反之亦然
* 通过`Brand` & `Country` 筛选`Model`列表
* **Model callback**中使用`Brand`,`Country`,`Model`确定唯一商品，展示在第一列
* 设置初始显示商品
* 在选中指定商品后再选择All，目前显示商品不变
