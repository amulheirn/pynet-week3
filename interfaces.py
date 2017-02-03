#!/usr/bin/env python

# import Kirk's snmp helper lib
import snmp_helper

# Set a few constants
community = 'galileo'
rtr1 = '184.105.247.70'
port = '161'

# Create a tuple of device, community and port.
# This tuple will be usd by snmp_helper.snmp_get_oid function

device = (rtr1, community, port)


# Here are the OIDs we're going to get.  This is a 
# tuple of tuples.
# First field is a human-readable thing, second is OID
# third is whether the OID is a counter object or not

snmp_oids = (
    ('sysName', '1.3.6.1.2.1.1.5.0', None),
    ('ifDescr_fa4', '1.3.6.1.2.1.2.2.1.2.5', None),
    ('ifInOctets_fa4', '1.3.6.1.2.1.2.2.1.10.5', True),
    ('ifOutOctets_fa4', '1.3.6.1.2.1.2.2.1.16.5', True)
)


# Now loop through snmp_oids:
for name,an_oid,is_count in snmp_oids:
    # get the current OID for the device and put it in snmp_data
    snmp_data = snmp_helper.snmp_get_oid(device,oid=an_oid)
    # Now use the snmp_extract function to get human-readable text
    output = snmp_helper.snmp_extract(snmp_data)
    print name + " : " + output
