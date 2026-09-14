from dataclasses import dataclass

from backend.app.schemas.common import Location, RecommendedAction, RiskLevel, ScenarioName, utc_now
from backend.app.schemas.risk import RiskFactor, RiskInputs, RiskResponse


@dataclass(frozen=True)
class FeatureSpec:
    name: str
    weight: float
    max_value: float
    explanation: str


FEATURES: tuple[FeatureSpec, ...] = (
    FeatureSpec("rainfall_intensity_mm_hr", 0.25, 60.0, "Short-duration rainfall drives rapid runoff."),
    FeatureSpec("cumulative_rainfall_mm_24h", 0.20, 180.0, "Recent accumulated rainfall is a saturation proxy."),
    FeatureSpec("slope_degrees", 0.15, 35.0, "Steeper terrain can concentrate flow faster."),
    FeatureSpec("soil_saturation", 0.20, 1.0, "Saturated soil increases runoff potential."),
    FeatureSpec("observed_water_level", 0.15, 1.0, "Demo water/torrent signal is auxiliary local evidence."),
    FeatureSpec("blockage_report_count", 0.05, 3.0, "Infrastructure reports increase operational concern."),
)

ASSUMPTIONS = [
    "Weights and thresholds are engineering assumptions for a deterministic SIH demo.",
    "Hazard arrival is scenario-derived decision support, not a certified hydrological forecast.",
    "Demo observations are reproducible fixtures, not live measured sensor data.",
]


def _clamp(value: float, lower: float = 0.0, upper: float = 1.0) -> float:
    return min(max(value, lower), upper)


def _risk_level(score: float) -> RiskLevel:
    if score >= 0.80:
        return RiskLevel.EXTREME
    if score >= 0.60:
        return RiskLevel.HIGH
    if score >= 0.35:
        return RiskLevel.MODERATE
    return RiskLevel.LOW


def _action(level: RiskLevel) -> RecommendedAction:
    return {
        RiskLevel.LOW: RecommendedAction.MONITOR,
        RiskLevel.MODERATE: RecommendedAction.PREPARE_TO_EVACUATE,
        RiskLevel.HIGH: RecommendedAction.MOVE_TO_HIGH_GROUND,
        RiskLevel.EXTREME: RecommendedAction.EVACUATE_NOW,
    }[level]


def _hazard_arrival_minutes(score: float) -> int | None:
    if score < 0.35:
        return None
    # Higher score shortens the scenario-derived arrival estimate.
    return round(75 - (score * 60))


def evaluate_risk(
    *,
    location: Location,
    inputs: RiskInputs,
    scenario: ScenarioName,
) -> RiskResponse:
    factors: list[RiskFactor] = []
    score = 0.0

    for spec in FEATURES:
        raw_value = float(getattr(inputs, spec.name))
        normalized = _clamp(raw_value / spec.max_value)
        contribution = normalized * spec.weight
        score += contribution
        factors.append(
            RiskFactor(
                name=spec.name,
                raw_value=raw_value,
                normalized_value=round(normalized, 4),
                weight=spec.weight,
                contribution=round(contribution, 4),
                explanation=spec.explanation,
            )
        )

    score = round(_clamp(score), 4)
    level = _risk_level(score)
    populated_features = sum(1 for factor in factors if factor.raw_value >= 0)
    confidence = round(_clamp(0.55 + 0.45 * (populated_features / len(FEATURES))), 2)

    return RiskResponse(
        location=location,
        risk_score=score,
        risk_level=level,
        confidence=confidence,
        hazard_arrival_minutes=_hazard_arrival_minutes(score),
        evacuation_minutes=None,
        recommended_action=_action(level),
        data_quality="demo",
        scenario=scenario,
        generated_at=utc_now(),
        factors=factors,
        assumptions=ASSUMPTIONS,
    )

