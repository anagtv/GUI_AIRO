#! /usr/bin/env python3
#  -*- coding:utf-8 -*-
###############################################################
# kenwaldek                           MIT-license

# Title: PyQt5 lesson 14              Version: 1.0
# Date: 09-01-17                      Language: python3
# Description: pyqt5 gui and opening files
# pythonprogramming.net from PyQt4 to PyQt5
###############################################################
# do something


import sys
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtGui import QIcon, QColor,QStandardItemModel
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QAction, QMessageBox,QTableWidget,QTableWidgetItem,QTabWidget
from PyQt5.QtWidgets import QCalendarWidget, QFontDialog, QColorDialog, QTextEdit, QFileDialog
from PyQt5.QtWidgets import QCheckBox, QProgressBar, QComboBox, QLabel, QStyleFactory, QLineEdit, QInputDialog
import pandas as pd
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
import sys
sys.path.append("/Users/anagtv/Desktop/Visitas_Airo/File_analysis/")
import python_analysis_dataframe_20200416
import datetime
from datetime import timedelta
import datetime
#matplotlib.use('Qt5Agg')

class window(QMainWindow):

    def __init__(self):
        super(window, self).__init__()

        self.setGeometry(50, 50, 1500, 1000)
        self.setWindowTitle('pyqt5 Tut')
        self.setWindowIcon(QIcon('pic.png'))
        self.current_row = 0
        self.current_row_folder = 0
        self.current_row_analysis = 0 
        self.current_row_files = 0
        self.current_row_logfiles = 0
        self.fileName = ""
        #self.rotor_control_app_path_output = os.path.join(self.dir_,"all_scans_rotor")
        zero_data = np.zeros(shape=(4,4))
        self.df_scans = pd.DataFrame(zero_data,columns=["SCAN_ROTOR","DAY_ROTOR","HOUR_ROTOR","FILE_NAME_ROTOR"])
        self.index_scan = 0
        self.logfile_type = "ROTOR"



        openFile = QAction('Open File', self)
        openFolder = QAction('Open Folder', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open File')
        openFile.triggered.connect(self.file_open)
        openFolder.triggered.connect(self.file_folder)
        self.statusBar()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(openFile)
        fileMenu.addAction(openFolder)

 
        self.setWindowTitle("AIRO logfile Analysis")

        self.fileMenu = QtWidgets.QMenu('&File', self)
        self.fileMenu.addAction('&Quit', self.fileQuit,
                                 QtCore.Qt.CTRL + QtCore.Qt.Key_Q)
        self.menuBar().addMenu(self.fileMenu)
        self.help_menu = QtWidgets.QMenu('&Help', self)
        self.menuBar().addSeparator()
        self.menuBar().addMenu(self.help_menu)
        self.main_widget = QtWidgets.QWidget(self)
        self.plot_widget = QWidget(self.main_widget)
        self.plot_widget.setGeometry(250,180,500,600)
        

        l = QtWidgets.QVBoxLayout(self.main_widget)
        m = QtWidgets.QVBoxLayout(self.plot_widget)
        self.main_widget.setFocus()
        self.setCentralWidget(self.main_widget)

        self.home(l)
        self.setMinimumSize(1000, 800)

       
    def editor(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)


    def file_open(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        python_analysis_dataframe_20200416.writing_files(file)
        self.tablefiles_tab2.setItem(self.current_row,0, QTableWidgetItem(self.fileName))
        self.tablefiles_tab2.setItem(self.current_row,1, QTableWidgetItem(str(target_number)))
        self.current_row += 1
        self.datos = [self.tableWidget.item(0,0).text()]
        with file:
            text = file.read()
            self.textEdit2.setText(text)


    def file_folder(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.dir_ = QFileDialog.getExistingDirectory(self, 'Select a folder:', '/Users/anagtv/Documents/OneDrive/Ana_GTV_Compartida/Visitas_Airo/', QFileDialog.ShowDirsOnly)
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
        print ("ALL DATAFRAMES")
        print (self.data_df_all_subsystems)
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


    def handleSelectionChanged_component(self, selected, deselected):
        index=(self.tablestatistic_tab2.selectionModel().currentIndex())
        self.fileName=index.sibling(index.row(),index.column()).data()
        print ("TYPE OF FILE")
        if self.fileName == "SystemManagerApp.log":
           self.logfile_type = "SYSTEM"
        elif self.fileName == "RotorControlApp.log":
           self.logfile_type = "ROTOR"
        elif self.fileName == "PendantUIApp.log":
           print ("IM HERE")
           self.logfile_type = "PENDANT"
        elif self.fileName == "GimbalControlApp.log":
           self.logfile_type = "GIMBAL"
        print (self.logfile_type)
        print ("HEREEEEEEE")
        print (index.row())
        print (index.column())
        print(self.fileName)

    def file_output(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.output_path = QFileDialog.getExistingDirectory(self, 'Select a folder:', 'C:\\', QFileDialog.ShowDirsOnly)
        column_file_names = "FILE_NAME_" + str(self.logfile_type) 
        column_day = "DAY_" + str(self.logfile_type)
        scan_day = "SCAN_" + str(self.logfile_type)
        hour_day = "HOUR_" + str(self.logfile_type)
        print ("DAY SELECTED")
        print (type(self.day_selected))
        print (getattr(self.data_df_all_subsystems,column_day))
        print (getattr(self.data_df_all_subsystems,scan_day))
        print ("Checking values")
        checking_values = []
        date_values = list((getattr(self.data_df_all_subsystems,column_day)))
        print (date_values)
        date_format = "%Y-%m-%d"
        date_stamp = datetime.datetime.strptime(self.day_selected,date_format).date()
        for i in range(len(date_values)):
              print ((date_values[i]))
              print (str(self.day_selected))
              try:
                 checking_values.append(date_values[i] == date_stamp)
              except:
                 checking_values.append(date_values[i] == str(self.day_selected))
        print (checking_values)
        print ((getattr(self.data_df_all_subsystems,column_day) == date_stamp))
        print (np.array((getattr(self.data_df_all_subsystems,scan_day) == self.scan_selected)))
        print ("INDEX ALTERNATIVE")
        index_alternative = np.array((self.data_df_all_subsystems[(getattr(self.data_df_all_subsystems,column_day) == date_stamp) & (getattr(self.data_df_all_subsystems,scan_day) == self.scan_selected) & getattr(self.data_df_all_subsystems,hour_day).str.contains(self.hour_selected[0:4])].index))
        #print (getattr(self.data_df_all_subsystems,hour_day).dt.strftime('%m/%d/%Y'))
        #print (adsfaf)
        print ("HEREEE")
        print (index_alternative)
        print (self.index_scan)
        self.index_scan = index_alternative[0]
        python_analysis_dataframe_20200416.generate_output_file(self,"/Users/anagtv/Desktop/Visitas_Airo/File_analysis")
        name = (getattr(self.data_df_all_subsystems,column_file_names)).dropna().iloc[index_alternative[0]]
        #name_2 = (getattr(self.data_df_all_subsystems,column_file_names)).dropna().iloc[index_alternative[1]]
        print ("HEREEEE")
        print (self.logfile_type)
        print ((getattr(self.data_df_all_subsystems,column_file_names)).dropna())     
        print (self.index_scan)
        print (name)
        self.file_to_display = os.path.join(self.output_path,name)
        file = open(str(self.file_to_display), "r")
        with file:
            text = file.read()
            self.textEdit_files.setText(text)


    def extract_best(self):
        file = open(str(self.file_to_display), "r")
        with file:
            text = file.read()
            self.textEdit_files.setText(text)


    def extract_scan(self):
        file = open(str(self.file_to_display), "r")
        with file:
            text = file.read()
            self.textEdit_files.setText(text)



    def filter_output_scan(self):
        print ("HEREEEEE")
        python_analysis_dataframe_20200416.reading_rotor_best_scan(self,"/Users/anagtv/Documents/Visitas_AIRO/Visita_AIRO_2020112123/AIRO-Logs-0168-2020-11-20T18-55-10")
        python_analysis_dataframe_20200416.reading_rotor_motion(self,"/Users/anagtv/Documents/Visitas_AIRO/Visita_AIRO_2020112123/AIRO-Logs-0168-2020-11-20T18-55-10")
        rotor_control_app_path_scan = os.path.join("/Users/anagtv/Documents/Visitas_AIRO/Visita_AIRO_2020112123/AIRO-Logs-0168-2020-11-20T18-55-10","scan_rotor_summary")
        rotor_control_app_path_best = os.path.join("/Users/anagtv/Documents/Visitas_AIRO/Visita_AIRO_2020112123/AIRO-Logs-0168-2020-11-20T18-55-10","best_rotor_summary")
        rotor_control_motion = os.path.join("/Users/anagtv/Documents/Visitas_AIRO/Visita_AIRO_2020112123/AIRO-Logs-0168-2020-11-20T18-55-10","motion_rotor_summary")
        file_scan = open(str(rotor_control_app_path_scan), "r")
        file_best = open(str(rotor_control_app_path_best), "r")
        file_motion = open(str(rotor_control_motion), "r")
        with file_scan:
            text_scan = file_scan.read()
            self.textEdit_files_selection_rotor.setText(text_scan)
        with file_best:
            text_best = file_best.read()
            self.textEdit_files_selection_2_rotor.setText(text_best)
        with file_motion:
            text_motion = (file_motion.readlines())
            print ("TEXT MOTION")
            print ("HEREEE")
            print (text_motion)
            print (len(text_motion))
            speed_values_1 = []
            speed_values_2 = []
            for line in (text_motion):
                print (line)
                print (line.split())
                speed_values_1.append(line.split()[5])
                speed_values_2.append(line.split()[-1])
        print ("SPEED VALUES")
        print (speed_values_1)
        print (speed_values_2)
        #self.sc3.axes.errorbar(speed_values_1,yerr=0,"o",label= "SPEED ROTOR 1", picker=5)
        #self.sc3.axes.errorbar(speed_values_2,yerr=0,"o",label= "SPEED ROTOR 2", picker=5)

    def file_output_second(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.output_path = QFileDialog.getExistingDirectory(self, 'Select a folder:', 'C:\\', QFileDialog.ShowDirsOnly)
        column_file_names = "FILE_NAME_" + str(self.logfile_type) 
        column_day = "DAY_" + str(self.logfile_type)
        scan_day = "SCAN_" + str(self.logfile_type)
        hour_day = "HOUR_" + str(self.logfile_type)
        print ("DAY SELECTED")
        print (type(self.day_selected))
        print (getattr(self.data_df_all_subsystems,column_day))
        print (getattr(self.data_df_all_subsystems,scan_day))
        print ("Checking values")
        checking_values = []
        date_values = list((getattr(self.data_df_all_subsystems,column_day)))
        print (date_values)
        date_format = "%Y-%m-%d"
        date_stamp = datetime.datetime.strptime(self.day_selected,date_format).date()
        for i in range(len(date_values)):
              print ((date_values[i]))
              print (str(self.day_selected))
              try:
                 checking_values.append(date_values[i] == date_stamp)
              except:
                 checking_values.append(date_values[i] == str(self.day_selected))
        print (checking_values)
        print ((getattr(self.data_df_all_subsystems,column_day) == date_stamp))
        print (np.array((getattr(self.data_df_all_subsystems,scan_day) == self.scan_selected)))
        print ("INDEX ALTERNATIVE")
        index_alternative = np.array((self.data_df_all_subsystems[(getattr(self.data_df_all_subsystems,column_day) == date_stamp) & (getattr(self.data_df_all_subsystems,scan_day) == self.scan_selected) & getattr(self.data_df_all_subsystems,hour_day).str.contains(self.hour_selected[0:3])].index))
        #print (getattr(self.data_df_all_subsystems,hour_day).dt.strftime('%m/%d/%Y'))
        #print (adsfaf)
        print ("Now also hour")
        print (getattr(self.data_df_all_subsystems,hour_day))
        print (self.hour_selected[0:3])
        print (getattr(self.data_df_all_subsystems,hour_day).str.contains(self.day_selected[0:2]))
        print ("HEREEE")
        print (index_alternative)
        print (self.index_scan)
        self.index_scan = index_alternative[0]
        python_analysis_dataframe_20200416.generate_output_file(self,"/Users/anagtv/Desktop/Visitas_Airo/File_analysis")
        name = (getattr(self.data_df_all_subsystems,column_file_names)).dropna().iloc[index_alternative[0]]
        #name_2 = (getattr(self.data_df_all_subsystems,column_file_names)).dropna().iloc[index_alternative[1]]
        print ("HEREEEE")
        print (self.logfile_type)
        print ((getattr(self.data_df_all_subsystems,column_file_names)).dropna())     
        print (self.index_scan)
        print (name)
        self.file_to_display_2 = os.path.join(self.output_path,name)
        file = open(str(self.file_to_display_2), "r")
        with file:
            text = file.read()
            self.textEdit_files_2.setText(text)
        #saving_files_summary_list.main(self,"/Users/anagtv/Desktop",0)

    def analyze_selected_files(self,values):
        self.question =  QMessageBox()
        self.question.setText("Select an output folder")
        self.question.setGeometry(QtCore.QRect(200, 300, 100, 50)) 
        self.question.setStandardButtons(QMessageBox.Save)
        self.question.buttonClicked.connect(self.file_output)
        self.question.show()

    def analyze_selected_files_second(self,values):
        self.question =  QMessageBox()
        self.question.setText("Select an output folder")
        self.question.setGeometry(QtCore.QRect(200, 300, 100, 50)) 
        self.question.setStandardButtons(QMessageBox.Save)
        self.question.buttonClicked.connect(self.file_output_second)
        self.question.show()

    def analyze_all_selected_files(self,values):
        self.question_all =  QMessageBox()
        self.question_all.setText("Select an output folder")
        self.question_all.setGeometry(QtCore.QRect(200, 300, 100, 50)) 
        self.question_all.setStandardButtons(QMessageBox.Save)
        self.question_all.buttonClicked.connect(self.combining_several_files)
        self.question_all.show() 
        
    def combining_several_files(self):
        file_components_path = []   
        output_name = str(self.df_day_scan_hour.SCAN_ROTOR.iloc[0]) + "_" + str(self.df_day_scan_hour.DAY_ROTOR.iloc[0]) + "_" + str(self.df_day_scan_hour.HOUR_ROTOR.iloc[0])
        output_name_combined = str(self.df_day_scan_hour.SCAN_ROTOR.iloc[0]) + "_" + str(self.df_day_scan_hour.DAY_ROTOR.iloc[0]) + "_" + str(self.df_day_scan_hour.HOUR_ROTOR.iloc[0]) + "_combined"
        output_path = os.path.join("/Users/anagtv/Documents/Visitas_AIRO/Visita_AIRO_2020112123/AIRO-Logs-0168-2020-11-20T18-55-10",output_name)
        output_path_combined = os.path.join("/Users/anagtv/Documents/Visitas_AIRO/Visita_AIRO_2020112123/AIRO-Logs-0168-2020-11-20T18-55-10",output_name_combined)
        for k in range(len(self.names_components)):
            file_name_path = (getattr(self.df_day_scan_hour,self.columns_names_components[k]))
            file_components_path.append(os.path.join("/Users/anagtv/Documents/Visitas_AIRO/Visita_AIRO_2020112123/AIRO-Logs-0168-2020-11-20T18-55-10",str(np.array(file_name_path)[0])))
        combined_file = []
        combined_file_element = []
        combined_file_hours = []
        for file_path_name in file_components_path:
          file_path_name_rotor_read = open(file_path_name,"r")
          for line in file_path_name_rotor_read:
             parts = line.split()
             combined_file.append(parts)
             combined_file_hours.append(parts[0][11:27])
             if (file_path_name[49]) == "R":
                 combined_file_element.append("ROTOR")
             elif (file_path_name[49]) == "G":
                 combined_file_element.append("GIMBAL")
             elif (file_path_name[49]) == "S":
                 combined_file_element.append("SYSTEM")
             elif (file_path_name[49]) == "P":
                 combined_file_element.append("PENDANT")
             # DEFINITION: SORTING COMBINED FILE BY HOUR           
        combined_file_sorted = [combined_file for _,combined_file in sorted(zip(combined_file_hours,combined_file))]
        combined_file_element_sorted = [combined_file_element for _,combined_file_element in sorted(zip(combined_file_hours,combined_file_element))]
        time_stamp = []
        message_information = []
        action = []
        file_type = []
        for i in range(len(combined_file_sorted)):
        #    # REMOVING EXTRA LINES
            if ">" not in combined_file_sorted[i][0]:
                time_stamp.append(combined_file_sorted[i][0][1:])
                message_information.append('_'.join(combined_file_sorted[i][1:3]))
                action.append('_'.join(combined_file_sorted[i][3:]))
                file_type.append(combined_file_element_sorted[i])
        ## SETTING DATAFRAME FOR USING AS AN OUTPUT
        data_df_combined = pd.DataFrame.from_records({'TIME_STAMP':time_stamp, 'TYPE': message_information, 'ACTION':action, 'FILE_TYPE': file_type})
        data_df_combined =  data_df_combined.loc[:, ['FILE_TYPE', 'TIME_STAMP',   'TYPE',  'ACTION']]  
        #WRITING 
        #file_path_name_combined = "test_" + str(j) + ".out"
        #file_path_name_combined_filtered = "test_filtered_" + str(j) + ".out"
        #tfs.write(output_path, data_df_combined, save_index="index_column")
        tfs.write(output_path, data_df_combined)
        data_to_verify = tfs.read(output_path)
        #KEEP REMOVING UNNECESARY ELEMENTS
        data_to_verify_1 = (data_to_verify[~data_to_verify.ACTION.str.contains("Previous_Entry_Repeats")])
        data_to_verify_2 = (data_to_verify_1[~data_to_verify_1.ACTION.str.contains("$s00_Executing_Transitioning_ScoutScan")])
        data_to_verify_3 = (data_to_verify_2[~data_to_verify_2.ACTION.str.contains("Handling_Client_Message:_#&22_History/RotorPC/LastKnownOnTime")])
        self.data_to_verify_4 = (data_to_verify_3[~data_to_verify_3.ACTION.str.contains("ConfigStore.Set:_History/RotorPC/LastKnownOnTime")])
        print ("HEREEEEE")
        print (self.data_to_verify_4)
        #print (data_to_verify)
        tfs.write(output_path_combined, self.data_to_verify_4) 
        file = open(str(output_path_combined), "r")
        with file:
            text = file.read()
            self.textEdit_files.setText(text)
        #self.df_scans = python_analysis_dataframe_20200416.selecting_entries(self.logfile,self.logfile_type) 


    def set_analysis_output_file(self,values):
        self.question =  QMessageBox()
        self.question.setText("Select an output folder")
        self.question.setGeometry(QtCore.QRect(200, 300, 100, 50)) 
        self.question.setStandardButtons(QMessageBox.Save)


    def set_output_path(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.fileanalysis_outputpath, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)

    def handleSelectionChanged_scan(self, selected, deselected):
        self.tablestatistic_tab2.setItem(0,0, QTableWidgetItem(str())) 
        self.tablestatistic_tab2.setItem(1,0, QTableWidgetItem(str())) 
        self.tablestatistic_tab2.setItem(2,0, QTableWidgetItem(str())) 
        self.tablestatistic_tab2.setItem(3,0, QTableWidgetItem(str())) 
        self.indexs=(self.tablefiles_tab2.selectionModel().currentIndex())
        self.index_scan = self.indexs.row()
        self.day_selected = self.indexs.sibling(self.index_scan,0).data()
        self.hour_selected = self.indexs.sibling(self.index_scan,1).data()
        self.scan_selected = self.indexs.sibling(self.index_scan,2).data()
        date_format = "%Y-%m-%d"
        date_stamp = datetime.datetime.strptime(self.day_selected,date_format).date()
        #selection of the scan in the dataframen
        df_day = (self.data_df_all_subsystems[self.data_df_all_subsystems["DAY_ROTOR"] == date_stamp])
        hour_index = (df_day[df_day["HOUR_ROTOR"] == self.hour_selected].index)
        df_day_scan = (df_day[df_day["SCAN_ROTOR"] == self.scan_selected])
        self.df_day_scan_hour = (df_day_scan[df_day_scan["HOUR_ROTOR"] == self.hour_selected])
        print ("ALL SCANS")
        print (self.data_df_all_subsystems)
        print ("SCAN DAY")
        print (df_day)
        print ("SCAN SELECTED")
        print (self.df_day_scan_hour)
        index_hour_rotor = ((df_day_scan.HOUR_ROTOR[df_day_scan["HOUR_ROTOR"] == self.hour_selected]).dropna())
        #index_hour_pendant = np.array((self.data_df_all_subsystems["HOUR_PENDANT"].iloc[hour_index]).dropna())
        #index_hour_system = np.array((self.data_df_all_subsystems["HOUR_SYSTEM"].iloc[hour_index]).dropna())
        #index_hour_gimbal = np.array((self.data_df_all_subsystems["HOUR_GIMBAL"].iloc[hour_index]).dropna())
        print ("before")
        print (self.hour_selected[0:3])
        print (getattr(self.data_df_all_subsystems,"HOUR_PENDANT").dropna())
        #print ((getattr(self.data_df_all_subsystems,"HOUR_PENDANT").dropna()).str.contains(self.hour_selected[0:2]))
        #print (self.data_df_all_subsystems.HOUR_ROTOR[(getattr(self.data_df_all_subsystems,"DAY_ROTOR") == date_stamp) & getattr(self.data_df_all_subsystems,"HOUR_ROTOR").str.contains(self.hour_selected[0:2]) & getattr(self.data_df_all_subsystems,"SCAN_ROTOR").str.contains(self.scan_selected)].index)
        if len(getattr(self.data_df_all_subsystems,"HOUR_ROTOR").dropna()) != 0:
           index_hour_rotor_all = (self.data_df_all_subsystems.HOUR_ROTOR[(getattr(self.data_df_all_subsystems,"DAY_ROTOR") == date_stamp) & getattr(self.data_df_all_subsystems,"HOUR_ROTOR").str.contains(self.hour_selected[0:4]) & getattr(self.data_df_all_subsystems,"SCAN_ROTOR").str.contains(self.scan_selected)].index)
        else:
           index_hour_rotor_all = []
        if len(getattr(self.data_df_all_subsystems,"HOUR_PENDANT").dropna()) != 0:
           index_hour_pendant = (self.data_df_all_subsystems.HOUR_PENDANT[(getattr(self.data_df_all_subsystems,"DAY_PENDANT") == date_stamp) & getattr(self.data_df_all_subsystems,"HOUR_PENDANT").str.contains(self.hour_selected[0:4]) & getattr(self.data_df_all_subsystems,"SCAN_PENDANT").str.contains(self.scan_selected)].index)
        else: 
            index_hour_pendant = []          
        if len(getattr(self.data_df_all_subsystems,"HOUR_SYSTEM").dropna()) != 0:
            index_hour_system = (self.data_df_all_subsystems.HOUR_SYSTEM[(getattr(self.data_df_all_subsystems,"DAY_SYSTEM") == date_stamp) & getattr(self.data_df_all_subsystems,"HOUR_SYSTEM").str.contains(self.hour_selected[0:4]) & getattr(self.data_df_all_subsystems,"SCAN_SYSTEM").str.contains(self.scan_selected)].index)
        else:
            index_hour_system = []
        if len(getattr(self.data_df_all_subsystems,"HOUR_GIMBAL").dropna()) != 0:
            index_hour_gimbal = (self.data_df_all_subsystems.HOUR_GIMBAL[(getattr(self.data_df_all_subsystems,"DAY_GIMBAL") == date_stamp) & getattr(self.data_df_all_subsystems,"HOUR_GIMBAL").str.contains(self.hour_selected[0:4]) & getattr(self.data_df_all_subsystems,"SCAN_GIMBAL").str.contains(self.scan_selected)].index)
        else:
            index_hour_gimbal  = []        #
        print ("HEREEE")
        #
        print ("INDEX HEREE")
        print (index_hour_rotor_all)
        print (index_hour_pendant)
        print (index_hour_system)
        print (index_hour_gimbal)
        len_index_hour_rotor =   len(index_hour_rotor_all)
        len_index_hour_pendant = len(index_hour_pendant)
        len_index_hour_system =  len(index_hour_system)
        len_index_hour_gimbal =  len(index_hour_gimbal)
        # DEFINTION: IF FOR A GIVEN DAY THERE IS NOT SCANS, THEN DO NOT CONSIDER THAT FILE.
        self.names_components = ["ROTOR","PENDANT","SYSTEM","GIMBAL"]
        self.columns_names_components = ["FILE_NAME_ROTOR","FILE_NAME_PENDANT","FILE_NAME_SYSTEM","FILE_NAME_GIMBAL"]
        self.index_hour = [index_hour_rotor,index_hour_pendant,index_hour_system,index_hour_gimbal] 
        self.len_index_hour = [len_index_hour_rotor,len_index_hour_pendant,len_index_hour_system,len_index_hour_gimbal] 
        print ("HERE CHECKING")
        print (self.len_index_hour)
        print (max(self.len_index_hour))
        zero_index = [m for m, e in enumerate(self.len_index_hour) if e == 0]
        not_completed = [m for m, e in enumerate(self.len_index_hour) if e != max(self.len_index_hour)]
        self.open_files = ["RotorControlApp.log","PendantUIApp.log","SystemManagerApp.log","GimbalControlApp.log"]
        print ("HEREEEE")
        print (index_hour_rotor)
        print (index_hour_pendant)
        print (index_hour_system)
        print (index_hour_gimbal)
        print (zero_index)
        print (not_completed)
        print ((df_day_scan.HOUR_ROTOR[df_day_scan["HOUR_ROTOR"] == self.hour_selected]))
        #print ((df_day_scan.HOUR_ROTOR[df_day_scan["HOUR_ROTOR"] == self.hour_selected]) - len(not_completed[0]))
        #Removing elements
        for l in range(len(zero_index)): 
            self.index_hour.pop(zero_index[l]-l)
            self.names_components.pop(zero_index[l]-l)
            self.columns_names_components.pop(zero_index[l]-l)
            self.open_files.pop(zero_index[l]-l)
        print ("trying a new thing")
        print (self.index_hour)
        print (self.names_components)
        print (self.columns_names_components)
        print (self.open_files)
        for ind_logfile in self.open_files: 
           self.tablestatistic_tab2.setItem(self.current_row_logfiles,0, QTableWidgetItem(str(ind_logfile))) 
           self.current_row_logfiles += 1
        self.current_row_logfiles = 0
        #self.tablestatistic_tab2.setItem(self.current_row_logfiles,0, QTableWidgetItem(str(hours.iloc[i])))
        #self.tablestatistic_tab2.setItem(self.current_row_logfiles,0, QTableWidgetItem(str(hours.iloc[i])))
        #self.fileName=index.sibling(index.row(),index.column()).data()
        #print(self.fileName)

    def folder_analyze(self,values):
        print (self.lis_files_names)
        self.question =  QMessageBox()
        self.question.setText("Select an output folder")
        self.question.setGeometry(QtCore.QRect(200, 300, 100, 50)) 
        self.question.setStandardButtons(QMessageBox.Save)
        self.question.buttonClicked.connect(self.file_output)
        self.question.show()

    def fileQuit(self):
        self.close()

    def closeEvent(self, ce):
        self.fileQuit()

    def createTable(self):
       # Create table
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(2)

    def color_picker(self):
        color = QColorDialog.getColor()
        self.styleChoice.setStyleSheet('QWidget{background-color: %s}' % color.name())

    def font_choice(self):
        font, valid = QFontDialog.getFont()
        if valid:
            self.styleChoice.setFont(font)

    def home(self, main_layout):

        self.tabs = QtWidgets.QTabWidget()
        self.tab2 = QtWidgets.QWidget()
        self.tab1 = QtWidgets.QWidget()
        self.tab3 = QtWidgets.QWidget()
        self.tab4 = QtWidgets.QWidget()
        self.tabs.resize(300,200)

        # Add tabs
        #self.tabs.addTab(self.tab1,"Individual Files")
        self.tabs.addTab(self.tab2,"Overview")
        self.tabs.addTab(self.tab1,"Rotor")
        self.tabs.addTab(self.tab3,"SystemManager/Pendant")
        #self.tabs.addTab(self.tab4,"Pendant")

        # tab 2: for trend analysis
        self.tab2.main_layout = QtWidgets.QVBoxLayout(self)
        self.tab2.setLayout(self.tab2.main_layout)

        # TAB 2

        self.widget_tab2 = QtWidgets.QWidget(self.tab2)
        self.widget_tab2.setGeometry(QtCore.QRect(20, 20, 280, 230))
        self.widget_tab2.setObjectName("widget")

        #self.textEdit = QtWidgets.QTextEdit()
        #self.toolbar_tab2.setGeometry(QtCore.QRect(250, 10, 1200, 800))

        self.textEdit_files = QtWidgets.QTextEdit(self.tab2)
        self.textEdit_files.setGeometry(QtCore.QRect(340, 10, 450, 600))

        self.textEdit_files_2 = QtWidgets.QTextEdit(self.tab2)
        self.textEdit_files_2.setGeometry(QtCore.QRect(800, 10, 450, 600))

        # TAB 3

        self.plot_central = Canvas_tab2(width=8, height=20, dpi=100, parent=self.tab1) 
        self.plot_central.setGeometry(QtCore.QRect(10, 10, 500, 500))

        self.textEdit_files_selection_rotor = QtWidgets.QTextEdit(self.tab1)
        self.textEdit_files_selection_rotor.setGeometry(QtCore.QRect(520, 10, 350, 430))

        self.textEdit_files_selection_2_rotor = QtWidgets.QTextEdit(self.tab1)
        self.textEdit_files_selection_2_rotor.setGeometry(QtCore.QRect(880, 10, 350, 430))

        self.pushButton_analyze_rotor = QtWidgets.QPushButton('Summarize Rotor', self.tab1)
        self.pushButton_analyze_rotor.setGeometry(QtCore.QRect(20, 490, 221, 30))

        self.pushButton_analyze_rotor.clicked.connect(self.filter_output_scan)


        # TAB 4

        self.label_best_pendant = QLabel("Best Search Pendant:",self.tab3)
        self.label_best_pendant.setGeometry(QtCore.QRect(10, 5, 200, 30))

        self.textEdit_files_selection_system = QtWidgets.QTextEdit(self.tab3)
        self.textEdit_files_selection_system.setGeometry(QtCore.QRect(10, 50, 400, 430))

        self.label_best_pendant = QLabel("Best Search System:",self.tab3)
        self.label_best_pendant.setGeometry(QtCore.QRect(450, 5, 200, 30))

        self.textEdit_files_selection_system = QtWidgets.QTextEdit(self.tab3)
        self.textEdit_files_selection_system.setGeometry(QtCore.QRect(450, 50, 400, 430))

        self.label_best_pendant = QLabel("Summary Scan Pendant:",self.tab3)
        self.label_best_pendant.setGeometry(QtCore.QRect(880, 5, 200, 30))

        self.textEdit_files_selection_2_system = QtWidgets.QTextEdit(self.tab3)
        self.textEdit_files_selection_2_system.setGeometry(QtCore.QRect(880, 50, 400, 430))

        self.pushButton_analyze = QtWidgets.QPushButton('Analyze', self.tab3)
        self.pushButton_analyze.setGeometry(QtCore.QRect(20, 490, 221, 30))


        #self.textbox_file = QtWidgets.QLineEdit(self.tab2)
        #self.textbox_file.setGeometry(QtCore.QRect(940, 10, 100, 30))
        #self.textbox_time = QtWidgets.QLineEdit(self.tab2)
        #self.textbox_time.setGeometry(QtCore.QRect(940, 50, 100, 30))
        #self.textbox_action = QtWidgets.QLineEdit(self.tab2)
        #self.textbox_action.setGeometry(QtCore.QRect(940, 90, 100, 30))
        #self.textbox_type = QtWidgets.QLineEdit(self.tab2)
        #self.textbox_type.setGeometry(QtCore.QRect(940, 130, 100, 30))

        #self.button_file = QPushButton('Filter by File', self.tab2)
        #self.button_file.setGeometry(QtCore.QRect(1050, 10, 200, 30))
        #self.button_time = QPushButton('Filter by Time', self.tab2)
        #self.button_time.setGeometry(QtCore.QRect(1050, 50, 200, 30))
        #self.button_action = QPushButton('Filter by Action', self.tab2)
        #self.button_action.setGeometry(QtCore.QRect(1050, 90, 200, 30))
        #self.button_type = QPushButton('Filter by Type', self.tab2)
        #self.button_type.setGeometry(QtCore.QRect(1050, 130, 200, 30))
        #self.button_all = QPushButton('Filter by All', self.tab2)
        #self.button_all.setGeometry(QtCore.QRect(1050, 170, 200, 30))
        # connect button to function on_click
        #self.button_file.clicked.connect(self.on_click)
        #self.show()
        #self.button_time.clicked.connect(self.on_click)
        #self.show()
        #self.button_action.clicked.connect(self.on_click)
        #self.show()
        #self.button_type.clicked.connect(self.on_click)
        #self.button_all.clicked.connect(self.on_click)
        self.show()

    

       #QMessageBox.question(self, 'Message - pythonspot.com', "You typed: " + textboxValue, QMessageBox.Ok, QMessageBox.Ok)
              #self.textbox.setText("")
        
        
        self.tablefiles_tab2 = QtWidgets.QTableWidget(self.tab2)
        self.tablefiles_tab2.setGeometry(QtCore.QRect(20, 10, 310, 350))
        self.tablefiles_tab2.setObjectName("tableWidget")
        self.tablefiles_tab2.setRowCount(100)
        self.tablefiles_tab2.setColumnCount(3)
        self.tablefiles_tab2.setHorizontalHeaderLabels(["Day","Hour","Scan"])

        self.tablestatistic_tab2 = QtWidgets.QTableWidget(self.tab2)
        self.tablestatistic_tab2.setGeometry(QtCore.QRect(20, 370, 221, 100))
        self.tablestatistic_tab2.setRowCount(5)
        self.tablestatistic_tab2.setColumnCount(1)
        self.tablestatistic_tab2.setHorizontalHeaderLabels(["Log Files"]) 
        self.tablestatistic_tab2.setObjectName("tableView")

        self.pushButton_analyze = QtWidgets.QPushButton('Analyze', self.tab2)
        self.pushButton_analyze.setGeometry(QtCore.QRect(20, 490, 221, 30))
        #
        self.pushButton_analyze_second = QtWidgets.QPushButton('Analyze on second screen', self.tab2)
        self.pushButton_analyze_second.setGeometry(QtCore.QRect(20, 530, 221, 30))
        #
        self.pushButton_analyze.clicked.connect(self.analyze_selected_files)
        self.pushButton_analyze_second.clicked.connect(self.analyze_selected_files_second)
        #
        self.pushButton_analyze = QtWidgets.QPushButton('Analyze all', self.tab2)
        self.pushButton_analyze.setGeometry(QtCore.QRect(20, 570, 221, 30))
        self.pushButton_analyze.clicked.connect(self.analyze_all_selected_files)

        self.selection_scan_tpye = self.tablefiles_tab2.selectionModel()
        self.selection_scan_tpye.selectionChanged.connect(self.handleSelectionChanged_scan)
        self.selection_logfile = self.tablestatistic_tab2.selectionModel()
        self.selection_logfile.selectionChanged.connect(self.handleSelectionChanged_component)
        self.show()
        # Add tabs to widget
        main_layout.addWidget(self.tabs)
        #self.setLayout(self.layout)


    def Clear(self):
        self.ui.widget.canvas.ax.clear()
        self.ui.widget.canvas.draw()
        self.axes_1.clear()
        self.ui.widget_2.canvas.draw()
        self.ui.widget_3.canvas.ax.clear()
        self.ui.widget_3.canvas.draw()
        self.ui.widget_4.canvas.ax.clear()
        self.ui.widget_4.canvas.draw()

    def on_click(self):
        self.textboxValue_file = self.textbox_file.text()
        self.textboxValue_time = self.textbox_time.text()
        self.textboxValue_action = self.textbox_action.text()
        self.textboxValue_type = self.textbox_type.text()
        print ("HEREEEEEEE")
        print (self.textboxValue_file)
        print (self.textboxValue_time)
        print (self.textboxValue_action)
        print (self.data_to_verify_4)
        self.data_to_verify_a = (self.data_to_verify_4[self.data_to_verify_4["ACTION"].str.contains(self.textboxValue_action)])
        print (self.data_to_verify_a)
        self.data_to_verify_a = (self.data_to_verify_a[self.data_to_verify_a["FILE_TYPE"].str.contains(self.textboxValue_file)])
        print (self.data_to_verify_a)
        self.data_to_verify_a = (self.data_to_verify_a[self.data_to_verify_a["TIME_STAMP"].str.contains(self.textboxValue_time)])
        print (self.data_to_verify_a)
        self.data_to_verify_a = (self.data_to_verify_a[self.data_to_verify_a["TYPE"].str.contains(self.textboxValue_type)])    
        tfs.write("test", self.data_to_verify_a) 
        file = open(str("test"), "r")
        #self.textEdit_files.setPlainText() 
        with file:
            text = file.read()
            self.textEdit_files.setPlainText(text)
            self.show()
        #self.textEdit_files.setText(self.data_to_verify_a)              



class Canvas(FigureCanvas):
    def __init__(self, width = 5, height = 5, dpi = 100, parent = None):
        self.fig, self.axes = plt.subplots(3, sharex=True)
        self.fig.tight_layout(pad=3.0)
        plt.gcf().autofmt_xdate()
        self.axes[0].tick_params(labelsize=10)
        self.axes[1].tick_params(labelsize=10)
        self.axes[2].tick_params(labelsize=10)
        plt.xticks(rotation=90)
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)

class Canvas_tab2(FigureCanvas):
    def __init__(self, width = 5, height = 5, dpi = 100, parent = None):
        self.fig, self.axes = plt.subplots(1, sharex=True,figsize=(width,height))
        self.fig.tight_layout(pad=3.0)
        plt.gcf().autofmt_xdate()
        self.axes.tick_params(labelsize=10)
        plt.xticks(rotation=90)
        #self.axes[1].tick_params(labelsize=10)
        #self.axes[2].tick_params(labelsize=10)
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)



if __name__ == "__main__":  # had to add this otherwise app crashed

    def run():
        app = QApplication(sys.argv)
        Gui = window()
        sys.exit(app.exec_())

run()
