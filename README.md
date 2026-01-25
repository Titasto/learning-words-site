# 🧠 LearnWords: spaced repetition system ![Python](https://img.shields.io/badge/Python-3.11-blue) ![Django](https://img.shields.io/badge/Django-5.0-green)
Interactive web application for learning and reviewing vocabulary with customizable training and personal dictionaries.

- [💡 Core Features](#-core-features)
- [⭐ Key Strengths](#-key-strengths)
- [🛠️ Technology Stack](#technology-stack)
- [🎯 Fit for Typical Vacancy Requirements](#-fit-for-typical-vacancy-requirements)
- [🧭 What to Improve (roadmap)](#-what-to-improve-roadmap)

# Core Features
 - Create/edit vocabulary lists
 - Dynamic word testing system
 - Configurable training modes
 - User profile management

# ⭐ Key Strengths
- **End-to-end user flow**: registration, login, password change, profile management, and feedback via email.
- **CRUD for dictionaries**: create/edit/manage word lists with transactional saves during list creation.
- **Flexible training logic**: direction of translation and training mode are configurable, progress stored in session.
- **Anti-spam and security**: captcha on feedback form.
- **External API integration**: word pronunciation via ElevenLabs.
- **DRF integration started**: serializer + ViewSet for vocabulary API (ready to expand REST layer).

# 🛠️ Technology Stack
 - Backend: Python 3.11, Django 5.0
 - API: Django REST Framework (partial)
 - Database: SQLite (local; easy to switch to MySQL/PostgreSQL via settings)
 - Frontend: HTML5, CSS3
 - Integrations: ElevenLabs (Text-to-Speech), django-simple-captcha
 - Infrastructure: Git

# 🎯 Fit for Typical Vacancy Requirements
- **Python + Django**: core application built entirely on Django.
- **Databases + SQL**: uses Django ORM and data modeling ready for MySQL/PostgreSQL in production.
- **Git**: Git-based workflow with clean app separation (users/words/training).
- **Team readiness**: modular apps and templates support team collaboration.
- **DRF**: initial API layer already exists and can be expanded quickly.

# 🧭 What to Improve (roadmap)
- **Full REST API**: extend DRF with auth (JWT/Session), CRUD for words/training, OpenAPI/Swagger docs.
- **MySQL/PostgreSQL**: move DB settings to environment variables and add docker-compose for reproducible setup.
- **Testing**: add unit/integration tests (pytest + coverage).
- **Production-ready**: add CI (GitHub Actions), linters (ruff/flake8), formatting (black), pre-commit.
