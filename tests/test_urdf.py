
from pathlib import Path
import xml.etree.ElementTree as ET

def find_urdf_files(directory):
    all_urdf = list(Path(directory).rglob("*.urdf"))
    return [file for file in all_urdf if file.name.startswith("adam_")]

all_test_urdf = find_urdf_files(".")

def test_urdf_files():
    assert len(all_test_urdf) > 0, "No URDF files found in the specified directory"
    for file in all_test_urdf:
        print(f"Found URDF file: {file}")
        assert file.suffix == ".urdf", f"Found non-URDF file: {file}"
        
def test_urdf():
    for file in all_test_urdf:
        tree = ET.parse(file)
        root = tree.getroot()
        joints = root.findall(".//joint")
        links = root.findall(".//link")
        joints_name = [joint.get("name") for joint in joints if joint.get("name") is not None]
        links_name = [link.get("name") for link in links if link.get("name") is not None]
        for link in links_name:
            assert link not in joints_name, f"Link {link} is also a joint in {file}"
