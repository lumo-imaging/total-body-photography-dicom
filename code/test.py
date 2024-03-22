import pydicom
from pydicom.dataset import Dataset, FileMetaDataset
from pydicom.sequence import Sequence

# File meta info data elements
file_meta = FileMetaDataset()
file_meta.FileMetaInformationGroupLength = 192
file_meta.FileMetaInformationVersion = b'\x00\x01'
file_meta.MediaStorageSOPClassUID = '1.2.840.10008.5.1.4.1.1.2'
file_meta.MediaStorageSOPInstanceUID = '1.3.6.1.4.1.5962.1.1.1.1.1.20040119072730.12322'
file_meta.TransferSyntaxUID = '1.2.840.10008.1.2.1'
file_meta.ImplementationClassUID = '1.3.6.1.4.1.5962.2'
file_meta.ImplementationVersionName = 'DCTOOL100'
file_meta.SourceApplicationEntityTitle = 'CLUNIE1'

# Main data elements
ds = Dataset()
ds.SpecificCharacterSet = 'ISO_IR 100'
ds.ImageType = ['ORIGINAL', 'PRIMARY', 'AXIAL']
ds.InstanceCreationDate = '20040119'
ds.InstanceCreationTime = '072731'
ds.InstanceCreatorUID = '1.3.6.1.4.1.5962.3'
ds.SOPClassUID = '1.2.840.10008.5.1.4.1.1.2'
ds.SOPInstanceUID = '1.3.6.1.4.1.5962.1.1.1.1.1.20040119072730.12322'
ds.StudyDate = '20040119'
ds.SeriesDate = '19970430'
ds.AcquisitionDate = '19970430'
ds.ContentDate = '19970430'
ds.StudyTime = '072730'
ds.SeriesTime = '112749'
ds.AcquisitionTime = '112936'
ds.ContentTime = '113008'
ds.AccessionNumber = ''
ds.Modality = 'CT'
ds.Manufacturer = 'GE MEDICAL SYSTEMS'
ds.InstitutionName = 'JFK IMAGING CENTER'
ds.ReferringPhysicianName = ''
ds.TimezoneOffsetFromUTC = '-0500'
ds.StationName = 'CT01_OC0'
ds.StudyDescription = 'e+1'
ds.ManufacturerModelName = 'RHAPSODE'
ds.PatientName = 'CompressedSamples^CT1'
ds.PatientID = '1CT1'
ds.PatientBirthDate = ''
ds.PatientSex = 'O'

# Other Patient IDs Sequence
other_patient_i_ds_sequence = Sequence()
ds.OtherPatientIDsSequence = other_patient_i_ds_sequence

# Other Patient IDs Sequence: Other Patient IDs 1
other_patient_i_ds1 = Dataset()
other_patient_i_ds_sequence.append(other_patient_i_ds1)
other_patient_i_ds1.PatientID = 'ABCD1234'
other_patient_i_ds1.TypeOfPatientID = 'TEXT'

# Other Patient IDs Sequence: Other Patient IDs 2
other_patient_i_ds2 = Dataset()
other_patient_i_ds_sequence.append(other_patient_i_ds2)
other_patient_i_ds2.PatientID = '1234ABCD'
other_patient_i_ds2.TypeOfPatientID = 'TEXT'

ds.PatientAge = '000Y'
ds.PatientWeight = '0.0'
ds.AdditionalPatientHistory = ''
ds.ContrastBolusAgent = 'ISOVUE300/100'
ds.ScanOptions = 'HELICAL MODE'
ds.SliceThickness = '5.0'
ds.KVP = '120.0'
ds.SpacingBetweenSlices = '5.0'
ds.DataCollectionDiameter = '480.0'
ds.SoftwareVersions = '05'
ds.ContrastBolusRoute = 'IV'
ds.ReconstructionDiameter = '338.6716'
ds.DistanceSourceToDetector = '1099.3100585938'
ds.DistanceSourceToPatient = '630.0'
ds.GantryDetectorTilt = '0.0'
ds.TableHeight = '133.699997'
ds.ExposureTime = '1601'
ds.XRayTubeCurrent = '170'
ds.Exposure = '170'
ds.FilterType = 'LARGE BOWTIE FIL'
ds.FocalSpots = '0.7'
ds.ConvolutionKernel = 'STANDARD'
ds.PatientPosition = 'FFS'
ds.StudyInstanceUID = '1.3.6.1.4.1.5962.1.2.1.20040119072730.12322'
ds.SeriesInstanceUID = '1.3.6.1.4.1.5962.1.3.1.1.20040119072730.12322'
ds.StudyID = '1CT1'
ds.SeriesNumber = '1'
ds.AcquisitionNumber = '2'
ds.InstanceNumber = '1'
ds.ImagePositionPatient = [-158.135803, -179.035797, -75.699997]
ds.ImageOrientationPatient = [1.000000, 0.000000, 0.000000, 0.000000, 1.000000, 0.000000]
ds.FrameOfReferenceUID = '1.3.6.1.4.1.5962.1.4.1.1.20040119072730.12322'
ds.Laterality = ''
ds.PositionReferenceIndicator = 'SN'
ds.SliceLocation = '-77.2040634155'
ds.ImageComments = 'Uncompressed'
ds.SamplesPerPixel = 1
ds.PhotometricInterpretation = 'MONOCHROME2'
ds.Rows = 128
ds.Columns = 128
ds.PixelSpacing = [0.661468, 0.661468]
ds.BitsAllocated = 16
ds.BitsStored = 16
ds.HighBit = 15
ds.PixelRepresentation = 1
ds.PixelPaddingValue = -2000
ds.RescaleIntercept = '-1024.0'
ds.RescaleSlope = '1.0'
ds.PixelData = # XXX Array of 32768 bytes excluded
ds.DataSetTrailingPadding = # XXX Array of 126 bytes excluded

ds.file_meta = file_meta
ds.is_implicit_VR = False
ds.is_little_endian = True
ds.save_as(r'path')