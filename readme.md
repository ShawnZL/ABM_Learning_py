# Mesa

## Space

### Grid

划分为单元格，代理只能在特定的单元格上，像棋盘上的棋子。

### Continuous

连续空间运行节点在任意位置。

网格和连续空间通常都是环形的，这意味着边缘环绕，右边缘的单元格连接到左边缘的单元格，顶部到底部。 这可以防止某些小区的邻居比其他小区少，或者代理能够离开环境的边缘。



[Building your own visualization component](https://mesa.readthedocs.io/en/latest/tutorials/adv_tutorial.html#adding-visualization)

## Best Practices

### Model Layout

`model.py` should contain the model class. If the file gets large, it may make sense to move the complex bits into other files, but this is the first place readers will look to figure out how the model works.

`server.py` should contain the visualization support, including the server class.

`run.py` is a Python script that will run the model when invoked via `mesa runserver`.