# 爬虫商品展示初版
   *Commodity Table Demo*

## 通过Brand-Country-Model控制展示商品。

---

*  *jupyterLab* 环境编写，生产环境内请使用[commodity.py](https://github.com/Aureliano-Berlindia/Commodity_table/blob/master/commodity.py)

*  数据源在Excel文件内，**保持格式不变**。 （后续视实际数据更新代码）

*  网页展示效果请访问 [Demo](http://wberlin.cn:9999)

---

## 目前功能

1. 通过Brand筛选Country选项列表，反之亦然
2. 通过Brand & Country 筛选Model列表
3. Model callback中使用Brand,Country,Model确定唯一商品，展示在第一列
4. 设置初始显示商品
5. 在选中指定商品后再选择All，目前显示商品不变
