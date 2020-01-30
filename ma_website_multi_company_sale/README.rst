=================
 Multi Ecommerce
=================

Multi Website support in eCommerce:

* adds field ``website_ids`` to payment.acquirer
* adds field ``website_ids`` to product.template
* adds field ``website_ids`` to product.public.category
* use separate sale order (cart) for different companies -- works by adding ``company_dependent`` attribute to ``last_website_so_id`` field
* different pricelist (and currency) for different website:

  * to avoid problems with Public User on websites that belong to different
    companies, the module disables multi-company access rules for pricelist.
    Alternative to this might be a new module that disables some rules for
    Public User only
  * workaround for authenticated user is filtering pricelists by website in ``_get_partner_pricelist`` method

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

    