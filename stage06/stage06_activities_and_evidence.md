# Stage 6 activities and evidence

Complete this one group record. Link actual issues, diffs, tests and reviews; avoid copying entire histories. Blank fields are intentional. Duplicate rows as needed. Use synthetic data only. Every member records their own meaningful contribution. Do not invent results, reviews or Copilot use.

- Group/tutorial: 

[Tuesday, 17:30]

- Members, GitHub usernames and cohorts: 

| Members          | GitHub Usernames | Cohort             |
| Janel Alfaro     | JVA101           | UG, Online Group 1 |
| James Greatbanks | greatbanks       | UG, Online Group 1 |
| Jerald Charanjit | Jerald420        | UG, Online Group 1 |

- Repository URL:

https://github.com/greatbanks/st1-assignment-3

- Starting SHA: 

2D8BE34BD18382C1E9FA4E5C4364330FAE5C593B52B3B9FCACD098EE2871E482

## A Requirement to issue activities

### FR-02 Patient Search

- **Title:**

PatientService.find_patient feature to be built 

- **Context:**

Currently have the python skeleton for the feature, but it has not been developed. 

- **Requirement:**

(FR-02) Find a patient by patient ID.

- **Acceptance criteria:**

Return the registered patient or raise LookupError for absence and ValueError for a blank/invalid ID.

- **Scope:**

(class method) 

- **Definition of Done:**

Stage 6 instructions are followed, team member develops the feature, the feature is reviewed and then merged too main.

- **Owner:**

Janel

- **Actual issue link:**

https://github.com/greatbanks/st1-assignment-3/issues/4

### FR-06 Appointment Cancellation with FR-07 retained history

- **Title:**

AppointmentService.cancel_appointment  feature to be built

- **Context:**

The SmartCare application currently provides the appointment domain model and a cancellation mechanism, but the AppointmentService.cancel_appointment feature has not yet been developed. 

- **Requirement:**

**FR-06:** Cancel only a SCHEDULED appointment. 

**FR-07:** Retain the same appointment with CANCELLED status in current-session history.  

- **Acceptance criteria:**

1. Cancel through the domain method and retain the appointment. 
2. Return the cancelled object.  
3. An unknown appointment ID raises LookupError. 
4. A blank or invalid appointment ID raises ValueError. 
5. Invalid transitions (repeated cancellation and cancellation from COMPLETED) raise ValueError and leave state unchanged. 

- **Scope:**

AppointmentService.cancel_appointment in project/smartcare/services.py 

- **Definition of Done:**

The cancellation feature is developed according to FR-06 and FR-07. Successful and unsuccessful cancellation scenarios are covered by meaningful automated tests. Existing tests continue to pass. The changes are committed and pushed to a focused feature branch, reviewed by another team member through a pull request, and merged into main after approval and successful integration testing. 

- **Owner:**

Jerald 

- **Actual issue link:**

https://github.com/greatbanks/st1-assignment-3/issues/1 

## B: Commit quality

| Original example                               | Strong or weak | Reason                                                                                                |
| ---                                            | ---            | ---                                                                                                   |
| changes                                        | Weak           | Ambiguous, does not provide any specific information about changes or features added/modified/removed |
| final version                                  | Weak           | Provides no context to the version history, or the purpose of the commit                              |
| Add patient search by ID                       | Strong         | Provides specific details about the feature added with no ambiguity                                   |
| fix stuff                                      | Weak           | Ambiguous, does not provide any specific information about changes or features added/modified/removed |
| Prevent cancellation of completed appointments | Strong         | Provides specific details about the feature added with no ambiguity                                   |


## C: Over scoped PR review

A cancellation PR also renames unrelated patient fields, restructures unrelated code and adds a new dependency.

### Response

The content of this PR should, when following best practices, only effect the parts of the codebase that directly pertain to appointment management and/or cancellation. However, the scope of this PR will affect code that is not relevant to the main issue (appointment cancellation) that the PR has been created to resolve and is therefore out-of-scope/over-scoped.
 
The responsibility of managing the content of the PR should be shared equally between multiple team members, mainly the owner/manager of the repository, and the author of the PR. Both parties should vet the PR for features that are out-of-scope and include/discard as deemed fit.
 
The architectural implications for this PR reach beyond the functionality and logic of appointment management into patient information. It is unclear what the impacts of “restructuring unrelated code” and adding a “new dependency” would be, but it is reasonable to assume that it may unexpectedly change the architecture of the program. The testing implications for this question couldn’t be reasonably assumed without knowing more specific information, but this kind of over-scoped PR will always add more complexity and testing overhead to any software project. 
 
Any code that is not directly relevant to the change or feature that the PR is intended to add or resolve should be either discarded or split into its own feature branch to be considered for merging in future.

## D: Challenge a weak Copilot review

GitHub Copilot says: "Looks good; tests pass."

### Response

The response from Copilot in this instance does not provide any context for the test being performed, what the program actually is, what it does, or what behaviour it is expecting from the program. Without any additional context or information, this review is useless.
 
#### 5 follow-up questions: 

1. Describe the intended function of the program. 
2. Does the output of the program align with the intended output? 
3. What tests were performed on the program? 
4. Why was each test performed?
5. Are there any problems with the program that may cause the program to throw an unexpected exception/error that would not be caught by the tests performed on it? 

## E: Team workflow agreement

| Practice                            | Team agreement                                                                                                                                                              |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Branch naming                       | Use hyphenated variable names, short and descriptive, indicative of features they pertain to.                                                                                               |
| Commit message convention           | Max of ~60 characters when possible (prevents line being truncated on GitHub), describe the specific purpose of the commit, e.g.: “Fixed references to deprecated sections” |
| PR size                             | Try to limit scope to only files that absolutely must be changed to implement or change a specific feature.                                                                 |
| Another-member review requirement   | All code must be reviewed by at least 2 people (including the author) before being merged.                                                                                  |
| Merge rule                          | Merges will be discussed with all members of the group unless a specific feature will not have to interface with any other code – then it will be discussed between the author and the owner of the repo (James). Copilot usage should be disclosed between group members and recorded for posterity and submission when applicable.                                                                                                                                                                            |
| Significant Copilot disclosure rule |  Merges will be discussed with all members of the group unless a specific feature will not have to interface with any other code – then it will be discussed between the author and the owner of the repo (James). Copilot usage should be disclosed between group members and recorded for posterity and submission when applicable.                                                                                                                                                                            |
| Agree who sets up the shared repository and how ownership/review rotates | James owns the shared repository and is responsible for creating all PRs on behalf of other members. Review rotates between the repository owner and the author of the code, or Janel and Jerald between themselves if James is unavailable. |


## F: Issue and backlog index

Create at least two focused issues. Add a linked practitioner-lookup issue or an explicit supporting criterion with the tutor if needed to cover all three service targets.

| Issue link | Requirement                                                                                                   | Owner                          | Acceptance criteria or precise link                                                                                                                                                                                                                                                                                           | Status |
|------------|---------------------------------------------------------------------------------------------------------------|--------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
| [issue 4]  | FR-02: Find patient by patient ID.                                                                            | Janel                          | Return the stored patient or raise LookupError for absence and ValueError for a blank/invalid ID.                                                                                                                                                                                                                             | Closed |
| [issue 6]  | FR-02: Find patient by patient ID.                                                                            | Janel                          | Return the stored patient or raise LookupError for absence and ValueError for a blank/invalid ID.                                                                                                                                                                                                                             | Closed |
| [issue 1]  | FR-06: Allow scheduled appointments to be cancelled, & FR-07: Cancelled appointments in the system’s history. | Jerald/Janel (revised version) | 1. Cancel a scheduled appointment and retain its history. 2. Return the cancelled object. 3. An unknown appointment ID raises LookupError. 4. A blank or invalid appointment ID raises ValueError. 5. Invalid transitions (repeated cancellation and cancellation from COMPLETED) raise ValueError and leave state unchanged. | Closed |

## G: Pull request evidence

Repeat this block per PR. Record actual events, not planned approvals.

| PR link and title:                                                         | <a href="https://github.com/greatbanks/st1-assignment-3/pull/3">link:</a> Completed Stage 6 TODO: find_practitioner                                       |
| Linked issue and requirement:                                              | <a href="https://github.com/greatbanks/st1-assignment-3/issues/4">link:</a> (FR-02) Find a patient by patient ID                                          |
| Feature branch:                                                            | `feature/patient-lookup`                                                                                                                                  |
| Changed behaviour:                                                         | from: NotImplementationError, to: captured requirements of the drafted issue                                                                              |
| Meaningful commits:                                                        | <a href="https://github.com/greatbanks/st1-assignment-3/pull/3/changes/c0e01cfa89d3758f31a850639d8081d4a578d125">link</a>                                 |
| Test command, directory and observed result:                               | `python main.py && python –m pytest`, `project/` , `8 passed [100%] - in green`                                                                           |
| Another-member reviewer:                                                   | James reviewed and approved for feature implementation                                                                                                    |
| Human observations recorded before Copilot:                                | N/A                                                                                                                                                       |
| Requirement, responsibilities, test assertions and unrelated-scope checks: | N/A                                                                                                                                                       |
| Key feedback:                                                              | N/A                                                                                                                                                       |
| Author response/change and verification:                                   | N/A                                                                                                                                                       |
| Reviewers recheck and approval:                                            | N/A                                                                                                                                                       |
| Merge outcome and SHA:                                                     | Merged into main, c0e01cfa89d3758f31a850639d8081d4a578d125                                                                                                |
| Significant Copilot assistance:                                            | Not used                                                                                                                                                  |
| Linked issue closure:                                                      | <a href="https://github.com/greatbanks/st1-assignment-3/issues/4">link</a>                                                                                |
| Each member updated main:                                                  | Confirmed                                                                                                                                                 |
| Integrated verification after merge:                                       | Confirmed in main, James merged the feature to main through GitHub’s website, `project/smartcare/services.py`, `c0e01cfa89d3758f31a850639d8081d4a578d125` |

| PR link and title:                                                         | <a href="https://github.com/greatbanks/st1-assignment-3/pull/5">link:</a> Completed Stage 6 TODO: find_practitioner                                                            |
| Linked issue and requirement:                                              | Stage 6 document did not require drafting this issue, otherwise it follows <a href="https://github.com/greatbanks/st1-assignment-3/issues/6">find_patient's</a> drafted issue. |
| Feature branch:                                                            | `feature/practitioner-lookup`                                                                                                                                                  |
| Changed behaviour:                                                         | from: `NotImplementationError`, to: captured requirements of the drafted issue                                                                                                 |
| Meaningful commits:                                                        | <a href="https://github.com/greatbanks/st1-assignment-3/pull/5/changes/76b55b181bb68a8817c88b301c8ad6ceedda6d9b">link</a>                                                      |
| Test command, directory and observed result:                               | `python main.py && python –m pytest`, `project/` , `8 passed [100%] - in green`                                                                                                |
| Another-member reviewer:                                                   | James reviewed and approved for feature implementation                                                                                                                         |
| Human observations recorded before Copilot:                                | N/A                                                                                                                                                                            |
| Requirement, responsibilities, test assertions and unrelated-scope checks: | N/A                                                                                                                                                                            |
| Key feedback:                                                              | N/A                                                                                                                                                                            |
| Author response/change and verification:                                   | N/A                                                                                                                                                                            |
| Reviewers recheck and approval:                                            | N/A                                                                                                                                                                            |
| Merge outcome and SHA:                                                     | Merged into main, `76b55b181bb68a8817c88b301c8ad6ceedda6d9b`                                                                                                                   |
| Significant Copilot assistance:                                            | Not used                                                                                                                                                                       |
| Linked issue closure:                                                      | Stage 6 document did not require drafting this issue, otherwise it follows <a href="https://github.com/greatbanks/st1-assignment-3/issues/6">find_patient's</a> drafted issue. |
| Each member updated main:                                                  | Confirmed                                                                                                                                                                      |
| Integrated verification after merge:                                       | Confirmed in main, James merged the feature to main through GitHub’s website, `project/smartcare/services.py`, `76b55b181bb68a8817c88b301c8ad6ceedda6d9b`                      |

| PR link and title:                                                         | <a href="https://github.com/greatbanks/st1-assignment-3/pull/7">Link:</a> Appointment cancellation                                                            |
| Linked issue and requirement:                                              | FR-06 Appointment Cancellation and FR-07 Retain History.                                                                                                      |
| Feature branch:                                                            | `feature/appointment-cancellation`                                                                                                                            |
| Changed behaviour:                                                         | AppointmentService.cancel_appointment() to allow scheduled appointments to be cancelled while retaining their history and updating their status to CANCELLED. |
| Meaningful commits:                                                        | <a href="https://github.com/greatbanks/st1-assignment-3/pull/7/changes/a9e8add287a1751db4b52527eaec91ad173387ac">Link</a>                                     |
| Test command, directory and observed result:                               | `python main.py && python –m pytest`, `project/` , `22 passed [100%] - in green`                                                                              |
| Another-member reviewer:                                                   | Janel reviewed and refined implementation                                                                                                                     |
| Human observations recorded before Copilot:                                | N/A                                                                                                                                                           |
| Requirement, responsibilities, test assertions and unrelated-scope checks: | N/A                                                                                                                                                           |
| Key feedback:                                                              | Reviewed the cancellation implementation and identified redundant logic in the Copilot suggestion.                                                            |
| Author response/change and verification:                                   | N/A                                                                                                                                                           |
| Reviewers recheck and approval:                                            | <a href="https://github.com/greatbanks/st1-assignment-3/pull/7">Link</a>                                                                                      |
| Merge outcome and SHA:                                                     | Merged into main, `a9e8add287a1751db4b52527eaec91ad173387ac`                                                                                                  |
| Significant Copilot assistance:                                            | Copilot suggested additional cancellation logic. We tested the suggestion and identified redundant behaviour, which was modified before being merged          |
| Linked issue closure:                                                      | <a href="https://github.com/greatbanks/st1-assignment-3/pull/7">Link</a>                                                                                      |
| Each member updated main:                                                  | Confirmed                                                                                                                                                     |
| Integrated verification after merge:                                       | Confirmed in main, James merged the feature to main through GitHub’s website, `project/smartcare/services.py`, `a9e8add287a1751db4b52527eaec91ad173387ac`     |

## H: Copilot collaboration record

Record meaningful required use, not every trivial completion. Repeat per significant interaction.

| Member and task:                                         | Jerald - Implementing AppointmentService.cancel_appointment() for appointment cancellation and history retention                                                                                                                                                                                                                                                                  |
| Prompt/purpose and relevant issue/diff:                  | Used Copilot to assist with the implementation as well as review appointment cancellation behaviour linked to FR-06 and FR-07. The aim was to ensure that only scheduled appointments can be cancelled and that all cancelled appointments remain in the systems history                                                                                                          |
| Summary of output:                                       | Copilot assistance which related to the cancellation implementation as well as handling of validation and error cases.                                                                                                                                                                                                                                                            |
| Human check against actual code, requirements and tests: | Tested Copilot's suggested approach against the existing implementation and requirements. Some of the suggested logic was redundant because the existing code already handled parts of the behaviour. This required reviewing the suggestion rather than adding duplicate logic as well as refining the implementation to keep it consistent with the existing project structure. |
| Decision — Accept/ Modify/Reject:                        | Modify                                                                                                                                                                                                                                                                                                                                                                            |
| Reason:                                                  | The redundant suggestion was not merged due to it causing conflict.                                                                                                                                                                                                                                                                                                                     |
| Verification/evidence:                                   |  <br>[GitHub PR link](https://github.com/greatbanks/st1-assignment-3/pull/7) appointment cancellation implementation. <br>Test command: python -m pytest <br>Result: 22 passed in 0.03s (100%).                                                                                                                                                                                   |

## I: Human versus Copilot review comparison

| Human reviewer noticed before consulting Copilot:                   | Some cancellation and validation behaviour was already handled by the existing code. |
| Copilot noticed:                                                    | Suggested additional cancellation and validation logic.                              |
| Overlap:                                                            | Both considered cancellation behaviour and validation.                               |
| What did the human reviewer notice that Copilot did not:            | The suggested logic duplicated existing functionality.                               |
| What did Copilot identify that the human reviewer initially missed: | An alternative approach to handling validation scenarios.                            |
| Unsupported or incorrect Copilot suggestion:                        | Some suggested logic was redundant.                                                  |
| Human judgement accepted, modified or rejected, and why:            | Modified                                                                             |
| Which evidence justified merge approval:                            | PR #7 and python -m pytest - 22 passed in 0.03s.                                     |

## J: Contributions

Repeat per member. Include only categories that describe actual work; write not applicable where appropriate. Pairing or mentoring can be supported by a short corroborated note.

| 1.  James                             |                                                                                                                            |
| ------------------------------------- |                                                                                                                            |
| Member:                               | James                                                                                                                      |
| Implementation:                       | Managed PRs and proofreading code                                                                                          |
| Testing:                              | Confirmed pytest output before merging                                                                                     |
| Review:                               | Proofreading code before merge                                                                                             |
| Issue refinement:                     | Noted ValueError handling in closed PR                                                                                     |
| Design and responsibility discussion: | No further input                                                                                                           |
| Debugging or integration:             | No further input                                                                                                           |
| Documentation or team support:        | Coordinating PRs, approvals, cancellations, repo management, writing responses and populating markdown file with responses |


| 2.  Janel                             |                                                                                                                |
| ------------------------------------- |                                                                                                                |
| Member:                               | Janel                                                                                                          |
| Implementation:                       | Passed pytest before pushing methods to branches:  <br>feature/patient-lookup <br>feature/practitioner\-lookup |
| Testing:                              | Drafted lookup contract issue, developed lookup contract codes, proofreading other member’s code               |
| Review:                               | Proofread cancellation contract’s issue draft and code.                                                        |
| Issue refinement:                     | Edited cancellation contract’s issue draft, provided feedback for cancel_appointment().                        |
| Design and responsibility discussion: | No further input                                                                                               |
| Debugging or integration:             | No further input                                                                                               |
| Documentation or team support:        | Communicated my PR’s, received support on GitHub knowledge, writing responses, and pulling.                    |


| 3.  Jerald                            |
| ------------------------------------- |
| Member:                               | Jerald                                                                                                                                                  |
| Implementation:                       | Implemented AppointmentService.cancel_appointment() for FR-06 and FR-07, allowing scheduled appointments to be cancelled while retaining their history. |
| Testing:                              | Ran python main.py and python -m pytest. All 22 tests passed (100%)                                                                                     |
| Review:                               | Reviewed the cancellation implementation and checked Copilot's suggestions against the existing code to identify redundant logic.                       |
| Issue refinement:                     | Contributed to refining issue #1 by addressing cancellation rules, validation and error-handling requirements.                                          |
| Design and responsibility discussion: | No further input                                                                                                                                        |
| Debugging or integration:             | No further input                                                                                                                                        |
| Documentation or team support:        | Contributed implementation and testing evidence with Copilot.                                                                                           |



## K: Exit question

Why is a high commit count not necessarily evidence of strong contribution?

### Exit question response

A high commit count has 0 correlation with strong contribution. A commit can be as small as a single character changed in a file. A total number of commits can be massively inflated, or deflated to one if you commit an entire codebase in one go. It is a meaningless metric. 

## L: Stage 6 formative questions

1. What is version control?

A means by which software development can be managed, keeping records of previous software versions, individual feature implementations, facilitating collaboration, and allowing rollbacks to previous versions.

2. Why is a feature branch useful?

Allows development or maintenance of a specific feature that may impact other parts of the software to stay isolated from the main repository, then merged when it has been tested and verified as functional.

3. What makes a commit a good engineering commit?

Descriptive and succint language, with any ambiguities or complex functionalities explained either in the commit message, or in comments/discussions related to the feature(s).

4. What is a pull request?

Requests for a specific feature (or files) to be merged into a repository.

5. What is the purpose of code review?

To catch potential bugs or logic that may cause issues with other aspects of the program, or with future features.

6. What does a Git diff show?

The difference between the content of two files, including deletions and additions.

7. What is a Definition of Done?

A self-defined set of criteria that, when met, assures the feature is completed.

8. What is the appropriate role of GitHub Copilot in pull-request review?

Identifying clerical errors, conflicts of interest within the repository, unforeseen issues.

9. Why should individual contribution not be judged only by commit count?

Commits can be any length - a member of a group who only corrects spelling mistakes in files with no software relevance (e.g. a README) could have the highest commit count on a project. The number has no direct correlation with the amount of work performed on any given task.

10. What is the Stage 6 engineering rule?

Ensuring coherent group collaboration processes, transparency between all parties, and maintaining a sensible approach to using version control and Git + GitHub to facilitate collaboration.

## M: Completion and handover

- Starting SHA: `567bac7ddcc11cea288d47efe423e35363a4d5ad`
- Final Stage 6 code SHA: `76b55b181bb68a8817c88b301c8ad6ceedda6d9b`
- Test command: `python -m test`
- Working directory: `/project/smartcare/`
- Observed result: All tests passed
- PR and another-member reviewer: <a href="https://github.com/greatbanks/st1-assignment-3/pull/3">Link 1,</a> <a href="https://github.com/greatbanks/st1-assignment-3/pull/5">Link 2,</a> <a href="https://github.com/greatbanks/st1-assignment-3/pull/7">Link 3</a>
- Unresolved issue or none: None
- Stage 7 handover status: Ready to continue
- Final submitted SHA if later than tested SHA: N/A

- [*] Three Stage 6 service targets completed and checked.
- [*] Original supplied tests retained and passing.
- [*] At least two focused issues link requirements and acceptance criteria.
- [*] Feature work reviewed by another member using the actual diff.
- [*] Human-first review and required Copilot comparison recorded.
- [*] Feedback resolved and approval recorded before merge.
- [*] Everyone pulled main and integrated checks passed.
- [*] Required activities, quiz responses and contribution notes completed.
- [*] Only synthetic data included; confidential peer material kept out.
- [*] Tutor can trace a requirement through issue, code, tests, PR and checkpoint.

Do not write a file's own future commit SHA into that file. Record the tested code SHA first, then commit the evidence; explain the difference when submitting.
