import config
SIZE = 400
GRID_LEN = 4
GRID_PADDING = 10

BACKGROUND_COLOR_GAME = "#92877d"
BACKGROUND_COLOR_CELL_EMPTY = "#9e948a"

BACKGROUND_COLOR_DICT = {2: "#eee4da", 4: "#ede0c8", 8: "#f2b179",
                         16: "#f59563", 32: "#f67c5f", 64: "#f65e3b",
                         128: "#edcf72", 256: "#edcc61", 512: "#edc850",
                         1024: "#edc53f", 2048: "#edc22e",

                         4096: "#eee4da", 8192: "#edc22e", 16384: "#f2b179",
                         32768: "#f59563", 65536: "#f67c5f", }

CELL_COLOR_DICT = {2: "#776e65", 4: "#776e65", 8: "#f9f6f2", 16: "#f9f6f2",
                   32: "#f9f6f2", 64: "#f9f6f2", 128: "#f9f6f2",
                   256: "#f9f6f2", 512: "#f9f6f2", 1024: "#f9f6f2",
                   2048: "#f9f6f2",

                   4096: "#776e65", 8192: "#f9f6f2", 16384: "#776e65",
                   32768: "#776e65", 65536: "#f9f6f2", }

FONT = ("Verdana", 40, "bold")
# default controls
if config.controls() == 'default':
	KEY_UP = "'w'"
	KEY_DOWN = "'s'"
	KEY_LEFT = "'a'"
	KEY_RIGHT = "'d'"
	KEY_BACK = "'b'"
elif config.controls() == 'azerty':
	KEY_UP = "'z'"
	KEY_DOWN = "'s'"
	KEY_LEFT = "'q'"
	KEY_RIGHT = "'d'"
	KEY_BACK = "'b'"
# vim controls
elif config.controls() == 'vim':
	KEY_UP = "'k'"
	KEY_DOWN = "'j'"
	KEY_LEFT = "'h'"
	KEY_RIGHT = "'l'"
	KEY_BACK = "'b'"
# why
elif config.controls() == 'why':
	KEY_UP = "'1'"
	KEY_DOWN = "'.'"
	KEY_LEFT = "'='"
	KEY_RIGHT = "'7'"
	KEY_BACK = "'b'"
# elif config.controls() == 'your control name here'
	# KEY_UP = "'key1'"
	# KEY_UP = "'key2'"
	# KEY_UP = "'key3'"
	# KEY_UP = "'key4'"
# will use default if nothing is in the return value of controls
else:
	KEY_UP = "'w'"
	KEY_DOWN = "'s'"
	KEY_LEFT = "'a'"
	KEY_RIGHT = "'d'"
	KEY_BACK = "'b'"

