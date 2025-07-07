import pandas as pd
from src.surface_builder import build_iv_surface

def test_build_iv_surface_valid_data():
    # mock options data with valid bid-ask prices
    mock_data = [{
        "expiry": "2025-12-20",
        "calls": pd.DataFrame([{
            "strike": 100,
            "bid": 5,
            "ask": 6
        }]),
        "puts": pd.DataFrame([{
            "strike": 100,
            "bid": 4,
            "ask": 5
        }])
    }]

    strikes, expiries, ivs = build_iv_surface(mock_data, spot_price=100, risk_free_rate=0.01, option_type="call")

    assert len(strikes) == 1
    assert len(expiries) == 1
    assert len(ivs) == 1
    assert ivs[0] > 0

def test_build_iv_surface_invalid_data():
    # invalid because bid and ask are zero
    mock_data = [{
        "expiry": "2025-12-20",
        "calls": pd.DataFrame([{
            "strike": 100,
            "bid": 0,
            "ask": 0
        }]),
        "puts": pd.DataFrame([{
            "strike": 100,
            "bid": 0,
            "ask": 0
        }])
    }]

    strikes, expiries, ivs = build_iv_surface(mock_data, spot_price=100, risk_free_rate=0.01, option_type="call")

    assert strikes == []
    assert expiries == []
    assert ivs == []