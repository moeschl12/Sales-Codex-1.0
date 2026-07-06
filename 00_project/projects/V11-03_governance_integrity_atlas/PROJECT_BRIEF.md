# V11-03 — Governance + Repository Integrity + Atlas Operationalization

Status: READY  
Owner: Executor Agent  
Reviewer: Independent Systems Auditor  
Editor: Felix

---

## 1. Mission

Integrate the essential V1.1 governance, repository-integrity and Atlas-freshness controls into the regular operating system without creating a heavy parallel bureaucracy.

---

## 2. Scope

Allowed work:

- Resolve or prepare decision bundles for OD-006, OD-007, OD-009, OD-010, OD-011 and OD-012 as applicable.
- Make Atlas refresh rules operational for relevant integrations.
- Define repository-integrity checks for IDs, references, status consistency and Atlas output freshness.
- Update operating documentation only where necessary and not redundantly.
- Create lightweight checklists or scripts only when clearly useful.
- Align Task Types, Bootstrap, Operating Manual and Atlas Governance where they contradict the V1.1 control model.

---

## 3. Non-Scope

Do not:

- rewrite the entire framework,
- create long prose manuals duplicating existing files,
- implement speculative external API/router/watchdog systems,
- perform bulk CTX backfill across all objects,
- change knowledge-object categories without Reserved Decision.

---

## 4. Dependencies

- V11-01 completed.
- V11-02 preferred, because evidence decisions influence governance priorities.

---

## 5. Execution Mode

Autonomous macro-project. Decision bundle first, implementation second. Stop if a Reserved Decision is needed.

---

## 6. Internal Checkpoints

- Scope Check after inventory of active governance files.
- State Check before changing any canonical instruction file.
- Health Check after Atlas/integrity updates.
- Context Reset between governance-decision analysis and implementation.
- Pre-Completion Check.

---

## 7. Definition of Done

V11-03 is DONE only when:

1. Relevant Open Decisions have explicit status: implemented / partially implemented / deferred / needs Editor Decision.
2. There is no duplicate source of truth for V1.1 program state.
3. Atlas refresh/integrity procedure is documented and tested.
4. Repository integrity checks are defined for the current repository type.
5. Bootstrap and session-start rules point to the V1.1 control plane without token-heavy overloading.
6. Any code changes to Atlas compiler are tested by a real compiler run.
7. Completion report and audit package exist.

---

## 8. Audit Requirements

Audit must verify:

- no governance sprawl,
- no contradictory status sources,
- Atlas freshness procedure works,
- no unauthorized framework or knowledge-model changes.
