# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import frappe

@frappe.whitelist()
def custom_docperm(self, method):
	doc = frappe.new_doc("DocPerm")
	doc.idx = 2
	doc.read = 1
	doc.write = 1
	doc.create = 1
	doc.delete = 1
	doc.parent = "Custom DocPerm"
	doc.parentfield = "permissions"
	doc.parenttype = "DocType"
	doc.role = "Local Admin"
	doc.db_insert()
