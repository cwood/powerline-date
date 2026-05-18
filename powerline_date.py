import time
from datetime import datetime
from dateutil import tz


def date(pl, format='%Y-%m-%d', timezone=None, timezones=None, cycle_seconds=5, istime=True):
    if timezones:
        entry = timezones[int(time.time() // cycle_seconds) % len(timezones)]
        timezone = entry['timezone']
        format = entry.get('format', format)
        hl_suffix = entry.get('highlight_group', timezone)
    else:
        hl_suffix = timezone

    group = ['time']
    if not timezone:
        now = datetime.now()
    else:
        now = datetime.now(tz.gettz(timezone))
        group.insert(0, "time:%s" % hl_suffix)

    return [{
        'contents': now.strftime(format).strip(),
        'highlight_groups': group,
        'divider_highlight_group': 'time:divider',
    }]
