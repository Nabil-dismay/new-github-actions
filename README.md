# OpenShift CI/CD Final Project

A small Flask application used to demonstrate a complete CI/CD workflow:
GitHub Actions for CI, Tekton pipelines on OpenShift, and deployment to OpenShift.

## Run locally
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt -r requirements-dev.txt
python app.py
```
Visit `/` and `/health` on port 8080.

## CI (GitHub Actions)
`.github/workflows/workflow.yml` runs **flake8** and **nose** on every push and pull request to `main`.

## Tekton pipeline (`oc-final`)
`.tekton/tasks.yml` defines the `cleanup`, `flake8` and `nose` tasks.
`.tekton/pipeline.yml` runs: cleanup -> git-clone -> flake8 -> nose.

```bash
oc apply -f openshift/pvc.yaml
oc apply -f .tekton/tasks.yml
oc apply -f .tekton/pipeline.yml
tkn pipeline start oc-final \
  -p repo-url=<your-repo-url> -p branch=main \
  -w name=pipeline-workspace,claimName=oc-pipelines-console-pvc \
  --showlog
```

## Deploy to OpenShift
```bash
oc new-app python~<your-repo-url> --name=python-cicd-app
oc expose svc/python-cicd-app
oc logs deployment/python-cicd-app
```
