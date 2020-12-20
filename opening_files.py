import pandas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from optparse import OptionParser
import os
from tkinter import *
from pandas import ExcelWriter
plt.rcParams.update({'font.size': 16})
plt.rcParams["figure.figsize"] = (15,10)
import sys
sys.path.append("/Users/anagtv/Desktop/Cyclotron_python")
sys.path.append("/Users/anagtv/Documents/Beta-Beat.src-master")
#from tfs_files import tfs_pandas
#from mpl_interaction import figure_pz
import matplotlib.pyplot as plt
import tfs
from collections import OrderedDict
import datetime
from datetime import timedelta
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtGui import QIcon, QColor,QStandardItemModel
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QAction, QMessageBox,QTableWidget,QTableWidgetItem,QTabWidget
from PyQt5.QtWidgets import QCalendarWidget, QFontDialog, QColorDialog, QTextEdit, QFileDialog
from PyQt5.QtWidgets import QCheckBox, QProgressBar, QComboBox, QLabel, QStyleFactory, QLineEdit, QInputDialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5 import QtCore, QtWidgets
from PyQt5 import QtCore, QtWidgets
from numpy import arange, sin, pi
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
sys.path.append("/Users/anagtv/Desktop/Cyclotron_python/")
import matplotlib.pyplot as plt
#import saving_files_summary
#import saving_files_summary_list
#import plotting_summary_files_one_target
import numpy as np
import os
import tfs
import python_analysis_dataframe_20200416

def file_folder_opening(self):
    #options = QFileDialog.Options()
    #options |= QFileDialog.DontUseNativeDialog
    #self.dir_ = QFileDialog.getExistingDirectory(self, 'Select a folder:', '/Users/anagtv/Documents/OneDrive/Ana_GTV_Compartida/Visitas_Airo/', QFileDialog.ShowDirsOnly)
    [self.rotor_control_app_path_output,self.gimbal_control_app_path_output,self.pendant_control_app_path_output,self.system_control_app_path_output] = python_analysis_dataframe_20200416.writing_files(self.dir_)
    self.logfile_rotor = open(self.rotor_control_app_path_output,'r') 
    self.logfile_gimbal = open(self.gimbal_control_app_path_output,'r') 
    self.logfile_system = open(self.system_control_app_path_output,'r') 
    self.logfile_pendant = open(self.pendant_control_app_path_output,'r') 
    #SCAN, HOUR AND DAY RECORDED EACH DAY
    self.df_scans_rotor = python_analysis_dataframe_20200416.selecting_entries(self.logfile_rotor,"ROTOR") 
    self.df_scans_gimbal = python_analysis_dataframe_20200416.selecting_entries(self.logfile_gimbal,"GIMBAL") 
    self.df_scans_system = python_analysis_dataframe_20200416.selecting_entries(self.logfile_system,"SYSTEM") 
    self.df_scans_pendant = python_analysis_dataframe_20200416.selecting_entries(self.logfile_pendant,"PENDANT") 
    self.data_df_all_subsystems = (pd.concat([self.df_scans_rotor,self.df_scans_gimbal,self.df_scans_system,self.df_scans_pendant], axis=1, sort=False))
    open_files = ["RotorControlApp.log","GimbalControlApp.log","SystemManagerApp.log","PendantUIApp.log"]
    column_names  = ["DAY_ROTOR","HOUR_ROTOR","SCAN_ROTOR"]
    hours = (getattr(self.df_scans_rotor,column_names[1])).dropna()
    scans = (getattr(self.df_scans_rotor,column_names[2])).dropna()
    days = (getattr(self.df_scans_rotor,column_names[0])).dropna()
    for i in range (len(hours)):
       self.tablefiles_tab2.setItem(self.current_row_files,0, QTableWidgetItem(str(days.iloc[i])))
       self.tablefiles_tab2.setItem(self.current_row_files,1, QTableWidgetItem(str(hours.iloc[i])))
       self.tablefiles_tab2.setItem(self.current_row_files,2, QTableWidgetItem(str(scans.iloc[i])))
       self.current_row_files +=1 

def classify_display_file(self,file_to_display):
    if "ROTOR" in self.file_to_display:
        self.file_to_display_rotor = file_to_display
    elif "GIMBAL" in self.file_to_display:
        self.file_to_display_gimbal = file_to_display
    elif "SYSTEM" in self.file_to_display:
        self.file_to_display_system = file_to_display
    elif "PENDANT" in self.file_to_display:
        self.file_to_display_pendant = file_to_display


def file_output_filtering(self):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    self.output_path = QFileDialog.getExistingDirectory(self, 'Select a folder:', 'C:\\', QFileDialog.ShowDirsOnly)
    column_file_names = "FILE_NAME_" + str(self.logfile_type) 
    column_day = "DAY_" + str(self.logfile_type)
    scan_day = "SCAN_" + str(self.logfile_type)
    hour_day = "HOUR_" + str(self.logfile_type)
    column_names  = [scan_day,column_day ,hour_day,column_file_names]
    checking_values = []
    #date_values = list((getattr(self.data_df_all_subsystems,column_day)))
    date_format = "%Y-%m-%d"
    date_stamp = datetime.datetime.strptime(self.day_selected,date_format).date()
    condition_1 = (getattr(self.data_df_all_subsystems,column_day) == date_stamp) 
    condition_2 = (getattr(self.data_df_all_subsystems,scan_day) == self.scan_selected) 
    condition_3 = (getattr(self.data_df_all_subsystems,hour_day).str.contains(self.hour_selected[0:4]))
    self.index_scan = np.array((self.data_df_all_subsystems[condition_1 & condition_2 & condition_3].index))[0]
    #self.index_scan = index_alternative[0]
    python_analysis_dataframe_20200416.generate_output_file(self,"/Users/anagtv/Desktop/Visitas_Airo/File_analysis",column_names )
    print (self.index_scan)
    name = (getattr(self.data_df_all_subsystems,column_file_names)).dropna().iloc[self.index_scan]
    #name_2 = (getattr(self.data_df_all_subsystems,column_file_names)).dropna().iloc[index_alternative[1]]
    self.file_to_display = (os.path.join(self.output_path,name))
    self.classify_display_file(self.file_to_display)
    file = open(str(self.file_to_display), "r")
    return file


def filter_general_file(self,file_summary,notebook,filters):
        python_analysis_dataframe_20200416.summarising_file(self,file_summary[2],file_summary[0],filters[0])
        python_analysis_dataframe_20200416.summarising_file(self,file_summary[2],file_summary[1],filters[1])      
        file_scan = open(str(file_summary[0]), "r")
        file_best = open(str(file_summary[1]), "r")
        print ("file_scan")
        print (file_summary[0])
        print ("file_best")
        print (file_summary[1])
        print (notebook[0])
        with file_scan:
            text_scan = file_scan.read()
            notebook[0].setText(text_scan)
        with file_best:
            text_best = file_best.read()
            notebook[1].setText(text_best)

def filter_rotor_speed(self,path_motion):
        file_motion = open(str(path_motion), "r")
        with file_motion:
            text_motion = (file_motion.readlines())
            speed_values_1 = []
            speed_values_2 = []
            for line in (text_motion):
                speed_values_1.append(float(line.split()[5][:-1]))
                speed_values_2.append(line.split()[-1])

def checking_functions(self,hour_column,day_column,scan_column,date_stamp,hour_selected,scan_selected):
        if len(getattr(self.data_df_all_subsystems,hour_column).dropna()) != 0:
           condition_day = getattr(self.data_df_all_subsystems,day_column) == date_stamp
           condition_hour = getattr(self.data_df_all_subsystems,hour_column).str.contains(self.hour_selected[0:4]) 
           condition_rotor = getattr(self.data_df_all_subsystems,scan_column).str.contains(self.scan_selected)
           index_hour = getattr(self.data_df_all_subsystems,hour_column)[(condition_day) & (condition_hour) & (condition_rotor)]
        else:
           index_hour = []
        return index_hour

def main():
    print ("HOLA")

if __name__ == "__main__":
    #_input_path,_output_path,target_current = _parse_args()
    main()