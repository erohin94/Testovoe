import itertools 
import operator 

class TreeStore:
	def __init__(self, items):
		self.items = items

	def getAll(self):
		return self.items
	
	def getItem(self, identificator, default = None):
		self.items = {item['id']: item for item in items}
		return self.items.get(identificator)

	def getChildren(self, identificator):
		self.children = {kl: [item['id'] for item in items]
		for kl, items in itertools.groupby(self.items.values(), operator.itemgetter('parent'))}
		return list(map(self.getItem, self.children.get(identificator, [])))

	def getAllParents(self, identificator):
		parent_id = self.getItem(identificator, {}).get('parent')
		if parent_id is not None:
			parent = self.getItem(parent_id)
			return parent
		return []


items = [
{"id": 1, "parent": "root"},
{"id": 2, "parent": 1, "type": "test"},
{"id": 3, "parent": 1, "type": "test"},
{"id": 4, "parent": 2, "type": "test"},
{"id": 5, "parent": 2, "type": "test"},
{"id": 6, "parent": 2, "type": "test"},
{"id": 7, "parent": 4, "type": None},
{"id": 8, "parent": 4, "type": None}
]

ts = TreeStore(items)
print(ts.getAll())
print(ts.getItem(7))
print(ts.getChildren(4))
print(ts.getChildren(5))
print(ts.getAllParents(7))
