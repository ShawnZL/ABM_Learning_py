#from money_model import *
from Collect_Data import *
from mesa.batchrunner import batch_run
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

if __name__ == '__main__':
    """
    # create 10 agents
    all_wealth = []
    # This runs the model 100 times, each model executing 10 steps.
    for j in range(100):
        # Run model
        model = MoneyModel(10) # 创建10个agent
        for i in range(10):
            model.step()

        # store the result
        for agent in model.schedule.agents:
            all_wealth.append(agent.wealth)
    plt.hist(all_wealth, bins=range(max(all_wealth) + 1))
    plt.show()
    """
    """
    # model with 50 agents on a 10x10 grid, and run it for 20 steps.
    model = MoneyModel(50, 10, 10)
    for i in range(100):
        model.step()
    agent_counts = np.zeros((model.grid.width, model.grid.height))
    #  every cell in the grid
    for cell in model.grid.coord_iter():
        cell_content, x, y = cell # 得到每一个格子中，含有的数目信息，位置信息！
        agent_count = len(cell_content)
        agent_counts[x][y] = agent_count
    gini = model.datacollector.get_model_vars_dataframe()
    gini.plot()
    plt.show()
    agent_wealth = model.datacollector.get_agent_vars_dataframe()
    # agent_wealth.to_csv('')
    print(agent_wealth.to_csv())
    # 99步目前钱财数据
    end_wealth = agent_wealth.xs(99, level="Step")["Wealth"]
    end_wealth.hist(bins=range(agent_wealth.Wealth.max() + 1))
    plt.show()
    # 编号14的在100步内的情况
    one_agent_wealth = agent_wealth.xs(14, level="AgentID")
    one_agent_wealth.Wealth.plot()
    plt.show()
    """
    params = {"width": 10, "height": 10, "N": range(10, 500, 10)} # N 永远指代数量， N从(10-500)每隔10取一次数据
    # 49 次N 的变换
    results = batch_run(
        MoneyModel,
        parameters=params,
        iterations=5, # 5次迭代
        max_steps=100, # 每一个模型最大运行100次
        number_processes=None,
        data_collection_period=1, # 每一步一个结果
        display_progress=True,
    )
    # print(type(results)) # list
    results_df = pd.DataFrame(results)
    # print(results_df)
    # print(type(results_df)) # pandas.core.frame.DataFrame
    # print(results_df.keys())
    """
        Index(['RunId', 'iteration', 'Step', 'width', 'height', 'N', 'Gini', 'AgentID','Wealth'],
        dtype='object')
    """
    """
    # 编号ID 0 step 100
    results_filtered = results_df[(results_df.AgentID == 0) & (results_df.Step == 100)]
    N_values = results_filtered.N.values
    gini_values = results_filtered.Gini.values
    
        # step of each episode and then scatter-plot the 
        # values for the Gini coefficient over the the number of agents
    
    plt.scatter(N_values, gini_values)
    plt.show()
    """
    """
    # First, we filter the results
    one_episode_wealth = results_df[(results_df.N == 10) & (results_df.iteration == 2)]
    # Then, print the columns of interest of the filtered data frame
    print(one_episode_wealth.to_string(index=False, columns=["Step", "AgentID", "Wealth"]))
    # For a prettier display we can also convert the data frame to html, uncomment to test in a Jupyter Notebook
    # from IPython.display import display, HTML
    # display(HTML(one_episode_wealth.to_html(index=False, columns=['Step', 'AgentID', 'Wealth'], max_rows=25)))
    """
    results_one_episode = results_df[
        (results_df.N == 10) & (results_df.iteration == 1) & (results_df.AgentID == 0)
        ]
    print(results_one_episode.to_string(index=False, columns=["Step", "Gini"], max_rows=25))
