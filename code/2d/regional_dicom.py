import json
from pydicom import dcmread, datadict
from sys import argv
import pydicom
import os
import numpy as np
from PIL import Image
from datetime import datetime


class RegionalImage():
    """
        This function adds a reference for the crop in the original wide field of view image
        Params:
        ds: dicom file's dataset instance
        coordinates: x, y coordinates for the crop Ex: (10,20)
        path: file_name/path Ex: "./test.dcm"
        coordinates_3d: x,y,z coordinates for the crop Ex: (10,20,30)
        
    """
    def add_lesion(ds, coordinates, path, coordinates_3d):
        li = []
        li.append(coordinates)
        li_3 = []
        li_3.append(coordinates_3d)
        if ds["00411010"].value == None or len(ds["00411010"].value) == 0:
            ds["00411010"].value = pydicom.multival.MultiValue(list, li)
            ds["00411011"].value = pydicom.multival.MultiValue(list, [])
            ds["00411011"].value = [path, path]
            ds["00411011"].value.pop(0)
        else: 
            ds["00411010"].value.append(coordinates[0])
            ds["00411010"].value.append(coordinates[1])
            if type(ds["00411011"].value) == str: 
                ds["00411011"].value= [ ds["00411011"].value, path ]
            else: 
                ds["00411011"].value.append(path)
        
        if ds["00411012"].value == None or len(ds["00411012"].value) == 0:
            ds["00411012"].value = pydicom.multival.MultiValue(list, li_3)
        else:
            for i in coordinates_3d: 
                ds["00411012"].value.append(i)
        addPrivateElementsToDict1()
        save_dcm(ds)


    def addPrivateElementsToDict1():
            """ Set private elements for Lumo Imaging in DICOM. """
            print("Called")
            new_dict_items = {
                0x00411010: ('FL', '1', "Lesion Co-ordinates"),
                0x00411011: ('CS', '1', "Lesion File Path"),    
                0x00411012: ('FL', '1', "Lesion 3-D Co-ordinates"),    
                }
            datadict.add_private_dict_entries('TBP', new_dict_items)



    # def remove_crop_from_image(i, ds):
    #     """
    #     This function recieves the index of the image crop, starting from 0
    #     and deletes that reference i.e, removes the crop 2d and 3d co-ordinates, filepath
    #     Ex: 
    #     Previous state of "Lesion Co-ordinates" = "2.0, 4.9, 3.0, 6.0, 4.6, 7.9"
    #     If the remove_crop_from_image is passed with 2 as the arguement, 
    #     it would delete the co-ordinates of the 3rd crop, that is 4.6, 7.9.
    #     Final state of "Lesion Co-ordinates" = "2.0, 4.9, 3.0, 6.0"
    #     Similar behaviour can be expected for other attributes   
    #     """

    #     crops_from_fov = ds["00411010"].value
    #     names = ds["00411011"].value
    #     threed_crops_from_fov = ds["00411012"].value
    #     if crops_from_fov == None: print("No Elements")
    #     elif len(crops_from_fov) == 0:
    #         print("No elements in the image")
    #     else:
    #         try:
    #             threed_crops_from_fov.pop(i*3)
    #             threed_crops_from_fov.pop(i*3)
    #             threed_crops_from_fov.pop(i*3)
    #             crops_from_fov.pop(i*2)
    #             crops_from_fov.pop(i*2)
    #             names = "" if type(names) == str else names.pop(i)
    #             ds["00411010"].value = crops_from_fov
    #             ds["00411011"].value = names
    #             ds["00411012"].value = threed_crops_from_fov
    #             print(ds["00411012"].value)
    #             save_dcm(ds)
    #         except IndexError:
    #             print("Incorrect Index")

    # def get_references(ds):
    #     try:
    #         return [
    #                 ds["00411011"].value, 
    #                 [(ds["00411010"].value[i*2], ds["00411010"].value[i*2 + 1]) for i in range(len(ds["00411010"].value) // 2)], 
    #                 [(ds["00411012"].value[i*3], ds["00411012"].value[i*3 + 1], ds["00411012"].value[i*3 + 2]) for i in range(len(ds["00411012"].value) // 3)]]
    #     except KeyError:
    #         print("No key!")

    # def path_2_dcm_file(path):
    #     return dcmread(path)

    # """
    #     Creates and returns a private creators block in the name of TBP with group tag 0x000f 
    # """
    # def create_block_dcm_file(ds):
    #     if "00411010" in ds:
    #         print("Already Initialised")
    #     else:    
    #         block = ds.private_block(0x0041, "Lumo Imaging", create=True)
    #         block.add_new(0x10, "FL", [])
    #         block.add_new(0x11, "CS", [])
    #         block.add_new(0x12, "FL", [])
    #         save_dcm(ds)
    #         return block

    # def get_block_dcm_file(ds):
    #     block = ds.private_block(0x0041, "TBP")
    #     return block

    # def save_dcm(ds):
    #     addPrivateElementsToDict1()
    #     with open(argv[1], 'wb') as outfile:
    #         ds.save_as(outfile)
    #     print("Image Saved")

    # def clear_references(ds):
    #     ds["00411010"].value = []
    #     ds["00411011"].value = []
    #     ds["00411012"].value = []
    #     save_dcm(ds)

    # def convert_2d_arr_to_coordinates(ds):
    #     if len(ds["00411010"].value) == 0:
    #         print("No values stored")
    #     else: 
    #         return [ (ds["00411010"].value[i*2], ds["00411010"].value[i*2+1]) for i in range(len(ds["00411010"].value)//2) ]

    # def convert_3d_arr_to_coordinates(ds):
    #     if len(ds["00411012"].value) == 0:
    #         print("No values stored")
    #     else: 
    #         return [ (ds["00411012"].value[i*3], ds["00411012"].value[i*3+1]) for i in range(len(ds["00411012"].value)//3) ]


    # def png_to_dcm(png_path, dcm_path, IMG_NUMBER):
    #     # Load PNG image using PIL library
    #     img = Image.open(png_path)
        
    #     # Convert to grayscale
    #     img_gray = img.convert('L')
        
    #     # Convert to numpy array
    #     img_array = np.array(img_gray)
        
    #     # Create DICOM object
    #     dcm = pydicom.dataset.FileDataset(dcm_path, {}, file_meta=None)
    #     dcm.PatientName = "Adarsh Chaluvaraju"
    #     dcm.PatientID = "123"
    #     dcm.PatientSex = "M"
        
    #     dcm.Modality = "CT"
    #     dcm.Rows, dcm.Columns = img_array.shape
        
    #     dcm.PixelSpacing = [1.0, 1.0]
    #     dcm.BitsAllocated = 8
    #     dcm.BitsStored = 8
    #     dcm.HighBit = 7
    #     dcm.PixelRepresentation = 0
    #     dcm.SamplesPerPixel = 1
        
    #     dcm.PhotometricInterpretation = "RGB"
    #     dcm.AcquisitionDeviceProcessingDescription = "super-res"
    #     dcm.ImageType = ["ORIGINAL", "PRIMARY", "white"]
    #     dcm.AcquisitionNumberAttribute = IMG_NUMBER
        
    #     dcm.StudyDate = datetime.today().strftime("%Y%m%d")
    #     dcm.StudyTime = datetime.now().strftime("%H%M%S.%f")

    #     dcm.SeriesDescription = "Dermascopic WFOV"
    #     dcm.SeriesNumber = 1

    #     # Convert numpy array to bytes
    #     img_bytes = img_array.tobytes()
        
    #     # Add image data to DICOM object
    #     dcm.PixelData = img_bytes
        
    #     # Save DICOM file
    #     dcm.save_as(dcm_path)



if __name__ == '__main__':

    # importing dicom file
    # ds = path_2_dcm_file(argv[1])
    
    # initialise private block
    # block = create_block_dcm_file(ds)
    
    # Funation call to add lesion
    # add_lesion(ds, (1.0,2.0),"./abc-1.jpg", (5.0,6.0,7.0))

    # Function call that returns references along with their coordinates    
    # print(get_references(ds))
    

    # 0-indexed reference remover
    # remove_crop_from_image(0, ds)

    # remove all references
    # clear_references(ds)
    
    # Example usage
    png_path = argv[1]
    dcm_path = f'{argv[1]}.dcm'
    png_to_dcm(png_path, dcm_path, 1)
