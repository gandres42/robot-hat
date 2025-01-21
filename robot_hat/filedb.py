import json

class fileDB(object):
	"""
	A file based database, read and write arguements in the specific file.
	"""
	def __init__(self, db_file:str):
		"""
		:param db_file: the file to save the data.
		:type db_file: str
		"""
		self._db_file_path = db_file

	def get(self, key, default_value = None):
		with open(self._db_file_path, "r") as db_file:
			db = json.load(db_file)
			if key in db:
				return db[key]
			else:
				return default_value

	def set(self, key, value):
		with open(self._db_file_path, "rw") as db_file:
			db = json.load(db_file)
			db[key] = value
			json.dump(db, db_file)