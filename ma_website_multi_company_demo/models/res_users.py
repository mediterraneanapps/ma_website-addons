import re

try:
    # python 3
    from urllib import parse
except ImportError:
    # python 2
    import urlparse as parse

from odoo import models, SUPERUSER_ID, api

WEBSITE_REFS = [
    'ma_website_multi_company_demo.website_books',
    'ma_website_multi_company_demo.website_bikes',
    'ma_website_multi_company_demo.website_watches',
]
WEBSITE_RE = r'shop\.(.*)\.example'


class Users(models.Model):
    _inherit = "res.users"

    @classmethod
    def authenticate(cls, db, login, password, user_agent_env):
        uid = super(Users, cls).authenticate(db, login, password, user_agent_env)
        with cls.pool.cursor() as cr:
            env = api.Environment(cr, SUPERUSER_ID, {})
            base_location = user_agent_env and user_agent_env.get('base_location')
            if not base_location:
                return uid

            base = env['ir.config_parameter'].get_param('web.base.url') or base_location

            prefix = None
            suffix = None
            if base:
                domain = parse.urlsplit(base).netloc.split(':')[0]
                prefix, _, suffix = domain.partition('.')

            if not (prefix and suffix):
                return uid

            for wref in WEBSITE_REFS:
                website = env.ref(wref, raise_if_not_found=False)
                if not website:
                    continue
                m = re.search(WEBSITE_RE, website.domain)
                if not m:
                    continue
                key = m.group(1)
                website.domain = '{prefix}.{key}.{suffix}'.format(prefix=prefix, suffix=suffix, key=key)

        return uid
