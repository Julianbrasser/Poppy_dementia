from poppy.creatures import PoppyTorso
import json

my_robot = autodetect_robot()

for m in my_robot.motors:
    m.goal_position = 0.0

config = my_robot.to_config()

with open('my_robot.json', 'wb') as f:
    json.dump(config, f)

my_robot = from_json('my_robot.json')

