class GameObject:
	def __init__(self):
		self._x = 0
		self._y = 0
		self._handlers = {}

	def on(self, event, handler):
		self._handlers[event] = handler

	def has_handler(self, event):
		return event in self._handlers

	def _trigger(self, event):
		if self.has_handler(event):
			self._handlers[event]()

	def update(self, map):
		pass