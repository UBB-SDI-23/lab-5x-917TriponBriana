from django.urls import path

# from .Views.AddConsultationsViews import AddConsultations
from .Views.ConsultationViews import ConsultationDetail, ConsultationInfo, AddConsultations
from .Views.DentistViews import DentistDetail, DentistInfo
# from .Views.MedicationByAvgDentAgeViews import MedicationByAvgDentistAge
# from .Views.MedicationByNoOfDentistsViews import MedicationByNumberOfOtherDentistsPrescribed
from .Views.MedicationDentistViews import MedicationDentistDetail, MedicationDentistInfo
from .Views.MedicationViews import MedicationDetail, MedicationInfo, MedicationByAvgDentistAge, MedicationByNumberOfOtherDentistsPrescribed
# from .Views.PatientIdsViews import PatientIds
# from .Views.PatientOlderThan10Views import PatientOlderThan18
from .Views.PatientViews import PatientDetail, PatientInfo, PatientIds, PatientOlderThan18

# from .views import PatientDetail, PatientInfo, DentistInfo, DentistDetail, PatientOlderThan18, ConsultationDetail, \
#     ConsultationInfo, PatientIds, MedicationByNumberOfOtherDentistsPrescribed, AddConsultations
# from .views import MedicationDetail, MedicationInfo, MedicationDentistDetail, MedicationDentistInfo, MedicationByAvgDentistAge


urlpatterns = [
    path("patient/", PatientDetail.as_view(), name="clin"),
    path("patient/<int:id>/", PatientInfo.as_view()),
    path("patient/older-than-18/", PatientOlderThan18.as_view()),
    path("patient/patient-ids/", PatientIds.as_view()),

    path("dentist/", DentistDetail.as_view(), name="clin"),
    path("dentist/<int:id>/", DentistInfo.as_view()),

    path("consultation/", ConsultationDetail.as_view(), name="clin"),
    path("consultation/<int:id>/", ConsultationInfo.as_view()),
    path("consultation/<int:id>/patient/", AddConsultations.as_view()),

    path("medication/", MedicationDetail.as_view(), name="clin"),
    path("medication/<int:id>/", MedicationInfo.as_view()),

    path("medication-dentist/", MedicationDentistDetail.as_view(), name="clin"),
    path("medication-dentist/<int:id>/", MedicationDentistInfo.as_view()),
    path("medication/order-by-avg-dentist-age/", MedicationByAvgDentistAge.as_view()),
    path("medication/by-number-of-other-dentists/", MedicationByNumberOfOtherDentistsPrescribed.as_view()),
]
