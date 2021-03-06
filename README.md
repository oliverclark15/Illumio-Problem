# Illumio-Problem

The constructor stores the rules (from CSV) in a dictionary with 4 keys and list values. The 4 keys are inbound-tcp, inbound-udp, outbound-tcp, and outbound-udp. Since the number of combinations of direction & protocol is finite, this is done to eliminate checking over rules that do not apply to the packet in question. This effectively eliminates 75% of the rules to check (assuming equal distribution over the 4 direction & protocol pairings).

The accept packet function simply iterates over all the rules applicable to the packet in question (according to the dir-protocol pair). It checks if the rule contains a "-" character, if yes -> it checks if the port/ip-addr falls in the range, if no -> checks equality. Immediately returns true if it finds a match and returns false after iterating over all the applicable rules without finding a match.

With further time I would like to improve the checking for when the rules contain ranges. This could be done by (in the constructor) replacing overlapping ranges with one range (replacing [1,1000] and [5,2400] with [1,2400]). Additionally, some constructor overhead could be added to sort the rules according to either port or ip-addr in order to improve runtimes.

I tested my program with what I deemed to be edge cases and standard cases. In order to check performance, I compared runtime for varying amounts of rules and determined that runtime increases roughly linearly with the number of rules in the csv (however this depends on the number of ranges in the rules).

## Team Interests
I am hugely interested in all three teams, however, if I had to choose I would select the Data team followed by the Policy team followed by the Platform team.


