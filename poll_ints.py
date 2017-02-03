#!/usr/bin/env python

import snmp_helper
import pygal
import time

community = 'galileo'
rtr1 = '184.105.247.70'
port = '161'
inoctets = []

device = (rtr1, community, port)



snmp_oids = (
    ('sysName', '1.3.6.1.2.1.1.5.0', None),
    ('ifDescr_fa4', '1.3.6.1.2.1.2.2.1.2.5', None),
    ('ifInOctets_fa4', '1.3.6.1.2.1.2.2.1.10.5', True),
    ('ifOutOctets_fa4', '1.3.6.1.2.1.2.2.1.16.5', True)
)




counter=0
while counter <= 5:
    for name,an_oid,is_count in snmp_oids:
        snmp_data = snmp_helper.snmp_get_oid(device,oid=an_oid)
        output = snmp_helper.snmp_extract(snmp_data)
        print name + " : " + output
    print "\n"
    output = snmp_helper.snmp_get_oid(device,oid=snmp_oids[2][1])
    temp = int(snmp_helper.snmp_extract(output))
    inoctets.append(temp)
    print inoctets
    counter += 1  
    time.sleep(5)

line_chart = pygal.Line()
line_chart.title = "Input bytes on fa4"
line_chart.x_labels = ['5','10','15','20','25']
line_chart.add('InBytes',inoctets)
line_chart.render_to_file('fa4.svg')


