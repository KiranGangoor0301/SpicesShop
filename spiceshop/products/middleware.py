# middleware.py

from django.utils.deprecation import MiddlewareMixin

class ContentTypeOptionsMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        response['x-content-type-options'] = 'nosniff'
        return response
