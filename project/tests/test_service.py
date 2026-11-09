from datetime import datetime
import pytest

from smartcare.data_store import SmartCareDataStore
from smartcare.domain import AppointmentStatus
from smartcare.services import (AppointmentService, PatientService, PractitionerService)


TIME_SLOT = datetime(2026, 10, 1, 9)


def booked_store():
    """A fresh SmartCareDataStore per test"""
    store = SmartCareDataStore()

    PatientService(store).register_patient("P1", "Alex Example")
    PatientService(store).register_practitioner("D1", "Taylor Example", "General")
    service = AppointmentService(store) # shortened as a variable
    appointment = service.book_appointment("A1", "P1", "D1", TIME_SLOT)

    return store, service, appointment


def test_patient_data_retained_while_id_unused() -> None:
    patients = PatientService(SmartCareDataStore())
    with pytest.raises(LookupError):
        patients.find_patient("P1")

    patient = patients.register_patient("P1", "Alex Example")

    assert patients.find_patient("P1") is patient
    assert patient.name == "Alex Example"


def test_disallow_duplicate_id_on_registration() -> None:
    store = SmartCareDataStore()
    patients = PatientService(store)
    original = patients.register_patient("P1", "Alex Example")

    with pytest.raises(ValueError):
        patients.register_patient("P1", "Replace")

    assert patients.find_patient("P1") is original
    assert original.name == "Alex Example"
    assert len(store.list_patients()) == 1


def test_allow_simultaneous_appointments_with_unique_practitioner() -> None:
    store, service, _ = booked_store()
    PractitionerService(store).register_patient("P2", "Ash Example")
    PractitionerService(store).register_practitioner("D2", "Sam Example", "General")

    with pytest.raises(ValueError):
        AppointmentService.book_appointment("A2", "P2", "D1", TIME_SLOT)

    other = AppointmentService.book_appointment("A3", "P2", "D2", TIME_SLOT)
    assert other.practitioner.practitioner_id("D2")
    assert other.status is AppointmentStatus.SCHEDULED


def test_reject_cancellation() -> None:
    _, service, _ = booked_store()
    service.cancel_appointment("A1")

    with pytest.raises(ValueError):
        service.cancel_appointment("A1")

    assert service.find_appointment("A1").status is AppointmentStatus.CANCELLED


def test_same_session_cancellation_retrieval() -> None:
    store, service, original_app = booked_store()

    service.cancel_appointment("A1")

    assert service.find_appointment("A1") is original_app
    assert original_app.status is AppointmentStatus.CANCELLED
    assert service.list_appointments() == [original_app]