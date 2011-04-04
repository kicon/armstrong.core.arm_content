from datetime import datetime
import random

from .arm_content_support.models import Article, Video
from ..publication.constants import PUB_STATUSES


def create_random_article(**options):
    random_int = random.randint(1000, 9999)
    data = {
        'pub_date': datetime.now(),
        'pub_status': PUB_STATUSES['Published'],
        'title': 'Random Article %s' % random_int,
        'body': str(random_int),
    }
    data.update(options)
    return Article.objects.create(**data)

def create_random_video(**options):
    random_int = random.randint(1000, 9999)
    data = {
        'pub_date': datetime.now(),
        'pub_status': PUB_STATUSES['Published'],
        'title': 'Random Article %s' % random_int,
        'youtube_id': str(random_int),
    }
    data.update(options)
    return Video.objects.create(**data)