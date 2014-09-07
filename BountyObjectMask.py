#Add 1 scene
#delete all materials of scene objects
import bpy, random
#REMARK

def RemoveAllMaterials():
	for obj in bpy.context.selected_editable_objects:
		if obj.type == 'MESH':
			while obj.data.materials:
				#obj.data.materials.clear()
				bpy.ops.object.material_slot_remove({'object': obj})
	return{'FINISHED'}

bpy.context.scene.render.engine = 'THEBOUNTY'

SceneName = "ObjectID Mask"
if SceneName in bpy.data.scenes: 
	bpy.data.scenes.remove(bpy.data.scenes[SceneName])
	#sys.exit()

	#Create new identical scene
bpy.ops.scene.new(type='FULL_COPY') 
scn = bpy.context.scene 
scn.name = SceneName

active = bpy.context.active_object
bpy.ops.object.select_all(action='SELECT') 
      
#Restict render for lights	  
for ob in bpy.data.scenes[scn.name].objects: 

	if ob.type == 'LAMP': 
		ob.hide_render = True

	if (ob.type == 'MESH'):

		#MESHLIGHTS
		if (ob.bounty.geometry_type == 'mesh_light'):
			ob.hide_render = True
		
		#PORTAL MESHLIGHTS
		if (ob.bounty.geometry_type == 'portal_light'):
			ob.hide_render = True

#remove all scene materials from objects
RemoveAllMaterials()

# b = bpy.context
# c = 0
# for obj in b.selected_editable_objects :
    # if obj.type == 'MESH':
        # c = c + 1
# range = 1/(c-1)
# value = 0

#set random colors to all mesh objects
for ob in bpy.context.selected_editable_objects:
	
	if ob.type == 'MESH':
		mat = bpy.data.materials.new('visuals')
		mat.bounty.mat_type = 'shinydiffusemat'
		r = random.random()
		mat.bounty.diff_color.hsv = (r,1,1)
		mat.diffuse_color = mat.bounty.diff_color
		mat.bounty.emittance = 1
		ob.data.materials.append(mat)
		#value = value + range
		
bpy.ops.object.select_all(action='DESELECT') 
if active.type == 'MESH':
	active.select = True
	#delete active object material
	bpy.ops.object.material_slot_remove({'object': active})

	#add pure white material to active object
	mat = bpy.data.materials.new('visuals')
	mat.bounty.mat_type = 'shinydiffusemat'
	mat.bounty.diff_color = (1,1,1)
	mat.diffuse_color = mat.bounty.diff_color
	mat.bounty.emittance = 1
	active.data.materials.append(mat)

#set render settings
bpy.context.scene.bounty.bg_transp = True
bpy.context.scene.bounty.intg_light_method = 'directlighting'
bpy.context.scene.bounty.intg_use_AO = False
bpy.context.scene.bounty.AA_passes = 4
bpy.context.scene.bounty.AA_inc_samples = 2
bpy.context.scene.bounty.AA_threshold = 0.003
bpy.context.scene.bounty.gs_clay_render = False
bpy.context.scene.bounty.gs_transp_shad = False
bpy.context.scene.bounty.gs_z_channel = False

