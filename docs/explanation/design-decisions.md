# Design decisions

> Explanation · [README](../../README.md#design-decisions)

### The smallest useful pipeline

**Decision.** pac-demo runs `ruff check` and `pytest` on a tiny Python
library, on pull requests and pushes to `main`, and reports a commit status.
**Why.** It shows how Pipelines-as-Code works on the site (webhook, run,
status, `/retest`) with nothing else in the way.

### No image build here

**Decision.** Building, scanning and pushing images is shown by the real
repositories that need it (gitops-scanner, the providers) and by the teams'
demo application, not here.
**Why.** The demo stays a lint-and-test example; the image pipeline lives
where it is used and maintained.

### Configured from the GitOps repository

**Decision.** Its namespace, PaC Repository, webhook and collaborator come
from gitops [`clusters/lab/ci/pac-demo/repository.yaml`](https://github.com/vincentbrobald/gitops/blob/main/clusters/lab/ci/pac-demo/repository.yaml), like every platform
CI repository.
