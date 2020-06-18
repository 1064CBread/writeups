# Good Plan? Great Plan!
## Challenge
Given a satellite TLE, a point target, a ground station, and a 48-hour time window, schedule mode transitions such that 120MB of captured data are downlinked and the spacecraft survives the entire duration.

There are 4 modes:
* sun_point, for charging batteries
* imaging, for imaging the target
* data_downlink, for downlinking data to the ground station
* wheel_desaturate, for desaturating reaction wheels

The challenge only requires UTC time stamps and mode transitions; you do not need to find the spacecraft attitude needed for the modes. Also assume that mode transitions are instantaneous. Mode transitions must occur at 1-minute intervals (ie when seconds is 00). Any mode may transition to any other mode.

## A very unscientific manual trial-and-error approach
First, I generated visibility intervals for the target and the ground station with this convenient Python package (https://rhodesmill.org/skyfield), assuming minimum elevation angle of 30 degrees for no particular reason. With imaging and downlink intervals in place, I filled in the remaining time with sun_point. I then submitted a schedule of the transitions between mode intervals.

Upon submitting a proposed schedule, the simulator runs and prints out relevant state at one-minute intervals (eg reaction wheel RPM, battery levels, component temperature, etc). At the end, it outputs either success, or the first thing that caused failure. Possible failure reasons include:

* Target was not visible during imaging mode
* Target was not illuminated by the Sun during imaging mode
* Ground station was not visible during downlink mode
* Battery fell below 10% capacity
* Imager temperature too high
* Comms temperature too high
* Reaction wheels saturated
* Did not collect and downlink enough data

After submitting this preliminary schedule, which failed, I removed imaging passes that were not illuminated. (I suppose I could have filtered them out in the previous step when generating visibility intervals, but I didn't).

The reaction wheels will saturate over time, so I added wheel_desaturates as needed. The imager and comms will drain battery and overheat if left on for too long, so I shortened those intervals as needed.

When I finally got to the end of the 48-hour window without breaking the spacecraft, the schedule failed because it didn't collect enough data. I was puzzled because it seemed like there weren't enough overflights to do so, when I realized that I had arbitrarily assumed a minimum elevation angle of 30 degrees. It turns out that the minimum elevation angle was more like 0.

Adding in some more imaging and downlink intervals with lower elevation angle, I managed to generate a successful schedule, and was rewarded with cute ASCII art of a satellite and the flag.

In conclusion, doing squeaky wheel scheduling by hand really makes me appreciate the existence of automated planning and scheduling.

Final schedule:
```
2020-04-22T00:00:00Z sun_point
2020-04-22T09:29:00Z imaging
2020-04-22T09:35:00Z sun_point
2020-04-22T10:47:00Z data_downlink
2020-04-22T10:52:00Z sun_point
2020-04-22T11:07:00Z imaging
2020-04-22T11:08:00Z sun_point
2020-04-22T18:00:00Z wheel_desaturate
2020-04-22T19:00:00Z sun_point
2020-04-22T22:22:00Z data_downlink
2020-04-22T22:27:00Z sun_point
2020-04-23T00:00:00Z data_downlink
2020-04-23T00:03:00Z sun_point
2020-04-23T07:00:00Z wheel_desaturate
2020-04-23T08:00:00Z sun_point
2020-04-23T09:33:00Z data_downlink
2020-04-23T09:35:00Z sun_point
2020-04-23T09:50:00Z imaging
2020-04-23T09:57:00Z sun_point
2020-04-23T11:12:00Z data_downlink
2020-04-23T11:14:00Z sun_point
2020-04-23T15:00:00Z wheel_desaturate
2020-04-23T16:00:00Z sun_point
2020-04-23T22:44:00Z data_downlink
2020-04-23T22:48:00Z sun_point
```

Relevant [code](good_plan_great_plan.py)