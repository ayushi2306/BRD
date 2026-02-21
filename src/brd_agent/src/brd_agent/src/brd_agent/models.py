from __future__ import annotations

from typing import List

from pydantic import BaseModel, Field


class BusinessGoal(BaseModel):
    title: str = Field(..., examples=["Increase trial-to-paid conversion"])
    metric: str = Field(..., examples=["+20% conversion in 2 quarters"])


class Stakeholder(BaseModel):
    role: str = Field(..., examples=["Head of Product"])
    expectation: str = Field(..., examples=["Prioritize roadmap by customer impact"])


class BRDRequest(BaseModel):
    company_name: str
    industry: str
    product_name: str
    geography: str = "Global"
    target_customers: str
    objectives: List[BusinessGoal] = Field(default_factory=list)
    stakeholders: List[Stakeholder] = Field(default_factory=list)
    known_competitors: List[str] = Field(default_factory=list)
    constraints: List[str] = Field(default_factory=list)


class CompetitorInsight(BaseModel):
    name: str
    positioning: str
    likely_strengths: List[str]
    likely_weaknesses: List[str]


class ResearchSummary(BaseModel):
    market_context: str
    customer_needs: List[str]
    risks: List[str]
    opportunities: List[str]
    competitor_insights: List[CompetitorInsight]


class BRDResponse(BaseModel):
    markdown: str
    executive_summary: str
    research_summary: ResearchSummary
