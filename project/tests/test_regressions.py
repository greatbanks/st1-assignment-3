"""Stage 8 regression tests"""

from datetime import datetime

import pytest

from smartcare.data_store import SmartCareDataStore
from smartcare.domain import AppointmentStatus
from smartcare.services import (
    AppointmentService,
    PatientService,
    PractitionerService,
)


TIME_SLOT = datetime(2026, 10, 1, 9)


@pytest.fixture()
def booking_store() -> SmartCareDataStore:
    """fresh isolated store per test"""
    return SmartCareDataStore()


@pytest.fixture()
def booking_service(booking_store: SmartCareDataStore) -> AppointmentService:
    """appointment service over the fixture store with synthetic clinic objects"""
    patients = PatientService(booking_store)
    patients.register_patient("P1", "Alex Example")
    patients.register_patient("P2", "Ash Example")

    practitioners = PractitionerService(booking_store)
    practitioners.register_practitioner("D1", "Taylor Example", "General")
    practitioners.register_practitioner("D2", "Sam Example", "General")

    return AppointmentService(booking_store)


def test_f8_01_same_practitioner_conflict_rejected_other_practitioner_allowed(
        booking_store: SmartCareDataStore, booking_service: AppointmentService) -> None:
    first = booking_service.book_appointment("A1", "P1", "D1", TIME_SLOT)

    with pytest.raises(ValueError):
        booking_service.book_appointment("A2", "P2", "D1", TIME_SLOT)
    assert booking_store.find_appointment("A2") is None
    assert booking_store.list_appointments() == [first]

    other = booking_service.book_appointment("A3", "P2", "D2", TIME_SLOT)
    assert other.practitioner.practitioner_id == "D2"
    assert other.status is AppointmentStatus.SCHEDULED
    assert booking_store.list_appointments() == [first, other]


def test_f8_02_cancelled_appointment_retained_and_retrievable(
        booking_store: SmartCareDataStore, booking_service: AppointmentService) -> None:
    booked = booking_service.book_appointment("A1", "P1", "D1", TIME_SLOT)
    booking_service.cancel_appointment("A1")

    assert booked.status is AppointmentStatus.CANCELLED
    assert booking_store.list_appointments() == [booked]
    assert booking_store.find_appointment("A1") is booked
    assert booking_service.find_appointment("A1") is booked

    with pytest.raises(ValueError):
        booking_service.cancel_appointment("A1")
    assert booked.status is AppointmentStatus.CANCELLED
    assert booking_store.list_appointments() == [booked]
