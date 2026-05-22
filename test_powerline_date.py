import time

import pytest

import powerline_date

# Literal markers (no % directives) keep format assertions independent of the
# wall clock; %Z is used where a deterministic, timezone-derived token is wanted.
TZS = [
    {"timezone": "America/New_York", "format": "EAST",       "highlight_group": "eastern"},
    {"timezone": "America/Chicago",  "format": "%Z CENTRAL", "highlight_group": "central"},
    {"timezone": "UTC",              "format": "%Z UTC",     "highlight_group": "UTC"},
]


@pytest.fixture
def frozen_time(monkeypatch):
    def freeze(t):
        monkeypatch.setattr(time, "time", lambda: t)

    return freeze


@pytest.mark.parametrize(
    "bucket,expected_hl,expected_marker",
    [
        (0, "time:eastern", "EAST"),
        (1, "time:central", "CENTRAL"),
        (2, "time:UTC", "UTC"),
    ],
)
def test_rotation_selects_entry_by_bucket(frozen_time, bucket, expected_hl, expected_marker):
    frozen_time(bucket * 30)
    seg = powerline_date.date(None, timezones=TZS, cycle_seconds=30)[0]
    assert seg["highlight_groups"] == [expected_hl, "time"]
    assert seg["contents"].endswith(expected_marker)
    assert seg["divider_highlight_group"] == "time:divider"


def test_rotation_wraps_modulo_length(frozen_time):
    frozen_time(3 * 30)  # one past the last entry wraps back to the first
    seg = powerline_date.date(None, timezones=TZS, cycle_seconds=30)[0]
    assert seg["highlight_groups"][0] == "time:eastern"


def test_highlight_group_defaults_to_timezone(frozen_time):
    frozen_time(0)
    seg = powerline_date.date(None, timezones=[{"timezone": "UTC", "format": "%Z"}])[0]
    assert seg["highlight_groups"] == ["time:UTC", "time"]


def test_entry_format_falls_back_to_default(frozen_time):
    frozen_time(0)
    seg = powerline_date.date(None, timezones=[{"timezone": "UTC"}], format="%Z DEFAULT")[0]
    assert seg["contents"] == "UTC DEFAULT"


def test_single_timezone_non_rotating():
    seg = powerline_date.date(None, timezone="UTC", format="%Z")[0]
    assert seg["highlight_groups"] == ["time:UTC", "time"]
    assert seg["contents"] == "UTC"


def test_no_timezone_uses_local_clock_without_suffix_group():
    seg = powerline_date.date(None, format="LOCAL")[0]
    assert seg["highlight_groups"] == ["time"]
    assert seg["contents"] == "LOCAL"
    assert seg["divider_highlight_group"] == "time:divider"
