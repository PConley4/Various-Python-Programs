import random

shiny = 0
resets = 0
time = 0

while shiny != 1:
    shiny = random.randrange(1, 8192)
    resets += 1
    time += 0.5

print("Getting a shiny Jirachi took %s resets and %s hours (%s days)." % (
                                                    (resets, time, time/24)))
