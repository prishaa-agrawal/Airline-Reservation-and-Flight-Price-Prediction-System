# FDS Airline AI: Premium Engineering Guide

Welcome to the executive flight intelligence suite. This document outlines the advanced architecture and operational procedures for the FDS platform.

## 🚀 Rapid Deployment (Docker)
The entire FDS ecosystem is containerized for professional orchestration.

1. **Prerequisites**: Ensure Docker and Docker Compose are installed.
2. **Launch**: Run the following command from the project root:
   ```bash
   docker-compose up --build
   ```
3. **Access**:
   - Frontend: `http://localhost:3000`
   - Backend API: `http://localhost:8000`
   - API Docs: `http://localhost:8000/docs`

## 🛠 Manual Setup (Development)
If you prefer to run services manually:

### 1. Backend (FastAPI)
```bash
# From project root
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### 2. Frontend (Next.js 14)
```bash
cd frontend
npm install
npm run dev
```

## 🧠 Intelligence Features
- **God Mode**: Accessible via the sidebar. Control the heartbeat of the live booking simulator and trigger manual XGBoost retraining cycles.
- **AI Assistant**: Click the floating "Sparkle" icon in the dashboard to interact with the Neural Operations Liaison.
- **Fleet Telemetry**: Click on flight paths in the RouteMap to view live altitude, speed, and fuel data.
- **Predictive Maintenance**: Check the Fleet tab for automated AI health alerts.

## 🛡️ Authentication
Use the secure Login/Signup flow. For development, any valid format user will be session-persisted in local storage.

---
**FDS GLOBAL - CLEAR FOR TAKEOFF**
- **CORS Management**: Configured for secure cross-origin communication.
- **Lazy Loading**: All dashboard modules utilize React Suspense and Skeleton loaders for perceived performance.
- **Persistent State**: Theme accents and user preferences are handled via localized state management.

---
