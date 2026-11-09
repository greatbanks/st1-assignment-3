# Stage 7 Testing and Verification Record

Group/tutorial: [complete]  Members/cohorts: [complete]
Requirements baseline: SmartCare A3 Requirements Baseline 2026, revision 2.
Use the same project/. Link actual evidence; keep responses concise. Blank fields are for your group. Copy rows only as needed.

All Assignment 3 stage materials are provided from the beginning. Complete this stage only after the previous applicable stage has been integrated, verified and recorded. Use this supplied record in stage07/ in your EXISTING repository. Preserve project/, all earlier tests, records and responses. Do not download another starter or copy staff solutions.

## A Tutorial Activities

### Activity 1 Requirement to test

For each requirement, propose one positive test, one negative test and the key assertion.

| Requirement                         | Positive test | Negative test | Key assertion |
| ----------------------------------- | ------------- | ------------- | ------------- |
| FR-01 Register patient              |               |               |               |
| FR-05 Prevent practitioner conflict |               |               |               |
| FR-06 Cancel appointment            |               |               |               |
| FR-07 Retain cancelled history      |               |               |               |

### Activity 2 Strong or weak assertion

For each, select Strong for stated behaviour or Weak/unclear and explain why. State the behaviour and limits.

`assert True`
Judgement: [Strong for stated behaviour / Weak/unclear]  Why: [response]

`assert appointment is not None`
Judgement: [Strong for stated behaviour / Weak/unclear]  Why: [response]

`assert appointment.status == AppointmentStatus.CANCELLED`
Judgement: [Strong for stated behaviour / Weak/unclear]  Why: [response]

`assert len(results) > 0`
Judgement: [Strong for stated behaviour / Weak/unclear]  Why: [response]

`assert data_store.find_appointment('A1') is appointment`
Judgement: [Strong for stated behaviour / Weak/unclear]  Why: [response]

### Activity 3 Boundary thinking

Design boundary or edge cases for blank identifiers, whitespace-only names, same-time practitioner bookings, cancelled appointments and invalid status transitions.
For each input/state, expected result and supporting contract: [response]

| Input | State | Expected result | Supporting contract |
|-------|-------|-----------------|---------------------|
|       |       |                 |                     |

### Activity 4 Critique GitHub Copilot tests

GitHub Copilot generates five tests, all of which pass. Two only assert that objects are not None, one asserts True, and two assume SMS notifications exist. Identify what is wrong and rewrite the test intentions.

| Candidate | What is wrong | Rewritten test intention |
| --------- | ------------- | ------------------------ |
| 1         |               |                          |
| 2         |               |                          |
| 3         |               |                          |
| 4         |               |                          |
| 5         |               |                          |

### Tutorial exit question

Why can 100% code coverage coexist with poor software verification?
[response]

## B Requirement to Test Traceability Matrix

Assign TEST IDs before implementation or generation. Use canonical AC IDs with their actual meaning; quote supporting revision 2 contracts when no canonical AC is assigned. Blank-ID validation is not AC-01.2. Identify supplied versus student-authored evidence.

| Requirement                                                                                        | Acceptance criterion | Test ID                                                           | Test type | Test name / location | Expected behaviour                                                                                                                                             | Result / observed status | Supplied or student-authored |
|----------------------------------------------------------------------------------------------------|----------------------|-------------------------------------------------------------------|-----------|----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------|------------------------------|
| Valid required patient data with an unused ID is stored                                            | AC-01.1              | `test_patient_data_retained_while_id_unused()`                    | Positive  | [locate]             | When valid patient data is submitted with an unused ID, the data is stored regardless and is accessible                                                        | [results]                | Supplied                     |
| Registration with an existing patient ID is rejected                                               | AC-01.2              | `test_disallow_duplicate_id_on_registration()`                    | Negative  | [locate]             | Registration attempt with duplicate ID is rejected                                                                                                             | [results]                | Supplied                     |
| Same practitioner/exact time/scheduled conflicts; another practitioner at the same time is allowed | AC-04.1 & AC-04.2    | `test_allow_simultaneous_appointments_with_unique_practitioner()` | Positive  | [locate]             | When booking in a duplicate timeslot, confirm that the practitioner name differs, and allow the appointment if the practitioners are distinct, disallow if not | [results]                | Supplied                     |
| Repeat cancellation is rejected                                                                    | AC-05.1              | `test_reject_repeat_cancellations()`                              | Negative  | [locate]             | If a cancellation has been performed on an existing appointment, prevent the cancellation from being performed again                                           | [results]                | Supplied                     |
| Cancelled history remains retrievable in the current session                                       | AC-05.2              | `test_same_session_cancellation_retrieval()`                      | Positive  | [locate]             | Allow cancellations to be viewed within the same session, do not discard data until session ends                                                               | [results]                | Supplied                     |

## C Test Design

Use descriptive test names such as `test_cancel_changes_status()` or `test_blank_patient_id_is_rejected()`. Explain what new evidence each case adds.

| Test ID                                                           | Requirement                                                                                        | Acceptance criterion | Positive / Negative / Boundary | Test intention                                                                                                                            | Observable result expected                                                                             | Added evidence beyond supplied tests |
|-------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|----------------------|--------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|--------------------------------------|
| `test_patient_data_retained_while_id_unused()`                    | Valid required patient data with an unused ID is stored                                            | AC-01.1              | Positive                       | Ensure valid patient data with unused ID is retained                                                                                      | Valid patient data is accessible regardless of ID status                                               | Not applicable                       |
| `test_disallow_duplicate_id_on_registration()`                    | Registration with an existing patient ID is rejected                                               | AC-01.2              | Negative                       | Ensure registration attempt(s) with duplicate ID(s) is/are rejected                                                                       | Logic prevents duplicate IDs being registered                                                          | Not applicable                       |
| `test_allow_simultaneous_appointments_with_unique_practitioner()` | Same practitioner/exact time/scheduled conflicts; another practitioner at the same time is allowed | AC-04.1 & AC-04.2    | Positive                       | Ensure bookings can be created under existing timeslots with differing practitioners, but not identical practitioners                     | Multiple appointments can be booked with the same time value provided the practitioner is not the same | Not applicable                       |
| `test_reject_repeat_cancellations()`                              | Repeat cancellation is rejected                                                                    | AC-05.1              | Negative                       | Ensure that if a cancellation has been performed on an existing appointment, prevent any subsequent cancellations on the same appointment | Prevent cancellations from occuring more than once for the same booking                                | Not applicable                       |
| `test_same_session_cancellation_retrieval()`                      | Cancelled history remains retrievable in the current session                                       | AC-05.2              | Positive                       | Ensure cancellations can be viewed within the same session, and that data is not made inaccessible before the session ends                | Cancellation info is not retained after program is restarted, but is still available before a restart  | Not applicable                       |

## D Arrange Act Assert Record

Arrange test data; act on one meaningful behaviour; assert the required observable outcome. Use the specific current exception with pytest.raises where needed.

| Test ID | Arrange | Act | Assert | Why meaningful / why assertion proves criterion |
| ------- | ------- | --- | ------ | ----------------------------------------------- |
|         |         |     |        |                                                 |
|         |         |     |        |                                                 |
|         |         |     |        |                                                 |
|         |         |     |        |                                                 |
|         |         |     |        |                                                 |

## E Domain Test Evidence

Cover Patient/Practitioner construction and validation; Appointment construction, initial status, cancellation and illegal/repeated transitions. Preserve the four reference intentions described in handout Part C.

| Test ID | Behaviour | Test file/function | Result |
| ------- | --------- | ------------------ | ------ |
|         |           |                    |        |
|         |           |                    |        |
|         |           |                    |        |

## F Service Test Evidence

Use fresh shared SmartCareDataStore state, registered objects and completed Stage 6 services.

| Test ID | Behaviour | Requirement / criterion | Test file/function | Result |
| ------- | --------- | ----------------------- | ------------------ | ------ |
|         |           |                         |                    |        |
|         |           |                         |                    |        |
|         |           |                         |                    |        |

## G Negative and Boundary Cases

Connect cases to actual contracts and verify unchanged state after rejection.

| Behaviour | Boundary/invalid input | Expected result | Test ID |
| --------- | ---------------------- | --------------- | ------- |
|           |                        |                 |         |
|           |                        |                 |         |
|           |                        |                 |         |

## H GitHub Copilot Test Design

Select ONE real acceptance criterion. Complete human-first fields before using Copilot. Do not require an accepted generated test.

| Prompt                           | Response           |
| -------------------------------- | ------------------ |
| Requirement                      | Cancel only a Scheduled Appointment. Any invalid transitions such as repeated cancellationsmust raise ValueError and leave the state unchanged.                          |
| Acceptance criterion             |AC-05.1 — "Repeat cancellation is rejected."|
| Behaviour to test                |If an appointment has already been cancelled, attempting to cancel it again must be rejected. The appointment must remain in the CANCELLED state.|
| Human-first test idea/categories | Arranging a valid scheduled appointment. Cancel once successfully. Attempt to cancel the same appointment again. Check the second attempt will raise ValueError and the appointment stays as CANCELLED. This is a negative and invalid state-transition test.      |
| Prompt and purpose               |Ask Github Copilot to suggest pytest cases for repeated appointment cancellation by using the existing Smartcare implementation and public contracts.The purpose is to indentify and critically assess useful tests and whether they verify the actual requirements. |

For each significant candidate, copy this entry as needed:

| Prompt                                    | Response                                      |
| ----------------------------------------- | --------------------------------------------- |
| Copilot test idea/candidate               | Verify that a scheduled appointment can be cancelled.                   |
| What it claims to verify                  |A scheduled appointment transitions to CANCELLED.                          |
| Requirement trace                         |FR-06, but this mainly tests the successful cancellation criterion, not AC-05.3.|
| Assertion quality                         |Checking appointment.status == AppointmentStatus.CANCELLED is meaningful and observable.                                    | 
| Human critique                            | Valid test idea, but it does not test repeated cancellation. |
| Decision                                  |Reject as a separate AC-05.3 candidate.|
| Reason                                    |It duplicates the successful cancellation behaviour rather than testing rejection of a second cancellation.|
| Final test reference if accepted/modified |Not retained separately.|
| Actual verification result                |Not executed|

| Prompt                                    | Response                                      |
| ----------------------------------------- | --------------------------------------------- |
| Copilot test idea/candidate               | Cancel an appointment once, then attempt cancellation again and expect ValueError.|
| What it claims to verify                  |Repeated cancellation is rejected.|
| Requirement trace                         |	FR-06, AC-05.3.|
| Assertion quality                         |pytest.raises(ValueError) checks the expected exception type.| 
| Human critique                            |This directly tests the acceptance criterion. The test should use the public Appointment.cancel() method and a valid appointment setup.|
| Decision                                  |Modify|
| Reason                                    |Keep this test, but combine it with Candidate 3 to also verify that the appointment's state remains CANCELLED.|
| Final test reference if accepted/modified |To be added if the modified test is implemented.|
| Actual verification result                |Not executed|

| Prompt                                    | Response                                      |
| ----------------------------------------- | --------------------------------------------- |
| Copilot test idea/candidate               | Check that the appointment remains CANCELLED after the second cancellation attempt is rejected.|
| What it claims to verify                  |An invalid repeated cancellation does not change the appointment's state.|
| Requirement trace                         |FR-06, AC-05.3|
| Assertion quality                         |Checking the public status property is an observable assertion| 
| Human critique                            |Strong assertion, but it overlaps with Candidate 2 and should be included in the same test rather than duplicated.|
| Decision                                  |Modify|
| Reason                                    |Combine with Candidate 2 to verify both rejection and unchanged state in one test.|
| Final test reference if accepted/modified |To be added if the modified test is implemented.|
| Actual verification result                |Not executed|

| Prompt                                    | Response                                      |
| ----------------------------------------- | --------------------------------------------- |
| Copilot test idea/candidate               |Test repeated cancellation through the shared SmartCareDataStore and retrieve the appointment afterwards.|
| What it claims to verify                  |The appointment remains stored and cancelled after a rejected second attempt.|
| Requirement trace                         |FR-06, AC-05.3|
| Assertion quality                         |Checking the stored appointment's status is useful. Checking object identity is less important to the acceptance criterion.| 
| Human critique                            |checking the stored record is useful, but Copilot's code calls store.cancel_appointment(), which is not a method on SmartCareDataStore. It also uses incorrect constructor arguments and does not register its patient and practitioner before adding the appointment.|
| Decision                                  |Reject as written.|
| Reason                                    |The generated code does not match the actual public API and would fail before testing the intended behaviour.|
| Final test reference if accepted/modified |Not retained.|
| Actual verification result                |Not executed|


Before accepting: traces to a requirement/criterion; can fail for the right reason; assertion checks required behaviour; no invented business rule; no unnecessary private implementation dependence. Reject/modify weak assertions, invented requirements, excessive mocking, duplicates, wrong exceptions, obsolete architecture and unnecessary dependencies.

## I Weak Copilot Test Reflection

Which Copilot-generated test looked convincing but was weak? 

Candidate 4 - the store-level repeated cancellation test: looked convincing because it attempted to test cancellation through the shared SmartCareDataStore and retrieve the appointment afterwards.

Why was it weak? 

code used store.cancel_appointment(), which does not match the actual SmartCareDataStore public API. Also contained incorrect constructor arguments and incomplete setup for the appointment. Therefore, the test would not reliably reach the behaviour it was intended to verify.

How did you strengthen it? 

retained the idea of checking observable appointment state, but focused the test on the public Appointment.cancel() method. The improved test performs an initial cancellation, checks that a second cancellation raises ValueError, and verifies that the appointment remains in the CANCELLED state.

Candidate 1: Rejected- tests successful cancellation rather than repeated cancellation.

Candidate 2: Modified-retained the ValueError assertion.

Candidate 3: Modified- combined the unchanged-state assertion with Candidate 2.

Candidate 4: Rejected- uses an incorrect API and invalid setup.

See the individual candidate evaluations in Section H. No generated test was claimed as executed.

## J Regression Run

Run python -m pytest from project/. Retain all accumulated tests. Record the tested SHA accurately.

| Command    | Working directory | Code SHA   | Passed     | Failed     | Failure summary | Product defect / test defect / unresolved | Evidence and interpretation |
| ---------- | ----------------- | ---------- | ---------- | ---------- | --------------- | ----------------------------------------- | --------------------------- |
|            |                   |            |            |            |                 |                                           |                             |
|            |                   |            |            |            |                 |                                           |                             |
|            |                   |            |            |            |                 |                                           |                             |

Individual test runs and changed-order independence evidence: [commands, results, links]
Optional tutor-led demonstration notes: [optional; leave blank if not used]
A meaningful test should detect a relevant incorrect result. Students do not have to perform the demonstration or submit failure/restoration evidence for assessment. The tutor restores the example and reruns its tests. This is not a Stage 8 fault activity.
Requirement → test → failure/observation → diagnosis → change → verification: [concise links where applicable]

## K What the Suite Still Does Not Prove

What does your test suite still not prove? [response]
Coverage if used: [result or not used]
Which uncovered areas matter, and why does coverage percentage alone not establish correctness? [response]
Optional fixtures/parametrisation used and why, if any: [response or not used]

## L Git and Review Evidence

Use links rather than copying GitHub history. Continue the Stage 6 workflow; no commit/PR count, conflict or individual test quota is imposed.

| Issue/task | Branch     | PR         | Reviewer   | Key feedback | Outcome    |
| ---------- | ---------- | ---------- | ---------- | ------------ | ---------- |
|            |            |            |            |              |            |
|            |            |            |            |              |            |
|            |            |            |            |              |            |

## M Contribution Evidence

Record actual work in test design, implementation, review, traceability, diagnosis, necessary fixes and integration. Do not include confidential peer ratings.

| Member     | Actual contribution | Evidence link |
| ---------- | ------------------- | ------------- |
|            |                     |               |
|            |                     |               |
|            |                     |               |

## N Formative Questions

1. What question does verification answer?
[response]

2. What question does validation answer?
[response]

3. What is a unit test?
[response]

4. What is a pytest fixture?
[response]

5. What is parametrisation in pytest?
[response]

6. What is regression testing?
[response]

7. What does code coverage tell us, and what does it not prove?
[response]

8. What makes an assertion weak?
[response]

9. What is the appropriate role of GitHub Copilot as a test assistant?
[response]

10. What is the Stage 7 engineering rule?
[response]

## O Stage Completion

Tested Stage 7 main SHA: [complete]
Full-suite result: [complete]
Unresolved defects and effect on baseline: [complete or none]
Clean working tree and integration evidence: [complete]
Stage 8 handover status: [complete; no Stage 8 work assigned]
All tutorial/formative responses and traceability/Copilot decisions complete: [confirm]
