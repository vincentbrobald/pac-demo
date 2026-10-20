# pac-demo

Demo CI project for Tekton [Pipelines-as-Code](https://pipelinesascode.com) on the
lab cluster. A tiny Python library (`src/greet`) with tests; `.tekton/ci.yaml`
clones the commit, runs `ruff check` and `pytest` on every pull request to `main`
and every push to `main`. The result appears as a commit status in Forgejo.

```sh
PYTHONPATH=src python3 -m greet Tekton     # Bonjour, Tekton !
python3 -m pytest                          # locally, with pytest installed
```

Try it: open a pull request that breaks a test (e.g. change the greeting) and
watch the status turn red; comment `/retest` to run it again.

Cluster side (namespace `pac-demo`, webhook, credentials): the gitops
repository's `clusters/<cluster>/ci/pac-demo/repository.yaml` (see its
[Platform CI repositories](https://github.com/vincentbrobald/gitops/blob/main/docs/reference/ci-repository.md)).

## Design decisions

Why it is built this way, the alternatives considered and when to revisit
them: [docs/explanation/design-decisions.md](docs/explanation/design-decisions.md).

## License

MIT (LICENSE), © 2026 Vincent Brobald.
