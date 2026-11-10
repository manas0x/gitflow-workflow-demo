from pathlib import Path
import unittest

PAGE = Path(__file__).parents[1] / "site" / "index.html"


class DeploymentPageTests(unittest.TestCase):
    def test_page_identifies_git_flow_and_release_branches(self):
        html = PAGE.read_text(encoding="utf-8")
        self.assertIn("<title>Git Flow Workflow Demo</title>", html)
        self.assertIn("develop", html)
        self.assertIn("release", html)

    def test_page_links_to_pipeline_and_analyzer(self):
        html = PAGE.read_text(encoding="utf-8")
        self.assertIn("https://github.com/manas0x/gitflow-workflow-demo/actions", html)
        self.assertIn("https://gitflow-analyzer.onrender.com/", html)


    def test_feature_change_targets_develop_before_release(self):
        html = PAGE.read_text(encoding="utf-8")
        self.assertIn("Feature integration sample", html)
        self.assertIn("feature/*", html)
        self.assertIn("release/*", html)


if __name__ == "__main__":
    unittest.main()
