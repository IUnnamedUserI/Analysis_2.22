#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from pathlib import Path
import tempfile
import os
from individual import create_db, add_worker, select_all, select_by_period


"""
Для индивидуального задания лабораторной работы 2.21 добавьте тесты с
использованием модуля unittest, проверяющие операции по работе с базой данных.
"""


class TestDatabaseOperations(unittest.TestCase):
    def setUp(self):
        self.db_fd, self.db_path = tempfile.mkstemp()
        create_db(Path(self.db_path))

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(self.db_path)

    def test_add_worker(self):
        add_worker(Path(self.db_path), "Петров Петр", "79998886452", 2000)
        workers = select_all(Path(self.db_path))
        self.assertEqual(len(workers), 1)
        self.assertEqual(workers[0]['name'], "Петров Петр")
        self.assertEqual(workers[0]['phone_number'], "79998886452")
        self.assertEqual(workers[0]['year'], 2000)

    def test_select_all(self):
        add_worker(Path(self.db_path), "Петров Петр", "79998886452", 2000)
        add_worker(Path(self.db_path), "Иванов Иван", "79995554291", 2015)
        workers = select_all(Path(self.db_path))
        self.assertEqual(len(workers), 2)

    def test_select_by_period(self):
        add_worker(Path(self.db_path), "Петров Петр", "79998886452", 2000)
        add_worker(Path(self.db_path), "Иванов Иван", "79995554291", 2015)
        workers = select_by_period(Path(self.db_path), 10)
        self.assertEqual(len(workers), 1)
        self.assertEqual(workers[0]['name'], "Петров Петр")


if __name__ == '__main__':
    unittest.main()
