# ✨爬虫商品展示初版
   *Commodity Table Demo，still developing*
   
---

## 💎目前功能:

* 通过`Brand`筛选`Country`选项列表，反之亦然
* 通过`Brand` & `Country` 筛选`Model`列表
* **Model callback**中使用`Brand`,`Country`,`Model`确定唯一商品，展示在第一列
* 设置初始显示商品
* 在选中指定商品后再选择All，目前显示商品不变

---

## 🚧注意事项：


1.  *jupyterLab* 环境编写，生产环境内请使用[commodity.py](https://github.com/Aureliano-Berlindia/Commodity_table/blob/master/commodity.py)

2.  数据源在Excel文件内，**保持格式不变**。 `后续视实际数据更新代码`

3.  网页展示效果请访问 [Demo](http://wberlin.cn:9999)  

4.  代码更新以[Commodity_table.ipynb](https://github.com/Aureliano-Berlindia/Commodity_table/blob/master/commodity_table.ipynb)为准, py文件和网页Demo更新可能不及时

---

## 🚀Updates:
```
 9.18 fix the bug that dropdown shows 'undefined' in some situations.
 
 9.19 add feature: now the table could select & display two commodities at once.
      add feature: edit Font/size/family
      
 9.21 add feature: add 'show_more' option, now the table only display 10 rows by default.
```

---

## 👀使用演示

**基于JupyterLab**

`GIF图无法显示请使用VPN`

<img src="https://raw.githubusercontent.com/Aureliano-Berlindia/Commodity_table/master/demo_gif.gif" align="center">
