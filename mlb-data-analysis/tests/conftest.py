import pytest
import vcr

# Record once; future runs replay the cassette (fast, offline, deterministic)
_my_vcr = vcr.VCR(
    cassette_library_dir="tests/cassettes",
    record_mode="once",            # "all" first time if you want to refresh
    match_on=["method", "scheme", "host", "port", "path", "query", "body"],
    filter_headers=[],
)

@pytest.fixture
def vcr():
    # Per-test fixture so each test can auto-pick a cassette by name
    def _use(name=None):
        # Default cassette name: the test function name (pytest supplies it)
        return _my_vcr.use_cassette(f"{name}.yaml" if name else None)
    return _my_vcr  # also allow direct use: with vcr.use_cassette("file.yaml"):
