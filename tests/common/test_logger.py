import pytest
import logging
from common.logger import get_logger

def test_logger_default_level():
    logger = get_logger("TestLogger")
    assert logger.level == logging.INFO

def test_logger_custom_level():
    logger = get_logger("TestLogger", level=logging.DEBUG)
    assert logger.level == logging.DEBUG  # DEBUG级别对应 10

def test_logger_output(caplog):
    logger = get_logger("TestLogger")
    logger.info("Test message")

    # Capture the log
    assert "Test message" in caplog.text
