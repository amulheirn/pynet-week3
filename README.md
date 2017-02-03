# pynet-week3
Week 3 exercises


*snmp.py* simply retrieves a few OIDs over snmp using Kirk Byers' snmp_helper library.

*interfaces.py* gets a variety of OIDs from fa4 of a Cisco router/

*poll_ints.py* retrieves input bytes on fa4 6 times.  It puts the values it gets into a list. 
It then uses pygal library to create an SVG graph of the data and writes it to fa4.svg
