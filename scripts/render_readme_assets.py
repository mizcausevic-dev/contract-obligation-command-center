from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.render import write_static_proof_pages
from app.services.contract_service import build_service


def main() -> None:
    screenshots = ROOT / "screenshots"
    service = build_service()
    write_static_proof_pages(
        screenshots,
        service.summary(),
        service.agreements(),
        service.obligations(),
        service.sample_payload(),
    )

    edge = shutil.which("msedge")
    if not edge:
        for candidate in [
            Path(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"),
            Path(r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"),
        ]:
            if candidate.exists():
                edge = str(candidate)
                break
    if not edge:
        raise SystemExit("msedge not found")

    for html in screenshots.glob("*.html"):
        png = html.with_suffix(".png")
        subprocess.run(
            [
                edge,
                "--headless",
                "--disable-gpu",
                "--hide-scrollbars",
                "--window-size=1600,1200",
                f"--screenshot={png}",
                html.resolve().as_uri(),
            ],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )

    print("rendered")


if __name__ == "__main__":
    main()
