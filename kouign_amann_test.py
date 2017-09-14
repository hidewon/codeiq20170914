#! /usr/bin/env python

# -*- coding:utf-8 -*-

import itertools
import sys

def add_fee(combo):
	global limit_days
	global limit_days_payments

	for mini_combo in combo:
		pay_day=mini_combo.split(",")
		pay=pay_day[0]	
		day=pay_day[1]
		limit_days+=int(day)
		if limit_days < 100:
			limit_days_payments+=int(pay)
			fee[limit_days_payments]=limit_days
		else:
			return 0	

fee={}
orders=[]
for line in sys.stdin:
	line=line.rstrip('\r\n')
	orders.append(line)

#combo_s=8
combo_s=len(orders)+1
#sys.exit(1)

for i in range(1,combo_s):
	c=list(itertools.combinations(orders,i))

	for combo in c:
		limit_days=0
		limit_days_payments=0
		add_fee(combo)

fees=sorted(fee.items(),reverse=True,key=lambda x: x[0])
print fees[0][0]
