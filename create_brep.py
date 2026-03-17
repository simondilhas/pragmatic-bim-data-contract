import os
import sys
import pandas as pd

# Add the parent directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.ifc_metadata_extractor import extract_metadata
from app.brep_exporter import export_to_brep

def main():
    if len(sys.argv) < 2:
        print("Usage: python create_brep.py <ifc_file_path>")
        sys.exit(1)

    ifc_file_path = sys.argv[1]
    
    # First extract metadata to get the ID mapping
    metadata, global_id_to_id = extract_metadata(ifc_file_path)
    
    # Then export BREP files using the same ID mapping
    export_to_brep(ifc_file_path, global_id_to_id=global_id_to_id)

if __name__ == "__main__":
    main()