from skyfield.api import EarthSatellite, Topos, load
import math
import numpy

ts = load.timescale(builtin=True)

satname = "USA 224"
line1 = "1 37348U 11002A   20053.50800700  .00010600  00000-0  95354-4 0    09"
line2 = "2 37348  97.9000 166.7120 0540467 271.5258 235.8003 14.76330431    04"
satellite = EarthSatellite(line1, line2, satname, ts)

st = ts.utc(2020, 4, 22, 0, 0, 0)
et = ts.utc(2020, 4, 24, 0, 0, 0)

#visibility intervals
target = Topos('35.234722 N', '53.920833 E')
t, events = satellite.find_events(target, st, et, altitude_degrees=0.0)
print("Target visibility intervals")
for ti, event in zip(t, events):
    name = ('rise', 'culminate', 'set')[event]
    print(ti.utc_jpl(), name)

#downlink intervals
gs = Topos('64.977488 N', '147.510697 W')
t, events = satellite.find_events(gs, st, et, altitude_degrees=5.0)
print("Ground station passes")
for ti, event in zip(t, events):
    name = ('rise', 'culminate', 'set')[event]
    print(ti.utc_jpl(), name)