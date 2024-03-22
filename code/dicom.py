import pydicom
from pydicom.dataset import Dataset, FileMetaDataset
from pydicom.uid import generate_uid
from utils import assign_if_exists, process_date, process_time, pad_age
class DICOM:
    """
    Represents a DICOM object.
    
    Attributes:
        dcm (pydicom.Dataset): The DICOM dataset.
    """
    def __init__(self, data) -> None:
        self.dcm = pydicom.Dataset()
        self.dcm.file_meta = self.init_metadata(data["metadata"])

        self.dcm.is_little_endian = True
        self.dcm.is_implicit_VR = True
        self.dcm.SpecificCharacterSet= 'ISO_IR 100'
        
        self.dcm.Manufacturer= 'Lumo Imaging'
        self.dcm.SoftwareVersions = 'LumoTrackv1'
        self.dcm.ContentQualification = 'RESEARCH'

        self.init_patient(data["patient"])
        self.init_study(data["study"])
        self.init_series(data["series"])
        self.save_dataset("./data.dcm")
        

    def init_metadata(self, metadata):
        """
        Initializes the metadata of the DICOM file.
        
        Args:
            metadata (Metadata): The metadata object containing the type of DICOM file.
        
        Sample Usage:
            metadata = Metadata(type="DER")
            init_metadata(metadata)
        """
        # File meta info data elements
        file_meta = FileMetaDataset()
        
        file_meta.FileMetaInformationGroupLength = 192
        file_meta.FileMetaInformationVersion = b'\x00\x01'
        if metadata["type"] == "DER":
            file_meta.MediaStorageSOPClassUID = '1.2.840.10008.5.1.4.1.1.77.1.7'
        elif metadata["type"] == "RI":
            file_meta.MediaStorageSOPClassUID = '1.2.840.10008.5.1.4.1.1.77.1.4'
        elif metadata["type"] == "3D-OBJ":
            file_meta.MediaStorageSOPClassUID = '1.2.840.10008.5.1.4.1.1.104.4'
        else:
            # Default SOPClassUID
            file_meta.MediaStorageSOPClassUID = '1.2.840.10008.5.1.4.1.1.77.1.4'

        file_meta.MediaStorageSOPInstanceUID = generate_uid()
        # check: https://github.com/pydicom/pydicom/blob/5612f566179fbbdcd5f935ccddef1443d8974662/doc/old/image_data_handlers.rst#L45
        file_meta.TransferSyntaxUID = '1.2.840.10008.1.2'
        file_meta.ImplementationClassUID = '1.2.276.0.5013353.3.0.3.6.1'
        file_meta.ImplementationVersionName = 'LUMOSCANv1'
        file_meta.SourceApplicationEntityTitle = 'LUMOSCAN'
        return file_meta
    
    def init_study(self, study):
        """
        Initializes the study attributes of the DICOM object.
        
        Args:
            study (dict): The study attributes.
            
        Sample Usage:
            study = {
                "StudyDescription": "Total Body Photography Scan", 
                "StudyDate": "2024-09-01", 
                "StudyTime": "12:00:00", 
                "StudyID": "1234",
                "AcquisitionDate": "2024-09-01"
            }
            init_study(study)
        """
        self.dcm.StudyInstanceUID = generate_uid()
        self.dcm.StudyDescription = study["StudyDescription"]
        self.dcm.StudyDate = process_date(study["StudyDate"])
        self.dcm.StudyTime = process_time(study["StudyTime"])
        self.dcm.AcquisitionDate = process_date(study["AcquisitionDate"])
        self.dcm.StudyID = study["StudyID"]
    
    def init_patient(self, patient):
        """
        Initializes the patient attributes of the DICOM object.
        
        Args:
            patient (dict): The patient attributes.
            
        Sample Usage:
            patient = {
                "PatientName": "Adarsh",
                "PatientID": "007",
                "PatientBirthDate": "26-07-2000",
                "PatientSex": "M",
                "PatientAge": "18",
                "PatientWeight": "200",  # in kgs only
                "AdditionalPatientHistory": "Has a history of carcinoma in the family."
            }
            init_patient(patient)
        """
        self.dcm.PatientName = assign_if_exists(patient["PatientName"])
        self.dcm.PatientID = assign_if_exists(patient["PatientID"])
        self.dcm.PatientBirthDate = process_date(assign_if_exists(patient["PatientBirthDate"]))
        self.dcm.PatientSex = assign_if_exists(patient["PatientSex"])
        self.dcm.PatientAge = pad_age(patient["PatientAge"]) if assign_if_exists(patient["PatientAge"]) != "" else ""
        self.dcm.PatientWeight = assign_if_exists(patient["PatientWeight"])
        self.dcm.AdditionalPatientHistory = assign_if_exists(patient["AdditionalPatientHistory"])
        
    def init_series(self, series):
        """
        Initializes the series attributes of the DICOM object.
        
        Args:
            series (dict): The series attributes.
            
        Sample Usage:
            series = {
                "SeriesDescription": "CT Scan",
                "SeriesDate": "2024-09-01",
                "SeriesTime": "12:00:00",
                "SeriesNumber": "1"
            }
            init_series(series)
        """
        self.dcm.SeriesInstanceUID = generate_uid()
        self.dcm.SeriesDescription = series["SeriesDescription"]
        self.dcm.SeriesDate = process_date(series["SeriesDate"])
        self.dcm.SeriesTime = process_time(series["SeriesTime"])
        self.dcm.SeriesNumber = series["SeriesNumber"]
        
    def save_dataset(self, path):
        """
        Saves the DICOM dataset to the specified path.

        Args:
            path (str): The path to save the dataset.

        Sample Usage:
            dcm = DICOM()
            # Initialize the DICOM object
            # ...
            dcm.save_dataset("/path/to/save/dataset.dcm")
        """
        self.dcm.save_as(path)
        
    


