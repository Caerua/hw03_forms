from django.utils import timezone


def year(request):
    """Добавляет переменную с текущим годом."""
    return {
        'year': int(str(timezone.localtime(timezone.now()))[:4])
    }
