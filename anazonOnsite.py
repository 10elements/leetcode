from operator import attrgetter
import heapq
class Order(object):
	"""docstring for Order"""
	def __init__(self, pid, toReigon, order_date, quantity, expected_days):
		self.pid = pid
		self.toReigon = toReigon
		self.order_date = order_date
		self.quantity = quantity
		self.expected_days = expected_days

	def getPid(self):
		return self.pid

	def getQuantity(self):
		return self.quantity

	def getDestination(self):
		return self.toReigon

class ProductInventory(object):
	"""docstring for ClassName"""
	def __init__(self, pid, quantity, region):
		self.pid = pid
		self.quantity = quantity
		self.region = region

	def getPid(self):
		return self.pid

	def getQuantity(self):
		return self.quantity

	def getRegion(self):
		return self.region

	def reduceQuantity(self, val):
		self.quantity -= val		

class ShippingCost(object):
	"""docstring for ShippingCost"""
	def __init__(self, ship_from, ship_to, cost_per_item, method, days):
		self.ship_from = ship_from
		self.ship_to = ship_to
		self.cost_per_item = cost_per_item
		self.days = days
		self.method = method

	def getShipFrom(self):
		return self.ship_from

	def getShipTo(self):
		return self.ship_to

	def getDays(self):
		return self.method
	
	def getCost(self):
		return self.cost_per_item

class ShippingCostExplorer(object):
	"""docstring for ShippingCostExplorer"""
	def __init__(self):

	def getShippingCostList(self, ship_to):

class ProductInventoryExplorer(object):
	"""docstring for ProductInventory"""
	def __init__(self):

	def getProductInventoryList(self, pid):

		
class ProductShippingCost(object):
	"""docstring for ProductShippingCost"""
	def __init__(self, product_inventory, shipping_cost):
		self.product_inventory = product_inventory
		self.shipping_cost = shipping_cost

	def getProductShippingCost(self, pid, ship_to):
		psc_list = []
		sce = ShippingCostExplorer()

		#get all the shipping costs that ship to ship_to
		shipping_cost_list = sce.getShippingCostList(ship_to)

		# save {ship_from_region : list(shippingCosts)} pairs
		shipping_cost_from = {}

		#iterate through the shipping_cost_list
		for shipping_cost in shipping_cost_list:

			#save (shipping_from, list(shippingCost)) pairs into shipping_cost_from
			shipping_from = shipping_cost.getShipFrom()

			# if shipping_cost_from does not contain shipping_from as a key
			if shipping_from not in shipping_cost_from:
				shipping_cost_from[shipping_from] = [shipping_cost]

			# if shipping_cost_from contains shiping_from as a key
			else:
				shipping_cost_from[shipping_from].append(shipping_cost)
		pie = ProductInventory()

		#get all the inventories that have product(pid)
		product_inventory_list = pie.getProductInventoryList(pid)

		# iterate through product_inventory_list
		for product_inventory in product_inventory_list:
			if product_inventory in shipping_cost_from:
				# create a new ProductShippingCost object that cantains a inventory and all the shippingCosts of that inventory
				psc = ProductShippingCost(product_inventory, shipping_cost_from[product_inventory])

				# append this object to psc_list
				psc_list.append(psc)

		return psc_list

class MileStone2:
	def __init(self)__:

	def function2(self, orders):	
		# sort orders based on increasing order of order.quantity
		orders.sort(key = attrgetter('quantity'))

		# save the destinations that each inventory can ship to
		destinationsOfInventory = {}

		for order in orders:
			psc_list = getProductShippingCost().getProductShippingCost(order.pid, order.ship_to)

			for productShippingCost in psc_list:
				if productShippingCost.product_inventory not in destinationsOfInventory:
					destinationsOfInventory[productShippingCost.product_inventory] = set(order.ship_to)
				else:
					destinationsOfInventory[productShippingCost.product_inventory].add(order.ship_to)

		numOfDestinationsOfInventory = {}

		for inventory, destinations in destinationsOfInventory.items():
			numOfDestinationsOfInventory[inventory] = len(destinations)

				
		# each time choose the order with currently smallest quantity to process
		for order in orders:

			# obtain all the productShippingCosts of the current order
			psc_list = getProductShippingCost().getProductShippingCost(order.pid, order.ship_to)

			orderBuilder = orderBuilder()

			# save all the fastestShippingCost of each inventory
			ShippingCost_list = []

			# total quantitys in all available inventories
			total_quantity_in_inventories = 0

			# for each productShippingCost 
			for productShippingCost in psc_list:

				# calculate the total product quantities in all available inventories
				total_quantity_in_inventories += productShippingCost.product_inventory.quantity

				fastestdays = float('inf')
				fastestShippingCost = None

				# find the fastest shippingCost of the current inventory
				for shippingCost in productShippingCost.shipping_cost:
					if ShippingCost.days < fastestdays:
						fastestdays = shippingCost.days
						fastestShippingCost = ShippingCost

				# put (fastestdays, (fastestShippingCost, correspongding product inventory)) into ShippingCost_list
				ShippingCost_list.append((fastestdays, (fastestShippingCost, productShippingCost.product_inventory)))

			# if total product quantity of the available inventories is sufficient
			if total_quantity_in_inventories >= order.quantity:

				# transfer shiipingCost_list into a min-heap based on fastestdays in O(n) time
				heapq.heapify(shippingCost_list)

				# the remainning product quantity to be sent of the current order
				quantity_to_send = order.quantity

				# while the current order is not finished
				while quantity_to_send > 0:

					# get the fastest shipping cost and its corresponding inventory
					fastest_shipping_cost, inventory_fastest_shipping_cost = heapq.heappop(shippingCost_list)[1]

					# if the inventory is not empty
					if inventory_fastest_shipping_cost.quantity > 0:

						# if the remainning product quantity to be sent is larger than the current inventory
						if quantity_to_send > inventory_fastest_shipping_cost.quantity:

							#adjust the remaining product quantity to be sent
							quantity_to_send -= inventory_fastest_shipping_cost.quantity

							#send out all the product of the current inventory
							orderBuilder.transfer(inventory_fastest_shipping_cost, fastest_shipping_cost, inventory_fastest_shipping_cost.quantity)
							orderBuilder.ship()

						# if the remaining product quantity to be sent is samller than or equal to the current inventory
						else:
							# send the remaining product quantity from the current inventory
							orderBuilder.transfer(inventory_fastest_shipping_cost, fastest_shipping_cost, quantity_to_send)
							orderBuilder.ship()
							quantity_to_send = 0

			# if the total product quantity of the available inventories is not enough
			else:
				orderBuilder.markAsUnfulfilled(order)

class MileStone3:
	def __init__(self):

		def function3(self, orders):	
		#sort orders based on increasing order of order.quantity
		orders.sort(key = attrgetter('quantity'))

		#each time choose the order with currently smallest quantity to process
		for order in orders:

			#obtain all the productShippingCosts given current order
			psc_list = getProductShippingCost().getProductShippingCost(order.pid, order.ship_to)

			orderBuilder = orderBuilder()

			#save the shippingCost, productInventory pair
			shippingCostToInventoryMap = {}

			#save all the shippingCosts
			ShippingCost_list = []

			#total quantitys in all the available inventories
			total_quantity_in_inventories = 0

			for productShippingCost in psc_list:

				#calculate the total product quantities in all available inventories
				total_quantity_in_inventories += productShippingCost.product_inventory.quantity

				for shippingCost in productShippingCost.shipping_cost:

					#put (shippingCost.cost_per_item, shippingcost) into shippingCost_list
					ShippingCost_list.append((shippingCost.cost_per_item, shippingCost))

					#map shippingCost to its corresponding inventory
					shippingCostToInventoryMap[ShippingCost] = productShippingCost.product_inventory

			# if total product quantity of the available inventories is enough
			if total_quantity_in_inventories >= order.quantity:

				#transfer shiipingCost_list into a min-heap based on shippingCost.cost in O(n) time
				heapq.heapify(shippingCost_list)

				#remainning product quantity to be sent of current order
				quantity_to_send = order.quantity

				while quantity_to_send > 0:

					#choose the cheapest shipping cost
					cheapest_shipping_cost = heapq.heappop(shippingCost_list)

					#get the corrresponding inventory of the cheapest shipping cost
					inventory_cheapest_shipping_cost = shippingCostToInventoryMap[cheapest_shipping_cost]

					#if the inventory is not empty
					if inventory_fastest_shipping_cost.quantity > 0:

						#if the remainning product quantity to be sent is larger than the current inventory
						if quantity_to_send > inventory_fastest_shipping_cost.quantity:

							#adjust the remaining product quantity to be sent
							quantity_to_send -= inventory_fastest_shipping_cost.quantity

							#send out all the product of the current inventory
							orderBuilder.transfer(inventory_fastest_shipping_cost, fastest_shipping_cost, inventory_fastest_shipping_cost.quantity)
							orderBuilder.ship()

						#if the remaining product quantity to be sent is samller than or equal to the current inventory
						else:
							#send the remaining product quantity from the current inventory
							orderBuilder.transfer(inventory_fastest_shipping_cost, fastest_shipping_cost, quantity_to_send)
							orderBuilder.ship()
							quantity_to_send = 0
