# Talk To Me Goose
## LaunchDotCom has a new satellite, the Carnac 2.0. What can you do with it from its design doc?

For this challenge we have an .xtce defining a telemetry service with a remote "satelite". Upon connecting to the server and submitting the ticket, there was a packet of data approximately every second.

It was fairly clear from the size of the received data that there was no flag hidden within it, so we had to actually implement the protocol defined by the .xtce and by the carnac 2 spec. Rather than create or find a .xtce parser, we manually built packet generators and parsers for all the packets. This can be seen in solution.py as the _decode and make methods.

Once these packet parsers were created and talking to the server via python's socket library, it was then a matter of figuring out what exactly was going on and how to get the flag. This was more or less straight-forward: we needed to enable the flag generator, and to do this we had to conserve enough power to make the EPS think it was safe to turn on. The twist was that disabling everthing to conserve power wasn't enough! Instead we also had to override the low power threshold to force the EPS to leave low power mode.

Our solution involved:
* Disable a Radio
* Disable the payload
* Disable the ADCS
* Enable the flag generator
* Override the Low Power Threshold

One note on the low power threshold - it wasn't clear exactly how to interpret the .xtce's scaling factors. In the end we just fuzzed that parameter until we found the lowest value that was not invalid, which was possible as we could send hundreds of commands per second. Eventually we found that any value over 900 was valid, so picked LowPowerThresh=1000 to be safe and with that we got the flag.

One other note on our solution: Something is slightly off in the flag decoder's algorithm, so we copied some code from our Can You Hear Me? solution that converted from 7-bit characters to ascii and simply printed it that way.

Python [solution](talk_to_me_goose.py)