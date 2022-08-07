#!/usr/bin/python3
""" Module init """

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
