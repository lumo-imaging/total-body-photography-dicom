from dicom import DICOM
import tempfile
from pydicom.dataset import Dataset, FileDataset
import datetime
import os

class ThreeD_TBP(DICOM):
    def __init__(self, data):
        super().__init__(data)
        # Add any additional initialization code here
        self.threeD_attributes()
        
    def load_mesh(self, mesh_path):
        if os.path.exists(mesh_path) and (mesh_path.lower() in ['.pcd', '.obj' , '.mlt']):
            self.generate_dicom_encapsulate_mesh(mesh_path, mesh_path.lower())
        else:
            print("Invalid image file format")
            # return "Invalid image file format"
    
    def generate_dicom_encapsulate_mesh(self, mesh_file, texture_file):
        suffix = '.dcm'
        filename = tempfile.NamedTemporaryFile(suffix=suffix).name

        file_meta = Dataset()
        file_meta.MediaStorageSOPClassUID = '1.2.840.10008.5.1.4.1.1.104.5'  # Encapsulated MTL Storage, see https://dicom.nema.org/medical/dicom/current/output/chtml/part04/sect_B.5.html
        file_meta.MediaStorageSOPInstanceUID = '2.16.840.1.114430.287196081618142314176776725491661159509.60.1'
        file_meta.ImplementationClassUID = '1.3.46.670589.50.1.8.0'
        file_meta.TransferSyntaxUID = '1.2.840.10008.1.2.1'  # Explicit VR Little Endian, see https://dicom.nema.org/medical/dicom/current/output/chtml/part18/sect_8.7.3.html

        self.dcm = FileDataset(filename, {},
                     file_meta=file_meta, preamble=b"\0" * 128)

        self.dcm.SOPClassUID = '1.2.840.10008.5.1.4.1.1.104.5'  # See https://dicom.nema.org/medical/dicom/current/output/chtml/part04/sect_B.5.html

        with open(mesh_file, 'rb') as f:
            self.dcm.EncapsulatedDocument = f.read()

        self.dcm.MIMETypeOfEncapsulatedDocument = 'model/mtl'  # See https://dicom.innolitics.com/ciods/encapsulated-stl/encapsulated-document/00420012
        self.dcm.RelativeURIReferenceWithinEncapsulatedDocument = texture_file
        
    def init_photogramettery_module(self, params):
        self.dcm.FocalLength = params["FocalLength"]
        self.dcm.ExposureTimeInSeconds = params["Exposure"]
        self.dcm.ApertureValue = params["Aperture"]
        
    def init_tbp_3d_module(self, params):
        self.dcm.SOPClassUID= 'Total Body Photography 3D IOD (Proposed)'
        self.dcm.SOPInstanceUID= '1.2.410.200049.2.473513877067425.3.1.20231005084847090.41160'

        # Define private creator tag
        private_creator = "TBP 3D Module"
        # Add a private block with a specific tag (e.g., (0x0011, 0x0010) - just an example)
        # You will need to choose an appropriate group number (odd number) and element number
        group_number = 0x0012  # Example group number (should be odd for private tags)
        element_number = 0x0010  # Starting element number for private block
        block_start = self.dcm.private_block(group_number, private_creator, create=True)
        
        block_start.add_new(element_number, 'DS', params["TBPCaptureProcedure"])  # FD is for float double
        element_number += 1

        block_start.add_new(element_number, 'FL', params["BodyCoverage"])  # Just an example value
        element_number += 1

        block_start.add_new(element_number, 'FL', params["MissingBodyParts"])
        element_number += 1


        block_start.add_new(element_number, 'SS', params["ReconstructionError"])
        element_number += 1

        block_start.add_new(element_number, 'FL', params["ReconstructionAlgorithm"])
        element_number += 1