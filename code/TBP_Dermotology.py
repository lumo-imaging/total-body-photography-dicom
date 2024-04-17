import os
import tempfile
from dicom import DICOM
from pydicom.dataset import Dataset, FileDataset
from PIL import Image
from PIL.ExifTags import TAGS

class Dermatology_TBP(DICOM):
    def __init__(self, data):
        super().__init__(data)
        # Add any additional initialization code here
        self.threeD_attributes()
        
    def load_img(self, img_path):
        if os.path.exists(img_path) and (img_path.lower() in ['.png', '.jpeg' , '.jpg']):
            img = Image.open(img_path)
            return img
        else:
            print("Invalid image file format")
            # return "Invalid image file format"
    
    def init_tbp_3d_module(self, params):
        self.dcm.SOPClassUID= 'Total Body Photography Dermoscopic IOD (Proposed)'
        self.dcm.SOPInstanceUID= '1.2.410.200049.2.473513877067425.3.1.20231005084847090.41161'

        # Define private creator tag
        private_creator = "TBP Dermotology Module"
        # Add a private block with a specific tag (e.g., (0x0011, 0x0010) - just an example)
        # You will need to choose an appropriate group number (odd number) and element number
        group_number = 0x0013  # Example group number (should be odd for private tags)
        element_number = 0x0010  # Starting element number for private block
        block_start = self.dcm.private_block(group_number, private_creator, create=True)
        
        block_start.add_new(element_number, 'DS', params["LesionID"])  # FD is for float double
        element_number += 1

        block_start.add_new(element_number, 'FL', params["VertexID"])  # Just an example value
        element_number += 1

        block_start.add_new(element_number, 'FL', params["2DCoordinateData"])
        element_number += 1


        block_start.add_new(element_number, 'SS', params["3DCoordinateData"])
        element_number += 1