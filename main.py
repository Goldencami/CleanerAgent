from Environment import Environment
from Sensors import Sensors
from Actuators import Actuator
from Agent import Agent

env = Environment(3)
sensors = Sensors(env)
actuators = Actuator(env)
agent = Agent(sensors, actuators)

env.display()
agent.run()