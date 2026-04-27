"""
snapdfy Configuration
"""

import os
from datetime import timedelta

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    # ── Core ──────────────────────────────────────────────────────────────────
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-change-in-production")
    DEBUG      = os.environ.get("DEBUG", "True") == "True"

    # ── Database ──────────────────────────────────────────────────────────────
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL",
        f"sqlite:///{os.path.join(BASE_DIR, 'snapdfy.db')}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # ── File uploads ──────────────────────────────────────────────────────────
    UPLOAD_FOLDER       = os.path.join(BASE_DIR, "uploads")
    REPORTS_FOLDER      = os.path.join(BASE_DIR, "static", "reports")
    ALLOWED_EXTENSIONS  = {"csv", "xlsx", "xls", "pdf", "docx", "txt"}
    MAX_CONTENT_LENGTH  = 10 * 1024 * 1024          # 10 MB

    # ── Session ───────────────────────────────────────────────────────────────
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)
    SESSION_COOKIE_HTTPONLY    = True
    SESSION_COOKIE_SAMESITE    = "Lax"

    # ── Mail (Flask-Mail) ─────────────────────────────────────────────────────
    MAIL_SERVER   = os.environ.get("MAIL_SERVER",   "smtp.gmail.com")
    MAIL_PORT     = int(os.environ.get("MAIL_PORT", 587))
    MAIL_USE_TLS  = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME", "your@gmail.com")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD", "your-app-password")
    MAIL_DEFAULT_SENDER = ("snapdfy", os.environ.get("MAIL_USERNAME", "your@gmail.com"))

    # ── Contact info (rendered in templates) ──────────────────────────────────
    CONTACT_PHONE = "+91 98765 43210"
    CONTACT_EMAIL = "contact@snapdfy.app"


class ProductionConfig(Config):
    DEBUG = False
    SESSION_COOKIE_SECURE = True


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
