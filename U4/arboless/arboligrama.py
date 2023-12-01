#árboles binarios

from anytree import Node, RenderTree

root = Node("DIRECTOR: Jose Ernesto Olvera Gonzalez")

level_1_child_1 = Node("SUBDIRECTOR: Dolores Alvarez Muñoz", parent=root)
level_1_child_2 = Node("SUBDIRECTOR: Ricardo Lara Colon", parent=root)
level_1_child_3 = Node("SUBDIRECTOR: Victor Manuel Velasco Gallardo", parent=root)
level_2_child_1 = Node("Departamento Gestion: Julissa Elayne Cosme", parent=level_1_child_1)
level_2_child_1 = Node("Departamento Comunicación: Adriana Villegas", parent=level_1_child_1)
level_2_child_1 = Node("Departamento De Ciencia: Magdalena Cuevas Martinez", parent=level_1_child_2)
level_2_child_1 = Node("Division De Estudios: Jorge Fernando Carmona", parent=level_1_child_2)
level_2_child_1 = Node("Departamento De Recursos Humanos: Tannia Carolina Moran Bonilla", parent=level_1_child_3)
level_2_child_1 = Node("Division De Recursos Financieros: Alberto Diaz Juarez", parent=level_1_child_3)

for pre, fill, node in RenderTree(root):
    print("%s%s" % (pre, node.name))