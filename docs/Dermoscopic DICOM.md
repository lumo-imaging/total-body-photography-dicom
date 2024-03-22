
This is the documentation on how to use TBP DICOM repo to generate and modify Dermoscopic DICOMs.

**![](https://lh7-us.googleusercontent.com/P-bTwnWXlhLz3k_cujsyLNAL15TO_uAVeZhQAJ2AaD176PAEVKzti2CRnRD3dZVMaApuNz8-wq-VVye6y3aFEVc-Cy8hV-mH6o3PFxnAbDNiiQPK7EKieL2MCtlJ9GlvPBrCky94ThWRp7xPf3tK-jBt1w=s2048)**
**
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


Certainly! Here is the table from the image converted into Markdown format:

#### A.XX.2.4.2 General Reference Module                                                               
General Reference Module is used to link the 3D Mesh and Dermoscopic Images with Regional Images.

| **A.XX.2.4.2 General Reference Module Attributes** |             |      |                                                                                                    |
| -------------------------------------------------- | ----------- | ---- | -------------------------------------------------------------------------------------------------- |
| Attribute Name                                     | Tag         | Type | Attribute Description                                                                              |
| Referenced Image Sequence                          | (0008,1140) | U    | This attribute can be utilized to create a linkage between Dermoscopic Images and Regional Images. |
| Referenced Instance Sequence                       | (0008,114A) | U    | This attribute can be employed to link Dermoscopic Images to 3D Mesh.                              |

#### A.XX.2.4.3.1 TBP Dermoscopic Module ATTRIBUTES

Dermoscopic crops are typically linked to two-dimensional regional images and three-dimensional surface meshes, necessitating the storage of crop coordinate data with respect to them. This module facilitates this requirement, by introducing essential attributes.

| **Attribute Name** | **Tag**     | **Type** | **Attribute Description**                                                                                             |
| ------------------ | ----------- | -------- | --------------------------------------------------------------------------------------------------------------------- |
| Lesion ID          | (0010,1301) | M        | Unique Identifier for each lesion                                                                                     |
| Vertex ID          | (0010,1302) | U        | Vertex ID denotes the index of the vertex in the ordered list of vertices comprising the surface mesh                 |
| 2D Coordinate Data | (0010,1303) | U        | Defines the two-dimensional spatial coordinates of the dermoscopic crop relative to the corresponding regional image. |
| 3D Coordinate Data | (0010,1304) | U        | Specifies the three-dimensional spatial coordinates of the dermoscopic crop relative to the associated surface mesh.  |


####  **Enhanced General Equipment Module**:

| Tag         | Attribute Name                   | VR  | Value              | Usage | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ----------- | -------------------------------- | --- | ------------------ | ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| (0008,2111) | Derivation Description Attribute | ST  | "Manual Selection" | U     | If an Image is identified to be a Derived image (see [Section C.8.7.1.1.1](http://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.8.7.html#sect_C.8.7.1.1.1)), Derivation Description (0008,2111) is an optional and implementation specific text description of the way the image was derived from an original image.  <br><br>This attribute can store the following codes:<br>a. Manual Selection                                                                                                                                             b. Algorithmic Selection |

##### To generate anatomical data:
For anatomical map: https://anatomymapper.com/Maps/NYU