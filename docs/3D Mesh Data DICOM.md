This is the documentation on how to use TBP DICOM repo to generate and modify 3D Meshes.
**![](https://lh7-us.googleusercontent.com/V3WLJaO-FFpOtHwGBb2mqqbi9okKkQVPsNiSvxz28nfcWkaNaKrW_AAfx0bEtK_fRNJKYh6JO9iv6foFgzB9nMhS8nlNrfmP7HCfxS4Ks8JX64yIt1q1S4F2kmNAiB2GvH_ptll__ye2_G5qbq5taTa0zA=s2048)**

### Equipment IE:

#### General Equipment Module:

General Reference Module is used to link the Regional Images with 3D Mesh.

| **Attribute Name**        | **Tag**     | **Type** | **Attribute Description**                                                                   |
| ------------------------- | ----------- | -------- | ------------------------------------------------------------------------------------------- |
| Referenced Image Sequence | (0008,1140) | U        | This attribute can be utilized to create a linkage between the 3D Mesh and Regional Images. |

#### Photogrammetry Module (Private Block):

Photogrammetry Module is designed to accurately capture details regarding the algorithms and calibration techniques used to generate high-fidelity spatial reconstructions. This module stores essential information about the photographic acquisition settings and reconstruction procedures
The proposed module will be a private block in our implementation.

| **Attribute Name** | **Tag**     | **Type** | **Attribute Description**                                                                               |
| ------------------ | ----------- | -------- | ------------------------------------------------------------------------------------------------------- |
| Focal Length       | (0010,1401) | U        | Focal Length (in mm)                                                                                    |
| Exposure           | (0010,1402) | U        | Defines the amount of light allowed to reach the image sensor during the photographic capture           |
| Aperture           | (0010,1403) | U        | Denotes the opening in a lens through which light passes to enter the camera body, measured in f-stops. |

#### TBP 3D Module

TBP 3D Module stores specific details of TBP acquisition, including capture procedure and body coverage, among others.
The proposed module will be a private block in our implementation.

| **Attribute Name**       | **Tag**     | **Type** | **Attribute Description**                                                                                                                                          |
| ------------------------ | ----------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| TBP Capture Procedure    | (0010,1411) | M        | Enumerate values of instant capture, continuous scanning, other types                                                                                              |
| Body Coverage            | (0010,1412) | U        | Specifies the percentage of the body's surface imaged, with values ranging from 0% (no coverage) to 100% (complete coverage).                                      |
| Missing Body Parts       | (0010,1413) | M        | Identifies absent anatomical regions, such as armpits and plantar surfaces. Should contain a list of anatomical region codes.                                      |
| Reconstruction Error     | (0010,1414) | U        | Metric quantifying the discrepancy between the patient's actual pose and the reconstructed dimensions, such as height, width, and girth, derived from imaging data |
| Reconstruction Algorithm | (0010,1415) | M        | Specifies the computational algorithm used to derive the three-dimensional meshes from two-dimensional images.                                                     |

##### A.XX.3.3.2.1 Modality:

The value of Modality (0008,0060) shall be M3D.
