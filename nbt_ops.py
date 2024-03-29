


#Instructions: Replace variables indicated by "Template" with modifier specific variable names

#Template replacements:
#   Need Three Variables for this file

#       ducky       for _node_group function and result variable
# OR    turntable   for _node_group function and result variable
# OR    derrk 

#       node_name_geonode    for geometry node modifier
#       'Node Name' Nodegroup  for the callable name of the modifier



import bpy
from . nbt_geonodes import ducky_node_group  #Template - node_name + _node_group
from .nbt_geonodes import turntable_node_group
from .nbt_geonodes import derrk_node_group
from bpy.types import Context, Operator

class nbt_OT_Create_Ducky_Geonode_Operator(Operator):   #Template - replace with node_name
    bl_idname = "object.create_ducky_geonode"     #Template - node_name with _geonode
    bl_label = "create geonode"
    bl_description = "Installs function geonode group"
    
    def execute(self, context):
        ducky = ducky_node_group()  #Template - 2 replacements with first variable: 1)functionname_this and 2) = functionname_this + _node_group()

        return {"FINISHED"}


class nbt_OT_Apply_Ducky_Operator(Operator):          #Template - replace with node_name
    bl_idname = "object.apply_ducky"                  #Template - replace with node_name
    bl_label = "modify object"
    bl_description = "Press to add modifier to active object"

    @classmethod
    def poll(cls, context):
        obj = context.object

        if obj is not None:
            if obj.mode == "OBJECT":
                if context.selected_objects:
                    if obj.type == "MESH":
                        return True
            
        return False
    
    def execute(self, context):

        active_obj = context.view_layer.objects.active

        try:
            bpy.data.node_groups['Ducky']   #Template - replace with 'Node Name'
            print("nodegroup already loaded")  
        except:   
            bpy.ops.object.create_ducky_geonode()   #Template - replace with node_name_geonode
            print("ducky geonode now loaded")

        modifier = active_obj.modifiers.new("Ducky_GeoNode", "NODES")
        bpy.ops.node.new_geometry_node_group_assign()
        bpy.data.node_groups.remove(modifier.node_group)
        modifier.node_group = bpy.data.node_groups['Ducky']  #Template - replace with 'Node Name'
        bpy.context.scene.frame_end = 150

        bpy.ops.screen.frame_jump(end=False)
        
    



        return {"FINISHED"}
    
class nbt_OT_Undo_Ducky_Operator(Operator):         #Template - replace with node_name  
    bl_idname = "object.undo_ducky"                 #Template - replace with node_name
    bl_label = "undo function to object"
    bl_description = "Press to remove geomodifier from active"

    @classmethod
    def poll(cls, context):
        obj = context.object

        if obj is not None:
            if obj.mode == "OBJECT":
                if context.selected_objects:
                    if obj.type == "MESH":                
                        return True
            
        return False
    
    def execute(self, context):
        active_obj = context.view_layer.objects.active
        bpy.ops.object.modifier_remove(modifier="Ducky_GeoNode")


        return {"FINISHED"}

# ___________________________________________________________
    
class nbt_OT_Create_Turntable_Geonode_Operator(Operator):   #Template - replace with node_name
    bl_idname = "object.create_turntable_geonode"     #Template - node_name with _geonode
    bl_label = "create geonode"
    bl_description = "Installs function geonode group"
    
    def execute(self, context):
        turntable = turntable_node_group()  #Template - 2 replacements with first variable: 1)functionname_this and 2) = functionname_this + _node_group()

        return {"FINISHED"}


class nbt_OT_Apply_Turntable_Operator(Operator):          #Template - replace with node_name
    bl_idname = "object.apply_turntable"                  #Template - replace with node_name
    bl_label = "modify object"
    bl_description = "Press to add modifier to active object"

    @classmethod
    def poll(cls, context):
        obj = context.object

        if obj is not None:
            if obj.mode == "OBJECT":
                if context.selected_objects:
                    if obj.type == "MESH":
                        return True
            
        return False
    
    def execute(self, context):

        active_obj = context.view_layer.objects.active

        try:
            bpy.data.node_groups['Turntable']   #Template - replace with 'Node Name'
            print("nodegroup already loaded")  
        except:   
            bpy.ops.object.create_turntable_geonode()   #Template - replace with node_name_geonode
            print("turntable geonode now loaded")

        modifier = active_obj.modifiers.new("Turntable_GeoNode", "NODES")
        bpy.ops.node.new_geometry_node_group_assign()
        bpy.data.node_groups.remove(modifier.node_group)
        modifier.node_group = bpy.data.node_groups['Turntable']  #Template - replace with 'Node Name'
        bpy.context.scene.frame_end = 150

        bpy.ops.screen.frame_jump(end=False)
        
    



        return {"FINISHED"}
    
class nbt_OT_Undo_Turntable_Operator(Operator):         #Template - replace with node_name  
    bl_idname = "object.undo_turntable"                 #Template - replace with node_name
    bl_label = "undo function to object"
    bl_description = "Press to remove geomodifier from active"

    @classmethod
    def poll(cls, context):
        obj = context.object

        if obj is not None:
            if obj.mode == "OBJECT":
                if context.selected_objects:
                    if obj.type == "MESH":                
                        return True
            
        return False
    
    def execute(self, context):
        active_obj = context.view_layer.objects.active
        bpy.ops.object.modifier_remove(modifier="Turntable_GeoNode")


        return {"FINISHED"}
    
    # ___________________________________________________________

class nbt_OT_Create_Derrk_Geonode_Operator(Operator):   #Template - replace with node_name
    bl_idname = "object.create_derrk_geonode"     #Template - node_name with _geonode
    bl_label = "create geonode"
    bl_description = "Installs function geonode group"
    
    def execute(self, context):
        derrk = derrk_node_group()  #Template - 2 replacements with first variable: 1)functionname_this and 2) = functionname_this + _node_group()

        return {"FINISHED"}


class nbt_OT_Apply_Derrk_Operator(Operator):          #Template - replace with node_name
    bl_idname = "object.apply_derrk"                  #Template - replace with node_name
    bl_label = "modify object"
    bl_description = "Press to add modifier to active object"

    @classmethod
    def poll(cls, context):
        obj = context.object

        if obj is not None:
            if obj.mode == "OBJECT":
                if context.selected_objects:
                    if obj.type == "MESH":
                        return True
            
        return False
    
    def execute(self, context):

        active_obj = context.view_layer.objects.active

        try:
            bpy.data.node_groups['Derrk']   #Template - replace with 'Node Name'
            print("nodegroup already loaded")  
        except:   
            bpy.ops.object.create_derrk_geonode()   #Template - replace with node_name_geonode
            print("derrk geonode now loaded")

        modifier = active_obj.modifiers.new("Derrk_GeoNode", "NODES")
        bpy.ops.node.new_geometry_node_group_assign()
        bpy.data.node_groups.remove(modifier.node_group)
        modifier.node_group = bpy.data.node_groups['Derrk']  #Template - replace with 'Node Name'
        bpy.context.scene.frame_end = 150

        bpy.ops.screen.frame_jump(end=False)
        
    



        return {"FINISHED"}
    
class nbt_OT_Undo_Derrk_Operator(Operator):         #Template - replace with node_name  
    bl_idname = "object.undo_derrk"                 #Template - replace with node_name
    bl_label = "undo function to object"
    bl_description = "Press to remove geomodifier from active"

    @classmethod
    def poll(cls, context):
        obj = context.object

        if obj is not None:
            if obj.mode == "OBJECT":
                if context.selected_objects:
                    if obj.type == "MESH":                
                        return True
            
        return False
    
    def execute(self, context):
        active_obj = context.view_layer.objects.active
        bpy.ops.object.modifier_remove(modifier="Derrk_GeoNode")


        return {"FINISHED"}