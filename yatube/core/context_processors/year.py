from django.utils import timezone


def year(request):
    """Добавляет переменную с текущим годом."""
    return {
        'year': int(str(timezone.now().year))
    }
