from dicom import DICOM
from PIL import Image
from PIL.ExifTags import TAGS
import os
from pydicom.sequence import Sequence, Dataset

class TwoD_TBP(DICOM):
    def __init__(self, data):
        super().__init__(data)
        # Add any additional initialization code here
        self.twoD_attributes()
        
    def load_img(self, img_path):
        if os.path.exists(img_path) and (img_path.lower().endswith('.png') or img_path.lower().endswith('.jpeg') or img_path.lower().endswith('.jpg')):
            img = Image.open(img_path)
            return img
        else:
            print("Invalid image file format")
            # return "Invalid image file format"
    
    def save_EXIF_data(self, img):
        exif_data = img._getexif()  
        # Check if the image has EXIF data
        if not exif_data:
            print("No EXIF Data")
            # return "No EXIF data found"
        else:
            # Extract camera-related properties
            camera_properties = {}
            for tag_id, value in exif_data.items():
                # Get the tag name
                tag_name = TAGS.get(tag_id, tag_id)
                # Filter for camera-related tags
                if tag_name in ["Make", "Model", "LensModel", "FocalLength", "WhiteBalance", "DateTimeOriginal", "ImageWidth", "ImageLength", "ExposureTime", "FNumber", "ISO"]:
                    camera_properties[tag_name] = value
            return camera_properties

    def add_camera_properties(self, camera_properties):
        self.dcm.FNumber = camera_properties["FNumber"]
        self.dcm.ExposureTime = camera_properties["ExposureTime"]
        self.dcm.WhiteBalance = camera_properties["WhiteBalance"]
        self.dcm.FocalLength = camera_properties["FocalLength"]
        
    def manufacturer_specific_data(self):
        self.dcm.AcquisitionNumberAttribute = "1"
        
        
    def init_image_attributes(self):
        # image specific
        self.dcm.ImageType= ['DERIVED', 'PRIMARY', 'SUPER-RES']
        self.dcm.AcquisitionDeviceProcessingDescription = "super-res"
        self.dcm.PhotometricInterpretation = "RGB"
        self.dcm.PixelSpacing = [1.0, 1.0]
        self.dcm.BitsAllocated = 8
        self.dcm.BitsStored = 8
        self.dcm.HighBit = 7
        self.dcm.PixelRepresentation = 0
        self.dcm.SamplesPerPixel = 1
       
    
    def init_tbp_module(self):
        self.dcm.SOPClassUID= 'Total Body Photography Regional Image IOD (Proposed)'
        self.dcm.SOPInstanceUID= '1.2.410.200049.2.473513877067425.3.1.20231005084847090.41159'
        self.dcm.Modality= 'XC'
        
    
    def add_anatomical_region(self):
         
        anatomic_region_sequence = Sequence()
        # Anatomic Region Sequence: Anatomic Region 1
        anatomic_region1 = Dataset()
        anatomic_region1.CodeValue = 'T-02471'
        anatomic_region1.CodingSchemeDesignator = 'DAS'
        anatomic_region1.CodeMeaning = 'Skin of buttock'
        anatomic_region_sequence.append(anatomic_region1)
        self.dcm.AnatomicRegionSequence = anatomic_region_sequence
    
    def image_plane(self):
        self.dcm.ImagePosition = '50\\25\\40'
        self.dcm.ImageOrientation = '1\\0\\0\\0\\1\\0'
        self.dcm.PixelSpacing = 3

    def add_VL_Image_Calibration_Module(self):
        # Define private creator tag
        private_creator = "VL Image Calibration Module"
        # Add a private block with a specific tag (e.g., (0x0011, 0x0010) - just an example)
        # You will need to choose an appropriate group number (odd number) and element number
        group_number = 0x0011  # Example group number (should be odd for private tags)
        element_number = 0x0010  # Starting element number for private block
        block_start = self.dcm.private_block(group_number, private_creator, create=True)
        
        # Add attributes to the private block
        # a. Focal Length
        block_start.add_new(element_number, 'DS', '1560')  # FD is for float double
        element_number += 1

        # b. Principal Point
        principal_point = [285.2,427.0] 
        block_start.add_new(element_number, 'FL', principal_point)  # Just an example value
        element_number += 1

        # c. Radial Distortion
        radial_distortion = [ 0.03583441216871274, 0.26, 0.5682430959708085 ]  # Example values
        block_start.add_new(element_number, 'FL', radial_distortion)
        element_number += 1

        # d. Parfocal

        parfocal = 1
        block_start.add_new(element_number, 'SS', parfocal)
        element_number += 1

        # e. Focus Distance
        focus_distance = 1.47
        block_start.add_new(element_number, 'FL', focus_distance)
        element_number += 1

        # f. Tangential Distortion
        # tangential_distortion = [0.01, -0.01]  # Example values
        # block_start.add_new(element_number, 'FD', tangential_distortion)
        # element_number += 1

    def twoD_attributes(self):
        # self.add_VL_Image_Calibration_Module()
        exif_data = self.save_EXIF_data(self.load_img("./00.jpg"))  
        self.add_camera_properties(exif_data)
        self.add_anatomical_region()
        self.add_VL_Image_Calibration_Module()
        self.image_plane()
        self.init_tbp_module()
        self.init_image_attributes()