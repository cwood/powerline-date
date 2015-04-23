version = '0.0.1'

from datetime import datetime
from dateutil import tz


def date(pl, format='%Y-%m-%d', istime=False, timezone=None):
    if not timezone:
        now = datetime.now()
    else:
        now = datetime.now(tz.gettz(timezone))

    return [{
        'contents': now.strftime(format),
        'highlight_groups': (['time'] if istime else []) + ['date'],
        'divider_highlight_group': 'time:divider' if istime else None,
    }]
