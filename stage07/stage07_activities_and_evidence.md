# Stage 7 Testing and Verification Record

Group/tutorial: Online Group 1, Tuesday 17:30  Members/cohorts: u3281958, u3217894, u3309034    
Requirements baseline: SmartCare A3 Requirements Baseline 2026, revision 2.
Use the same project/. Link actual evidence; keep responses concise. Blank fields are for your group. Copy rows only as needed.

All Assignment 3 stage materials are provided from the beginning. Complete this stage only after the previous applicable stage has been integrated, verified and recorded. Use this supplied record in stage07/ in your EXISTING repository. Preserve project/, all earlier tests, records and responses. Do not download another starter or copy staff solutions.

## A Tutorial Activities

### Activity 1 Requirement to test

For each requirement, propose one positive test, one negative test and the key assertion.

| Requirement                          | Positive test                                                                                                                                                                                                                          | Negative test                                                                                                                                              | Key assertion                                                                                                                                                                                     |
|--------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| FR-01 Register patient               | Register a patient through the service with a valid unused ID and non-blank name (P1, Alex Example)                                                                                                                                    | Register a second patient with an ID already in store.                                                                                                     | Positive: data_store.find_patient(“P1”) is returned patient, and returned_patient.name == “Alex Example”. Negative: ValueError raised, and the stored name is unchanged.                          |
| FR-05 Prevent practitioner conflict  | Register patients P1, P2 and P3, and practitioners D1 and D2. Book A1 for P1 to see D1 at datetime (2026,10,1,9). Then call book_appointment(“A2”, “P2”, “D2”, datetime(2026,10,1,9), a different practitioner for the same time slot. | A1 already booked, call book_appointment(“A3”, “P3”, “D1”, datetime (2026,10,1,9)), the same practitioner for the same time slot with a different patient. | Positive: data_store.find_appointment(“A2”) as status AppointmentStatus.SCHEDULED. Negative: ValueError raised, date_store.find_appointment(“A3”) is None                                         |
| FR-06 Cancel appointment             | Book an appointment, then AppointmentService(data_store).cancel_appointment(A1)                                                                                                                                                        | Call on cancel_appointment again                                                                                                                           | Positive: Returned object’s status is stored with status is AppointmentStatus.SCHEDULED. Negative: ValueError raised and status remains AppointmentStatus.CANCELLED, leaving the state unchanged. |
| FR-07 Retain cancelled history       | Cancel a SCHEDULED appointment, then retrieve it by ID.                                                                                                                                                                                | Retrieve an appointment ID that was never booked.                                                                                                          | Positive: data_store.find_appointment(A1) is AppointmentStatus.CANCELLED. Negative: LookupError raised and no appointment created.                                                                |

### Activity 2 Strong or weak assertion

For each, select Strong for stated behaviour or Weak/unclear and explain why. State the behaviour and limits.

`assert True`
Judgement: Unclear  Why: If the code works or not, the result can only be true. It doesn’t state any requirements, and the outcome establishes nothing that can be observed and interpreted. 

`assert appointment is not None`
Judgement: Weak/unclear  Why: It can be useful for a sanity check otherwise it provides an outcome that has nothing to interpret. We can get a return, but it doesn’t show that the appointment is the right one, with correct fields, or that it was stored.

`assert appointment.status == AppointmentStatus.CANCELLED`
Judgement: Strong for stated behaviour  Why: It clearly checks that after an appointment is cancelled, its status is changed to CANCELLED. Otherwise, any other outcome would fail the required behaviour.

`assert len(results) > 0`
Judgement: Weak/unclear  Why: It only answers for if the list of results is empty or holds 1 or more items. It doesn’t specify the actual count of items in the list or call on any other specification within the results list.

`assert data_store.find_appointment('A1') is appointment`
Judgement: Strong for stated behaviour  Why: It proves that the booked appointment object has been stored and is retrievable, although it does not specify anything about the appointment details. 

### Activity 3 Boundary thinking

Design boundary or edge cases for blank identifiers, whitespace-only names, same-time practitioner bookings, cancelled appointments and invalid status transitions.
For each input/state, expected result and supporting contract: 

| Input                           | State                                                                                                                                       | Expected result                                                                        | Supporting contract                                                                                                                                                                                                              |
|---------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Blank identifier                | Patient(“”, “Alex Example”)                                                                                                                 | ValueError                                                                             | Public validation and state contracts: “IDs are strings, trimmed, non-blank, and case-sensitive.                                                                                                                                 |
| White-space only name           | Patient(“P1”, “”)                                                                                                                           | ValueError                                                                             | FR-01: Register a patient with a unique ID and required name.                                                                                                                                                                    |
| Same-time practitioner bookings | D1 has an existing appointment booked for specific timeslot. Another appointment attempted to be SCHEDULED for the same timeslot for the D1 | ValueError (nothing stored)                                                            | BR-05: Same practitioner + exact time + SCHEDULED conflicts; different practitioner at the same time is allowed. AC-04.1/04.2: Same practitioner/exact time/SCHEDULED conflicts; another practitioner at that time is permitted. |
| Cancelled appointment           | Cancelled appointment                                                                                                                       | Retrieved statues == AppointmentStatus.CANCELLED, cancelling again raises ValueError   | BR-06: Only SCHEDULED can be cancelled. AC-05.1: Scheduled cancellation changes status.                                                                                                                                          |
| Invalid status transition       | Cancel a COMPLETED appointment                                                                                                              | ValueError, status stays COMPLETED                                                     | BR-06: Only SCHEDULED can be cancelled. BR-08: Statuses are SCHEDULED, CANCELLED and COMPLETED. COMPLETED may be a test fixture; no completion workflow is required.                                                             |

### Activity 4 Critique GitHub Copilot tests

GitHub Copilot generates five tests, all of which pass. Two only assert that objects are not None, one asserts True, and two assume SMS notifications exist. Identify what is wrong and rewrite the test intentions.

| Candidate  | What is wrong                                                                                         | Rewritten test intention                                                                                                                                    |
|------------|-------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1          | Superficial, only returns that something exists, doesn’t establish anything specific.                 | Assert a specific required outcome (e.g. after cancelling an appointment, it is still retrievable and has a CANCELLED status.                               |
| 2          | Superficial, only returns that something exists, doesn’t establish anything specific.                 | Assert a specific required outcome.                                                                                                                         |
| 3          | Doesn’t provide evidence. Assertion can’t fail so it passes behaviour, even if the code is incorrect. | Assert a required observable result (e.g. registering a valid patient).                                                                                     |
| 4          | Assumption extends the scope of the problem and tests a feature beyond the application.               | Replace with an assertion that test the actual features of the application (e.g. for AppointmentStatus: cancelling a SCHEDULED changes status to CANCELLED) |
| 5          | Assumption extends the scope of the problem and tests a feature beyond the application.               | Replace with an assertion that test the actual features of the application.                                                                                 |

### Tutorial exit question

Why can 100% code coverage coexist with poor software verification?
It’s possible to create a test that spans the whole program and asserts one thing. That would be 100% coverage but does not verify anything specific: business rules, acceptance criteria, or required behaviour. Therefore, 100% code coverage can coexist with poor software verification.

## B Requirement to Test Traceability Matrix

Assign TEST IDs before implementation or generation. Use canonical AC IDs with their actual meaning; quote supporting revision 2 contracts when no canonical AC is assigned. Blank-ID validation is not AC-01.2. Identify supplied versus student-authored evidence.

| Requirement                                                                                        | Acceptance criterion | Test ID                                                           | Test type | Test name / location           | Expected behaviour                                                                                                                                             | Result / observed status   | Supplied or student-authored |
|----------------------------------------------------------------------------------------------------|----------------------|-------------------------------------------------------------------|-----------|--------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------|------------------------------|
| Valid required patient data with an unused ID is stored                                            | AC-01.1              | `test_patient_data_retained_while_id_unused()`                    | Positive  | project/tests/test_services.py | When valid patient data is submitted with an unused ID, the data is stored regardless and is accessible                                                        | Passed, green [20%]        | Student-authored             |
| Registration with an existing patient ID is rejected                                               | AC-01.2              | `test_disallow_duplicate_id_on_registration()`                    | Negative  | project/tests/test_services.py | Registration attempt with duplicate ID is rejected                                                                                                             | Passed, green [40%]        | Student-authored             |
| Same practitioner/exact time/scheduled conflicts; another practitioner at the same time is allowed | AC-04.1 & AC-04.2    | `test_allow_simultaneous_appointments_with_unique_practitioner()` | Positive  | project/tests/test_services.py | When booking in a duplicate timeslot, confirm that the practitioner name differs, and allow the appointment if the practitioners are distinct, disallow if not | Passed, green [60%]        | Student-authored             |
| Repeat cancellation is rejected                                                                    | AC-05.1              | `test_reject_repeat_cancellations()`                              | Negative  | project/tests/test_services.py | If a cancellation has been performed on an existing appointment, prevent the cancellation from being performed again                                           | Passed, green [80%]        | Student-authored             |
| Cancelled history remains retrievable in the current session                                       | AC-05.2              | `test_same_session_cancellation_retrieval()`                      | Positive  | project/tests/test_services.py | Allow cancellations to be viewed within the same session, do not discard data until session ends                                                               | Passed, green [100%]       | Student-authored             |
| Appointment state transitions are guarded                                                          | AC-05.1              | `test_completed_appointment_cannot_be_cancelled()`                | Negative  | project/tests/test_domains.py  | A COMPLETED appointment refuses cancellation and keeps COMPLETED status                                                                                        | Passed, green [50%]        | Student-authored             |
| Patient/practitioner required fields are validated                                                 | AC-01.1              | `test_construction_rejects_blank_fields_and_trims_valid_text()`   | Boundary  | project/tests/test_domains.py  | Blank required fields raise ValueError and a valid text is trimmed and kept                                                                                    | Passed, green [100%]       | Student-authored             |

## C Test Design

Use descriptive test names such as `test_cancel_changes_status()` or `test_blank_patient_id_is_rejected()`. Explain what new evidence each case adds.

| Test ID                                                           | Requirement                                                                                        | Acceptance criterion | Positive / Negative / Boundary | Test intention                                                                                                                            | Observable result expected                                                                              | Added evidence beyond supplied tests |
|-------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|----------------------|--------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|--------------------------------------|
| `test_patient_data_retained_while_id_unused()`                    | Valid required patient data with an unused ID is stored                                            | AC-01.1              | Positive                       | Ensure valid patient data with unused ID is retained                                                                                      | Valid patient data is accessible regardless of ID status                                                | Not applicable                       |
| `test_disallow_duplicate_id_on_registration()`                    | Registration with an existing patient ID is rejected                                               | AC-01.2              | Negative                       | Ensure registration attempt(s) with duplicate ID(s) is/are rejected                                                                       | Logic prevents duplicate IDs being registered                                                           | Not applicable                       |
| `test_allow_simultaneous_appointments_with_unique_practitioner()` | Same practitioner/exact time/scheduled conflicts; another practitioner at the same time is allowed | AC-04.1 & AC-04.2    | Positive                       | Ensure bookings can be created under existing timeslots with differing practitioners, but not identical practitioners                     | Multiple appointments can be booked with the same time value provided the practitioner is not the same  | Not applicable                       |
| `test_reject_repeat_cancellations()`                              | Repeat cancellation is rejected                                                                    | AC-05.1              | Negative                       | Ensure that if a cancellation has been performed on an existing appointment, prevent any subsequent cancellations on the same appointment | Prevent cancellations from occurring more than once for the same booking                                | Not applicable                       |
| `test_same_session_cancellation_retrieval()`                      | Cancelled history remains retrievable in the current session                                       | AC-05.2              | Positive                       | Ensure cancellations can be viewed within the same session, and that data is not made inaccessible before the session ends                | Cancellation info is not retained after program is restarted, but is still available before a restart   | Not applicable                       |

## D Arrange Act Assert Record

Arrange test data; act on one meaningful behaviour; assert the required observable outcome. Use the specific current exception with pytest.raises where needed.

| Test ID                                                           | Arrange                                                                                                    | Act                                                                                                          | Assert                                                                                            | Why meaningful / why assertion proves criterion                                                                                                                                                  |
|-------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `test_patient_data_retained_while_id_unused()`                    | New SmartCareDataStore and PatientService.find_patient('P1) raises LookupError, indicating ID is unused.   | register_patient('P1', 'Alex Example')                                                                       | find_patient('P1')                                                                                | Arrange sets up that the ID is not used, and assertion proves that patient can now be retired from the store. Together, showing registration stored the patient, which proves criterion AC-01.1. |
| `test_disallow_duplicate_id_on_registration()`                    | Register 'P1', 'Alex Example' and keep patient object.                                                     | register_patient('P1', 'Replace') inside pytest.raises(ValueError)                                           | Raised error. find_patient('P1') is the original, name is unchanged, and len(list_patient()) == 1 | An implementation could raise a ValueError after replacing the existing patient, which would violate  AC-01.2. The test also asserts that the stored object is still the original.               |
| `test_allow_simultaneous_appointments_with_unique_practitioner()` | Register 'P1', 'P2', 'D1', 'D2'. Book appointment A1 for 'P1' with 'D1' at TIME_SLOT = datetime(26,10,1,9) | Book A2 for 'P2' with 'D1' during TIME_SLOT inside pytest.raises(ValueError), and then book A3 for 'P2' 'D2' | Raised error. data_store.find_appointment('A2') is None and A3 is SCHEDULED with 'D2'             | Using a different patient isolates the practitioner as the cause of conflict and None checks that that booking conflict is rejected. Assertion proves criterion AC-04.1 and AC-04.2.             |
| `test_reject_repeat_cancellations()`                              | Register 'P1' and 'D1', book A1, then cancel_appointment('A1') one time                                    | cancel_appointment('A1') a second time inside pytest.raises(ValueError)                                      | Raised error. find_appointment('A1').status is AppointmentStatus.CANCELLED                        | An illegal transition is made on the second cancellation and checking the status checks for an unchanged state. Assertion proves criterion AC-05.1.                                              |
| `test_same_session_cancellation_retrieval()`                      | Register 'P1' and 'D1', book A1 and keep appointment object                                                | cancel_appointment('A1') on the same store                                                                   | find_appointment('A1') status is CANCELLED and list_appointments() == original                    | In one session the tests cancels A1, then looks it up, which returns the original object with a CANCELLED status retained in list_appointments(). Assertion proves AC-05.2.                      |

## E Domain Test Evidence

Cover Patient/Practitioner construction and validation; Appointment construction, initial status, cancellation and illegal/repeated transitions. Preserve the four reference intentions described in handout Part C.

| Test ID                                                         | Behaviour                                                                                                       | Test file/function                                                                         | Result |
|-----------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|--------|
| `test_completed_appointment_cannot_be_cancelled()`              | required_text trims valid Patient and Practitioner fields on construction and raises ValueError for blanks ones | project/tests/test_domains.py::test_completed_appointment_cannot_be_cancelled              | Passed |
| `test_construction_rejects_blank_fields_and_trims_valid_text()` | A COMPLETED appointment refuses cancel() and keeps original status                                              | project/tests/test_domains.py::test_construction_rejects_blank_fields_and_trims_valid_text | Passed |

## F Service Test Evidence

Use fresh shared SmartCareDataStore state, registered objects and completed Stage 6 services.

| Test ID                                                           | Behaviour                                                                                                                              | Requirement / criterion | Test file/function                                                                            | Result |
|-------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|-------------------------|-----------------------------------------------------------------------------------------------|--------|
| `test_patient_data_retained_while_id_unused()`                    | Registering a patient with an unsued ID store the patient object so it can be retrieved again                                          | AC-0.1                  | project/tests/test_services.py::test_patient_data_retained_while_id_unused                    | Passed |
| `test_disallow_duplicate_id_on_registration()`                    | Registering with an existing patient ID is rejected and the original record is unchanged                                               | AC-01.2                 | project/tests/test_services.py::test_disallow_duplicate_id_on_registration                    | Passed |
| `test_allow_simultaneous_appointments_with_unique_practitioner()` | Double booking a practitioner in the same time slot is rejected, but booking a different practitioner in the same time slot is allowed | AC-04.1 & AC-04.2       | project/tests/test_services.py::test_allow_simultaneous_appointments_with_unique_practitioner | Passed |
| `test_reject_repeat_cancellations()`                              | Cancelling an already cancelled appointment is rejected and the status stays CANCELLED                                                 | AC-05.1                 | project/tests/test_services.py::test_reject_repeat_cancellations                              | Passed |
| `test_same_session_cancellation_retrieval()`                      | A cancelled appointment is retriable with status CANCELLED, through the store in the current session                                   | AC-05.2                 | project/tests/test_services.py::test_same_session_cancellation_retrieval                      | Passed |

## G Negative and Boundary Cases

Connect cases to actual contracts and verify unchanged state after rejection.

| Behaviour                                                    | Boundary/invalid input                                                      | Expected result | Test ID                                                            |
|--------------------------------------------------------------|-----------------------------------------------------------------------------|-----------------|--------------------------------------------------------------------|
| Patient lookup before registration                           | ID "P1" absent from store                                                   | LookupError     | test_patient_data_retained_while_id_unused                         |
| Patient register with a duplicate ID                         | Existing valid ID "P1" reused with a different name ("Replace")             | ValueError      | test_disallow_duplicate_id_on_registration                         |
| Practitioner booking conflict                                | Same practitioner "D1" and timeslot has two existing SCHEDULED appointments | ValueError      | test_allow_simultaneous_appointments_with_unique_practitioner      |
| Repeat calculation on the same appointment                   | A second cancel_appointment("A1") on an appointment already CANCELLED       | ValueError      | test_reject_repeat_cancellations                                   |
| Patient/Practitioner construction with blank required fields | Patient("P1",""), Practitioner("D1", "Taylor Example". "")                  | ValueError      | test_completed_appointment_cannot_be_cancelled                     |
| Cancelling a non SCHEDULED (COMPLETED) appointment           | Appointments with status COMPLETED are passed to cancel()                   | ValueError      | test_construction_rejects_blank_fields_and_trims_valid_text        |

## H GitHub Copilot Test Design

Select ONE real acceptance criterion. Complete human-first fields before using Copilot. Do not require an accepted generated test.

| Prompt                           | Response                                                                                                                                                                                                                                                             |
|----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Requirement                      | Cancel only a Scheduled Appointment. Any invalid transitions such as repeated cancellation must raise ValueError and leave the state unchanged.                                                                                                                      |
| Acceptance criterion             | AC-05.1 — "Repeat cancellation is rejected."                                                                                                                                                                                                                         |
| Behaviour to test                | If an appointment has already been cancelled, attempting to cancel it again must be rejected. The appointment must remain in the CANCELLED state.                                                                                                                    |
| Human-first test idea/categories | Arranging a valid scheduled appointment. Cancel once successfully. Attempt to cancel the same appointment again. Check the second attempt will raise ValueError and the appointment stays as CANCELLED. This is a negative and invalid state-transition test.        |
| Prompt and purpose               | Ask Github Copilot to suggest pytest cases for repeated appointment cancellation by using the existing Smartcare implementation and public contracts.The purpose is to indentify and critically assess useful tests and whether they verify the actual requirements. |

For each significant candidate, copy this entry as needed:

| Prompt                                     | Response                                                                                                    |
|--------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| Copilot test idea/candidate                | Verify that a scheduled appointment can be cancelled.                                                       |
| What it claims to verify                   | A scheduled appointment transitions to CANCELLED.                                                           |
| Requirement trace                          | FR-06, but this mainly tests the successful cancellation criterion, not AC-05.3.                            |
| Assertion quality                          | Checking appointment.status == AppointmentStatus.CANCELLED is meaningful and observable.                    | 
| Human critique                             | Valid test idea, but it does not test repeated cancellation.                                                |
| Decision                                   | Reject as a separate AC-05.3 candidate.                                                                     |
| Reason                                     | It duplicates the successful cancellation behaviour rather than testing rejection of a second cancellation. |
| Final test reference if accepted/modified  | Not retained separately.                                                                                    |
| Actual verification result                 | Not executed                                                                                                |

| Prompt                                     | Response                                                                                                                                |
|--------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Copilot test idea/candidate                | Cancel an appointment once, then attempt cancellation again and expect ValueError.                                                      |
| What it claims to verify                   | Repeated cancellation is rejected.                                                                                                      |
| Requirement trace                          | 	FR-06, AC-05.3.                                                                                                                        |
| Assertion quality                          | pytest.raises(ValueError) checks the expected exception type.                                                                           | 
| Human critique                             | This directly tests the acceptance criterion. The test should use the public Appointment.cancel() method and a valid appointment setup. |
| Decision                                   | Modify                                                                                                                                  |
| Reason                                     | Keep this test, but combine it with Candidate 3 to also verify that the appointment's state remains CANCELLED.                          |
| Final test reference if accepted/modified  | To be added if the modified test is implemented.                                                                                        |
| Actual verification result                 | Not executed                                                                                                                            |

| Prompt                                     | Response                                                                                                           |
|--------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| Copilot test idea/candidate                | Check that the appointment remains CANCELLED after the second cancellation attempt is rejected.                    |
| What it claims to verify                   | An invalid repeated cancellation does not change the appointment's state.                                          |
| Requirement trace                          | FR-06, AC-05.3                                                                                                     |
| Assertion quality                          | Checking the public status property is an observable assertion                                                     | 
| Human critique                             | Strong assertion, but it overlaps with Candidate 2 and should be included in the same test rather than duplicated. |
| Decision                                   | Modify                                                                                                             |
| Reason                                     | Combine with Candidate 2 to verify both rejection and unchanged state in one test.                                 |
| Final test reference if accepted/modified  | To be added if the modified test is implemented.                                                                   |
| Actual verification result                 | Not executed                                                                                                       |

| Prompt                                     | Response                                                                                                                                                                                                                                                               |
|--------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Copilot test idea/candidate                | Test repeated cancellation through the shared SmartCareDataStore and retrieve the appointment afterwards.                                                                                                                                                              |
| What it claims to verify                   | The appointment remains stored and cancelled after a rejected second attempt.                                                                                                                                                                                          |
| Requirement trace                          | FR-06, AC-05.3                                                                                                                                                                                                                                                         |
| Assertion quality                          | Checking the stored appointment's status is useful. Checking object identity is less important to the acceptance criterion.                                                                                                                                            | 
| Human critique                             | checking the stored record is useful, but Copilot's code calls store.cancel_appointment(), which is not a method on SmartCareDataStore. It also uses incorrect constructor arguments and does not register its patient and practitioner before adding the appointment. |
| Decision                                   | Reject as written.                                                                                                                                                                                                                                                     |
| Reason                                     | The generated code does not match the actual public API and would fail before testing the intended behaviour.                                                                                                                                                          |
| Final test reference if accepted/modified  | Not retained.                                                                                                                                                                                                                                                          |
| Actual verification result                 | Not executed                                                                                                                                                                                                                                                           |


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

| Command                                 | Working directory | Code SHA                                  | Passed | Failed | Failure summary             | Product defect / test defect / unresolved            | Evidence and interpretation          |
|-----------------------------------------|-------------------|-------------------------------------------|--------|--------|-----------------------------|------------------------------------------------------|--------------------------------------|
| python -m pytest tests/test_domain.py   | project/          | 67387c24c035620de4856dda52c8a1d8fec2cbfd  | Passed |        |                             |                                                      | ran command and passed in the green  |
| python -m pytest tests/test_services.py | project/          | ffbaa1e3507b2da728c59dc2cf1cc7409435201d  |        | Failed | Raised implementation error | Did not merge appointment cancellation into main yet | Checked main and it didn't have it   |
| python -m pytest tests/test_services.py | project/          | 0ca4e086d28f97bf1b3cbbac61c4cd887c2ad2e9  | Passed |        |                             |                                                      | ran command and passed in the green  |
| python -m pytest                        | project/          | 0ca4e086d28f97bf1b3cbbac61c4cd887c2ad2e9  | Passed |        |                             |                                                      | ran command and passed in the green  |

Individual test runs and changed-order independence evidence: [python -m pytest/tests/test_domain.py -> 2 passed], [python -m pytest/tests/test_services.py -> 3 passed, 2 failed before the fix, then after the fix 5 passed]
Optional tutor-led demonstration notes: [optional; leave blank if not used]
A meaningful test should detect a relevant incorrect result. Students do not have to perform the demonstration or submit failure/restoration evidence for assessment. The tutor restores the example and reruns its tests. This is not a Stage 8 fault activity.
Requirement → test → failure/observation → diagnosis → change → verification: 
[AC-05.1 and AC-05.2 -> test_reject_repeat_cancellations, test_same_session_cancellation_retrievable -> NotImplementedError (stage 6: appointment cancellation) -> AppointmentService.cancel_appointment raises NotImplementedError -> implemented the method -> Rerun and both tests pass]

## K What the Suite Still Does Not Prove

What does your test suite still not prove? Cancelling an appointment ID that doesn't exist, which should raise LookupError.
Coverage if used: not used
Which uncovered areas matter, and why does coverage percentage alone not establish correctness? Cancelling an appointment that doesn't exist. No test calls cancel_appointment with an unregistered ID like "A999", which should raise LookupError. Our cancellation tests only use the existing "A1" appointment ID.
Optional fixtures/parametrisation used and why, if any: not used

## L Git and Review Evidence

Use links rather than copying GitHub history. Continue the Stage 6 workflow; no commit/PR count, conflict or individual test quota is imposed.

| Issue/task              | Branch                | PR                                                      | Reviewer | Key feedback | Outcome      |
|-------------------------|-----------------------|---------------------------------------------------------|----------|--------------|--------------|
| Write the domain tests  | tests/test_domains    | https://github.com/greatbanks/st1-assignment-3/pull/11  | James    | Satisfied    | Implementing |
| Write the service tests | tests/test_service.py | https://github.com/greatbanks/st1-assignment-3/pull/10  | Jerald   | Satisfied    | Implemented  |

## M Contribution Evidence

Record actual work in test design, implementation, review, traceability, diagnosis, necessary fixes and integration. Do not include confidential peer ratings.

| Member | Actual contribution                                                                                       | Evidence link                                                                                                                                                       |
|--------|-----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| James  | Worked on sections B and C, and reviewed tests/test_domains                                               | https://github.com/greatbanks/st1-assignment-3/commit/3ad13339e0fd07e10e76992c46ac4596ba549680                                                                      |
| Janel  | Completed sections A, D, E, F, G, J, K, L, M and N. Finalised sections B and C, and wrote and fixed tests | https://github.com/greatbanks/st1-assignment-3/pull/10 and https://github.com/greatbanks/st1-assignment-3/pull/11/changes/67387c24c035620de4856dda52c8a1d8fec2cbfd  |
| Jerald | Completed AI sections H and I, and reviewed and merged service tests                                      | https://github.com/greatbanks/st1-assignment-3/pull/8/changes/b9072d18a526ec8705c000adee1c462090033d2f                                                              |

## N Formative Questions

1. What question does verification answer?
Verification answers if the specification document is being supported by the program. It checks that the functional requirements, business rules, and acceptance criterions are being satisfied.

2. What question does validation answer?
Validation answers if the program actually solves the problem or meets the needs of the client or the end user. It also checks that the program fits in real-world application.

3. What is a unit test?
A unit test is done to verify that one piece of the program works as intended. For example, testing that a COMPLETED appointment cannot be CANCELLED would test a singular behaviour of one method.

4. What is a pytest fixture?
The pytest fixture is an instance or a set of data that is defined and can be passed into tests, creating a reusable test object. Conceptually, it’s like creating a variable for a test object at a default state.  

5. What is parametrisation in pytest?
The pytest parametrisation works the opposite of a fixture, rather than allowing for multiple tests to use a predefined instance of data, it focuses on allowing one test in a single run to go through multiple different data inputs. Testing the parameters of that method/function with different arguments. 

6. What is regression testing?
Regression testing is retesting a feature or unit of code after updating, debugging, or deleting a feature to make sure that the change did not break or negatively affect the features that already work. The scope of the test depends on the scale of the change, ranging from changing an integer to float to upgrading an entire engine. 

7. What does code coverage tell us, and what does it not prove?
Code coverage tells us how much code is being covered in a test but cannot tell us what is being verified, showing quantity not quality.

8. What makes an assertion weak?
An assertion is weak if it is too vague and cannot give us an observable outcome for something specific.  

9. What is the appropriate role of GitHub Copilot as a test assistant?
As a test assistance, GitHub Copilot is a candidate generator for a draft rather than having any authority over the final revision. 

10. What is the Stage 7 engineering rule?
Every test executed in the SmartCare application must validate a specific requirement and provide evidence that proves the required behaviour. 

## O Stage Completion

Tested Stage 7 main SHA: complete
Full-suite result: complete
Unresolved defects and effect on baseline: none
Clean working tree and integration evidence: complete
Stage 8 handover status: Stage 8 work partly assigned
All tutorial/formative responses and traceability/Copilot decisions complete: confirm
