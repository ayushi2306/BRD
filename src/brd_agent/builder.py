from __future__ import annotations

from importlib.resources import files

from jinja2 import Environment, FileSystemLoader, select_autoescape

from .models import BRDRequest, BRDResponse
from .research import generate_research_summary


def _executive_summary(request: BRDRequest) -> str:
    top_objective = request.objectives[0].title if request.objectives else "achieve measurable growth"
    return (
        f"{request.company_name} is preparing a strategic initiative for {request.product_name} in the "
        f"{request.industry} market. This BRD aligns cross-functional teams to {top_objective}, "
        "grounded in customer needs, competitive positioning, and operational constraints."
    )


def generate_brd(request: BRDRequest) -> BRDResponse:
    research = generate_research_summary(request)
    executive_summary = _executive_summary(request)

    template_dir = files("brd_agent").joinpath("templates")
    env = Environment(
        loader=FileSystemLoader(str(template_dir)),
        autoescape=select_autoescape(default_for_string=False),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    template = env.get_template("brd.md.j2")
    markdown = template.render(request=request, research=research, executive_summary=executive_summary)

    return BRDResponse(
        markdown=markdown,
        executive_summary=executive_summary,
        research_summary=research,
    )
