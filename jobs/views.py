from rest_framework.decorators import api_view
from rest_framework.response import Response

from .jobposting import process_job


@api_view(["GET","POST"])
def add_job(request):

    result = process_job(request.data)

    return Response(result)