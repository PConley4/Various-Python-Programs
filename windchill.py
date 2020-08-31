import math

print 'This will calulate the wind chill of the area. Type in the current temperature.'

CT = raw_input()

print 'Entered %s' % (CT)

print 'Now type in the wind speed.'

WS = raw_input()

print 'Entered %s' % (WS)

WC = (35.74 + .6215) *float(CT) - (35.75) *(float(WS)**.16) + (.4275) * (float(WS)**.16) + (.4275)*float(CT)*(float(WS)**.16)

print 'Your wind chill is %s' % round(WC,2)
