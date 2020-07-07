import json

DEFAULT_CONFIG = {
	"keylayout": 'default'
}

global config
try:
	with open("./config.json") as fp:
		config = json.load(fp)
except:
	try:
		with open("./config.json", "w") as fp:
			json.dump(DEFAULT_CONFIG, fp)
	except:
		pass
	config = DEFAULT_CONFIG

def get_config_option(key):
	if key in config.keys():
		return config[key]
	else:
		return None

# controls options are: default (wasd), azerty (zqsd)
# other control options must be added manually in constants.py
