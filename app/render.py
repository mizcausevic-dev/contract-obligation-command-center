from __future__ import annotations

from pathlib import Path
from typing import Any


def page_shell(title: str, eyebrow: str, heading: str, body: str, content: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{title}</title>
  <style>
    :root {{
      --bg: #09121d;
      --panel: #122436;
      --line: #2d4a67;
      --text: #edf2f8;
      --muted: #9ab1c8;
      --accent: #8ecbff;
      --warn: #ffc97e;
      --danger: #ff8c88;
      --ok: #9ad5a8;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      background:
        radial-gradient(circle at top right, rgba(105, 150, 210, 0.16), transparent 26%),
        linear-gradient(180deg, #06111b 0%, #0a1521 100%);
      color: var(--text);
      font-family: "Segoe UI", Inter, sans-serif;
    }}
    .page {{ max-width: 1420px; margin: 0 auto; padding: 56px; }}
    .frame {{
      border: 1px solid rgba(142, 203, 255, 0.14);
      border-radius: 34px;
      background: rgba(5, 13, 23, 0.76);
      padding: 28px;
      box-shadow: 0 24px 80px rgba(0, 0, 0, 0.34);
    }}
    .nav {{ display:flex; gap:12px; justify-content:flex-end; margin-bottom:14px; }}
    .pill {{
      border-radius: 999px;
      padding: 10px 16px;
      border: 1px solid rgba(142, 203, 255, 0.18);
      background: rgba(18, 36, 54, 0.9);
      color: var(--text);
      font-size: 14px;
      font-weight: 600;
    }}
    .hero {{
      border: 1px solid rgba(142, 203, 255, 0.15);
      border-radius: 28px;
      padding: 34px;
      background: linear-gradient(160deg, rgba(18,36,54,0.98), rgba(10,22,35,0.96));
      margin-bottom: 24px;
    }}
    .eyebrow {{
      color: var(--accent);
      letter-spacing: 0.26em;
      text-transform: uppercase;
      font-size: 13px;
      margin-bottom: 14px;
      font-weight: 700;
    }}
    h1 {{
      margin: 0 0 12px;
      font-size: 64px;
      line-height: 0.95;
      font-family: Georgia, "Times New Roman", serif;
      max-width: 980px;
    }}
    .body {{
      margin: 0;
      color: var(--muted);
      font-size: 25px;
      max-width: 980px;
      line-height: 1.4;
    }}
    .metrics {{
      display:grid;
      grid-template-columns: repeat(4, minmax(0, 1fr));
      gap: 18px;
      margin-bottom: 24px;
    }}
    .metric, .card {{
      border-radius: 22px;
      background: rgba(18,36,54,0.96);
      border: 1px solid rgba(142, 203, 255, 0.14);
      padding: 24px;
    }}
    .label {{
      color: var(--accent);
      text-transform: uppercase;
      letter-spacing: 0.18em;
      font-size: 12px;
      margin-bottom: 14px;
      font-weight: 700;
    }}
    .value {{
      font-size: 46px;
      font-weight: 700;
      margin-bottom: 10px;
      font-family: Georgia, "Times New Roman", serif;
    }}
    .sub, .copy {{
      color: var(--muted);
      font-size: 17px;
      line-height: 1.5;
    }}
    .grid {{
      display:grid;
      grid-template-columns: repeat(12, minmax(0, 1fr));
      gap: 18px;
    }}
    .span-4 {{ grid-column: span 4; }}
    .span-8 {{ grid-column: span 8; }}
    .span-12 {{ grid-column: span 12; }}
    .row {{
      display:flex;
      justify-content:space-between;
      gap:18px;
      padding: 16px 0;
      border-top: 1px solid rgba(142, 203, 255, 0.1);
    }}
    .row:first-of-type {{ border-top: 0; padding-top: 0; }}
    .title {{ font-size: 24px; font-weight: 700; margin-bottom: 8px; }}
    .lane {{
      border-radius: 999px;
      padding: 8px 14px;
      font-size: 13px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      white-space: nowrap;
      height: fit-content;
    }}
    .lane.escalate {{ background: rgba(255, 140, 136, 0.14); color: var(--danger); }}
    .lane.watch {{ background: rgba(255, 201, 126, 0.14); color: var(--warn); }}
    .lane.clear {{ background: rgba(154, 213, 168, 0.14); color: var(--ok); }}
    pre {{
      margin: 0;
      white-space: pre-wrap;
      font-size: 15px;
      line-height: 1.55;
      color: #d6e8ff;
    }}
  </style>
</head>
<body>
  <div class="page">
    <div class="frame">
      <div class="nav">
        <div class="pill">Overview</div>
        <div class="pill">Queue</div>
        <div class="pill">Obligations</div>
        <div class="pill">API summary</div>
      </div>
      <section class="hero">
        <div class="eyebrow">{eyebrow}</div>
        <h1>{heading}</h1>
        <p class="body">{body}</p>
      </section>
      {content}
    </div>
  </div>
</body>
</html>"""


def render_overview(summary: dict[str, Any], agreements: list[dict[str, Any]]) -> str:
    metrics = f"""
    <section class="metrics">
      <div class="metric"><div class="label">agreements</div><div class="value">{summary['agreementCount']}</div><div class="sub">active contracts under review</div></div>
      <div class="metric"><div class="label">critical</div><div class="value">{summary['criticalCount']}</div><div class="sub">same-cycle escalation lanes</div></div>
      <div class="metric"><div class="label">watch</div><div class="value">{summary['watchCount']}</div><div class="sub">review blockers within 30 days</div></div>
      <div class="metric"><div class="label">avg risk</div><div class="value">{summary['averageRiskScore']}</div><div class="sub">portfolio obligation pressure</div></div>
    </section>
    """
    queue = "".join(
        f"""
        <div class="row">
          <div>
            <div class="title">{agreement['counterparty']} <span class="copy">· {agreement['agreementType']}</span></div>
            <div class="copy">{agreement['obligationStatus']}. {agreement['nextAction']}</div>
          </div>
          <div class="lane {agreement['lane']}">{agreement['lane']}</div>
        </div>
        """
        for agreement in agreements
    )
    content = metrics + f"""
    <section class="grid">
      <div class="card span-8">
        <div class="label">obligation queue</div>
        {queue}
      </div>
      <div class="card span-4">
        <div class="label">legal ops recommendation</div>
        <div class="title">Pull blockers into a single obligation review lane before renewals harden.</div>
        <div class="copy">{summary['leadRecommendation']}</div>
      </div>
    </section>
    """
    return page_shell(
        "Contract Obligation Command Center",
        "Contract Obligation Command Center",
        "Every obligation should have a deadline, an owner, and an escalation path.",
        "This command layer turns clause friction, renewal pressure, and blocked approvals into a queue legal ops teams can act on.",
        content,
    )


def render_queue(agreements: list[dict[str, Any]]) -> str:
    rows = "".join(
        f"""
        <div class="row">
          <div>
            <div class="title">{agreement['counterparty']} · {agreement['ownerLane']}</div>
            <div class="copy">Risk {agreement['riskScore']} · Window {agreement['obligationWindowDays']} days · {agreement['approvalBlocker']}</div>
          </div>
          <div class="lane {agreement['lane']}">{agreement['lane']}</div>
        </div>
        """
        for agreement in agreements
    )
    return page_shell(
        "Obligation Queue",
        "Prioritized Queue",
        "The queue should explain which blocker matters before the deadline does.",
        "Legal ops, compliance, procurement, and business owners all need the same obligation story in time to act on it.",
        f'<section class="card span-12"><div class="label">active queue</div>{rows}</section>',
    )


def render_obligations(obligations: list[dict[str, Any]]) -> str:
    cards = "".join(
        f"""
        <div class="card span-4">
          <div class="label">{obligation['severity']} obligation</div>
          <div class="title">{obligation['title']}</div>
          <div class="copy">{obligation['counterparty']} · {obligation['agreementType']}</div>
          <div class="copy">Owner: {obligation['owner']} · Deadline window {obligation['daysToDeadline']} days</div>
          <div class="copy">Trigger: {obligation['trigger']}</div>
        </div>
        """
        for obligation in obligations
    )
    return page_shell(
        "Obligation Board",
        "Obligation Board",
        "The clause is only part of the story. The handoff around it is where risk usually lives.",
        "Each obligation carries severity, timing, and ownership context so the team can see what must move next.",
        f'<section class="grid">{cards}</section>',
    )


def render_api_summary(payload: dict[str, Any]) -> str:
    return page_shell(
        "API Summary",
        "API Summary",
        "The same legal-ops layer can feed review queues, portfolio reporting, and audit evidence.",
        "This keeps downstream systems aligned on the same contract risk story instead of rebuilding it separately in BI, CRM, and intake tools.",
        f'<section class="card span-12"><div class="label">sample payload</div><pre>{payload}</pre></section>',
    )


def write_static_proof_pages(output_dir: Path, summary: dict[str, Any], agreements: list[dict[str, Any]], obligations: list[dict[str, Any]], payload: dict[str, Any]) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    pages = {
        "01-overview.html": render_overview(summary, agreements),
        "02-queue.html": render_queue(agreements),
        "03-obligations.html": render_obligations(obligations),
        "04-api-summary.html": render_api_summary(payload),
    }
    for filename, html in pages.items():
        (output_dir / filename).write_text(html, encoding="utf-8")
