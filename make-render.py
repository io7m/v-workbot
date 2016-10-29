import bpy
import io

for s in bpy.data.scenes:
  if "io7m_meta_preview" in s:
    print("Rendering %s" % s.name)
    s.render.filepath = '//preview_%s.jpg' % s.name
    bpy.context.screen.scene = s
    bpy.ops.render.render(write_still = True)

