#!/usr/bin/env python

import snmp_helper

ipaddr = '184.105.247.70'
port = '161'
auth_key = 'galileo1'
encrypt_key = 'galileo1'

user = 'pysnmp'

snmp_user = (user, auth_key, encrypt_key)

rtr1 = (ipaddr, port)

oids = ('1.3.6.1.2.1.1.5.0', '1.3.6.1.2.1.1.1.0','1.3.6.1.2.1.1.3.0','1.3.6.1.2.1.2.2.1.2.5')

for oid in oids:
    snmp_data = snmp_helper.snmp_get_oid_v3(rtr1, snmp_user, oid)
    snmp_output = snmp_helper.snmp_extract(snmp_data)
    print snmp_output

