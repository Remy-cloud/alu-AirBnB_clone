#!/usr/bin/env python3
"""Initializes the storage engine"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
