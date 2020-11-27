def has_body_params(request):
    return request.data and request.data != {}
