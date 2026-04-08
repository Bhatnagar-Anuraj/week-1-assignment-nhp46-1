"""
DIGM 131 - Assignment 1: Procedural Scene Builder
==================================================

OBJECTIVE:
    Build a simple 3D scene in Maya using Python scripting.
    You will practice using maya.cmds to create and position geometry,
    and learn to use descriptive variable names.

REQUIREMENTS:
    1. Create a ground plane (a large, flat polygon plane).
    2. Create at least 5 objects in your scene.
    3. Use at least 2 different primitive types (e.g., cubes AND spheres,
       or cylinders AND cones, etc.).
    4. Position every object using descriptive variable names
       (e.g., house_x, tree_height -- NOT x1, h).
    5. Add comments explaining what each section of your code does.

GRADING CRITERIA:
    - [20%] Ground plane is created and scaled appropriately.
    - [30%] At least 5 objects are created using at least 2 primitive types.
    - [25%] All positions/sizes use descriptive variable names.
    - [15%] Code is commented clearly and thoroughly.
    - [10%] Scene is visually coherent (objects are placed intentionally,
            not overlapping randomly).

TIPS:
    - Run this script from Maya's Script Editor (Python tab).
    - Use maya.cmds.polyCube(), maya.cmds.polySphere(), maya.cmds.polyCylinder(),
      maya.cmds.polyCone(), maya.cmds.polyPlane(), etc.
    - Use maya.cmds.move(x, y, z, objectName) to position objects.
    - Use maya.cmds.scale(x, y, z, objectName) to resize objects.
    - Use maya.cmds.rename(oldName, newName) to give objects meaningful names.
"""

import maya.cmds as cmds

# ---------------------------------------------------------------------------
# Clear the scene so we start fresh each time the script runs.
# (This is provided for you -- do not remove.)
# ---------------------------------------------------------------------------
cmds.file(new=True, force=True)

# ---------------------------------------------------------------------------
# Ground Plane
# ---------------------------------------------------------------------------
# Descriptive variables for the ground plane dimensions and position.
ground_width = 50
ground_depth = 50
ground_y_position = 0

ground = cmds.polyPlane(
    name="ground_plane",
    width=ground_width,
    height=ground_depth,
    subdivisionsX=1,
    subdivisionsY=1,
)[0]
cmds.move(0, ground_y_position, 0, ground)

# ---------------------------------------------------------------------------
# Example Object 1 -- a simple building (cube)
# This is provided as an example. Study it, then add your own objects below.
# ---------------------------------------------------------------------------
building_width = 4
building_height = 6
building_depth = 4
building_x = -8
building_z = 5

building = cmds.polyCube(
    name="building_01",
    width=building_width,
    height=building_height,
    depth=building_depth,
)[0]
# Raise the building so its base sits on the ground plane.
cmds.move(building_x, building_height / 2.0, building_z, building)

# ---------------------------------------------------------------------------
# Create a second object using a DIFFERENT primitive type than the cube above.
# Remember to:
#   - Use descriptive variable names for size and position.
#   - Name the object meaningfully with the 'name' parameter or cmds.rename().
#   - Position it so it sits on the ground (not floating or buried).
# ---------------------------------------------------------------------------
tree_trunk_radius = 0.6
tree_trunk_height = 4
tree_trunk_x_position = 5
tree_trunk_z_position = 6

tree_trunk = cmds.polyCylinder(
    name="tree_trunk_01",
    radius=tree_trunk_radius,
    height=tree_trunk_height,
)[0]
cmds.move(
    tree_trunk_x_position,
    tree_trunk_height / 2.0,
    tree_trunk_z_position,
    tree_trunk
)

# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
tree_top_radius = 2
tree_top_x_position = 5
tree_top_z_position = 6
tree_top_y_position = tree_trunk_height + tree_top_radius

tree_top = cmds.polySphere(
    name="tree_top_01",
    radius=tree_top_radius,
)[0]
cmds.move(
    tree_top_x_position,
    tree_top_y_position,
    tree_top_z_position,
    tree_top
)

# testing
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
roof_radius = 3
roof_height = 3
roof_x_position = building_x
roof_z_position = building_z
roof_y_position = building_height + (roof_height / 2.0)

roof = cmds.polyCone(
    name="roof_01",
    radius=roof_radius,
    height=roof_height,
)[0]
cmds.move(
    roof_x_position,
    roof_y_position,
    roof_z_position,
    roof
)


# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
water_tower_radius = 1.5
water_tower_height = 5
water_tower_x_position = 10
water_tower_z_position = -4

water_tower = cmds.polyCylinder(
    name="water_tower_01",
    radius=water_tower_radius,
    height=water_tower_height,
)[0]
cmds.move(
    water_tower_x_position,
    water_tower_height / 2.0,
    water_tower_z_position,
    water_tower
)

# ---------------------------------------------------------------------------
# Consider: trees, lamp posts, fences, vehicles, animals, etc.
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# Frame All -- so the whole scene is visible in the viewport.
# (This is provided for you -- do not remove.)
# ---------------------------------------------------------------------------
cmds.viewFit(allObjects=True)
print("Scene built successfully!")
