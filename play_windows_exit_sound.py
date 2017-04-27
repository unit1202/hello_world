# To play a sound in Windows we need to import the winsound module
# The winsound module provides access to the basic sound-playing 
# machinery provided by Windows platforms. It includes functions 
# and several constants.

# Link: https://docs.python.org/3/library/winsound.html#module-winsound

import winsound
# Play Windows exit sound.
winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
