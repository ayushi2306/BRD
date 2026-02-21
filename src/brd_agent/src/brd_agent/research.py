from __future__ import annotations

from collections import defaultdict

from .models import BRDRequest, CompetitorInsight, ResearchSummary

_DEFAULT_INDUSTRY_NEEDS = {
    "fintech": [
        "Trustworthy onboarding and transparent pricing",
        "Fast transaction times with visible status",
        "Compliance with regional regulations",
    ],
    "healthtech": [
        "Privacy-preserving data handling",
        "Simple workflows for clinicians and administrators",
        "Interoperability with existing systems",
    ],
    "ecommerce": [
        "Low-friction checkout experience",
        "Real-time inventory and delivery visibility",
        "Personalized product discovery",
    ],
}


def _normalize(text: str) -> str:
    return text.strip().lower()


def generate_research_summary(request: BRDRequest) -> ResearchSummary:
    industry = _normalize(request.industry)
    customer_needs = list(_DEFAULT_INDUSTRY_NEEDS.get(industry, []))

    if not customer_needs:
        customer_needs = [
            f"Clear value proposition for {request.target_customers}",
            "Predictable performance and reliability",
            "Measurable return on investment",
        ]

    opportunities = [
        f"Differentiate {request.product_name} for {request.target_customers}",
        "Establish defensible distribution channels",
    ]
    if request.geography and _normalize(request.geography) != "global":
        opportunities.append(f"Localize offering for {request.geography} market requirements")

    risks = [
        "Slow adoption due to switching costs",
        "Execution risk from unclear ownership across teams",
    ]
    if request.constraints:
        risks.append("Delivery risk from stated budget/timeline constraints")

    competitor_insights = []
    for competitor in request.known_competitors:
        competitor_insights.append(
            CompetitorInsight(
                name=competitor,
                positioning=f"Established player in {request.industry} with recognizable brand",
                likely_strengths=[
                    "Distribution reach",
                    "Mature feature set",
                ],
                likely_weaknesses=[
                    "Legacy UX complexity",
                    "Slower adaptation to niche segments",
                ],
            )
        )

    market_context = (
        f"{request.industry} market for {request.target_customers} is increasingly competitive, "
        "with buyers expecting faster time-to-value and lower adoption friction."
    )

    # Deduplicate while preserving order.
    seen = defaultdict(bool)
    unique_needs = []
    for need in customer_needs:
        if not seen[need]:
            unique_needs.append(need)
            seen[need] = True

    return ResearchSummary(
        market_context=market_context,
        customer_needs=unique_needs,
        risks=risks,
        opportunities=opportunities,
        competitor_insights=competitor_insights,
    )
