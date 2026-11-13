# Stage 8 activities and evidence

UG and PG | One evolving group project | Complete this blank record using the Stage 8 handout.

All Assignment 3 stage materials are provided from the beginning. Complete this stage only after the previous applicable stage has been integrated, verified and recorded. Use this supplied record in stage08/ in your EXISTING repository. Preserve project/, all earlier tests, records and responses. Do not download another starter or copy staff solutions. The Stage 8 preparation utility is supplied or run by teaching staff when Stage 8 begins. Follow your tutor’s controlled workflow and the handout. If temporarily supplied, keep it outside the repository in a sibling Stage_8_Assets/ folder; exclude it from Git and the final submission.

Group/tutorial: Online Group 1, Tuesday 17:30

Members/cohorts: u3281958, u3217894, u3309034

Record owner / contribution links for each member: No single record owner, roughly equal ownership between contributors. Major contributions: <a href="https://github.com/greatbanks/st1-assignment-3/pull/20">Janel</a>, <a href="https://github.com/greatbanks/st1-assignment-3/commit/5da00df9b4cffeeaa17b244fa6185f44eb57d80f">James</a>, <a href="https://github.com/greatbanks/st1-assignment-3/commit/fc7969499e3df33b8af762c0c1d43fd410680570">Jerald</a>

Use concise results and accessible artefact links rather than copying entire logs. Keep human-first entries before consulting GitHub Copilot. Link shared evidence once; do not repeat it across sections. No entries below are specimen answers or claimed results.

## A. Tutorial activities

### A.1 Classify all five statements

For each, choose symptom, evidence or hypothesis/opinion, and explain your reason. These are discussion statements, not confirmed diagnoses.

#### 1. Appointment disappears after cancellation.
#### 2. The data-store removal path is probably being called.
#### 3. The failing test shows store.find_appointment('A1') returns None.
#### 4. The service layer is badly designed.
#### 5. Traceback points to smartcare/services.py line 42 in the example.

The example line number is illustrative; inspect the actual line in your run. The removal hypothesis must be tested against the current project, which has no public delete operation.

Response and reason: 

| Question number | Symptom, evidence, or hypothesis/opinion? | Reason                                                                                      |
|-----------------|-------------------------------------------|---------------------------------------------------------------------------------------------|
| 1               | Symptom                                   | No specific programming terminology used, but is symptomatic of a logic problem             |
| 2               | Hypothesis/Opinion                        | Usage of the word "probably", without specific reference to a line of code or program state |
| 3               | Evidence                                  | Specific reference to a type issue and object                                               |
| 4               | Hypothesis/Opinion                        | "Badly designed" is subjective and vague, therefore, it is an opinion                       |
| 5               | Evidence                                  | Specific reference to a line of code from a traceback                                       |

### A.2 Build a debugging record

Choose the cancelled-history scenario or a same-practitioner/time booking. Before changing code, record expected behaviour, observed behaviour, minimal reproduction, a hypothesis and evidence to inspect. Use a requirement to justify the expectation. Keep the initial hypothesis even if later evidence disproves it.

Chosen scenario: Cancelled-history

| Expected behaviour                                           | Observed behaviour                                                                                                                                                                                                                                                                   | Minimal reproduction                                                                                                                                                                                                                    | Hypothesis                          | Evidence to inspect                 |
|--------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------|-------------------------------------|
| Cancelled history remains retrievable in the current session | When an appointment is attempted to be cancelled, its status is checked to ensure it is not an invalid cancellation attempt, then the status is updated only if the cancellation attempt is valid. The appointment data is retained under a CANCELLED status until the session ends. | <a href="https://github.com/greatbanks/st1-assignment-3/blob/main/project/smartcare/domain.py">Domain</a>&nbsp;&amp;&nbsp;<a href="https://github.com/greatbanks/st1-assignment-3/blob/main/project/smartcare/services.py">Services</a> | N/A - feature functions as intended | N/A - feature functions as intended |

### A.3 Test defect or product defect

A test expects cancelled appointments to be deleted, but FR-07 says history must be retained. What should be changed? Explain why. Also decide whether a test expecting different practitioners at the same time to conflict reflects AC-04.2. Do not assume every failing test is correct.

Response and reason:

It is not necessarily an issue for a test to expect a differing result than a feature requirement without understanding the context or methodology behind the test. However, if the test must be run in future and is expected to pass and align with feature requirements, the test should be changed to align with the actual feature requirements of the application, and ensure functionality by testing other aspects of the program.

### A.4 Refactoring smell hunt

Consider a hypothetical 70-line AppointmentService method containing duplicate status strings, direct collection manipulation, printing, validation and four nested conditionals. Identify the smells and propose small refactorings that preserve required behaviour. The direct collection work replaces the old storage-specific scenario; use the existing SmartCareDataStore boundary. Do not implement an extra architecture.

Classify these proposed changes as refactoring, repair or feature: rename appt to appointment; extract a repeated conflict helper; add rescheduling; restore retained cancellation lookup; replace a magic status string with the existing enum. Explain the behaviour that must remain unchanged.

Response and reason: 

| Proposed change                                      | Refactoring, Repair or Feature | Unchanged behaviour                                                        |
|------------------------------------------------------|--------------------------------|----------------------------------------------------------------------------|
| Rename appt to appointment                           | Refactoring                    | Core functionality of code using "appt"                                    |
| Extract a repeated conflict helper                   | Refactoring                    | Core functionality of the function                                         |
| Add rescheduling                                     | Feature                        | The rest of the codebase                                                   |
| Restore retained cancellation lookup                 | Repair                         | The rest of the codebase                                                   |
| Replace a magic status string with the existing enum | Refactoring                    | Value of the magic status string (i.e. enum should have the same function) |

### A.5 Traceback and hypothesis ranking

Using one actual failure, identify its exception/assertion, expected and observed values, test line, application call path and supporting requirement. List three plausible causes and rank them by fit with the available evidence. For each cause, name a check that could distinguish it from the others. Explain why a traceback alone does not establish the cause.

Response and reason: 

`test_allow_simultaneous_appointments_with_unique_practitioner()` threw a ValueError. 

3 possible causes:

1. Program is not handling conflict checking as intended
2. Incorrect enum being used for a booking
3. Booking service method is not calling the conflict check

3 distinguishing checks for causes:

1. Isolate logic and test all cases
2. Iterate through all enum options and check if there is a logic error
3. Inspect code and ensure conflict check is being performed

A traceback alone will only indicate the type of error, not the root cause of the error.

### A.6 Exit question

Why is changing code immediately after seeing a failure often a poor debugging strategy?

Response and reason: 

Changing code immediately before isolation and fully understanding the nature of the failure introduces the possibility that more issues will be introduced inadvertantly, and that previously functional aspects of the program may cease to function as intended.

## B. Stage 7 baseline and safe preparation

| Question                                                               | Response                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Stage 7 code SHA and requirement baseline                              | `23326aba765d853b3a98480cde5661e4d8d983d6` / SmartCare A3 Requirements Baseline 2026 revision 2                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Baseline test command / working directory / observed result / evidence | `python -m pytest -q` / `project/` / `15 passed in 0.01s (in green)` / https://github.com/greatbanks/st1-assignment-3/pull/13                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Clean preparation SHA if a record-only commit followed Stage 7         | `bbb980dbe2957931884a235fa0b71a1b36075769`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Branch and preparer / how teammates obtained this branch               | `debug/stage08` prepared by teaching staff against the group's existing project, then pushed. Group obtained via fetch.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Downloaded tool version, source SHA256 and `--check` outcome           | Stage 8 tool 1.1; preflight PASS; baseline SHA256 `b4a1993e878c59a9df5e9055320702b2d318c5b6055bb1693a3afc25cd8fd375`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `--apply` and `--verify` output summaries / artefact references        | `--apply`: PREPARED F8-01 practitioner conflict; F8-02 retained-history lookup; test_f8_01_conflict; test_f8_02_history (2 failed); backup/hash recorded in .stage8_faults / `--verify`: exactly 2 expected failures; both approved symptom signatures present. Run by tutor.                                                                                                                                                                                                                                                                                                                            |
| Bounded diff inspected and recovery location (not committed)           | `git show --stat origin/debug/stage08` -> 1 file changed: `project/smartcare/data_store.py`, 11 insertions (+), 18 deletions(-), no other file touched. Recovery location: `project/.stage8_faults/`                                                                                                                                                                                                                                                                                                                                                                                                       |
| Prepared faulty-state commit SHA                                       | `20b58c327177642eb5b8bacb10e3153210b00b31` - "Prepare Stage08 debug"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Preparation or recovery issues and resolution, if any                  | Utility v1.1 not held locally by the group, supplied and run by teaching staff against the existing project, then pushed as `debug/stage08`. Branch sits 1 commit ahead an 9 behind main, but `data_store.py` is unchanged across those 9 commits, so prepared base matches main for file under repair. `project/tests/test_domains.py` is present on main but not on the prepared branch, although it covers domain construction and Appointment.cancel() which is not touched by the prepared faults, so it does not hide either defects (noted as a baseline difference only).                        |
| Initial prepared full-suite command / result / key failures            | Command: `cd project && python -m pytest -q` on `debug/stage08` / result: 4 failed, 9 passed in 0.02s. / key failures: <br> `tests/test_services.py::test_allow_simultaneous_appointments_with_unique_practitioner` - DID NOT RAISE <class 'ValueError'>; <br> `tests/test_services.py::test_reject_repeat_cancellations` - Appointment not found; <br> `tests/test_services.py::test_same_session_cancellation_retrieval`  - LookupError: Appointment not found; <br> `tests/test_started::test_conflict_rule_and_different_practitioner` - DID NOT RAISE <class 'ValueError'>. These four tests detect the two prepared defects. |

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
| Repair SHA / focused verification result                          | `b8daa61fe20896f288b2e770e2d603f97e351c5e` / tests/test_services.py::test_allow_simultaneous_appointments_with_unique_practitioner PASSED; tests/test_starter.py::test_conflict_rule_and_different_practitioner PASSED <a href="https://github.com/greatbanks/st1-assignment-3/pull/14">[terminal screenshot]</a> |


## D. F8-02 diagnosis and repair

| Question                                                          | Response                                                                                                                                                                                                                                                                            |
|-------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Symptom / observed behaviour                                      | tests/test_services.py::test_same_session_cancellation_retrieval - LookupError: Appointment not found; and tests/test_services.py::test_reject_repeat_cancellations - LookupError: Appointment not found. After cancellation the appointment can't be retrieved.                    |
| Expected behaviour and requirement                                | FR-07: Retain the same appointment with CANCELLED status in current-session history. BR-07: cancellation changes state and does not delete history. AC-05.2: cancelled history remains retrievable this session and AC-05.3: repeated cancellation is rejected.                     |
| Minimal synthetic reproduction steps                              | Register P1/D1, book A1 at TIME_SLOT, cancel A1, then find A1. list_appointments() -> 'A1', status -> AppointmentStatus.CANCELLED, find_appointment('A1') -> None -> False.                                                                                                         |
| Meaningful failing test path/name and exact relevant failure      | tests/test_services.py::test_same_session_cancellation_retrieval failed: LookupError - Appointment not found and tests/test_services.py::test_reject_repeat_cancellations on the repeat cancellation, reports None before ValueError.                                               |
| Human hypothesis and intended checks                              | When an appointment is cancelled the lookup excludes it but the appointment is still retained in store. Check that list_appointments() after cancellation still contains the object while find_appointment returns None.                                                            |
| Supported root cause and inspected code/runtime evidence          | In SmartCareDataStore.find_appointment, the state reads appointment.status.value != "cancelled" which returns appointments that are not equal to cancelled and cancelled appointments are returned as None.                                                                         |
| Smallest justified fix / diff / why other behaviour is preserved  | Remove the cancelled-status exclusion lookup so that lookup returns any stored appointment by their ID. list_appointments cancel transition is untouched to preserve the behaviour for AC-05.3: repeated cancellation is rejected.                                                  |
| Repair SHA / focused verification result                          | `3073876aeba04f3dd0fe3a4f29f179d17ff7442e` / tests/test_services.py::test_same_session_cancellation_retrieval PASSED and tests/test_services.py::test_reject_repeat_cancellations PASSED <a href="https://github.com/greatbanks/st1-assignment-3/pull/15">[terminal screenshot]</a> | 

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

| Checkpoint                                     | Code SHA or precise diff                                                                                                              | Command and working directory                             | Actual result and artefact reference                                                                                    |
|------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| F8-01 before repair                            | `20b58c327177642eb5b8bacb10e3153210b00b31`                                                                                            | python -m pytest tests/test_regressions.py -v in project/ | 2 failed in 0.02s, <a href="https://github.com/greatbanks/st1-assignment-3/pull/18">[terminal screenshot]</a>           |
| F8-01 after repair                             | `b8daa61fe20896f288b2e770e2d603f97e351c5e` / diff: practitioner_id != practitioner_id -> practitioner_id in has_practitioner_conflict | python -m pytest tests/test_regressions.py -v in project/ | 1 failed, 1 passed in 0.02s, <a href="https://github.com/greatbanks/st1-assignment-3/pull/18">[terminal screenshot]</a> |
| F8-02 before repair                            | `b8daa61fe20896f288b2e770e2d603f97e351c5e`                                                                                            | python -m pytest tests/test_regressions.py -v in project/ | 1 failed, 1 passed in 0.02s, <a href="https://github.com/greatbanks/st1-assignment-3/pull/18">[terminal screenshot]</a> |
| F8-02 after repair                             | `3073876aeba04f3dd0fe3a4f29f179d17ff7442e` / diff: removed appointment.status != "cancelled" from find_appointment                    | python -m pytest tests/test_regressions.py -v in project/ | 2 passed in 0.02s, <a href="https://github.com/greatbanks/st1-assignment-3/pull/18">[terminal screenshot]</a>           |
| Full suite after both repairs, before refactor | `3073876aeba04f3dd0fe3a4f29f179d17ff7442e` plus regression commit `bcfbcae0e70b57c98e4e4e8bf202eb6d15dab484d`                         | python -m pytest -q in project/                           | 2 passed in 0.02s, <a href="https://github.com/greatbanks/st1-assignment-3/pull/18">[terminal screenshot]</a>           |

Explain how the assertions detect each relevant incorrect result and protect previous behaviour:  
F8-01: the same practitioner booking inside pytest.raise(ValueError) detected the missing rejection, since the faulty != comparison found no conflict and raise DID NOT RAISE. the unchanged state assertion and the permitted different practitioner booking protect AC-04.1 and AC-04.2.  
  
F8-02: asserting find_appointment("A1") is booked after cancellation detected the injected faulty lookup returning None. Identity rather than equality also confirms the same object was kept and the status and listing assertions protect FR-07 and BR-07; the repeated-cancellation check protects AC-05.3.  
  
Unrelated failures investigated / resolution: Not applicable  
All failures traced to the two injected faults, and the suite is fully gree after both repairs. The regression tests were written after the repairs so the fail-to-pass evidence was reproduced by checking out earlier commits. 

## H. Refactoring decision and before/after verification

Smell and exact location: Magic status string "scheduled" in appointment.status.value under SmartCareDataStore.has_practitioner_conflict, project/smartcare/data_store.py. It duplicates AppointmentStatus enum as a raw string, so a typo or change to the enum value would break the conflict detection.   

Small proposed structural change / why justified: Replace it with appointment.status is AppointmentStatus.SCHEDULED. This matches the existing enum and matches how the other tests and the domain compare status. It behaves correctly but leads to poor maintainability, so it is not a repair but rather refactoring for structural maintenance.  

External behaviour to preserve / relevant tests: A second SCHEDULED booking for the same practitioner during the same time slot raises ValueError (FR-05). A different practitioner at the same time is allowed (AC-04.2). Cancelled or completed appointments still do not block a booking and the method still returns a bool and does not change anything. Relevant tests: test_regressions.py::test_f8_01_same_practitioner_conflict_rejected_other_practitioner_allowed, test_services.py::test_allow_simultaneous_appointments_with_unique_practitioner, test_starter.py::test_conflict_rule_and_different_practitioner, and the full suite.   

Before result: see G, full passing suite.  

Actual change / diff / separate refactor SHA: one line in data_store: appointment.status.value == "scheduled" -> appointment.status is AppointmentStatus.SCHEDULED / separate commit from both repairs / 21c87dfa524db05591f3c84f3d4e18c8e9399dbe  

Focused and full after-refactor commands / working directory / results / evidence: python -m pytest tests/test_regressions.py::test_f8_01_same_practitioner_conflict_rejected_other_practitioner_allowed tests/test_services.py::test_allow_simultaneous_appointments_with_unique_practitioner tests/test_starter.py::test_conflict_rule_and_different_practitioner -v and python -m pytest -q / in project/ / focused: 3 passed in 0.02s, full: 15 passed in 0.01s /  <a href="https://github.com/greatbanks/st1-assignment-3/pull/19">[terminal screenshot]</a>  

Result — accepted, revised or rejected / reason / behaviour-preservation conclusion: Accepted. The status comparison is equivalent, and the suite result is identical before and after. The change removes a duplicated literal and matches the store's conflict check with the enum contract being used in domain and tests.   

## I. Git, human review and integration

Issues for both defects / refactor scope and owners: No defects identified, scope and ownership unchanged

Branch / prepared, repair and refactor checkpoints: N/A

PR link and another member's reviewer identity: <a href="https://github.com/greatbanks/st1-assignment-3/commit/e63bdf22048b655d545714675afd844bc38d92e6#diff-2466a553164d4bfe9beb10fc1eab176e01078c60dc098a73f2f1ad38567dcdec">Janel PR, James approval</a>

Key human feedback, difference from Copilot findings and response/outcome: Described in detail in Section J

Actual review approval / merge evidence: See GitHub PR approvals

Integrated code SHA and team pull/retest command / working directory / result: `6e492e3b13db233a77acfaa7fe0f9b6694903686`, completed, `project/tests/test_regressions.py`,

Evidence-only later SHA / explanation if different: N/A

Each member's substantive contribution and artefact: Links in intro

## J. Required reflections

1. Which Copilot diagnosis appeared convincing but lacked evidence?

Copilot's suggestion that the cancellation service was removing appointments from the data store appeared convincing because two failing tests produced LookupError exceptions after cancellation. However, this diagnosis lacked direct source-code evidence. The test results showed that appointments could not be retrieved after cancellation, but did not establish whether they had been deleted or were simply excluded by the lookup method. We therefore treated it as a possible cause rather than a confirmed diagnosis.

2. What evidence changed your group's view?

The failing tests helped us realise that the cancellation problem involved more than simply changing an appointment's status. The repeated-cancellation test returned a LookupError instead of the expected ValueError, suggesting that the appointment lookup or status-checking sequence might also be involved. We therefore kept alternative explanations in mind until the implementation could be examined further.

3. How did regression tests protect the refactoring?

Regression tests helped us check that changes to the appointment service and data store did not break existing functionality. After refactoring, we reran tests covering booking conflicts, cancellations, appointment retrieval and repeated cancellations. All tests passed, confirming that the existing functionality continued to work as expected.

## K. Ten formative questions

#### 1. What should an engineer do before changing code in response to a failure? 
First, attempt to determine the cause of the failure, and ensure there is a good understanding of the full context of the failure within the program (e.g. objects/variables/functions involved). After determining the cause and nature of the failure, attempt to make a minor iterative change to mitigate the failure, repeating until a solution is found.
  
#### 2. Where should expected behaviour come from during debugging? 
Expected behaviour should be described in a document outlining the intended purpose of the program, ideally a sequence diagram.
  
#### 3. What is a debugging hypothesis? 
A debugging hypothesis is an expectation of what issues may exist in the program based on an individual's knowledge and personal interpretation of the program logic, structure, and design. These expectations can be informed through empirical evidence via error handling and exceptions.
  
#### 4. What is a regression test and why is it retained? 
A regression test is a test that is performed regularly throughout the development process to ensure that features remain functional after changes are made to the program. The test is retained so it can be executed again after a change.
  
#### 5. What is meant by root cause? 
The 'root cause' of a failure is the point of failure that can be best attributed as the primary cause for that specific failure.
  
#### 6. What is refactoring? 
Refactoring is the process of rewriting code for the purpose of improvement in a specific area, e.g. overall performance or coherent structure, without changing its functionality.
  
#### 7. What is a swallowed exception? 
A swallowed exception is an exception that has been caught without any handling of the exception, subsequently allowing the program to continue.
  
#### 8. What is a code smell? 
A code smell is a general indication that something is semantically wrong with the code, not necessarily that is it not functional, moreso code that may be difficult to maintain or add features to if it is not refactored.
  
#### 9. How should GitHub Copilot-generated debugging diagnoses be treated? 
With a great deal of skepticism and methodical verification and validation. Each claim should be individually assessed and validated as an actual concern before being addressed.
  
#### 10. What is the Stage 8 engineering rule? 
 Structure software for change, not just execution.

## L. Completion and handover

- [x] Existing project, earlier tests and stage records preserved.
- [x] Passing Stage 7 SHA and safe preparation details recorded.
- [x] Both defects reproduced with meaningful failing tests.
- [x] Both human hypotheses recorded before Copilot; actual suggestions evaluated with evidence.
- [x] Supported causes and minimal repairs explained; focused and full regression results recorded.
- [x] One genuine refactor verified under passing before/after tests.
- [x] Human PR review, feedback resolution and integrated retest recorded.
- [x] Tutorial, three reflections and ten formative responses complete.
- [x] Local recovery metadata excluded from submitted source.
- [x] Same project and full suite ready for Stage 9 after Stage 8 integration, verification and recording.

Verified integrated code SHA / result: see I.
Submitted SHA and evidence-only difference if any: [complete]
Unresolved issues or incomplete checks / owner / next action: [complete]
Handover note: [complete]
