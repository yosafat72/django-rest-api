from django.http import JsonResponse


class Response:

    @staticmethod
    def base(values=None, message="", status=200):
        if values is None:
            values = []

        return JsonResponse({
            'success': True,
            'message': message,
            'data': values
        }, status=status)

    @staticmethod
    def ok(values=None, message=''):
        return Response().base(values=values, message=message, status=200)

    @staticmethod
    def badRequest(values=None, message=''):
        return Response().base(values=values, message=message, status=400)
