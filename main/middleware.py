from django.http import HttpResponseForbidden

class ExperienceMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user_experience = request.user.profile.experience
        if user_experience < 1:
            # Действия для пользователей с опытом менее 10 лет
            return HttpResponseForbidden("Вы слишком неопытны!")
        
        response = self.get_response(request)
        return response
