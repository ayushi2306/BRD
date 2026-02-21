# BRD
diff --git a/README.md b/README.md
index 1abf2d8e0c1afa6e47e6ab6e66339821f9bf13a1..55dbee46da1da8e687b2ea3429531a9fc8f3c81a 100644
--- a/README.md
+++ b/README.md
@@ -1,2 +1,84 @@
-# Autonomous-Market-Research-Competitive-Intelligence-Agent
-A multi-agent system that autonomously researches markets, analyzes competitive landscapes, and generates strategic recommendations based on real-time data..
+# Autonomous Market Research & Competitive Intelligence Agent
+
+This repository now includes a complete, runnable **Business Requirements Document (BRD) generator** with:
+
+- A structured request schema for business context, objectives, stakeholders, and competitors.
+- A research synthesis layer that produces market context, customer needs, opportunities, and risks.
+- A markdown BRD renderer using templates.
+- A FastAPI service for programmatic generation.
+- A CLI for local document creation.
+- Automated tests.
+
+## Project Structure
+
+```text
+src/brd_agent/
+  api.py               # FastAPI app
+  builder.py           # BRD orchestration and rendering
+  cli.py               # Command line interface
+  models.py            # Pydantic request/response models
+  research.py          # Market and competitor insight synthesis
+  templates/brd.md.j2  # BRD markdown template
+tests/
+  test_api.py
+  test_builder.py
+```
+
+## Quickstart
+
+### 1) Install dependencies
+
+```bash
+python -m pip install -e .[dev]
+```
+
+### 2) Generate a BRD via CLI
+
+```bash
+brd-agent generate sample_request.json BRD.md
+```
+
+### 3) Run API locally
+
+```bash
+uvicorn brd_agent.api:app --reload
+```
+
+Then open docs at: `http://127.0.0.1:8000/docs`
+
+## API Usage
+
+### POST `/generate`
+
+Request body matches `BRDRequest`.
+
+Example:
+
+```json
+{
+  "company_name": "Acme Corp",
+  "industry": "ecommerce",
+  "product_name": "Acme Store",
+  "target_customers": "D2C brands"
+}
+```
+
+Response includes:
+- `markdown`: Full BRD content.
+- `executive_summary`: Top-level summary.
+- `research_summary`: Structured insights (context, needs, risks, opportunities, competitor insights).
+
+## Current Scope
+
+This implementation provides a deterministic foundation for BRD generation and can be extended with:
+
+- Live market data connectors.
+- LLM-backed deep analysis.
+- Multi-agent role separation (researcher, strategist, reviewer, editor).
+- Persistent project memory and versioning.
+
+## Testing
+
+```bash
+pytest
+```
