
This is the documentation on how to use TBP DICOM repo to generate and modify 2D Regional DICOMs.

**![](https://lh7-us.googleusercontent.com/uzxZ6h4hUPlcxu8QKkSQ2un109JZI8JbjIbYWO44ugl80rmUFby3UOp9OYo4WY4LNj_ItBn-E0CxTwiLfwG7bDn6tKJYO-s4-bKjEXuP3hTHJVwY-T8zgBJyayiBH_9eSMuledhDMDjfjZItddvhp4Yk6Q=s2048)**

### DICOM Glossary:
The DICOM data model's hierarchical structure can be justified and understood through the interrelated concepts of IODs, IEs, Modules, and Attributes:

1. **IOD (Information Object Definition):** At the top of the hierarchy, an IOD defines a real-world object within the DICOM context, such as a CT scan or an MRI image. It's essentially a blueprint that encapsulates all the data (in a structured and standardized way) necessary to represent these objects.
    
2. **IE (Information Entity):** Within each IOD, there are different Information Entities that represent a distinct level or category of the data hierarchy. For example, a Patient IE (at the top of the hierarchy) would be followed by Study IE, Series IE, and Image IE, each representing a lower level of the data structure and a more specific aspect of the information object.
    
3. **Modules:** The DICOM model uses Modules to break down the IEs into even more manageable parts. Each Module contains related Attributes necessary for the description of an IE. For instance, the Patient Module, which is part of the Patient IE, contains Attributes like Patient Name and Patient ID.
    
4. **Attributes:** These are the lowest level in the hierarchy and represent the actual data points that contain the values describing the characteristics of an image, patient, or study. Attributes are neatly organized within Modules, and each Attribute has a unique identifier and data type defined by DICOM standards.

### Patient IE:

| Tag          | Attribute Name       | VR  | Value                | Description |
| ------------ | -------------------- | --- | -------------------- | ----------- |
| (0010, 0010) | Patient's Name       | PN  | 'Adarsh Chaluvaraju' |             |
| (0010, 0020) | Patient ID           | LO  | '123'                |             |
| (0010, 0030) | Patient's Birth Date | DA  | '20000726'           |             |
| (0010, 0040) | Patient's Sex        | CS  | 'M'                  |             |
| (0010, 1020) | Patient's Size       | DS  | '1.76'               |             |
| (0010, 1030) | Patient's Weight     | DS  | '67.0'               |             |

### Equipment IE:

#### General Equipment Module:
This module would receive all the values from the EXIF metadata stored in the acquired PNG image. 

| Tag          | Attribute Name | VR  | Value  | Description        |
| ------------ | -------------- | --- | ------ | ------------------ |
| (0016, 0029) | Focal Length   | DS  | '5.54' | Focal Length in mm |
| (0016, 0043) | White Balance  | US  | 1      | White Balance      |
| (0018, 1150) | Exposure Time  | IS  | '0'    | Exposure Time      |

####  **Enhanced General Equipment Module**:


| Tag          | Attribute Name                            | VR  | Value              | Usage | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ------------ | ----------------------------------------- | --- | ------------------ | ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| (0018, 1020) | Software Versions                         | LO  | 'LumoTrackv1'      | U     | Mention the software version                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| (0018, 1400) | Acquisition Device Processing Description | LO  | 'super-res'        | U     | If the WFOV image undergoes any type of processing, this attribute can describe that change. For example: "Super Resolution" (super-res), "Downsampled" (down-sample).                                                                                                                                                                                                                                                                                                                                                                                                                    |
| (0018, 9004) | Content Qualification                     | CS  | 'RESEARCH'         | U     | Takes either "PRODUCT",<br>"RESEARCH",<br>"SERVICE"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| (0008,2111)  | Derivation Description Attribute          | ST  | "Manual Selection" | U     | If an Image is identified to be a Derived image (see [Section C.8.7.1.1.1](http://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.8.7.html#sect_C.8.7.1.1.1)), Derivation Description (0008,2111) is an optional and implementation specific text description of the way the image was derived from an original image.  <br><br>This attribute can store the following codes:<br>a. Manual Selection                                                                                                                                             b. Algorithmic Selection |
| (0008, 0070) | Manufacturer                              | LO  | Lumo Imaging       | U     | Mention the manufacturer's name                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

## Image IE
#### VL Image Calibration Module:  

| Tag          | Attribute Name    | VR  | Value                                             | Description                                                                                                                                                                                                  |
| ------------ | ----------------- | --- | ------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| (0011, 0010) | Private Creator   | LO  | 'VL Image Calibration Module'                     |                                                                                                                                                                                                              |
| (0011, 1010) | Focal Length      | DS  | '1560.0'                                          | Focal Length(in pixel unit)                                                                                                                                                                                  |
| (0011, 1011) | Principal Point   | FL  | '[285.2, 427.0]'                                  | The pixel coordinate on the image sensor where the optical axis intersects, specified in pixel coordinates (x, y).                                                                                           |
| (0011, 1012) | Radial Distortion | FL  | '[0.03583441216871274, 0.26, 0.5682430959708885]' | Quantifies the deviation of light rays from rectilinear projection, typically caused by the lens shape. <br><br>This attribute consists of a list of coefficients indicating the degree of image distortion. |

#### Extended VL Photographic Acquisition Module:  

| Tag          | Attribute Name | VR  | Value | Description                                                                                                                                                                                                                                      |
| ------------ | -------------- | --- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| (0011, 1013) | Parfocal       | SS  | 1     | Lens characteristic where the focus remains constant when magnification or focal length is changed. <br><br>This attribute indicates a binary value, with  <br><br>1 representing a parfocal lens and  <br><br>0 indicating a non-parfocal lens. |
| (0011, 1014) | Focal Distance | FL  | 1.47  | Distance between the lens and the subject at which the image is sharply focused, measured in meters.                                                                                                                                             |

#### Image Plane Module:
| Tag          | Attribute Name    | VR  | Value                | Description                                                                                                                                                   |
| ------------ | ----------------- | --- | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| (0020, 0030) | Image Position    | DS  | '[50, 25, 40]'       | Image Position (0020,0032) specifies the x, y, and z coordinates of the upper left hand corner of the image; it is the center of the first voxel transmitted. |
| (0020, 0035) | Image Orientation | DS  | '[1, 0, 0, 0, 1, 0]' | Image Orientation (0020,0037) specifies the direction cosines of the first row and the first column with respect to the patient.                              |

#### General Image Module:

| Tag         | Attribute Name                     | VR  | Value                             | Description |
| ----------- | ---------------------------------- | --- | --------------------------------- | ----------- |
| (0008,2218) | Anatomic Region Sequence Attribute | SQ  | 1                                 |             |
| (0008,0008) | Image Type                         | CS  | ['DERIVED', 'SECONDARY', 'OTHER'] |             |

#### Image Pixel Module:

| Tag          | Attribute Name             | VR  | Value | Description |
| ------------ | -------------------------- | --- | ----- | ----------- |
| (0028, 0002) | Samples per Pixel          | US  | 1     |             |
| (0028, 0004) | Photometric Interpretation | CS  | 'RGB' |             |
| (0028, 0010) | Rows                       | US  | 8192  |             |
| (0028, 0011) | Columns                    | US  | 6144  |             |
| (0028, 0030) | Pixel Spacing              | DS  | '3.0' |             |


For anatomical map
https://anatomymapper.com/Maps/NYU