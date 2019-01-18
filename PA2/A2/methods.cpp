//
//  scene.cpp
//  A2
//
//  Created by 金启林 on 1/4/19.
//  Copyright © 2019 金启林. All rights reserved.
//
#define _USE_MATH_DEFINES
#include <stdio.h>
#include <iostream>
#include <Eigen/Dense>
#include "methods.hpp"

using namespace Eigen;

MatrixXf getgetTransformMatrix(float x, float y, float z, float radius, float* u,
                              float* v, float* w, float* e, float l, float r,
                              float b, float t, float n, float f, float nx, float ny)
{
    MatrixXf scaleM(4,4);
    scaleM << radius,0,0,0,0,radius,0,0,0,0,radius,0,0,0,0,1;
    
    MatrixXf transM(4,4);
    transM << 1,0,0,x,0,1,0,y,0,0,1,z,0,0,0,1;
    
    MatrixXf mM(4,4);
    mM= transM*scaleM;
    
    MatrixXf mvp(4,4);
    mvp << (nx/2),0,0,(nx-1)/2,0,ny/2,0,(ny-1)/2,0,0,1,0,0,0,0,1;
    
    MatrixXf morth(4,4);
    morth << 2/(r-l),0,0,-1*(r+l)/(r-l),0,2/(t-b),0,-1*(t+b)/(t-b),0,0,2/(n-f),-1*(n+f)/(n-f),0,0,0,1;
    //morth << (r-l)/2,0,0,(l+r)*(l-r)/-4,0,(t-b)/2,0,(t+b)*(t-b)/-4,0,0,(n-f)/2,(n+f)*(n-f)/-4,0,0,0,1;
    
    MatrixXf mp(4,4);
    mp << n,0,0,0,0,n,0,0,0,0,n+f,-1*f*n,0,0,1,0;
    
    
    MatrixXf mCam(4,4);
    mCam << 1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1;
    mCam = mCam.inverse();
    
    //return mvp*morth*mp*mCam*mM;
    return morth*mp*mCam*mM;
    //return mp*mCam*mM;
    //return mCam*mM;
}

float getArea(float x1,float y1,float x2,float y2,float x3,float y3){
    float abx = x2-x1;
    float aby = y2-y1;
    float bcx = x3-x2;
    float bcy = y3-y2;
    
    return fabs((abx*bcy-aby*bcx)/2);
}

bool isIn(float x1,float y1,float x2,float y2,float x3,float y3, float x0, float y0){
    float area0 = getArea(x1,y1,x2,y2,x3,y3);
    
    float area1 = getArea(x1,y1,x2,y2,x0,y0);
    float area2 = getArea(x1,y1,x0,y0,x3,y3);
    float area3 = getArea(x0,y0,x2,y2,x3,y3);
    
    if(area1+area2+area3>area0*1.2)//1.1
        return false;
    else
        return true;
}
