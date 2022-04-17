from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector


def compute_gini(model):
    agent_wealths = [agent.wealth for agent in model.schedule.agents]
    x = sorted(agent_wealths) # 排序
    N = model.num_agents
    B = sum(xi * (N - i) for i, xi in enumerate(x)) / (N * sum(x))
    return 1 + (1 / N) - 2 * B

class MoneyAgent(Agent):
    # An agent with fixed initial wealth.
    # 通过构造方法定义类的属性
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.wealth = 1
    # 定义类的方法
    def step(self):
        # use grid
        self.move()
        if self.wealth > 0:
            self.give_money()
    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            # Return a list of cells that are in the neighborhood of a certain point.
            # moore: Boolean for whether to use Moore neighborhood (including
            # diagonals) or Von Neumann (only up/down/left/right).
            self.pos,
            moore=True,
            include_center=False) # 返回除(x,y)之外的其他节点，
        new_position = self.random.choice(possible_steps) # 返回一个list，从中随机选择一个
        self.model.grid.move_agent(self, new_position)

    def give_money(self):
        cellmates = self.model.grid.get_cell_list_contents([self.pos])
        if len(cellmates) > 1:
            other = self.random.choice(cellmates)
            other.wealth += 1
            self.wealth -= 1

class MoneyModel(Model):
    """A model with some number of agents."""
    def __init__(self, N, width, height):
        """
        Create a new model. Overload this method with the actual code to
                start the model.
        Attributes:
            schedule: schedule object 调度对象
            running: a bool indicating if the model should continue running
        :param N:
        """
        self.num_agents = N
        self.grid = MultiGrid(width, height, True)
        # Activates all the agents once per step, in random order.
        self.schedule = RandomActivation(self)
        self.running = True

        # Creat Agents
        for i in range(self.num_agents):
            # 实例化——通过类得到对象MoneyAgent
            a = MoneyAgent(i, self)
            self.schedule.add(a)
            # add the agents to random grid cell
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            # an agent and an (x, y) tuple of the coordinates to place the agent.
            self.grid.place_agent(a, (x, y))

        self.datacollector = DataCollector(
            model_reporters={"Gini": compute_gini}, agent_reporters={"Wealth": "wealth"}
        )

    def step(self):
        """Advance the model by one step."""
        self.datacollector.collect(self)
        self.schedule.step()
        """
        At every step of the model, the datacollector will collect and store the model-level current Gini coefficient, 
        as well as each agent’s wealth, associating each with the current step.
        """


