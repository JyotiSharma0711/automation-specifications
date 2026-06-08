# Deploy Workflow Migration

This repository is migrating only the `deploy-eks.yml` flow to a centralized reusable workflow. `spec-workflow.yml` remains unchanged and branch-local for now.

## Files

### `.github/workflows/_onix-deploy-reusable.yml`

This file lives on `main` and contains the shared deploy implementation.

It is triggered with `workflow_call`, so it does not run by itself on push. A branch workflow calls it and passes the branch-specific deployment values.

The reusable workflow keeps the existing deploy behavior:

- checkout the pushed specification branch or requested ref
- setup Node.js
- parse `config` into `build.yaml`
- validate `build.yaml`
- upload `build.yaml`
- read domain and version
- calculate GHCR image name and tag
- generate ONIX build output
- generate RAG table
- push generated data to DB
- build and push the Docker image
- checkout `ondc-official/automation-iac`
- update the configured Helm values file
- commit and push the IaC change

### `.github/workflows/deploy-eks.yml`

This file remains on each long-lived service branch, but it is now a small caller.

Its job is to:

- listen for push events on that branch type
- call `_onix-deploy-reusable.yml@main`
- pass the correct DB credentials and IaC values file for that branch type

The caller determines whether the deployment is draft/dev or release/staging. The reusable workflow does not infer this automatically.

### `.github/workflows/onix-deploy-dispatch.yml`

This file lives on `main` and provides the manual GitHub UI entry point.

Use it for:

- manually running the deploy flow
- choosing whether the manual run should use draft/dev or release/staging configuration

Manual dispatch is centralized on `main`; branch-local push deployments still run from the branch caller.

## Push Flow

For a release branch push:

1. A developer pushes to a branch such as `release-eks-FIS12-2.0.3`.
2. GitHub reads `.github/workflows/deploy-eks.yml` from that release branch.
3. The release branch caller starts one workflow run.
4. The caller loads the reusable workflow definition from:

   ```yaml
   ONDC-Official/automation-specifications/.github/workflows/_onix-deploy-reusable.yml@main
   ```

5. This does not create a separate workflow run on `main`. The run is still caused by the release branch push.
6. The reusable workflow checks out the pushed commit SHA from the release branch.
7. The existing build, DB push, image push, and IaC update steps run using the release/staging values passed by the caller.

For a draft branch push, the same flow happens, but the branch caller passes draft/dev values.

## Draft/Dev vs Release/Staging Configuration

The branch caller must pass the correct DB and IaC values based on deployment type.

Draft/dev caller:

```yaml
on:
  push:
    branches:
      - "draft-*"

jobs:
  deploy:
    uses: ONDC-Official/automation-specifications/.github/workflows/_onix-deploy-reusable.yml@main
    permissions:
      contents: read
      packages: write
    with:
      source_ref: ${{ github.sha }}
      deploy_values_file: k8/aws/helm/domain-layer/values.yaml
    secrets:
      db_api_key: ${{ secrets.EKS_DB_SERVICE_API_KEY }}
      db_api_base_url: ${{ secrets.EKS_DB_SERVICE_BASE_URL }}
      redis_password: ${{ secrets.REDIS_PASSWORD }}
      iac_repo_pat: ${{ secrets.IAC_REPO_PAT }}
```

Release/staging caller:

```yaml
on:
  push:
    branches:
      - "release-*"

jobs:
  deploy:
    uses: ONDC-Official/automation-specifications/.github/workflows/_onix-deploy-reusable.yml@main
    permissions:
      contents: read
      packages: write
    with:
      source_ref: ${{ github.sha }}
      db_api_base_url: ${{ vars.STAGING_EKS_DB_SERVICE_BASE_URL }}
      deploy_values_file: k8/aws/helm/domain-layer/values-staging.yaml
    secrets:
      db_api_key: ${{ secrets.STAGING_EKS_DB_SERVICE_API_KEY }}
      redis_password: ${{ secrets.REDIS_PASSWORD }}
      iac_repo_pat: ${{ secrets.IAC_REPO_PAT }}
```

If a branch has a non-standard name but needs release/staging behavior, keep the trigger pattern appropriate for that branch name and still pass the release/staging DB and values-file settings. The deployment type is controlled by the caller values, not by the reusable workflow.

## Rollout Order

1. Commit and push the `main` workflow changes first.
2. Update one release branch caller and test a push.
3. Update one draft branch caller and test a push.
4. Roll out the small caller workflow to the remaining long-lived branches.

The `main` reusable workflow must exist before branch callers that reference `@main` are pushed.
