# 🐴 Turf Analytics

Platform for analysis and prediction of horse races using web scraping and machine learning.

## 📋 Project Overview

**Turf Analytics** is a comprehensive system that:
- 📊 Extracts daily race data from elTurf.com
- 🗄️ Centralizes information about races, horses, jockeys, trainers, and owners
- 📈 Provides analytics dashboards for administrators and end users
- 🤖 Predicts race outcomes using Machine Learning
- 📱 Offers intuitive web interface for analysis

## 🏗️ Architecture

```
Backend: Django 4.2.7 + DRF 3.14.0 + SQLite
Frontend: React 18.2.0 + Redux Toolkit + Bootstrap 5
Web Scraper: Selenium + BeautifulSoup
ML: scikit-learn + XGBoost (Pending)
Scheduler: Celery + Redis (Pending)
```

## 📁 Project Structure

```
turf-analytics/
├── backend/              # Django REST API
│   ├── apps/
│   │   ├── accounts/     # User & Authentication
│   │   ├── races/        # Programs & Results
│   │   ├── entities/     # Horses, Jockeys, Trainers, Owners
│   │   ├── predictions/  # ML Predictions
│   │   └── scrapers/     # Web Scraper
│   ├── config/           # Django Settings
│   ├── manage.py
│   └── requirements.txt
├── frontend/             # React Application
│   ├── src/
│   │   ├── components/   # React Components
│   │   ├── pages/        # Page Components
│   │   ├── redux/        # Redux Store
│   │   ├── config/       # Centralized Configuration
│   │   ├── services/     # API Services
│   │   └── App.js
│   ├── package.json
│   └── .env
├── docs/                 # Documentation
├── .gitignore
└── README.md
```

## 🚀 Quick Start

### Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 8000
```

Backend runs on: **http://localhost:8000**

### Frontend Setup

```bash
cd frontend
npm install
cp .env.example .env  # Configure environment variables
npm start
```

Frontend runs on: **http://localhost:3000**

## 📚 Documentation

- [Specifications](./docs/ESPECIFICACIONES.md) - Complete project specifications
- [Implementation Log](./IMPLEMENTATION_LOG.md) - Development progress
- [Configuration Refactoring](./CONFIGURATION_REFACTORING_SUMMARY.md) - Configuration system details

## 🔐 Default Credentials (Development)

```
Email: admin@turf-analytics.com
Password: Admin123!@#

OR

Email: demo@turf-analytics.com  
Password: Demo123!@#
```

## 📊 API Documentation

Swagger UI available at: **http://localhost:8000/api/docs/**

### Main Endpoints

**Authentication:**
- `POST /api/auth/login/` - User login
- `POST /api/auth/register/` - User registration
- `GET /api/auth/me/` - Get current user
- `POST /api/auth/token/refresh/` - Refresh JWT token

**Data Management:**
- `GET /api/programs/` - List all race programs
- `GET /api/horses/` - List all horses
- `GET /api/jockeys/` - List all jockeys
- `GET /api/predictions/` - List ML predictions
- `GET /api/results/` - List race results

**Scraper:**
- `GET /api/scraper-logs/` - View scraper logs
- `GET /api/scraper-logs/latest/` - Get latest scraper run
- `POST /api/scraper/run/` - Manually trigger scraper

## 🛠️ Technology Stack

### Backend
- **Framework:** Django 4.2.7
- **API:** Django REST Framework 3.14.0
- **Database:** SQLite (Development) / PostgreSQL (Production)
- **Authentication:** djangorestframework-simplejwt 5.5.1
- **Scraping:** Selenium + BeautifulSoup
- **Validation:** Django REST Framework validators

### Frontend
- **Framework:** React 18.2.0
- **State Management:** Redux Toolkit 1.9.7
- **HTTP Client:** Axios 1.6.0
- **Routing:** React Router 6.18.0
- **UI Framework:** Bootstrap 5.3.2
- **Styling:** Bootstrap CSS + Custom CSS

## 🔄 Workflow

### For Developers

1. **Branch Naming:** `feature/name`, `bugfix/name`, `hotfix/name`
2. **Commits:** Use descriptive messages
3. **Pull Requests:** Create PR with detailed description
4. **Testing:** Run tests before merging

### Phases Completed ✅

- **Phase 1.1:** Backend API (12 models, 100+ endpoints, JWT auth)
- **Phase 1.2:** Web Scraper (Selenium-based, data parsing, validation)
- **Phase 1.3:** Admin Panel (React, Redux, authentication, dashboards)
- **Configuration Refactoring:** Centralized config with environment variables

### Phases Pending ⏳

- **Phase 1.4:** Frontend npm setup and testing
- **Phase 2:** Integration Testing
- **Phase 3:** ML Models Implementation
- **Phase 4:** Production Deployment

## 📝 License

MIT License - Feel free to use this project for learning and development.

## 📧 Contact

**Author:** Andres Garriga  
**GitHub:** [@garrigaandres35-code](https://github.com/garrigaandres35-code)

---

**Status:** 🚀 In Development  
**Current Version:** 1.0.0-alpha  
**Last Updated:** October 28, 2025
