from TBP_2d import TwoD_TBP
import pydicom

data = {
    "study": {
                "StudyDescription": "Total Body Photography Scan", 
                "StudyDate": "2024-09-01", 
                "StudyTime": "12:00:00", 
                "StudyID": "1234",
                "AcquisitionDate": "2024-09-01"
            },
    "metadata": { 
        "type": "VL",
    },
    "patient": {
        "PatientName": "Adarsh",
        "PatientID": "007",
        "PatientBirthDate": "2000-07-26",
        "PatientSex": "M",
        "PatientAge": "18",
        "PatientWeight": "200",  # in kgs only
        "AdditionalPatientHistory": "Has a history of carcinoma in the family."
    },
    "series": {
         "SeriesDescription": "CT Scan",
                "SeriesDate": "2024-09-01",
                "SeriesTime": "12:00:00",
                "SeriesNumber": "1"
    }
}

# def read_dicom_file(file_path):
#     dicom_data = pydicom.dcmread(file_path)
#     return dicom_data

# file_path = "/mnt/c/Users/cadar/Projects/Lumo/dicom-tbp/code/dcm/data.dcm"
# read_dcm = read_dicom_file(file_path)
# print(read_dcm)
dcm = TwoD_TBP(data)
dcm.add_VL_Image_Calibration_Module()

print(dcm.dcm)
