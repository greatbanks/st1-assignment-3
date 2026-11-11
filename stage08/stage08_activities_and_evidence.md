# Stage 8 activities and evidence

UG and PG | One evolving group project | Complete this blank record using the Stage 8 handout.

All Assignment 3 stage materials are provided from the beginning. Complete this stage only after the previous applicable stage has been integrated, verified and recorded. Use this supplied record in stage08/ in your EXISTING repository. Preserve project/, all earlier tests, records and responses. Do not download another starter or copy staff solutions. The Stage 8 preparation utility is supplied or run by teaching staff when Stage 8 begins. Follow your tutor’s controlled workflow and the handout. If temporarily supplied, keep it outside the repository in a sibling Stage_8_Assets/ folder; exclude it from Git and the final submission.

Group/tutorial: Online Group 1, Tuesday 17:30
Members/cohorts: u3281958, u3217894, u3309034
Record owner / contribution links for each member: 

Use concise results and accessible artefact links rather than copying entire logs. Keep human-first entries before consulting GitHub Copilot. Link shared evidence once; do not repeat it across sections. No entries below are specimen answers or claimed results.

## A. Tutorial activities

### A.1 Classify all five statements

For each, choose symptom, evidence or hypothesis/opinion, and explain your reason. These are discussion statements, not confirmed diagnoses.

1. Appointment disappears after cancellation.
2. The data-store removal path is probably being called.
3. The failing test shows store.find_appointment('A1') returns None.
4. The service layer is badly designed.
5. Traceback points to smartcare/services.py line 42 in the example.

The example line number is illustrative; inspect the actual line in your run. The removal hypothesis must be tested against the current project, which has no public delete operation.

Response and reason: 

1. 
2. 
3. 
4. 
5. 

### A.2 Build a debugging record

Choose the cancelled-history scenario or a same-practitioner/time booking. Before changing code, record expected behaviour, observed behaviour, minimal reproduction, a hypothesis and evidence to inspect. Use a requirement to justify the expectation. Keep the initial hypothesis even if later evidence disproves it.

Response and reason: [complete]

### A.3 Test defect or product defect

A test expects cancelled appointments to be deleted, but FR-07 says history must be retained. What should be changed? Explain why. Also decide whether a test expecting different practitioners at the same time to conflict reflects AC-04.2. Do not assume every failing test is correct.

Response and reason: [complete]

### A.4 Refactoring smell hunt

Consider a hypothetical 70-line AppointmentService method containing duplicate status strings, direct collection manipulation, printing, validation and four nested conditionals. Identify the smells and propose small refactorings that preserve required behaviour. The direct collection work replaces the old storage-specific scenario; use the existing SmartCareDataStore boundary. Do not implement an extra architecture.

Classify these proposed changes as refactoring, repair or feature: rename appt to appointment; extract a repeated conflict helper; add rescheduling; restore retained cancellation lookup; replace a magic status string with the existing enum. Explain the behaviour that must remain unchanged.

Response and reason: [complete]

### A.5 Traceback and hypothesis ranking

Using one actual failure, identify its exception/assertion, expected and observed values, test line, application call path and supporting requirement. List three plausible causes and rank them by fit with the available evidence. For each cause, name a check that could distinguish it from the others. Explain why a traceback alone does not establish the cause.

Response and reason: [complete]

### A.6 Exit question

Why is changing code immediately after seeing a failure often a poor debugging strategy?

Response and reason: [complete]

Classification responses (1–5, each with reason): 

1. 
2. 
3. 
4. 
5. 

Tutorial debugging record — expected; observed; reproduction; hypothesis; evidence to inspect: 

| Debugging step      | Response |
| ------------------- | -------- |
| Expected            |          |
| Observed            |          |
| Reproduction        |          |
| Hypothesis          |          |
| Evidence to inspect |          |

Traceback — exception/assertion; expected/observed values; test line; call path; requirement; ranked causes and discriminating checks: 

| Traceback step                          | Response |
| --------------------------------------- | -------- |
| Exception/assertion                     |          |
| Expected/observed values                |          |
| Test line                               |          |
| Call path                               |          |
| Requirement                             |          |
| Ranked causes and discriminating checks |          |

## B. Stage 7 baseline and safe preparation

| Question                                                                | Response                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|-------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Stage 7 code SHA and requirement baseline                               | 23326aba765d853b3a98480cde5661e4d8d983d6 / SmartCare A3 Requirements Baseline 2026 revision 2                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Baseline test command / working directory / observed result / evidence  | python -m pytest -q / project/ / 15 passed in 0.01s (in green) / https://github.com/greatbanks/st1-assignment-3/pull/13                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Clean preparation SHA if a record-only commit followed Stage 7          | bbb980dbe2957931884a235fa0b71a1b36075769                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Branch and preparer / how teammates obtained this branch                | debug/stage08 prepared by teaching staff against the group's existing project, then pushed. Group obtained via fetch.                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Downloaded tool version, source SHA256 and `--check` outcome            | Stage 8 tool 1.1; preflight PASS; baseline SHA256 b4a1993e878c59a9df5e9055320702b2d318c5b6055bb1693a3afc25cd8fd375                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `--apply` and `--verify` output summaries / artefact references         | `--apply`: PREPARED F8-01 practitioner conflict; F8-02 retained-history lookup; test_f8_01_conflict; test_f8_02_history (2 failed); backup/hash recorded in .stage8_faults / `--verify`: exactly 2 expected failures; both approved symptom signatures present. Run by tutor.                                                                                                                                                                                                                                                                                                                       |
| Bounded diff inspected and recovery location (not committed)            | git show --stat origin/debug/stage08 -> 1 file changed: project/smartcare/data_store.py, 11 insertions (+), 18 deletions(-), no other file touched. Recovery location: project/.stage8_faults/                                                                                                                                                                                                                                                                                                                                                                                                      |
| Prepared faulty-state commit SHA                                        | 20b58c327177642eb5b8bacb10e3153210b00b31 - "Prepare Stage08 debug"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Preparation or recovery issues and resolution, if any                   | Utility v1.1 not held locally by the group, supplied and run by teaching staff against the existing project, then pushed as debug/stage08. Branch sits 1 commit ahead an 9 behind main, but data_store.py is unchanged across those 9 commits, so prepared base matches main for file under repair. project/tests/test_domains.py is present on main but not on the prepared branch, although it covers domain construction and Appointment.cancel() which is not touched by the prepared faults, so it does not hide either defects (noted as a baseline difference only).                          |
| Initial prepared full-suite command / result / key failures             | Command: cd project and python -m pytest -q on debug/stage08 / result: 4 failed, 9 passed in 0.02s. / key failures: tests/test_services.py::test_allow_simultaneous_appointments_with_unique_practitioner - DID NOT RAISE <class 'ValueError'>; tests/test_services.py::test_reject_repeat_cancellations - Appointment not found; tests/test_services.py::test_same_session_cancellation_retrieval  - LookupError: Appointment not found; tests/test_started::test_conflict_rule_and_different_practitioner - DID NOT RAISE <class 'ValueError'>. These four tests detect the two prepared defects. |

## C. F8-01 diagnosis and repair

| Question                                                          | Response                                                                                                                                                                                                                                                                                                          |
|-------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Symptom / observed behaviour                                      | test_allow_simultaneous_appointments_with_unique_practitioner failed: DID NOT RAISE <class 'ValueError'>; and test_conflict_rule_and_different_practitioner failed: DID NOT RAISE <class 'ValueError'>. Booking for the same practitioner in the same time slot is accepted instead of rejected.                  |
| Expected behaviour and requirement                                | FR-05: Reject another SCHEDULED booking for the same practitioner at exactly the same datetime. BR-05: Same practitioner + exact time + SCHEDULED conflicts; different practitioner at the same time is allowed. AC-04.1: Same practitioner/exact time/SCHEDULED conflicts.                                       | 
| Minimal synthetic reproduction steps                              | Register P1/D1, P2/D2; book D1 at TIME_SLOT, then attempt a second D1 booking at TIME_SLOT (expect ValueError, observed accepted). Then book D2 at TIME_SLOT (expect success, observed rejected)                                                                                                                  |
| Meaningful failing test path/name and exact relevant failure      | tests/test_services.py::test_allow_simultaneous_appointments_with_unique_practitioner failed: DID NOT RAISE <class 'ValueError'> and tests/test_started::test_conflict_rule_and_different_practitioner shares the same failure                                                                                    |
| Human hypothesis and intended checks                              | The practitioner comparison is inverted and only identifies a clash when the practitioners differ rather then being the same. Check the outcomes invert if the comparison is flipped: book the same practitioner at TIME_SLOT which should raise, and a different practitioner at TIME_SLOT which should succeed. |
| Supported root cause and inspected code/runtime evidence          | In SmartCareDataStore.has_practitioner_conflict, state reads appointment.practitioner.practitioner_id != practitioner_id where behaviour compares equality, . With !=, an existing D1 booking is not matched with a new D1 booking, D1 instead is matched to a new D2 booking.                                    |
| Smallest justified fix / diff / why other behaviour is preserved  | Restore the equality comparison appointment.practitioner.practitioner_id == practitioner_id. The enum for status is status.value == "scheduled", leaving enum to be refactored rather then changing it during this repair.                                                                                        |
| Repair SHA / focused verification result                          | b8daa61fe20896f288b2e770e2d603f97e351c5e / tests/test_services.py::test_allow_simultaneous_appointments_with_unique_practitioner PASSED; tests/test_starter.py::test_conflict_rule_and_different_practitioner PASSED <a href="https://github.com/greatbanks/st1-assignment-3/pull/14">[screenshot]</a>            |


## D. F8-02 diagnosis and repair

| Question                                                          | Response                                                                                                                                                                                                                                                                 |
|-------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Symptom / observed behaviour                                      | tests/test_services.py::test_same_session_cancellation_retrieval - LookupError: Appointment not found; and tests/test_services.py::test_reject_repeat_cancellations - LookupError: Appointment not found. After cancellation the appointment can't be retrieved.         |
| Expected behaviour and requirement                                | FR-07: Retain the same appointment with CANCELLED status in current-session history. BR-07: cancellation changes state and does not delete history. AC-05.2: cancelled history remains retrievable this session and AC-05.3: repeated cancellation is rejected.          |
| Minimal synthetic reproduction steps                              | Register P1/D1, book A1 at TIME_SLOT, cancel A1, then find A1. list_appointments() -> 'A1', status -> AppointmentStatus.CANCELLED, find_appointment('A1') -> None -> False.                                                                                              |
| Meaningful failing test path/name and exact relevant failure      | tests/test_services.py::test_same_session_cancellation_retrieval failed: LookupError - Appointment not found and tests/test_services.py::test_reject_repeat_cancellations on the repeat cancellation, reports None before ValueError.                                    |
| Human hypothesis and intended checks                              | When an appointment is cancelled the lookup excludes it but the appointment is still retained in store. Check that list_appointments() after cancellation still contains the object while find_appointment returns None.                                                 |
| Supported root cause and inspected code/runtime evidence          | In SmartCareDataStore.find_appointment, the state reads appointment.status.value != "cancelled" which returns appointments that are not equal to cancelled and cancelled appointments are returned as None.                                                              |
| Smallest justified fix / diff / why other behaviour is preserved  | Remove the cancelled-status exclusion lookup so that lookup returns any stored appointment by their ID. list_appointments cancel transition is untouched to preserve the behaviour for AC-05.3: repeated cancellation is rejected.                                       |
| Repair SHA / focused verification result                          | 3073876aeba04f3dd0fe3a4f29f179d17ff7442e / tests/test_services.py::test_same_session_cancellation_retrieval PASSED and tests/test_services.py::test_reject_repeat_cancellations PASSED <a href="https://github.com/greatbanks/st1-assignment-3/pull/15">[screenshot]</a> | 

## E. Human-first hypotheses

Complete both entries BEFORE Copilot. C/D supply observed/expected/reproduction/test; retain those initial facts and link them here.

### F8-01 human entry

| Human entry                                                                 | Response |
| --------------------------------------------------------------------------- | -------- |
| Likely cause and why plausible                                              |          |
| Evidence intended to inspect / competing explanation / discriminating check |          |
| Member and saved sequence/time or commit showing this preceded consultation |          |


### F8-02 human entry

| Human entry                                                                 | Response |
| --------------------------------------------------------------------------- | -------- |
| Likely cause and why plausible                                              |          |
| Evidence intended to inspect / competing explanation / discriminating check |          |
| Member and saved sequence/time or commit showing this preceded consultation |          |

## F. GitHub Copilot prompts, findings and human decisions

Use the full handout prompt separately for BOTH defects, after E. Keep each actual prompt or accessible reference; include observed behaviour, expected behaviour, reproduction, failing test, human hypothesis, relevant code, three ranked causes and discriminating checks, with the no-rewrite/no-invented-requirements constraints.

### F8-01 Copilot review

Actual prompt / output reference and member: [complete]

| Ranked suggestion (Name + number) | Evidence check | Observed evidence | Correct, partly correct or wrong | Accept, modify or reject with reason |
|-----------------------------------|----------------|-------------------|----------------------------------|--------------------------------------|
| 1                                 |                |                   |                                  |                                      |
| 2                                 |                |                   |                                  |                                      |
| 3                                 |                |                   |                                  |                                      |

Final human conclusion and comparison with initial hypothesis: [complete]

### F8-02 Copilot review

Actual prompt / output reference and member: [complete]

| Ranked suggestion (Name + number) | Evidence check | Observed evidence | Correct, partly correct or wrong | Accept, modify or reject with reason |
|-----------------------------------|----------------|-------------------|----------------------------------|--------------------------------------|
| 1                                 |                |                   |                                  |                                      |
| 2                                 |                |                   |                                  |                                      |
| 3                                 |                |                   |                                  |                                      |

Final human conclusion and comparison with initial hypothesis: [complete]

## G. Failing to passing regression evidence

| Checkpoint                                     | Code SHA or precise diff | Command and working directory | Actual result and artefact reference |
|------------------------------------------------|--------------------------|-------------------------------|--------------------------------------|
| F8-01 before repair                            |                          |                               |                                      |
| F8-01 after repair                             |                          |                               |                                      |
| F8-02 before repair                            |                          |                               |                                      |
| F8-02 after repair                             |                          |                               |                                      |
| Full suite after both repairs, before refactor |                          |                               |                                      |

Explain how the assertions detect each relevant incorrect result and protect previous behaviour: [complete]
Unrelated failures investigated / resolution: [complete or not applicable with reason]

## H. Refactoring decision and before/after verification

Smell and exact location: [complete]
Small proposed structural change / why justified: [complete before editing]
External behaviour to preserve / relevant tests: [complete]
Before result: see G, full passing suite.
Actual change / diff / separate refactor SHA: [complete]
Focused and full after-refactor commands / working directory / results / evidence: [complete]
Result — accepted, revised or rejected / reason / behaviour-preservation conclusion: [complete]

## I. Git, human review and integration

Issues for both defects / refactor scope and owners: [complete]
Branch / prepared, repair and refactor checkpoints: [link B/C/D/H]
PR link and another member's reviewer identity: [complete]
Key human feedback, difference from Copilot findings and response/outcome: [complete]
Actual review approval / merge evidence: [complete]
Integrated code SHA and team pull/retest command / working directory / result: [complete]
Evidence-only later SHA / explanation if different: [complete or not applicable]
Each member's substantive contribution and artefact: [complete]

## J. Required reflections

1. Which Copilot diagnosis appeared convincing but lacked evidence? [complete; report honestly if none and discuss the least-supported real suggestion]
2. What evidence changed your group's view? [complete]
3. How did regression tests protect the refactoring? [complete]

## K. Ten formative questions

1. What should an engineer do before changing code in response to a failure?

First, attempt to determine the cause of the failure, and ensure there is a good understanding of the full context of the failure within the program (e.g. objects/variables/functions involved). After determining the cause and nature of the failure, attempt to make a minor iterative change to mitigate the failure, repeating until a solution is found.

2. Where should expected behaviour come from during debugging?

Expected behaviour should be described in a document outlining the intended purpose of the program, ideally a sequence diagram.

3. What is a debugging hypothesis?

A debugging hypothesis is an expectation of what issues may exist in the program based on an individual's knowledge and personal interpretation of the program logic, structure, and design. These expectations can be informed through empirical evidence via error handling and exceptions.

4. What is a regression test and why is it retained?

A regression test is a test that is performed regularly throughout the development process to ensure that features remain functional after changes are made to the program. The test is retained so it can be executed again after a change.

5. What is meant by root cause?

The 'root cause' of a failure is the point of failure that can be best attributed as the primary cause for that specific failure.

6. What is refactoring?

Refactoring is the process of rewriting code for the purpose of improvement in a specific area, e.g. overall performance or coherent structure, without changing its functionality.

7. What is a swallowed exception?

A swallowed exception is an exception that has been caught without any handling of the exception, subsequently allowing the program to continue.

8. What is a code smell?

A code smell is a general indication that something is semantically wrong with the code, not necessarily that is it not functional, moreso code that may be difficult to maintain or add features to if it is not refactored.

9. How should GitHub Copilot-generated debugging diagnoses be treated?

With a great deal of skepticism and methodical verification and validation. Each claim should be individually assessed and validated as an actual concern before being addressed.

10. What is the Stage 8 engineering rule?

Structure software for change, not just execution.

## L. Completion and handover

- [ ] Existing project, earlier tests and stage records preserved.
- [ ] Passing Stage 7 SHA and safe preparation details recorded.
- [ ] Both defects reproduced with meaningful failing tests.
- [ ] Both human hypotheses recorded before Copilot; actual suggestions evaluated with evidence.
- [ ] Supported causes and minimal repairs explained; focused and full regression results recorded.
- [ ] One genuine refactor verified under passing before/after tests.
- [ ] Human PR review, feedback resolution and integrated retest recorded.
- [ ] Tutorial, three reflections and ten formative responses complete.
- [ ] Local recovery metadata excluded from submitted source.
- [ ] Same project and full suite ready for Stage 9 after Stage 8 integration, verification and recording.

Verified integrated code SHA / result: see I.
Submitted SHA and evidence-only difference if any: [complete]
Unresolved issues or incomplete checks / owner / next action: [complete]
Handover note: [complete]
