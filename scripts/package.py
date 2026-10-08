"""Build reproducible, allowlisted plugin upload archives. No dependencies."""
import json
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]
manifest = json.loads((ROOT / "plugin.json").read_text(encoding="utf-8"))
claude = json.loads((ROOT / ".claude-plugin/plugin.json").read_text(encoding="utf-8"))
assert manifest["version"] == claude["version"], "Platform versions must match"
packages = {
    "openai": ["plugin.json", "mcp.json", "skills/akiflow-workflows/SKILL.md"],
    "claude": [".claude-plugin/plugin.json", ".mcp.json", "skills/akiflow-workflows/SKILL.md"],
}
output = ROOT / "dist"
output.mkdir(exist_ok=True)
for platform, members in packages.items():
    archive = output / f"akiflow-workflows-{platform}-{manifest['version']}.zip"
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as bundle:
        for member in members:
            assert not member.startswith("/") and ".." not in member.split("/")
            data = (ROOT / member).read_bytes()
            if member.endswith(".json"):
                json.loads(data)
            entry = zipfile.ZipInfo(member, date_time=(2026, 1, 1, 0, 0, 0))
            entry.compress_type = zipfile.ZIP_DEFLATED
            entry.external_attr = 0o100644 << 16
            bundle.writestr(entry, data)
    with zipfile.ZipFile(archive) as bundle:
        assert bundle.namelist() == members
        assert bundle.testzip() is None
        assert all(bundle.read(name) == (ROOT / name).read_bytes() for name in members)
        assert archive.stat().st_size < 100 * 1024 * 1024
    print(f"PASS {archive.name}: verified paths, JSON, CRC and source bytes")
