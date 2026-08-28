from typing import List, Optional, Any
from dataclasses import dataclass

@dataclass
class Filters:
    severity: Optional[str] = None
    alert_type: Optional[str] = None
    country_iso: Optional[str] = None

@dataclass
class AlertData:
    id: int
    alert_type: str
    severity: str
    country_iso: str
    location: str
    latitude: float
    longitude: float
    description: str
    event_date: str
    created_at: str
    source: str
    external_id: str
    polygon: Optional[str] = None
    country_code: Optional[str] = None

@dataclass
class Alerts:
    total: int
    skip: int
    limit: int
    filters: Filters
    data: List[AlertData]
    data_updated_at: str
    generated_at: str


@dataclass
class CountryData:
    iso_code: str
    name: str
    advisory_level: int
    risk_score: float
    base_risk_score: float
    active_alerts: int
    last_updated: str
    country_code: Optional[str] = None

@dataclass
class Countries:
    total: int
    skip: int
    limit: int
    data: List[CountryData]