"""Include the research-word standard-library checks in package CI."""
import importlib.util
from pathlib import Path

path = Path(__file__).resolve().parents[1] / 'skills/research-word/scripts/test_inspect_docx.py'
spec = importlib.util.spec_from_file_location('research_word_package_tests', path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
PackageChecks = module.PackageChecks
