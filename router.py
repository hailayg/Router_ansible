#!/usr/bin/env python3
#import sys
#import json
#import subprocess
import openstack
#import os

key = 'key'
edge_router1= 'hqEdgeRouter'
edge_router2= 'branchEdgeRouter'
router1 ='hqInternalRouter1'
router2 ='hqInternalRouter2'
router3 ='branchInternalRouter1'
router4 ='branchInternalRouter2'

network1 ='HQ_network'
network2 ='Branch_network'
#network3 ='ISP_network'

hq_sub1 = 'HQ_sub_1'
hq_sub2 = 'HQ_sub_2'

edge_sub1= 'edge_sub1'
edge_sub2 = 'edge_sub2'

node = 'node'

#Network and Subnets
conn = openstack.connect()
Hq_net = conn.network.create_network(name=network1)
HQ_subnet1 = conn.network.create_subnet(network_id=Hq_net.id, name=hq_sub1, cidr="10.1.0.0/30", ip_version=4)
HQ_subnet2 = conn.network.create_subnet(network_id=Hq_net.id, name=hq_sub2, cidr="10.1.0.4/30", ip_version=4)

edge_net = conn.network.create_network(name=network2)
Edge_subnet1 = conn.network.create_subnet(network_id=edge_net.id, name=edge_sub1, cidr="20.1.0.0/30", ip_version=4)
Edge_subnet2 = conn.network.create_subnet(network_id=edge_net.id, name=edge_sub2, cidr="20.1.0.4/30", ip_version=4)

#Routers
HQ_router = conn.network.create_router(name=edge_router1)
HQ_router1 = conn.network.create_router(name=router1)
HQ_router2 = conn.network.create_router(name=router2)
Edge_router = conn.network.create_router(name=edge_router2)
Br_router1 = conn.network.create_router(name=router3)
Br_router2 = conn.network.create_router(name=router4)







