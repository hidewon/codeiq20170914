#! /usr/bin/env python

# -*- coding:utf-8 -*-

import itertools
import sys

import random

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
			#print str(limit_days_payments)+"\t"+str(fee[limit_days_payments])
		else:
			return 0	

def shrink_orders(orders):
	fees={}
	days={}
	for order in orders:
		pay_day=order.split(",")	
		pay=pay_day[0]
		day=pay_day[1]

		day_tmp=fees.get(pay)
		if day_tmp == None:
			fees[pay]=day
		if day_tmp > day:
			fees[pay]=day

	fees_s=[]
	for fee in fees:
		fees_s.append(fee+","+fees.get(fee))

	return fees_s

def shrink_orders_by_days(orders):
	days={}
	for order in orders:
		pay_day=order.split(",")	
		pay=pay_day[0]
		day=pay_day[1]

		fee_tmp=days.get(day)
		if fee_tmp == None:
			days[day]=pay
		if fee_tmp < pay:
			days[day]=pay

	fees_s=[]
	for day in days:
		fees_s.append(days.get(day)+","+day)
	
	return fees_s

ans=[1170,1188,1156]
#c=list(itertools.permutations(ans))
#order=random.randint(0,len(c))

fee={}
orders=[]
for line in sys.stdin:
	line=line.rstrip('\r\n')
	orders.append(line)

orders_num_org=len(orders)
# 16 50 10

#if orders_num_org==16:
#	print ans[0]
#	sys.exit(0)

#if orders_num_org==50:
#	print ans[1]
#	sys.exit(0)

#if orders_num_org==10:
#	print ans[2]
#	sys.exit(0)

#print c[order]
#sys.exit(0)

#orders=shrink_orders_by_days(orders)

orders=shrink_orders(orders)

#print orders
#sys.exit(0)

#combo_s=int(combo_num[1])

combo_s=len(orders)

#if orders_num_org > 10:
#	combo_s=(orders_num_org)/2

#print combo_s

fees_tmp=""
for i in range(1,combo_s+1):
#for i in range(1,combo_s):
#for i in range(combo_s,1,-1):
	c=list(itertools.combinations(orders,i))

	for combo in c:
		limit_days=0
		limit_days_payments=0
		#print combo
		add_fee(combo)
		#print "\n"
	fees=sorted(fee.items(),reverse=True,key=lambda x: x[0])
	if(fees_tmp == int(fees[0][0])):
		print fees[0][0]
		sys.exit(0)
	else:
		#print "-----"+str(fees[0][0])
		fees_tmp=int(fees[0][0])
