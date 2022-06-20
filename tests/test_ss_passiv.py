from datetime import datetime, timedelta, timezone

from pvconsumer.solar_sheffield_passiv import (
    get_all_latest_pv_yield_from_solar_sheffield,
    get_all_systems_from_solar_sheffield,
)


def test_get_all_systems():
    pv_systems = get_all_systems_from_solar_sheffield()

    assert len(pv_systems) == 24663


def test_get_all_systems_filter():

    pv_systems = get_all_systems_from_solar_sheffield(pv_system_ids=[52, 64, 65])

    assert len(pv_systems) == 3


def test_get_all_latest_pv_yield():
    pv_yields = get_all_latest_pv_yield_from_solar_sheffield()

    assert len(pv_yields) > 0
    assert "datetime_utc" in pv_yields.columns
    assert "solar_generation_kw" in pv_yields.columns
    assert "system_id" in pv_yields.columns

    assert pv_yields["solar_generation_kw"].mean() >= 0
    assert pv_yields.iloc[0].datetime_utc <= datetime.utcnow()
    assert pv_yields.iloc[0].datetime_utc >= datetime.utcnow() - timedelta(minutes=10)