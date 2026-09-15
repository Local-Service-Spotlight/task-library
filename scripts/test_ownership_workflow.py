from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / '.github' / 'workflows' / 'ownership-map.yml'


class OwnershipWorkflowSafety(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = WORKFLOW.read_text()

    def test_push_deployment_is_limited_to_main(self):
        push = re.search(r'^  push:\n(?P<body>(?:    .+\n)+)', self.source, re.M)
        self.assertIsNotNone(push)
        self.assertIn('branches: [main]', push.group('body'))

    def test_push_event_cannot_send_email(self):
        email_step = re.search(
            r'^      - name: Email the map\n(?P<body>.*?)(?=^      - name:|^  [a-z]|\Z)',
            self.source,
            re.M | re.S,
        )
        self.assertIsNotNone(email_step)
        condition = re.search(r'^        if: (.+)$', email_step.group('body'), re.M)
        self.assertIsNotNone(condition)
        self.assertIn("github.event_name == 'schedule'", condition.group(1))
        self.assertIn("github.event_name == 'workflow_dispatch'", condition.group(1))
        self.assertIn('inputs.skip_email == false', condition.group(1))
        self.assertNotRegex(
            condition.group(1),
            r"schedule'\s*\|\|\s*inputs\.skip_email",
        )


if __name__ == '__main__':
    unittest.main()
