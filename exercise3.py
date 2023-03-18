#!/usr/bin/python
from __future__ import unicode_literals

ipvsix_first = "684D:1111:222:3333:4444:5555:6:77"
IPVSIX_SECOND = "2001:db8:3333:4444:CCCC:DDDD:EEEE:FFFF. ::"
ipv6_3rd = "2001:db8:3333:4444:5555:6666:7777:8888"

if ( ipvsix_first == IPVSIX_SECOND ):
    print("Varible 1 is equal to Variable 2")
else:
    print("Variable 1 is not equal to Variable 2")

if ( ipvsix_first != ipv6_3rd ):
    print("Varible 1 is not equal to Variable 3")
else:
    print("Variable 1 not equal to Variable 2")