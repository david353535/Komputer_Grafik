import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# =============================
# DATA KUBUS 3D
# =============================
cube_vertices = [
    (-1, -1, -1), (1, -1, -1), (1, 1, -1), (-1, 1, -1),
    (-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1)
]

cube_edges = [
    (0,1),(1,2),(2,3),(3,0),
    (4,5),(5,6),(6,7),(7,4),
    (0,4),(1,5),(2,6),(3,7)
]

# Transformasi Kubus
cube_tx = -3
cube_ty = 0
cube_tz = -10
cube_rx = 0
cube_ry = 0
cube_scale = 1


# =============================
# DATA PERSEGI 2D
# =============================
rect_vertices = [
    (-1,-1,0),
    (1,-1,0),
    (1,1,0),
    (-1,1,0)
]

# Transformasi Persegi
rect_tx = 3
rect_ty = 0
rect_scale = 1
rect_rot = 0
shear_x = 0
shear_y = 0
reflect_x = 1
reflect_y = 1


# =============================
# FUNGSI KUBUS
# =============================
def draw_cube():
    glPushMatrix()

    glTranslatef(cube_tx, cube_ty, cube_tz)
    glRotatef(cube_rx, 1,0,0)
    glRotatef(cube_ry, 0,1,0)
    glScalef(cube_scale, cube_scale, cube_scale)

    glBegin(GL_LINES)
    glColor3f(1,1,1)
    for edge in cube_edges:
        for v in edge:
            glVertex3fv(cube_vertices[v])
    glEnd()

    glPopMatrix()


# =============================
# FUNGSI SHEAR + REFLECT 2D
# =============================
def transform_rect(vertices):
    new = []
    for x,y,z in vertices:

        # reflection
        x *= reflect_x
        y *= reflect_y

        # shear
        x = x + shear_x*y
        y = y + shear_y*x

        new.append((x,y,z))
    return new


# =============================
# FUNGSI PERSEGI
# =============================
def draw_rect():
    glPushMatrix()

    glTranslatef(rect_tx, rect_ty, -10)
    glRotatef(rect_rot, 0,0,1)
    glScalef(rect_scale, rect_scale, 1)

    verts = transform_rect(rect_vertices)

    glBegin(GL_QUADS)
    glColor3f(0,1,0)
    for v in verts:
        glVertex3fv(v)
    glEnd()

    glPopMatrix()


# =============================
# MAIN PROGRAM
# =============================
def main():
    global cube_tx,cube_ty,cube_rx,cube_ry,cube_scale
    global rect_tx,rect_ty,rect_scale,rect_rot
    global shear_x,shear_y,reflect_x,reflect_y

    pygame.init()
    display = (1000,700)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, display[0]/display[1], 0.1, 50)
    glEnable(GL_DEPTH_TEST)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()

            if event.type == KEYDOWN:

                # =====================
                # KONTROL KUBUS 3D
                # =====================
                if event.key == K_w: cube_ty += 0.5
                if event.key == K_s: cube_ty -= 0.5
                if event.key == K_a: cube_tx -= 0.5
                if event.key == K_d: cube_tx += 0.5

                if event.key == K_q: cube_rx += 5
                if event.key == K_e: cube_ry += 5

                if event.key == K_z: cube_scale += 0.1
                if event.key == K_x: cube_scale -= 0.1


                # =====================
                # KONTROL PERSEGI 2D
                # =====================
                if event.key == K_i: rect_ty += 0.5
                if event.key == K_k: rect_ty -= 0.5
                if event.key == K_j: rect_tx -= 0.5
                if event.key == K_l: rect_tx += 0.5

                if event.key == K_u: rect_rot += 5
                if event.key == K_o: rect_rot -= 5

                if event.key == K_n: rect_scale += 0.1
                if event.key == K_m: rect_scale -= 0.1

                # shear
                if event.key == K_1: shear_x += 0.2
                if event.key == K_2: shear_y += 0.2

                # reflect
                if event.key == K_3: reflect_x *= -1
                if event.key == K_4: reflect_y *= -1

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        draw_cube()
        draw_rect()

        pygame.display.flip()
        pygame.time.wait(10)


main()
