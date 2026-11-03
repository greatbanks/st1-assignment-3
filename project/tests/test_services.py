
"""Tests for the Stage 6 SmartCare service methods."""

from datetime import datetime

import pytest

from smartcare.data_store import SmartCareDataStore
from smartcare.domain import AppointmentStatus
from smartcare.services import (
    AppointmentService,
    PatientService,
    PractitionerService,
)


@pytest.fixture
def services():
    store = SmartCareDataStore()

    patients = PatientService(store)
    practitioners = PractitionerService(store)
    appointments = AppointmentService(store)

    patient = patients.register_patient("P001", "Alex Smith")
    practitioner = practitioners.register_practitioner(
        "PR001", "Dr Taylor", "General Practice"
    )

    return store, patients, practitioners, appointments, patient, practitioner


def test_find_patient_returns_stored_patient(services):
    store, patients, _, _, patient, _ = services

    assert patients.find_patient("P001") is patient
    assert store.find_patient("P001") is patient


def test_find_patient_unknown_id_raises_lookup_error(services):
    _, patients, _, _, _, _ = services

    with pytest.raises(LookupError):
        patients.find_patient("UNKNOWN")


@pytest.mark.parametrize("patient_id", ["", "   "])
def test_find_patient_blank_id_raises_value_error(services, patient_id):
    _, patients, _, _, _, _ = services

    with pytest.raises(ValueError):
        patients.find_patient(patient_id)


def test_find_practitioner_returns_stored_practitioner(services):
    store, _, practitioners, _, _, practitioner = services

    assert practitioners.find_practitioner("PR001") is practitioner
    assert store.find_practitioner("PR001") is practitioner


def test_find_practitioner_unknown_id_raises_lookup_error(services):
    _, _, practitioners, _, _, _ = services

    with pytest.raises(LookupError):
        practitioners.find_practitioner("UNKNOWN")


@pytest.mark.parametrize("practitioner_id", ["", "   "])
def test_find_practitioner_blank_id_raises_value_error(
    services, practitioner_id
):
    _, _, practitioners, _, _, _ = services

    with pytest.raises(ValueError):
        practitioners.find_practitioner(practitioner_id)


def test_cancel_appointment_returns_same_stored_object(services):
    store, _, _, appointments, _, _ = services

    appointment = appointments.book_appointment(
        "A001",
        "P001",
        "PR001",
        datetime(2026, 11, 4, 10, 0),
    )

    cancelled = appointments.cancel_appointment("A001")

    assert cancelled is appointment
    assert store.find_appointment("A001") is appointment
    assert appointments.find_appointment("A001") is appointment
    assert appointment.status is AppointmentStatus.CANCELLED


def test_cancel_unknown_appointment_raises_lookup_error(services):
    _, _, _, appointments, _, _ = services

    with pytest.raises(LookupError):
        appointments.cancel_appointment("UNKNOWN")


@pytest.mark.parametrize("appointment_id", ["", "   "])
def test_cancel_blank_appointment_id_raises_value_error(
    services, appointment_id
):
    _, _, _, appointments, _, _ = services

    with pytest.raises(ValueError):
        appointments.cancel_appointment(appointment_id)


def test_cancelling_twice_raises_value_error_without_changing_state(services):
    _, _, _, appointments, _, _ = services

    appointment = appointments.book_appointment(
        "A002",
        "P001",
        "PR001",
        datetime(2026, 11, 5, 10, 0),
    )

    appointments.cancel_appointment("A002")
    original_status = appointment.status

    with pytest.raises(ValueError):
        appointments.cancel_appointment("A002")

    assert appointment.status is original_status
    assert appointment.status is AppointmentStatus.CANCELLED


def test_completed_appointment_cannot_be_cancelled(services):
    _, _, _, appointments, _, _ = services

    appointment = appointments.book_appointment(
        "A003",
        "P001",
        "PR001",
        datetime(2026, 11, 6, 10, 0),
    )

    # Set up a completed appointment for this transition test.
    appointment._status = AppointmentStatus.COMPLETED

    with pytest.raises(ValueError):
        appointments.cancel_appointment("A003")

    assert appointment.status is AppointmentStatus.COMPLETED
