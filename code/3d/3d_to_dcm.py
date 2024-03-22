# import pydicom
from pydicom import Dataset
import tempfile
import datetime
import pydicom
from pydicom.dataset import Dataset, FileDataset
# from stl import mesh

def generate_dicom_encapsulate_mesh(mesh_file, texture_file):
    suffix = '.dcm'
    filename = tempfile.NamedTemporaryFile(suffix=suffix).name

    file_meta = Dataset()
    file_meta.MediaStorageSOPClassUID = '1.2.840.10008.5.1.4.1.1.104.5'  # Encapsulated MTL Storage, see https://dicom.nema.org/medical/dicom/current/output/chtml/part04/sect_B.5.html
    file_meta.MediaStorageSOPInstanceUID = '2.16.840.1.114430.287196081618142314176776725491661159509.60.1'
    file_meta.ImplementationClassUID = '1.3.46.670589.50.1.8.0'
    file_meta.TransferSyntaxUID = '1.2.840.10008.1.2.1'  # Explicit VR Little Endian, see https://dicom.nema.org/medical/dicom/current/output/chtml/part18/sect_8.7.3.html

    ds = FileDataset(filename, {},
                 file_meta=file_meta, preamble=b"\0" * 128)

    ds.is_little_endian = True
    ds.is_implicit_VR = False

    dt = datetime.datetime.now()
    ds.ContentDate = dt.strftime('%Y%m%d')
    timeStr = dt.strftime('%H%M%S.%f')
    ds.ContentTime = timeStr

    ds.SOPClassUID = '1.2.840.10008.5.1.4.1.1.104.5'  # See https://dicom.nema.org/medical/dicom/current/output/chtml/part04/sect_B.5.html

    with open(mesh_file, 'rb') as f:
        ds.EncapsulatedDocument = f.read()

    ds.MIMETypeOfEncapsulatedDocument = 'model/mtl'  # See https://dicom.innolitics.com/ciods/encapsulated-stl/encapsulated-document/00420012

    # ds.Modality = 'DOC' #document
    # ds.ConversionType = 'WSD' #workstation
    # ds.SpecificCharacterSet = 'ISO_IR 100' 
    # more codes for charecter encoding here https://dicom.innolitics.com/ciods/surface-scan-mesh/sop-common
    ds.RelativeURIReferenceWithinEncapsulatedDocument = texture_file
    
    return ds




import argparse
import datetime

def generate_random_uid():
    return '1.9.9.' + str(datetime.datetime.now().strftime('%H%M%S%f%d%m%Y'))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_mesh', type=str, help='Encapsulate a mesh file to DICOM')
    parser.add_argument('--texture_file', type=str, help='Encapsulate a mesh file to DICOM')
    args = parser.parse_args()
    input_mesh = args.input_mesh
    texture_file = args.texture_file
    output_ds = generate_dicom_encapsulate_mesh(input_mesh, texture_file)

    output_ds.PatientName = 'Adarsh C'
    output_ds.PatientID = generate_random_uid()
    output_ds.PatientSex = 'M'
    output_ds.StudyInstanceUID = generate_random_uid()

    output_ds.SeriesInstanceUID = generate_random_uid()
    output_ds.SOPInstanceUID = generate_random_uid() 

    output_ds.save_as('converted_mtl.dcm')