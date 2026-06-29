# FIFA World Cup Analytics Platform (AWS + AI)

Production-ready, AI-powered analytics platform inspired by AWS Builder Center's FIFA World Cup reference, implemented in a unique way using FastAPI, React, and Terraform.

## High-level architecture

- Amazon S3 as the central data lake for historical match data and Athena query results.
- Amazon Athena for interactive analytics on structured match data.
- Amazon Bedrock for LLM-powered narrative insights and calibrated match predictions.
- Amazon QuickSight (optional) for rich dashboards and tournament visualizations.
- FastAPI backend exposes REST APIs for predictions and analytics, integrating with AWS services.
- React + Vite frontend provides a fan-friendly UI for exploring predictions.
- Terraform IaC for provisioning core AWS resources (S3, Athena workgroup, IAM placeholders).

## Local development

Backend:

```bash
cd backend
python -m venv .venv
source .venv/bin/activate  # on Windows use .venv\\Scripts\\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8080
```

Frontend:

```bash
cd frontend
npm install
npm run dev
```

Infra:

```bash
cd infra
terraform init
terraform plan
terraform apply
```

## Production notes

- Containerize the backend using the provided Dockerfile and deploy to Amazon ECS/Fargate or AWS App Runner.
- Frontend can be built and hosted on Amazon S3 + CloudFront.
- Configure IAM roles for least-privilege access to S3, Athena, Bedrock, and QuickSight.
- Add proper logging, tracing, and metrics using CloudWatch and AWS X-Ray.

## Uniqueness features

- Simple, opinionated FastAPI backend instead of Node/Express.
- Clean React UI focused on match prediction UX.
- Extensible Terraform setup for evolving the data platform.
