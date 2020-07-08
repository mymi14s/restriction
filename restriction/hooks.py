# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "restriction"
app_title = "Restriction"
app_publisher = "masonarmani38@gmail.com"
app_description = "Restriction"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "masonarmani38@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/restriction/css/restriction.css"
# app_include_js = "/assets/restriction/js/restriction.js"

# include js, css files in header of web template
# web_include_css = "/assets/restriction/css/restriction.css"
# web_include_js = "/assets/restriction/js/restriction.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "restriction.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "restriction.install.before_install"
# after_install = "restriction.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "restriction.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	("Expense Claim","Purchase Order", "Sales Order" ,"Sales Invoice" , "Purchase Invoice"): {
		"on_change": "restriction.restriction.doctype.limit_restriction.limit_restriction.check_restriction",
	}
 }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"restriction.tasks.all"
# 	],
# 	"daily": [
# 		"restriction.tasks.daily"
# 	],
# 	"hourly": [
# 		"restriction.tasks.hourly"
# 	],
# 	"weekly": [
# 		"restriction.tasks.weekly"
# 	]
# 	"monthly": [
# 		"restriction.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "restriction.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "restriction.event.get_events"
# }

