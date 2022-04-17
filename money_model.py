from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid

class MoneyAgent(Agent):
    # An agent with fixed initial wealth.
    # 通过构造方法定义类的属性
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.wealth = 1
    # 定义类的方法
    def step(self):
        """
        # The agent's step will go here.
        # For demonstration purposes we will print the agent's unique_id

        if self.wealth == 0:
            return
        other_agent = self.random.choice(self.model.schedule.agents)
        other_agent.wealth += 1
        self.wealth -= 1
        print("Hi, I am Agent " + str(self.unique_id) + ", money " + str(self.wealth))
        """
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

    def step(self):
        """Advance the model by one step."""
        self.schedule.step()


# if __name__ == '__main__':
    # print_hi('PyCharm')

