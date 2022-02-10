import datetime
from datetime import date

today = datetime.datetime.now().today()

inv = {'toothbrush': {'price': 12, 'quantity': 100, 'gst':18}} 
daily_sale = {}

def add_to_inventory(name, price, quantity, gst):
	inv[name] = {'price': price, 'quantity': quantity, 'gst': gst}

def item_sale(name, quantity=1):

	global daily_sale

	if datetime.datetime.now().today() > today:
		daily_sale = {}

	if inv[name]['quantity'] == 0:
		print('Item out of stock')	
	
	else:
		inv[name]['quantity'] = inv[name]['quantity'] - quantity
		daily_sale[name] = quantity

	sales_report()

def sales_report():
	sales = 0.0
	gst = 0
	for i in daily_sale:
		sales += daily_sale[i]*inv[i]['price']
		gst += sales*inv[i]['gst']/100

	revenue = sales - gst

	total_list = []
	total_list.append('Sales     : {}'.format(sales))
	total_list.append('GST       : {}'.format(' '*(len(str(sales)) - len(str(gst))))+ str(gst))
	total_list.append('Total       : {}'.format(' '*(len(str(sales)) - len(str(revenue))))+ str(revenue))

	with open(f'{date.today().strftime("%d.%m.%Y")} sales report.txt', 'w+') as f:
		f.write('\n'.join(total_list))

item_sale('toothbrush',10)