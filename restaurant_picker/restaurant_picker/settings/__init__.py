from restaurant_picker.settings.base import *

try:
    from restaurant_picker.settings.local import *
    _live = False
except ImportError:
    _live = True

if _live:
    from restaurant_picker.settings.prod import *