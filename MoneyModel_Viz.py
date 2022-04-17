from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from Collect_Data import *
from mesa.visualization.modules import ChartModule

def agent_portrayal(agent):
    portrayal = {"Shape": "circle",
                 "Filled": "true",
                 "r": 0.5}
    if 0 < agent.wealth < 2:
        portrayal["Color"] = "red"
        portrayal["Layer"] = 0
    elif 1 < agent.wealth < 3:
        portrayal["Color"] = "green"
        portrayal["Layer"] = 0
    elif 2 < agent.wealth < 4:
        portrayal["Color"] = "blue"
        portrayal["Layer"] = 0
    elif 3 < agent.wealth:
        portrayal["Color"] = "purple"
        portrayal["Layer"] = 0
    else:
        portrayal["Color"] = "grey"
        portrayal["Layer"] = 1
        portrayal["r"] = 0.2
    return portrayal

grid = CanvasGrid(agent_portrayal, 10, 10, 500, 500)
# 10*10 grid  500*500 pixel

chart = ChartModule([{"Label": "Gini", # which must match the name of a model-level variable collected by the DataCollector
                      "Color": "Black"}],
                    data_collector_name='datacollector')

server = ModularServer(MoneyModel,
                       [grid, chart],
                       "Money Model",
                       {"N":100, "width":10, "height":10})
                        # 100 agents
server.port = 8521 # The default
server.launch()