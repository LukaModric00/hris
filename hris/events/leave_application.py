import frappe
from frappe import _
from frappe.utils import nowdate
from hrms.hr.doctype.leave_application.leave_application import get_leave_balance_on


def validate(doc, method):
    if doc.leave_type == "Sick Leave - Half Pay":
        balance = frappe.call(
            "frappe.desk.report.leave_balance.leave_balance.get_leave_balance_on",
            employee=doc.employee,
            leave_type="Sick Leave - Full Pay",
            date=nowdate()
        )
        if balance and balance.get("balance", 0) > 0:
            frappe.throw(_("You still have Sick Leave - Full Pay balance. You cannot apply for Half Pay yet."))
    if doc.leave_type == "Maternity Leave":
        gender = frappe.db.get_value("Employee", doc.employee, "gender")
        if gender == "Male":
            frappe.throw(_("Maternity Leave is not allowed for male employees."))
    if doc.leave_type == "Paternity Leave":
        gender = frappe.db.get_value("Employee", doc.employee, "gender")
        if gender == "Female":
            frappe.throw(_("Paternity Leave is not allowed for female employees."))
    if doc.leave_type == "Sick Leave - Half Pay":
        full_balance = get_leave_balance_on(
            employee=doc.employee,
            leave_type="Sick Leave - Full Pay",
            date=doc.from_date
        )
        if full_balance.get("leave_balance", 0) > 0:
            frappe.throw(_("You still have Sick Leave - Full Pay balance."))

    staff_type = frappe.db.get_value("Employee", doc.employee, "staff_type")

    if doc.leave_type == "Annual Leave - Local" and staff_type == "International":
        frappe.throw(_("Annual Leave - Local is not allowed for International Staff."))

    if doc.leave_type == "Annual Leave - International" and staff_type == "Local":
        frappe.throw(_("Annual Leave - International is not allowed for Local Staff."))
        
    leave_type_meta = frappe.get_doc("Leave Type", doc.leave_type)
    doc.custom_requires_medical_cert = leave_type_meta.custom_requires_medical_cert

    if doc.custom_requires_medical_cert and not doc.attached_medical_certificat:
        frappe.throw(_("A medical certificate must be attached for this leave type."))