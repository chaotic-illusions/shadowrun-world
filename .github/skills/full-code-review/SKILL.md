---
name: full-code-review
description: 'Perform a full top-down, read-only code review. Use for repository audits covering correctness, security, concurrency, dead or unreachable code, duplication, consistency, comments, tests, migrations, dependencies, and deployment. Produces evidence-based findings grouped by severity without changing application code.'
argument-hint: 'Optional focus area, risk, or paths'
user-invocable: true
disable-model-invocation: false
---

# Full Code Review

Perform a repository-wide review and report actionable findings. Do not modify application,
configuration, documentation, test, or generated files during the review. Creating the review
artifact itself is allowed only when the user explicitly requests it.

## Review Contract

- Treat the request as a code review: findings lead, ordered by severity.
- Ground every finding in a concrete controlling path with workspace-relative file and line links.
- Explain what is wrong, how it manifests, the recommended remediation, and the missing regression test.
- Do not report a symbol as dead until all language, template, inline-handler, and dynamic references
  have been checked.
- Do not report documented design choices as defects unless the current implementation creates a
  correctness, security, operational, or maintainability risk.
- Do not make code changes. Ask the user to select findings for remediation after the report.

## Procedure

1. Read repository guidance first: `AGENTS.md`, `.github/copilot-instructions.md`, and any path-scoped
   instructions that apply to reviewed files.
2. Inventory the architecture and identify ownership boundaries: entry points, routers/controllers,
   services, persistence, schemas, frontend, tests, migrations, tools, dependencies, and deployment.
3. Split substantial reviews into parallel read-only audits when subagents are available:
   - backend, authentication, authorization, persistence, and transactions;
   - domain engines, state machines, concurrency, and random behavior;
   - frontend rendering, DOM XSS, async races, dead UI, and API parity;
   - tests, migrations, dependencies, container/runtime configuration, and operational scripts;
   - cross-cutting registration, model/schema/API parity, duplication, and stale documentation.
4. Require each audit to return exact evidence, manifestation, remediation, and test coverage. Reject
   generic style opinions and claims based only on naming.
5. Independently inspect every Critical and High candidate in the controlling code. Sample Medium and
   Low candidates, merge duplicates, and discard speculative or intentionally deferred work.
6. Run the repository's existing read-only validation commands. Prefer, when available:
   - full tests and focused tests for candidate behavior;
   - syntax, type, lint, and text-hygiene checks;
   - frontend parser checks for standalone and inline scripts;
   - migration graph checks and upgrade of a disposable empty database;
   - dependency consistency and container configuration checks.
7. Never point destructive or migration experiments at the configured development database. Override
   the database URL with a unique disposable path and remove it afterward.
8. Report validation results separately. A green test suite does not invalidate a demonstrated bug;
   call out the missing test boundary when that occurs.

## Review Checklist

### Correctness And Consistency

- Validate input constraints consistently across create and update schemas.
- Trace frontend calls to real routes and verify methods, payloads, and response fields.
- Check registration and wiring for routers, models, services, pages, migrations, and startup hooks.
- Compare comments and documentation with current behavior; flag misleading guidance that can cause
  regressions.
- Find duplicated rules, catalogs, serializers, and helpers that can drift.

### Security And Privacy

- Verify authentication and authorization at the server boundary, including ownership transitions.
- Verify hidden or privileged data is removed server-side, including preview/impersonation modes.
- Check bootstrap credentials, token lifecycle, credential storage, rate limits, CORS, and proxy trust.
- Trace all user/server/AI-controlled values entering HTML, attributes, inline handlers, URLs, logs,
  commands, SQL, or external-service requests.
- Check request and collection bounds for denial-of-service and cost-amplification paths.

### Concurrency And Persistence

- Identify read-check-write races, lost updates, non-atomic counters, duplicate allocation, and
  inconsistent multi-commit workflows.
- Verify optimistic locking protects every writer of shared state.
- For JSON columns, confirm nested changes are copied/reassigned and transactionally persisted.
- Check startup/migration races, swallowed schema failures, connection cleanup, and worker behavior.

### Dead And Unreachable Code

- Search definitions and all direct, dynamic, HTML, template, and event-handler references.
- Verify API endpoints against frontend, tests, tools, documentation, and declared external contracts.
- Distinguish compatibility shims and supported external APIs from dead code.
- Flag UI controls that call missing endpoints or states that can never be reached.

### Tests, Migrations, And Deployment

- Look for assertion-free tests, tests that reproduce logic instead of calling production code, and
  contract tests that prove only symbol existence.
- Exercise migrations from an empty database and representative populated prior revisions.
- Compare runtime schema guards with migration history and recorded revision state.
- Review dependency pinning, image provenance, runtime user, copied build context, health checks,
  secret defaults, and shutdown cleanup.

## Severity Rubric

- **Critical:** straightforward unauthenticated compromise, administrative takeover, destructive data
  loss, or equivalent impact under plausible deployment conditions.
- **High:** privilege escalation, sensitive data disclosure, stored code execution, major rules or
  state-machine bypass, or deployment failure on a supported path.
- **Medium:** meaningful correctness, race, integrity, denial-of-service, integration, or maintainability
  defect requiring specific conditions.
- **Low:** bounded operational weakness, stale/dead code, misleading comments, or duplication with a
  credible future cost.

Reduce severity when exposure requires an already privileged actor, a non-default unsupported setup,
or several unlikely preconditions. State those assumptions explicitly.

## Output Format

Group findings under `Critical`, `High`, `Medium`, and `Low`. For each finding include:

1. A concise title and file/line links.
2. **Problem:** the violated invariant and code evidence.
3. **Manifestation:** a concrete request, interleaving, deployment, or user workflow that triggers it.
4. **Fix:** one primary remediation and any viable alternative.
5. **Test:** the regression or integration test that should fail before the fix and pass afterward.

Finish with:

- **Validation:** commands run and their outcomes.
- **Coverage and caveats:** areas reviewed, unavailable checks, and residual risk.
- A concise invitation to select finding IDs for implementation, without changing code during review.