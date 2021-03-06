
import math

# *_BORDER_WIDTH is the width INCLUDING the border.
STOKE_BORDER_WIDTH   = 7.5
STOKE_BORDER_COLOR   = "#616161"
STOKE_UNFILLED_COLOR = "#E0E0E0"
STOKE_UNFILLED_WIDTH = 6
STOKE_FILLING_COLOR  = "#00C853"
STOKE_FILLED_COLOR   = "#00C853"
STOKE_FILLED_WIDTH   = 6

# brush settings
SHOW_BRUSH              = True
SHOW_BRUSH_FRONT_BORDER = True
BRUSH_COLOR             = "#00C853"
BRUSH_WIDTH             = 8
BRUSH_BORDER_COLOR      = "#00C853"
BRUSH_BORDER_WIDTH      = 10

WAIT_AFTER = 1.5

# gif settings
DELETE_TEMPORARY_FILES = True
GIF_SIZE               = 150
GIF_FRAME_DURATION     = 0.04
GIF_BACKGROUND_COLOR   = '#EEEEEE'
# set to true to allow transparent background, much bigger file!
GIF_ALLOW_TRANSPARENT  = False

# edit here to decide what will be generated
GENERATE_SVG           = True
GENERATE_JS_SVG        = False
GENERATE_GIF           = False

# sqrt, ie a stroke 4 times the length is drawn
# at twice the speed, in twice the time.
def stroke_length_to_duration(length):
    return math.sqrt(length)/8

# global time rescale, let's make animation a bit
# faster when there are many strokes.
def time_rescale(interval):
    return math.pow(2 * interval, 2.0/3)

# Possibilities are linear, ease, ease-in, ease-in-out, ease-out, see
#   https://developer.mozilla.org/en-US/docs/Web/CSS/timing-function
# for more info.
TIMING_FUNCTION = "ease-in-out"

#
# colorful debug settings
#
#STOKE_BORDER_COLOR   = "#00f"
#STOKE_UNFILLED_COLOR = "#ff0"
#STOKE_FILLING_COLOR  = "#f00"
#STOKE_FILLED_COLOR   = "#000"
#BRUSH_COLOR = "#0ff"
#BRUSH_BORDER_COLOR = "#0f0"
