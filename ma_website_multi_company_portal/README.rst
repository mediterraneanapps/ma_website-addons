=======================================
 Real Multi Website (portal extension)
=======================================

Multi Website support in Portal:

* update user's company_id value for portal user or internal users with when current company is in user's **Allowed companies** list. List of features that requires proper user's company_id value:

  * show orders, invoices, etc. only for current company
  * pay invoices via proper payment processor. See `search condition of acquirer_id in pay method <https://github.com/odoo/odoo/blob/12.0/addons/website_payment/controllers/main.py#L40-L42>`__.
  * don't get access error when download invoice via controller ``/report/pdf/account.report_invoice/123``

Credits
=======

Contributors
------------
* `Mediterranean Apps <mediterranean.apps@gmail.com>`__

Sponsors
--------
* `Mediterranean Apps <mediterranean.apps@gmail.com>`__

Maintainers
-----------
* `Mediterranean Apps <mediterranean.apps@gmail.com>`__

     