from __future__ import annotations

import sys
from pathlib import Path

from fastapi.testclient import TestClient

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.main import app


def main() -> None:
    client = TestClient(app)
    for path in ["/", "/queue", "/obligations", "/api-summary", "/api/dashboard/summary", "/api/agreements", "/api/sample"]:
        response = client.get(path)
        response.raise_for_status()
    print("smoke-ok")


if __name__ == "__main__":
    main()
