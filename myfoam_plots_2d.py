#!/usr/bin/python

import matplotlib.pyplot as plt
import os
import csv
import numpy as np

def plotU(path,output_name):
    #path is a string indicating where the input csv file lies in
    #output_name is a string for output figure file
    with open(path, 'rb') as csvfile:
        reader = csv.reader(csvfile)
        Uhistory = list(reader)
        Uhistory = np.array(Uhistory)
        Uhistory = Uhistory.astype(np.float)#convert string to floats

    #plot wave height history
    plt.figure()
    plt.plot(Uhistory[:,0],Uhistory[:,2],'r-',label='Ux')
    legend = plt.legend(loc='upper center', shadow=True, fontsize='x-large')
    #plt.xlim(3.0,4.0)
    plt.xlabel('time (s)')
    plt.ylabel('velocity Ux (m/s)')
    plt.title('velocity history at center of tank')
    if not('myplot' in os.listdir('./')):
        os.mkdir('myplot')
    plt.savefig('./myplot/'+output_name+'.png', bbox_inches='tight')
    plt.close()

def plot_alpha1(path,output_name):
    #path is a string indicating where the input csv file lies in
    #output_name is a string for output figure file
    with open(path, 'rb') as csvfile:
        reader = csv.reader(csvfile)
        history = list(reader)
        history = np.array(history)
        history = history.astype(np.float)#convert string to floats

    #plot wave height history
    plt.figure()
    plt.plot(history[:,0],history[:,1],'r-',label='wave height')
    plt.ylim((0,0.6))
    legend = plt.legend(loc='upper center', shadow=True, fontsize='x-large')
    #plt.xlim(3.0,4.0)
    plt.xlabel('time (s)')
    plt.ylabel('wave height (m)')
    plt.title('wave height history at center of tank')
    if not('myplot' in os.listdir('./')):
        os.mkdir('myplot')
    plt.savefig('./myplot/'+output_name+'.png', bbox_inches='tight')
    plt.close()

def plot_forces(path,output_name):
    #path is a string indicating where the input csv file lies in
    #output_name is a string for output figure file
    with open(path, 'rb') as csvfile:
        reader = csv.reader(csvfile)
        history = list(reader)
        history = np.array(history)
        history = history.astype(np.float)#convert string to floats

    #plot wave height history
    plt.figure()
    plt.plot(history[:,0],history[:,1]+history[:,2],'r-',label='forces in x direction')
    #plt.ylim((0,0.6))
    legend = plt.legend(loc='upper center', shadow=True, fontsize='x-large')
    #plt.xlim(3.0,4.0)
    plt.xlabel('time (s)')
    plt.ylabel('forces (N)')
    plt.title('time history of forces on all houses')
    if not('myplot' in os.listdir('./')):
        os.mkdir('myplot')
    plt.savefig('./myplot/'+output_name+'.png', bbox_inches='tight')
    plt.close()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#path = './postProcessing/history/origin_U.csv.point_6.csv'
#output_name = 'Ux_at_z=0.19'
#plotU(path, output_name)
#
#
#path_alpha1 = './postProcessing/history_origin_alpha.water.csv'
#output_name_alpha1 = 'alpha.water'
#plot_alpha1(path_alpha1,output_name_alpha1)


path = './postProcessing/forces.csv'
output_name = 'Fx'
plotU(path, output_name)
