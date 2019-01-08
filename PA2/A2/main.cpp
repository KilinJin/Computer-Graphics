//
//  main.cpp
//  A2
//
//  Created by 金启林 on 1/4/19.
//  Copyright © 2019 金启林. All rights reserved.
//

#include <iostream>
#include <math.h>
#include <stdio.h>
#include "methods.hpp"
#include <OpenGL/gl.h>
#include <GLUT/GLUT.h>
#include "sphere_generator.hpp"

using namespace std;

double startImageX = -1.001953125;
double startImageY = -1.001953125;
double  imageDis = 0.00390625;
double pointSize = 390625;
double zBuffer[512][512] = {};

float getMax(float x, float y, float z){
    if(x>=y && x>=z)
        return x;
    else if (y>x&&y>=z)
        return y;
    else
        return z;
}
float getMin(float x, float y, float z){
    if(x<y && x<z)
        return x;
    else if (y<=x&&y<z)
        return y;
    else
        return z;
}

void testAndColor(float x1, float y1, float z1, float x2, float y2, float z2, float x3, float y3, float z3){
    double zValue = z1+z2+z3/3;
    float max_x, max_y, min_x, min_y;
    int maxX, maxY, minX, minY;
    max_x = getMax(x1, x2, x3);
    max_y = getMax(y1, y2, y3);
    min_x = getMin(x1, x2, x3);
    min_y = getMin(y1, y2, y3);
    maxX = (int)((max_x-startImageX)/imageDis)+1;
    maxY = (int)((max_y-startImageY)/imageDis)+11;
    minX = (int)((min_x-startImageX)/imageDis);
    minY = (int)((min_y-startImageY)/imageDis);
    cout<<zBuffer[1][1]<<endl;
    for (int i = minX;i<=maxX;i++){
        for (int j = minY;j<=maxY;j++){
            if(zBuffer[i][j]==0)
                zBuffer[i][j] = zValue;
            if(isIn(x1,y1,x2,y2,x3,y3,startImageX+(i+1)*imageDis, startImageY+(j+1)*imageDis) && zValue<=zBuffer[i][j]){
                zBuffer[i][j] = zValue;
                glBegin(GL_POINTS);
                glPointSize(pointSize);
                glVertex2f(startImageX+(i+1)*imageDis, startImageY+(j+1)*imageDis);
                glColor3f(1, i, j);
                glEnd();
            }
        }
    }
}

void display()
{
    glClear(GL_COLOR_BUFFER_BIT);
    create_scene();
    
    float u[3] = {1,0,0};
    float v[3] = {0,1,0};
    float w[3] = {0,0,1};
    float e[3] = {0,0,0};
    
    MatrixXf transform(4,4);
    transform<<getgetTransformMatrix(0,0,-7,2,u,v,w,e,-0.1,0.1,-0.1,0.1,-0.1,-1000,512,512);
    
    MatrixXf temp(4,1);
    
    for(int i = 0;i<gNumVertices;i++){
        temp << gVertices[i][0], gVertices[i][1], gVertices[i][2], gVertices[i][3];
        temp = transform*temp;
        gVertices[i][0] = temp(0,0)/temp(3,0);
        gVertices[i][1] = temp(1,0)/temp(3,0);
        gVertices[i][2] = temp(2,0)/temp(3,0);
        gVertices[i][3] = temp(3,0)/temp(3,0);
        //glBegin(GL_POINTS);
        //glVertex2f(temp(0,0)/temp(3,0), temp(1,0)/temp(3,0));
        //glColor3f(1, 1, 1);
        //glEnd();
    }
    for(int i = 0;i<gNumTriangles;i++){
        testAndColor(gVertices[gIndexBuffer[i*3]][0], gVertices[gIndexBuffer[i*3]][1],gVertices[gIndexBuffer[i*3]][2],gVertices[gIndexBuffer[i*3+1]][0], gVertices[gIndexBuffer[i*3+1]][1], gVertices[gIndexBuffer[i*3+1]][2],
            gVertices[gIndexBuffer[i*3+2]][0], gVertices[gIndexBuffer[i*3+2]][1],
                     gVertices[gIndexBuffer[i*3+2]][2]);
    }
    glFlush();
}
int main(int argc, char ** argv)
{
    glutInit(&argc, argv);
    glutCreateWindow("PA2");
    glutDisplayFunc(display);
    glutMainLoop();
    
    return 0;
}
