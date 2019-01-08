//
//  sphere_generator.hpp
//  A2
//
//  Created by 金启林 on 1/5/19.
//  Copyright © 2019 金启林. All rights reserved.
//

#ifndef sphere_generator_hpp
#define sphere_generator_hpp

#include <stdio.h>
void create_scene();
extern int     gNumVertices;// Number of 3D vertices.
extern int     gNumTriangles;// Number of triangles.
extern int*    gIndexBuffer;// Vertex indices for the triangles.
extern float** gVertices;
#endif /* sphere_generator_hpp */
