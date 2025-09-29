# ml-deploy-fastapi

[![Python](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/)  
[![FastAPI](https://img.shields.io/badge/api-FastAPI-teal.svg)](https://fastapi.tiangolo.com/)  
[![Docker](https://img.shields.io/badge/container-Docker-blue.svg)](https://www.docker.com/)  
[![CI](https://github.com/<your-username>/ml-deploy-fastapi/actions/workflows/ci.yml/badge.svg)](https://github.com/<your-username>/ml-deploy-fastapi/actions)  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Serve a trained ML model with **FastAPI** and containerize it with **Docker**.  
Includes **CI/CD pipeline** with GitHub Actions.  

**Recruiter takeaway:** *“Can ship ML to production with modern SWE practices.”*  

---

## 🚀 Features
- Serve ML models via **FastAPI** (`/predict` endpoint).
- **Configurable + reproducible** model loading (scikit-learn).
- **Containerized** with Docker for portability.
- **Tested** with pytest (root + predict endpoint).
- **Automated CI/CD** with GitHub Actions.

---

## ⚡ Quickstart

```bash
# clone repo
git clone https://github.com/<your-username>/ml-deploy-fastapi.git
cd ml-deploy-fastapi

# create venv
python3 -m venv .venv
source .venv/bin/activate   # Mac/Linux
# .venv\Scripts\activate    # Windows

# install
pip install -e '.[dev]'

# run API
uvicorn src.mldeploy.main:app --reload --port 8000
```

## Test with curl
```
curl -X POST http://127.0.0.1:8000/predict \
    -H "Content-Type: application/json" \
    -d '{"features":[5.1,3.5,1.4,0.2]}'
```

## 🐳 Docker
```
docker build -t ml-deploy-fastapi .
docker run -p 8000:8000 ml-deploy-fastapi
```