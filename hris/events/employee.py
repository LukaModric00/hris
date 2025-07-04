import frappe
from frappe.utils import nowdate, add_days

def assign_leave_policy(employee, policy_name: str):
    if frappe.db.exists("Leave Policy Assignment", {"employee": employee.name, "leave_policy": policy_name}):
        print(f"[HRIS] Leave Policy déjà assignée à {employee.name}")
        return

    assignment = frappe.get_doc({
        "doctype": "Leave Policy Assignment",
        "employee": employee.name,
        "leave_policy": policy_name,
        "effective_from": employee.date_of_joining,
        "effective_to": add_days(employee.date_of_joining, 365),
    })
    assignment.insert(ignore_permissions=True)
    assignment.submit()

def after_insert(doc, method):
    print(f"[HRIS] New employee created: {doc.name} ({doc.employee_name})")

def on_update(doc, method):
    print(f"[HRIS] Employee updated: {doc.name} ({doc.employee_name})")

def before_save(doc, method):
    if not doc.is_new():
        previous = frappe.get_doc(doc.doctype, doc.name)
        if doc.staff_type != previous.staff_type:
            if doc.staff_type == 'Local':
                policy_name = frappe.db.get_value(
                    "Leave Policy", 
                    {"title": "Leave Policy (Local)"},
                    "name"
                )
                print(policy_name)
                assign_leave_policy(doc, policy_name)



