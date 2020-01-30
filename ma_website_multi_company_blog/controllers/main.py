 
 

from odoo import SUPERUSER_ID
from odoo import http
from odoo.addons.website_blog.controllers.main import WebsiteBlog
from odoo.http import request
from odoo.tools.safe_eval import safe_eval


 
 
 
def get_domain_from_rule(rule):
    return safe_eval(rule.domain_force, rule._eval_context())


class WebsiteBlogExtended(WebsiteBlog):

    @http.route()
    def blog(self, blog=None, tag=None, page=1, **opt):
        blog_super = super(WebsiteBlogExtended, self).blog(blog, tag, page, **opt)

        if request.env.context.get('uid', 0) == SUPERUSER_ID:
            blog_env = blog_super.qcontext['blogs']
            updated_blogs = blog_env.search(get_domain_from_rule(request.env.ref('ma_website_multi_company_blog.blog_rule_all')))
            blog_super.qcontext.update({
                'blogs': updated_blogs,
            })
        return blog_super

    @http.route()
    def blogs(self, page=1, **post):
        blog_super = super(WebsiteBlogExtended, self).blogs(page, **post)

        if request.env.context.get('uid', 0) == SUPERUSER_ID:
            post_env = blog_super.qcontext['posts']
            updated_posts = post_env.search(get_domain_from_rule(request.env.ref('ma_website_multi_company_blog.post_rule_all')))
            blog_super.qcontext.update({
                'posts': updated_posts,
            })
        return blog_super
