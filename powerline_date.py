version = '0.0.1'

from datetime import datetime
from dateutil import tz


def date(pl, format='%Y-%m-%d', timezone=None):
    group = ['time']
    if not timezone:
        now = datetime.now()
    else:
        now = datetime.now(tz.gettz(timezone))
        group.insert(0, "time:%s" % timezone)


    return [{
        'contents': now.strftime(format).strip(),
        'highlight_groups': group,
        'divider_highlight_group': 'time:divider',
    }]
