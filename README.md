````markdown
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
Backend: Django + Django REST Framework + PostgreSQL
Frontend: React + Recharts/Plotly
Web Scraper: Selenium + BeautifulSoup
ML: scikit-learn + XGBoost
Scheduler: Celery + Redis
```

## 📁 Project Structure

```
turf-analytics/
├── backend/           # Django application
├── frontend/          # React application
├── ml_models/         # Machine learning models and training
├── scrapers/          # Web scraping scripts
├── docs/              # Documentation
└── docker-compose.yml # Container configuration
```

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- Node.js 16+
- Docker & Docker Compose (optional)
- PostgreSQL 12+

### Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### Frontend Setup

```bash
cd frontend
npm install
npm start
```

## 📖 Documentation

- [Specifications](../ESPECIFICACIONES.md) - Complete project specifications
- [Setup Guide](./docs/SETUP.md) - Detailed setup instructions
- [API Documentation](./docs/API.md) - API endpoints reference
- [Architecture](./docs/ARCHITECTURE.md) - System architecture overview
- [Session 10 Report](./SESSION_10_REPORT.md) - Development progress and CORS configuration
- [Status](./STATUS.md) - Current project status

## 🔄 Workflow

### Daily Scraping
- Scheduled daily scraping at 6:00 AM
- Extracts: Programs, Results, Horses, Jockeys, Trainers, Owners
- Data validation and deduplication
- Statistics calculation

### ML Pipeline
- Weekly model retraining
- Feature engineering from historical data
- Prediction generation for upcoming races
- Performance monitoring

### Admin Features
- Monitor scraping status
- Manage data identities (deduplication)
- Train and evaluate ML models
- Generate reports

### User Features
- View upcoming races
- Analyze horse statistics
- Explore jockey/trainer/owner data
- Access ML predictions
- Global search and filters

## 🛠️ Development

### Running Tests

```bash
cd backend
pytest -v --cov

cd frontend
npm test
```

### Code Style

- Python: PEP 8 (Black formatter)
- JavaScript: ESLint + Prettier

```bash
# Format backend
black .
isort .

# Format frontend
npm run format
```

## 🐳 Docker

```bash
docker-compose up -d
```

Services:
- Backend: http://localhost:8000
- Frontend: http://localhost:3000
- PostgreSQL: localhost:5432

## 🤝 Contributing

1. Create a feature branch
2. Make your changes
3. Run tests
4. Submit a pull request

## 📝 License

MIT License

## 📧 Contact

For questions or issues, contact the development team.

---

**Status:** In Development - Session 10 (Configuration & CORS Setup)  
**Version:** 0.2.0  
**Last Updated:** October 28, 2025
**Backend:** ✅ Running (localhost:8000)  
**Frontend:** ✅ Running (localhost:3000)  
**Authentication:** ✅ JWT Configured (Testing in progress)

````