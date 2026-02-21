from brd_agent.builder import generate_brd
from brd_agent.models import BRDRequest, BusinessGoal


def test_generate_brd_contains_core_sections() -> None:
    request = BRDRequest(
        company_name="Acme Corp",
        industry="fintech",
        product_name="Acme Pay",
        geography="India",
        target_customers="SMBs",
        objectives=[BusinessGoal(title="Increase activation", metric="+15% in Q3")],
        known_competitors=["RivalOne"],
    )

    response = generate_brd(request)

    assert "# Business Requirements Document" in response.markdown
    assert "## 6. Competitive Intelligence" in response.markdown
    assert "RivalOne" in response.markdown
    assert response.research_summary.customer_needs
