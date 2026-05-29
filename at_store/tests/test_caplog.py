# tests/test_logging_example.py
import logging
import pytest


def test_caplog_basic(caplog):
    logger = logging.getLogger(__name__)

    with caplog.at_level(logging.DEBUG):  # Временный уровень для блока
        logger.debug("Это сообщение появится в caplog")
        logger.info("Это тоже")

    # Проверка: сообщение есть в логах?
    assert "Это сообщение появится в caplog" in caplog.text
    assert (__name__, logging.DEBUG,
            "Это сообщение появится в caplog") in caplog.record_tuples
