# Todo App – Kubernetes & FastAPI

## Description

Cette application est une **Todo App** simple comprenant :  

- **Backend** : FastAPI + SQLAlchemy + PostgreSQL  
- **Frontend** : HTML, CSS, JS (communication via API REST)  
- **Database** : PostgreSQL  
- **Orchestration** : Kubernetes (Minikube)  

Le projet est conçu pour être déployé sur **Minikube/Kubernetes**, avec des **Services** et **Deployments** pour chaque composant.

---

## Fonctionnalités

- Ajouter des tâches  
- Lister toutes les tâches  
- Supprimer des tâches  
- Interface utilisateur simple et responsive  
- Déploiement facile sur Kubernetes

---
## Prérequis

- Docker  
- Minikube  
- Kubectl  
- Python 3.11+ (pour le backend)  
- PostgreSQL (si tu veux tester en local sans Minikube)

---

## Instructions de déploiement sur Minikube

### 1️⃣ Configurer Docker pour Minikube

**PowerShell :**

```powershell
minikube -p minikube docker-env --shell powershell | Invoke-Expression

## 2️⃣ Construire les images Docker

```powershell
docker build -t todo-frontend:latest ./frontend
docker build -t todo-app:latest ./backend

## 3️⃣ Déployer les services et pods

```powershell
kubectl apply -f k8s/postgres-deployment.yaml
kubectl apply -f k8s/backend-deployment.yaml
kubectl apply -f k8s/backend-service.yaml
kubectl apply -f k8s/frontend-deployment.yaml
kubectl apply -f k8s/frontend-service.yaml

## 4️⃣ Vérifier les pods et services

```powershell
# Lister les pods pour vérifier qu'ils sont en état Running
kubectl get pods

# Lister les services pour vérifier les NodePorts et ClusterIPs
kubectl get svc

## 5️⃣ Tester le frontend

### Port-forward (recommandé sur Windows)

```powershell
# Rediriger les ports pour accéder aux services localement
kubectl port-forward svc/backend-service 8000:80
kubectl port-forward svc/frontend-service 8080:80

### Accès aux services

- **Frontend** → [http://localhost:8080](http://localhost:8080)  
- **Backend API** → [http://localhost:8000/tasks](http://localhost:8000/tasks)

## API Endpoints

| Méthode | Endpoint       | Description                            |
|---------|----------------|----------------------------------------|
| GET     | /tasks         | Liste toutes les tâches                |
| POST    | /tasks         | Ajoute une tâche (`{"title": "..."}`) |
| DELETE  | /tasks/{id}    | Supprime une tâche par ID              |
