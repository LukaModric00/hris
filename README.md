Here's your refined, professional, and concise technical test for the Frappe/ERPNext + HRMS developer position, clearly structured and without providing explicit code snippets or SOPs.

---

# 🚀 **Technical Test – Frappe/ERPNext Developer + HRMS**

### 🎯 **Objective**

This test aims to evaluate your ability to set up a Docker-based Frappe development environment, install ERPNext and HRMS, develop custom functionalities based on given instructions, and create a business-focused report.

---

## 🛠️ **Step 1 – Setup Development Environment**

* Clone the following repository:
  [https://github.com/yamenzk/FrappeDev](https://github.com/yamenzk/FrappeDev)

* Carefully follow the instructions provided in the README to:

  * Launch a Docker-based Frappe environment.
  * Install ERPNext and HRMS.
  * Run and validate the local Frappe site (`dev.localhost`).

---

## 📦 **Step 2 – Integrate Existing Application**

* Fork and install the existing HR application available here:
  [https://github.com/LukaModric00/hris](https://github.com/LukaModric00/hris)

* Ensure proper integration and verify that the app is working on your local Frappe site.

---

## 💻 **Step 3 – Custom Development (HR Module)**

### **Create a new Doctype named: "Leave Request" in the "hris" app**

* **Required fields:**

  * `employee` *(Link → Employee)*
  * `leave_type` *(Link → Leave Type)*
  * `from_date` *(Date)*
  * `to_date` *(Date)*
  * `total_days` *(Automatically calculated based on from/to dates)*
  * `reason` *(Small Text, optional)*
  * `status` *(Select: Draft → Submitted → Approved → Rejected)*

* **Business Logic (Backend - Python):**

  * Validate the employee's annual leave balance (max. 30 days/year).
  * If the leave balance is exceeded, raise a clear validation error.

* **Form Behavior (Frontend - JS):**

  * Auto-calculate and display the total leave days (`total_days`).
  * If requested leave exceeds 15 days, display an informational message prompting confirmation with HR.

* **Approval Workflow:**

  * Configure a clear and functional workflow:

    * Employee submits → HR Manager approves/rejects.

---

## 📊 **Step 4 – Custom Report**

### **Report: "Annual Leave Usage Report"**

* **Type:** Script Report
* **Report Columns:**

  * Employee Name
  * Total Leave Days Used (current year)
  * Remaining Balance (based on 30 days per year)
* **Filter Options:**

  * Employee
  * Year
* **Highlight employees** who've already consumed more than 20 leave days this year.

---

## 📑 **Step 5 – Documentation & Submission**

* Provide a short, clear README.md (maximum 15 lines) containing:

  * Simple instructions to reproduce your environment.
  * List of commands used (Docker, bench, etc.).
  * Brief explanation of the implemented workflow.

---

## 📥 **Deliverables**

Upon completion, send a public GitHub repository containing clearly:

* ✅ Your customized `hris` application.
* ✅ Exported Fixtures (`bench export-fixtures`).
* ✅ Screenshots of:

  * Leave Request form.
  * Frontend informational message (for leave requests > 15 days).
  * Generated "Annual Leave Usage Report".
* ✅ README.md as described above.

---

## 📌 **Evaluation Criteria**

* Clear understanding and respect of instructions provided.
* Functional correctness and completeness of requested features.
* Code quality, readability, and adherence to Frappe best practices.
* Clarity and accuracy of provided documentation.

---

**🖥️ Once you have completed the test, please inform me immediately.**

Good luck!
