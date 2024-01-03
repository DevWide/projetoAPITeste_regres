import pytest
import pytest_html
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if report.when == 'call' and report.failed:
        log = item.catch_log()
        report.extra = report.extra or []
        report.extra.append(pytest_html.extras.text('\n'.join(log), name='Logs'))
