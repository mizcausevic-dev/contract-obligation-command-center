from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.services.contract_service import build_service


def main() -> None:
    service = build_service()
    summary = service.summary()
    print("contract-obligation-command-center demo")
    print(f"agreementCount: {summary['agreementCount']}")
    print(f"criticalCount: {summary['criticalCount']}")
    print(f"watchCount: {summary['watchCount']}")
    print(f"averageRiskScore: {summary['averageRiskScore']}")
    print(f"averageWindowDays: {summary['averageWindowDays']}")
    for agreement in service.agreements()[:3]:
        print(f"{agreement['contractId']}: {agreement['lane']} / risk {agreement['riskScore']}")


if __name__ == "__main__":
    main()
