import datetime
import pickle

empty = {}
dir = ''

try:

	with open('inventory.bin', 'rb') as f:
	    inv = pickle.load(f)
except:

	with open('inventory.bin', 'wb') as f:
		pickle.dump({},f)

	with open('inventory.bin', 'rb') as f:
	    inv = pickle.load(f)

try:	    

	with open('daily_report.bin', 'rb') as f:
		daily_sale = pickle.load(f)

except:

	with open('daily_report.bin', 'wb') as f:
		pickle.dump({},f)

	with open('daily_report.bin', 'rb') as f:
		daily_sale = pickle.load(f)

try:

	with open('date.bin', 'rb') as f:
		today = pickle.load(f)

except:

	with open('date.bin', 'wb') as f:
		pickle.load(datetime.date.today(), f)

def add_to_inventory(name, price, quantity, gst):
	inv[name] = {'price': price, 'quantity': quantity, 'gst': gst}

	with open('inventory.bin', 'wb') as f:
		pickle.dump(inv,f)

def update_inventory(name, price, quantity, gst):
	inv[name] = {'price': price, 'quantity': quantity, 'gst': gst}

	with open('inventory.bin', 'wb') as f:
		pickle.dump(inv,f)

def item_sale(name, quantity=1):

	global daily_sale
	global today
	global today1

	if datetime.date.today() > today:

		today = datetime.date.today()
		today = today

		with open('date.bin', 'wb') as f:
			pickle.dump(today,f)
			
		with open('daily_report.bin', 'wb') as f:
			pickle.dump(empty,f)
		daily_sale = empty

	if inv[name]['quantity'] == 0:
		print('Item out of stock')	
	
	else:
		inv[name]['quantity'] = inv[name]['quantity'] - quantity
		with open('inventory.txt', 'wb') as f:
			pickle.dump(inv,f)
		try:
			daily_sale[name] += quantity
		except:
			daily_sale[name] = 0
			daily_sale[name] += quantity

	with open('daily_report.txt', 'wb') as f:
		pickle.dump(daily_sale,f)

	sales_report()

def sales_report():
	sales = 0.0
	gst = 0
	for i in daily_sale:
		sales += daily_sale[i]*inv[i]['price']
		
		gst += sales*inv[i]['gst']/100

	revenue = sales - gst

	statement = f'Sales : {sales}\nGST : {gst} \nTotal : {revenue}'

	with open(dir + f'{datetime.datetime.today().strftime("%d.%m.%Y")} sales report.txt', 'w+') as f:
		f.write(statement)
