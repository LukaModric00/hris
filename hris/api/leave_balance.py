import frappe
from frappe.utils import nowdate
from hrms.hr.doctype.leave_application.leave_application import get_leave_balance_on

@frappe.whitelist()
def get_balance(employee, leave_type):
    return get_leave_balance_on(
        employee=employee,
        leave_type=leave_type,
        date=nowdate()
    )