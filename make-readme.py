import bpy
import io

with open("README.md", "wt") as f:
  with open("README-HEADER.txt") as f_header:
    for line in f_header:
      f.write(line)
    f.write("\n")

    f.write("License\n")
    f.write("===\n")
    f.write("\n")
    f.write("```\n")
    for line in bpy.data.texts['license'].lines:
      f.write(line.body)
      f.write("\n")
    f.write("```\n")
    f.write("\n")

    f.write("Scene statistics\n")
    f.write("===\n")
    f.write("\n")
    f.write("```\n")

    for mesh in bpy.data.meshes:
      if not ("io7m_meta_measured" in mesh):
        continue
      #endif

      mesh_poly_count = 0
      for poly in mesh.polygons:
        if len(poly.vertices) > 3:
          mesh_poly_count = mesh_poly_count + (len(poly.vertices) / 2)
        else:
          mesh_poly_count = mesh_poly_count + 1
        #endif
      #endfor

      f.write("Mesh: %s\n" % mesh.name)
      f.write("  Polygons: %d\n" % mesh_poly_count)

      for material in mesh.materials:
        if len(material.texture_slots) > 0:
          f.write("  Textures:\n")
          for slot in material.texture_slots:
            if slot:
              img = slot.texture.image
              f.write("    Image: %s %dx%d\n" % (img.name, img.size[0], img.size[1]))
        #endif
      f.write("\n")
      #endfor
    #endfor

    f.write("```\n")
    f.write("\n")

  #endwith
#endwith
