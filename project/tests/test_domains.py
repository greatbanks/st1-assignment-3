from datetime import datetime

import pytest

from smartcare.domain import (
    Appointment,
    AppointmentStatus,
    Patient,
    Practitioner)

TIME_SLOT = datetime(2026, 10, 1, 9)

def test_construction_rejects_blank_fields_and_trims_valid_text() -> None:
    patient = Patient(" P1 "," Alex Example ")
    assert patient.patient_id == "P1"
    assert patient.name == "Alex Example"

    practitioner = Practitioner(" D1 "," Taylor Example "," General ")
    assert practitioner.practitioner_id == "D1"
    assert practitioner.specialty == "General"

    with pytest.raises(ValueError):
        Patient("P1","")
    with pytest.raises(ValueError):
        Practitioner("D1","Taylor Example","")


def test_completed_appointment_cannot_be_cancelled() -> None:
    appointment = Appointment(
        "A1",
        Patient("P1","Alex Example"),
        Practitioner("D1","Taylor Example","General"),
        TIME_SLOT,
        AppointmentStatus.COMPLETED)

    with pytest.raises(ValueError):
        appointment.cancel()

    assert appointment.status is AppointmentStatus.COMPLETED