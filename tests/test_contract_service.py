from __future__ import annotations

import unittest

from app.services.contract_service import build_service


class ContractServiceTests(unittest.TestCase):
    def setUp(self) -> None:
        self.service = build_service()

    def test_summary_counts(self) -> None:
        summary = self.service.summary()
        self.assertEqual(summary["agreementCount"], 4)
        self.assertEqual(summary["criticalCount"], 1)

    def test_critical_agreement_exists(self) -> None:
        agreement = self.service.agreement("ctr-1004")
        self.assertEqual(agreement["lane"], "escalate")

    def test_obligations_include_counterparty(self) -> None:
        obligation = self.service.obligations()[0]
        self.assertIn("counterparty", obligation)


if __name__ == "__main__":
    unittest.main()
