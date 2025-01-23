import json
import os

class fileDB(object):
	"""
	A file based database, read and write arguements in the specific file.
	"""
	def __init__(self, db_file_path:str):
		"""
		:param db_file: the file to save the data.
		:type db_file: str
		"""
  
		if not os.path.exists(db_file_path):
			os.makedirs(os.path.dirname(db_file_path), exist_ok=True)
			with open(db_file_path, "w") as file:
				file.write("{}")
		self._db_file_path = db_file_path

	def get(self, key, default_value = None):
		with open(self._db_file_path, "r") as db_file:
			db = json.load(db_file)
			if key in db:
				return db[key]
			else:
				if default_value is not None:
					return default_value
				else:
					raise FileNotFoundError("key does not exist")

	def set(self, key, value):
		with open(self._db_file_path, "r") as db_file:
			db = json.load(db_file)
		with open(self._db_file_path, "w") as db_file:
			db[key] = value
			json.dump(db, db_file)
