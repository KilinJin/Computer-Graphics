//
//  scene.hpp
//  A2
//
//  Created by 金启林 on 1/4/19.
//  Copyright © 2019 金启林. All rights reserved.
//

#ifndef methods_hpp
#define methods_hpp

#include <stdio.h>
#include <Eigen/Dense>
using namespace Eigen;
MatrixXf getgetTransformMatrix(float x, float y, float z, float radius, float* u,
                              float* v, float* w, float* e, float l, float r,
                              float b, float t, float n, float f, float nx, float ny);
float getArea(float x1,float y1,float x2,float y2,float x3,float y3);
bool isIn(float x1,float y1,float x2,float y2,float x3,float y3, float x0, float y0);
#endif /* scene_hpp */
