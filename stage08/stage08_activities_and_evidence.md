# Stage 8 activities and evidence

UG and PG | One evolving group project | Complete this blank record using the Stage 8 handout.

All Assignment 3 stage materials are provided from the beginning. Complete this stage only after the previous applicable stage has been integrated, verified and recorded. Use this supplied record in stage08/ in your EXISTING repository. Preserve project/, all earlier tests, records and responses. Do not download another starter or copy staff solutions. The Stage 8 preparation utility is supplied or run by teaching staff when Stage 8 begins. Follow your tutor’s controlled workflow and the handout. If temporarily supplied, keep it outside the repository in a sibling Stage_8_Assets/ folder; exclude it from Git and the final submission.

Group/tutorial: [complete]
Members and UG/PG cohorts: [complete]
Record owner / contribution links for each member: [complete]

Use concise results and accessible artefact links rather than copying entire logs. Keep human-first entries before consulting GitHub Copilot. Link shared evidence once; do not repeat it across sections. No entries below are specimen answers or claimed results.

## A. Tutorial activities

### A.1 Classify all five statements
For each, choose symptom, evidence or hypothesis/opinion, and explain your reason. These are discussion statements, not confirmed diagnoses.
- Appointment disappears after cancellation.
- The data-store removal path is probably being called.
- The failing test shows store.find_appointment('A1') returns None.
- The service layer is badly designed.
- Traceback points to smartcare/services.py line 42 in the example.
The example line number is illustrative; inspect the actual line in your run. The removal hypothesis must be tested against the current project, which has no public delete operation.

Response and reason: [complete]

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


Classification responses (1–5, each with reason): [complete]
Tutorial debugging record — expected; observed; reproduction; hypothesis; evidence to inspect: [complete]
Traceback — exception/assertion; expected/observed values; test line; call path; requirement; ranked causes and discriminating checks: [complete]

## B. Stage 7 baseline and safe preparation

- Stage 7 code SHA and requirement baseline: [complete]
- Baseline test command / working directory / observed result / evidence: [complete]
- Clean preparation SHA if a record-only commit followed Stage 7: [complete]
- Branch and preparer / how teammates obtained this branch: [complete]
- Downloaded tool version, source SHA256 and --check outcome: [complete]
- --apply and --verify output summaries / artefact references: [complete]
- Bounded diff inspected and recovery location (not committed): [complete]
- Prepared faulty-state commit SHA: [complete]
- Preparation or recovery issues and resolution, if any: [complete]
- Initial prepared full-suite command / result / key failures: [complete]

## C. F8-01 diagnosis and repair

- Symptom / observed behaviour: [complete]
- Expected behaviour and requirement: [complete]
- Minimal synthetic reproduction steps: [complete]
- Meaningful failing test path/name and exact relevant failure: [complete]
- Human hypothesis and intended checks: see E, F8-01.
- Supported root cause and inspected code/runtime evidence: [complete after diagnosis]
- Smallest justified fix / diff / why other behaviour is preserved: [complete]
- Repair SHA / focused verification result: [complete]

## D. F8-02 diagnosis and repair

- Symptom / observed behaviour: [complete]
- Expected behaviour and requirement: [complete]
- Minimal synthetic reproduction steps: [complete]
- Meaningful failing test path/name and exact relevant failure: [complete]
- Human hypothesis and intended checks: see E, F8-02.
- Supported root cause and inspected code/runtime evidence: [complete after diagnosis]
- Smallest justified fix / diff / why other behaviour is preserved: [complete]
- Repair SHA / focused verification result: [complete]

## E. Human-first hypotheses

Complete both entries BEFORE Copilot. C/D supply observed/expected/reproduction/test; retain those initial facts and link them here.




### F8-01 human entry

Likely cause and why plausible: The practitioner conflict-checking logic may not be correctly identifying existing appointments for the same practitioner at the same date and time. This is plausible because the failing tests show that the system accepts a second booking instead of raising the expected ValueError.

Evidence intended to inspect / competing explanation / discriminating check: Inspect appointment_service.book_appointment() and the relevant conflict-checking method in the data store. Check whether existing appointments are retrieved and compared using both practitioner ID and appointment datetime. A competing explanation is that the booking service does not call the conflict-checking method. Compare the service execution path with the data store's conflict-checking result.

Member and saved sequence/time or commit showing this preceded consultation: Member: Jerald. Human-first hypothesis recorded before Copilot consultation. Record the actual save time and preserve the Git diff as evidence.

### F8-02 human entry

Likely cause and why plausible:

The cancellation process may be removing the appointment from the data store, or the lookup method may be excluding cancelled appointments. This is plausible because test_same_session_cancellation_retrieval produces a LookupError: Appointment not found after cancellation, even though the appointment should remain retrievable.

Evidence intended to inspect / competing explanation / discriminating check:

Inspect cancel_appointment() in the appointment service and find_appointment() in the data store. Check whether cancellation changes the appointment status to CANCELLED while retaining the same appointment object in the store. A competing explanation is that the appointment remains stored but the lookup method incorrectly filters out cancelled appointments. Compare the stored appointment collection before and after cancellation and inspect the result of find_appointment().

Member and saved sequence/time or commit showing this preceded consultation:

Member: Jerald. Human-first hypothesis recorded before Copilot consultation. Record the actual save time and preserve the Git diff as evidence.



## F. GitHub Copilot prompts, findings and human decisions

Use the full handout prompt separately for BOTH defects, after E. Keep each actual prompt or accessible reference; include observed behaviour, expected behaviour, reproduction, failing test, human hypothesis, relevant code, three ranked causes and discriminating checks, with the no-rewrite/no-invented-requirements constraints.

### F8-01 Copilot review

Actual prompt / output reference and member:

Member: Jerald. Consulted GitHub Copilot Chat using the F8-01 debugging prompt. Copilot's response provided three ranked possible causes based on the observed failing tests and stated requirements. Actual response retained in GitHub Copilot Chat.

1. Ranked suggestion: The conflict predicate checks date/time but does not also check practitioner identity.

Evidence check: Inspect AppointmentService.book_appointment() and the conflict-checking method it uses. Check whether the condition compares both the appointment datetime and practitioner ID.

Observed evidence: The existing test output shows that bookings for the same practitioner and datetime are accepted when they should raise ValueError. However, the exact predicate has not yet been inspected.

Evaluation: Plausible, but not yet confirmed.

Decision: Accept as the leading hypothesis for further investigation because it directly explains the observed behaviour while preserving the rule allowing different practitioners to have appointments at the same time.

2. Ranked suggestion: The booking service does not call the conflict validator, or validation is bypassed.

Evidence check: Inspect the execution order in book_appointment() and determine whether conflict validation occurs before the appointment is added to the store.

Observed evidence: The failing tests show that the second booking is accepted. No source-code evidence has yet established whether validation is missing, bypassed or incorrectly ordered.

Evaluation: Plausible but unconfirmed.

Decision: Retain as an alternative hypothesis. Inspect the service execution path before deciding whether it is the cause.

3. Ranked suggestion: The store compares the wrong practitioner identifier or searches the wrong set of appointments.

Evidence check: Inspect the appointment model fields and the data-store conflict or lookup method. Check whether the correct practitioner ID and appointment collection are used.

Observed evidence: The failing tests demonstrate that the conflict is not detected, but do not establish whether an incorrect field or collection is responsible.

Evaluation: Possible but less directly supported than the first two suggestions.

Decision: Retain as a lower-ranked alternative until the relevant source code is inspected.

Final human conclusion and comparison with initial hypothesis:

Copilot's highest-ranked suggestion is consistent with my original human-first hypothesis that practitioner conflict-checking logic is not correctly identifying existing appointments for the same practitioner and datetime. Copilot also identified two alternative explanations: validation may be bypassed, or the wrong identifier or appointment collection may be checked. I will inspect the actual service and data-store implementation before confirming the root cause or choosing a repair.

### F8-02 Copilot review

**Actual prompt / output reference and member:**

Member: Jerald. Consulted GitHub Copilot Chat using the F8-02 debugging prompt. Copilot provided three ranked possible causes based on the observed failing tests and the cancellation-history requirements. Actual response retained in GitHub Copilot Chat.

**1. Ranked suggestion:** The cancellation service removes the appointment from the store instead of marking it as cancelled.

**Evidence check:** Inspect `AppointmentService.cancel_appointment()` and the store methods it calls. Check whether the appointment is removed using `remove`, `pop` or `del`, rather than having its status changed to `CANCELLED`.

**Observed evidence:** `test_same_session_cancellation_retrieval` reports `LookupError` after cancellation. `test_reject_repeat_cancellations` also reports `LookupError` instead of the expected `ValueError`. The actual removal operation has not yet been confirmed.

**Evaluation:** Plausible and strongly consistent with both failing tests.

**Decision:** Accept as the leading hypothesis for further investigation because it directly explains why the appointment cannot be retrieved and why repeated cancellation produces the wrong exception.

**2. Ranked suggestion:** The lookup method excludes cancelled appointments from its results.

**Evidence check:** Inspect `SmartCareDataStore.find_appointment()` and the appointment-listing methods. Check whether they filter out appointments with `CANCELLED` status and whether the object remains in the underlying collection.

**Observed evidence:** Same-session retrieval fails after cancellation, but the current test output does not establish whether the appointment was deleted or merely excluded by lookup.

**Evaluation:** Plausible but unconfirmed.

**Decision:** Retain as an alternative hypothesis. Inspect the lookup implementation and backing collection before confirming the cause.

**3. Ranked suggestion:** The repeated-cancellation guard checks the wrong state or runs in the wrong order.

**Evidence check:** Inspect the order of lookup, status validation and exception handling in `cancel_appointment()`.

**Observed evidence:** The repeated-cancellation test raises `LookupError` instead of the expected `ValueError`. The current output does not establish why the status guard is not reached.

**Evaluation:** Plausible as a secondary explanation, potentially related to the first or second suggestion.

**Decision:** Retain as a lower-ranked hypothesis until the cancellation and lookup code is inspected.

**Final human conclusion and comparison with initial hypothesis:**

Copilot's leading suggestion supports my original human-first hypothesis that cancellation may remove the appointment from the data store instead of retaining it with `CANCELLED` status. It also identified an alternative explanation: the appointment may remain stored but be excluded by the lookup method. The incorrect exception on repeated cancellation may indicate that the lookup or status-checking order is also affected. I will inspect the actual implementation before confirming the root cause or choosing a repair.

## G. Failing to passing regression evidence

| Checkpoint | Code SHA or precise diff | Command and working directory | Actual result and artefact reference |
|---|---|---|---|
| F8-01 before repair | [complete] | [complete] | [complete] |
| F8-01 after repair | [complete] | [complete] | [complete] |
| F8-02 before repair | [complete] | [complete] | [complete] |
| F8-02 after repair | [complete] | [complete] | [complete] |
| Full suite after both repairs, before refactor | [complete] | [complete] | [complete] |

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

Response: [complete]

2. Where should expected behaviour come from during debugging?

Response: [complete]

3. What is a debugging hypothesis?

Response: [complete]

4. What is a regression test and why is it retained?

Response: [complete]

5. What is meant by root cause?

Response: [complete]

6. What is refactoring?

Response: [complete]

7. What is a swallowed exception?

Response: [complete]

8. What is a code smell?

Response: [complete]

9. How should GitHub Copilot-generated debugging diagnoses be treated?

Response: [complete]

10. What is the Stage 8 engineering rule?

Response: [complete]

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
