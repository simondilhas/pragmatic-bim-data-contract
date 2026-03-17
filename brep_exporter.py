import ifcopenshell
import ifcopenshell.geom
import logging
from pathlib import Path
from typing import Dict, Optional
from OCC.Core.BRepBuilderAPI import (
    BRepBuilderAPI_MakeSolid,
    BRepBuilderAPI_MakeCompound,
    BRepBuilderAPI_MakeVertex,
    BRepBuilderAPI_MakeEdge,
    BRepBuilderAPI_MakeFace,
    BRepBuilderAPI_MakeWire,
    BRepBuilderAPI_MakeShell
)
from OCC.Core.BRep import BRep_Builder
from OCC.Core.TopoDS import TopoDS_Compound
from OCC.Core.gp import gp_Pnt
from OCC.Core.BRepTools import breptools_Write
from OCC.Core.TopoDS import TopoDS_Shape
from OCC.Core.BRep import BRep_Builder
from OCC.Core.TopoDS import TopoDS_Compound
from OCC.Core.BRepTools import breptools_Write
from OCC.Core.BRepTools import breptools_Read
from OCC.Core.BRepTools import breptools_Clean
from OCC.Core.BRepTools import breptools_WriteShape
from OCC.Core.BRepTools import breptools_ReadShape
from OCC.Core.BRepTools import breptools_WriteShapeToFile
from OCC.Core.BRepTools import breptools_ReadShapeFromFile
from .ifc_metadata_extractor import extract_metadata

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def _build_element_id_mapping(ifc_file) -> Dict[str, int]:
    """Build a mapping of GlobalId to sequential IDs for all elements."""
    globalid_to_id = {}
    all_elements = []

    # Get project and products
    project = ifc_file.by_type("IfcProject")[0]
    all_elements.append(project)

    for el in ifc_file.by_type("IfcProduct"):
        if not el.is_a("IfcOpeningElement"):  # Skip openings
            all_elements.append(el)

    # Assign sequential IDs
    for idx, el in enumerate(all_elements, start=1):
        globalid_to_id[el.GlobalId] = idx

    return globalid_to_id

def export_to_brep(ifc_file_path: str, output_dir: str = None, global_id_to_id: Optional[Dict[str, int]] = None) -> None:
    """
    Export IFC elements to individual BREP files.
    
    Args:
        ifc_file_path (str): Path to the IFC file
        output_dir (str, optional): Directory to save BREP files. If None, creates 'brep_output' in same directory as IFC file.
        global_id_to_id (Dict[str, int], optional): Mapping of GlobalId to sequential IDs. If None, will be generated.
    """
    try:
        logger.info(f"Opening IFC file: {ifc_file_path}")
        ifc_file = ifcopenshell.open(ifc_file_path)
        
        # Set up output directory
        if output_dir is None:
            output_dir = str(Path(ifc_file_path).parent / "brep_output")
        Path(output_dir).mkdir(parents=True, exist_ok=True)
        
        # Get or create ID mapping
        if global_id_to_id is None:
            global_id_to_id = _build_element_id_mapping(ifc_file)
        
        # Create geometry settings
        settings = ifcopenshell.geom.settings()
        settings.set(settings.USE_WORLD_COORDS, True)
        
        # Process all products
        products = ifc_file.by_type('IfcProduct')
        logger.info(f"Found {len(products)} products in IFC file")
        
        processed_count = 0
        failed_count = 0
        
        for product in products:
            if not hasattr(product, 'Representation'):
                continue
                
            try:
                # Create shape
                shape = ifcopenshell.geom.create_shape(settings, product)
                
                # Get the OpenCascade shape
                occ_shape = shape.brep_data
                
                # Create output filename using the same ID as metadata
                element_type = product.is_a()
                element_id = global_id_to_id.get(product.GlobalId, product.GlobalId)
                output_file = Path(output_dir) / f"{element_type}_{element_id}.brep"
                
                # Write BREP file
                breptools_WriteShapeToFile(occ_shape, str(output_file))
                
                processed_count += 1
                logger.info(f"Exported {element_type}_{element_id} to {output_file}")
                
            except Exception as e:
                logger.warning(f"Error processing geometry for {product.GlobalId}: {str(e)}")
                failed_count += 1
                continue
        
        logger.info(f"BREP export complete. Successfully processed {processed_count} products, failed to process {failed_count} products")
        
    except Exception as e:
        logger.error(f"Error in export_to_brep: {str(e)}", exc_info=True)
        raise

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        export_to_brep(sys.argv[1])
    else:
        print("Please provide an IFC file path as argument") 