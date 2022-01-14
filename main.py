# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import math
from math import sqrt, pow, log, exp, sin, cos, tan
import re
import sympy
import numpy as np
from numpy import log as ln
import matplotlib.pyplot as plt

select_method = ""
main_text_box = ""
input_function = ""

f = None
compiled_function = None

def bisection(a, b, e, n):
    iteration = 1
    add_text('\n\n*** BISECTION METHOD IMPLEMENTATION ***')
    condition = True
    Xold = None
    while condition and n != 0:
        x_middle = (a + b) / 2
        add_text(str(('Iteration-%d, x_middle = %0.6f and f(x_middle) = %0.6f' % (iteration, x_middle, f(x_middle)))))
        if (Xold == None):
            add_text(str(('')))
        else:
            #add_text(str((', error =', abs((x_middle - Xold) / x_middle * 100), '%')
           add_text(str("error =%0.6f" %(abs(x_middle - Xold))))

        if f(a) * f(x_middle) < 0: ## if f(a) and f(x_middle) both have same sign then a_new = x_middle, else, b_new = x_middle
            b = x_middle
           
        elif f(b) * f(x_middle) < 0:
            a = x_middle
          
        else :
          break
            
        
        add_text(str(("\tUPDATE : a = %0.6f, b = %0.6f\n" %(a,b))))
        #if (x_middle==0):
         #   break

        iteration += 1
        #condition = abs(f(x_middle)) > e
        if (Xold!=None):
            condition = abs(x_middle-Xold) >e
           
            
        n-=1
        Xold=x_middle
        

    add_text(str(('\nRequired Root is : %0.8f' % x_middle)))


def falseposition(a, b, e, n):
    iteration = 1
    add_text(str(('\n\n*** FALSE POSITION METHOD IMPLEMENTATION ***')))
    condition = True
    point_old = None
    while condition and n != 0:
        if f(a) == f(b):
            add_text(str(('Divide by zero error!')))
            break
        x_middle = a - f(a) * (a - b) / (f(a) - f(b))
        add_text(str(('Iteration-%d, point = %0.6f and f(point) = %0.6f' % (iteration, x_middle, f(x_middle)))))
        if (point_old == None):
            add_text(str(('')))
        else:
            add_text(str(('error =%0.6f'%(abs(x_middle - point_old)))))
            
        if f(a) * f(x_middle) < 0:
            b = x_middle
        elif f(b) * f(x_middle) < 0:
            a = x_middle
        else:
            break
            
        add_text(str(("\tUPDATE : a = %0.6f, b = %0.6f\n" %(a,b))))
        

        iteration = iteration + 1
        if(point_old != None):
            condition = abs(x_middle-point_old) > e
        n -= 1
        point_old = x_middle

    add_text(str(('\nRequired Root is : %0.8f' % x_middle)))

def secant(a, b, e, N):
    add_text(str(('\n\n*** SECANT METHOD IMPLEMENTATION ***')))
    iteration = 1
    condition = True
    Xold = None
    while condition:
        if f(a) == f(b):
            add_text(str(('Divide by zero error!')))
            break
        
        p2 = a - (b - a) * f(a) / (f(b) - f(a))
        add_text(str("USING : P0 = %0.6f, P1=%0.6f" %(a, b)))
        add_text(str(('Iteration-%d, p2 = %0.6f and f(p2) = %0.6f' % (iteration, p2, f(p2)))))
        if (Xold == None):
            add_text('')
        else:
            add_text(str('error = %0.6f' %(abs((p2 - Xold)))))
        a = b
        b = p2
        iteration +=1

        if iteration > N:
            break
        
        add_text(str(())) ##newline
        if(Xold !=None):
            condition = abs(p2-Xold) > e
        Xold = p2
    add_text(str(('\n point: %0.8f' % (p2))))


def newtonRaphson(x0, e, n, func):
    global f_dash
    input_function_sympy = sympy.parse_expr(func, evaluate=False)
    differentiation_function = sympy.diff(input_function_sympy)
    tmp = sympy.Symbol('x')
    f_dash = sympy.lambdify(tmp, differentiation_function)
    add_text(str(('\n\n*** NEWTON RAPHSON METHOD IMPLEMENTATION ***')))
    iteration = 1
    flag = 1
    condition = True
    while condition:
        if f_dash(x0) == 0.0:
            add_text(str(('Divide by zero error!')))
            x1 = x0
            break

        x1 = x0 - f(x0) / f_dash(x0)
        add_text(str(('Iteration-%d, x1 = %0.6f and f(x1) = %0.6f, error = %0.6f %% ' % (iteration, x1, f(x1), abs(x1-x0)))))
        x0 = x1
        iteration = iteration + 1

        if iteration > n:
            flag = 0
            break

        condition = abs(f(x1)) > e

    if flag == 1:
        add_text(str(('\nRequired root is: %0.8f' % x1)))
    else:
        add_text(str(('\nNot Convergent.')))

def newton_begin():
    # Input Section
    x0 = input('Enter Guess: ')
    e = input('Tolerable Error: ')
    n = int(input('Maximum iterations: '))

    # Converting input to float
    x0 = float(x0)
    e = float(e)

    newtonRaphson(x0, e, n)


def Muller(a, b, c, N, e):
    add_text(str(('\n\n MULLER METHOD IMPLEMENTATION')))
    res = 0
    step = 0
    condition = True
    while condition:

        # Calculating various constants
        # required to calculate x3
        f1 = f(a)
        f2 = f(b)
        f3 = f(c)
        d1 = f1 - f3
        d2 = f2 - f3
        h1 = a - c
        h2 = b - c
        a0 = f3
        a1 = (((d2 * pow(h1, 2)) -(d1 * pow(h2, 2))) / ((h1 * h2) * (h1 - h2)))
        a2 = (((d1 * h2) - (d2 * h1)) / ((h1 * h2) * (h1 - h2)))
        x = ((-2 * a0) / (a1 + abs(math.sqrt(a1 * a1 - 4 * a0 * a2))))
        y = ((-2 * a0) / (a1 - abs(math.sqrt(a1 * a1 - 4 * a0 * a2))))

        # Taking the root which is
        # closer to x2
        if (x >= y):
            res = x + c
        else:
            res = y + c

        # checking for resemblance of x3
        # with x2 till two decimal places
        m = res * 100
        n = c * 100
        m = math.floor(m)
        n = math.floor(n)
        add_text(str(('Iteration-%d, x3 = %0.6f and f(x3) = %0.6f' % (step, c, f(c)))))
        if (m == n):
            break
        a = b
        b = c
        c = res

        condition = abs(f(c)) > e

        step += 1
        if (step > N):
            add_text(str(("Root cannot be found using","Muller's method")))
            break

    if (step <= N):
        add_text(str(("The value of the root is", res)))
        

def add_text(text):
    ui.textEdit_2.append(text)
    
def clear_text():
    ui.textEdit_2.clear()
    
class Ui_Dialog(object):
    
    def radioButton_clicked(self):
        global select_method
        ui.lineEdit.setEnabled(True)
        ui.lineEdit_2.setEnabled(True)
        ui.lineEdit_3.setEnabled(True)
        ui.lineEdit_4.setEnabled(True)
        ui.lineEdit_5.setEnabled(True)
        
        if self.radioButton.isChecked():
            select_method = "Bisection"
            ui.lineEdit_3.setEnabled(False)
        elif self.radioButton_2.isChecked():
            select_method = "False Position"
            ui.lineEdit_3.setEnabled(False)
        elif self.radioButton_3.isChecked():
            select_method = "Secant"
            ui.lineEdit_3.setEnabled(False)
        elif self.radioButton_4.isChecked():
            select_method = "Newton"
            ui.lineEdit_3.setEnabled(False)
            ui.lineEdit_2.setEnabled(False)
        elif self.radioButton_5.isChecked():
            select_method = "Muller"
            
                
    def button_clicked(self):
        global f, compiled_function
        clear_text()
        try:
            func = self.textEdit.toPlainText()
            func = re.sub('\s+',' ',func)
            func = func.replace('^', "**")
            input_function = func
            compiled_function = compile(input_function, "<string>", "eval")
            f = lambda x: eval(compiled_function)
            a = float(self.lineEdit.text())
            b = None
            if(select_method != "Newton"):
                b = float(self.lineEdit_2.text())
            e = float(self.lineEdit_4.text())
            m = int(self.lineEdit_5.text())
            if(select_method == "Bisection"):
                    if f(a) * f(b) > 0.0:
                        add_text(str(('Given guess values do not bracket the root.')))
                        add_text(str(('Try Again with different guess values.')))
                    else:
                        add_text(str(("INPUTS : a = %0.6f, b = %0.6f" %(a,b))))
                        bisection(a, b, e, m)
            elif(select_method == "False Position"):
                if f(a) * f(b) > 0.0:
                    add_text(str(('Given guess values do not bracket the root.')))
                    add_text(str(('Try Again with different guess values.')))
                else:
                    add_text(str(("INPUTS : a = %0.6f, b = %0.6f" %(a,b))))
                    falseposition(a,b,e,m)
            elif(select_method == "Secant"):
                add_text(str(("INPUTS : po = %0.6f, p1 = %0.6f" %(a,b))))
                secant(a, b, e, m)
            elif(select_method == "Newton"):
                newtonRaphson(a, e, m, func)
            elif(select_method == "Muller"):
                c = float(self.lineEdit_3.Text())
                Muller(a, b, c, m, e)
            if(ui.checkBox.isChecked()):
                if(b == None):
                    xpts = np.linspace(a-10, a+10, 1000)
                else:
                    xpts = np.linspace(a, b, 1000)
                plt.figure(figsize=(10,5))
                plt.plot(xpts, list(map(f, xpts)))
                plt.xticks(xpts)
                plt.show()
        except ValueError:
            add_text("Wrong Inputs!")
        except ZeroDivisionError:
            add_text("Division By Zero Error!")
        except Exception as e:
            clear_text()
            add_text("Something Wrong! Please Check Inputs")
            add_text(str((e)))

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(634, 456)
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 481, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.textEdit.setFont(font)
        self.textEdit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit.setAcceptRichText(False)
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(500, 10, 121, 41))
        self.pushButton.setObjectName("pushButton")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 60, 161, 141))
        self.pushButton.clicked.connect(self.button_clicked)
        self.groupBox.setObjectName("groupBox")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(10, 20, 82, 17))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(10, 40, 82, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_3.setGeometry(QtCore.QRect(10, 60, 82, 17))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_4.setGeometry(QtCore.QRect(10, 80, 82, 17))
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_5 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_5.setGeometry(QtCore.QRect(10, 100, 82, 17))
        self.radioButton_5.setObjectName("radioButton_5")
        self.textEdit_2 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 210, 611, 241))
        self.radioButton.toggled.connect(self.radioButton_clicked)
        self.radioButton_5.toggled.connect(self.radioButton_clicked)
        self.radioButton_2.toggled.connect(self.radioButton_clicked)
        self.radioButton_3.toggled.connect(self.radioButton_clicked)
        self.radioButton_4.toggled.connect(self.radioButton_clicked)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setObjectName("textEdit_2")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(180, 60, 441, 141))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(10, 20, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(230, 20, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(230, 50, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(10, 80, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit.setGeometry(QtCore.QRect(100, 20, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 50, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(100, 80, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(330, 20, 101, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(330, 50, 101, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox.setGeometry(QtCore.QRect(230, 80, 171, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Solve"))
        self.groupBox.setTitle(_translate("Dialog", "Methods"))
        self.radioButton.setText(_translate("Dialog", "Bisection"))
        self.radioButton_2.setText(_translate("Dialog", "False Position"))
        self.radioButton_3.setText(_translate("Dialog", "Secant"))
        self.radioButton_4.setText(_translate("Dialog", "Newton"))
        self.radioButton_5.setText(_translate("Dialog", "Muller"))
        self.groupBox_2.setTitle(_translate("Dialog", "Inputs"))
        self.label.setText(_translate("Dialog", "First Point"))
        self.label_2.setText(_translate("Dialog", "Second Point"))
        self.label_3.setText(_translate("Dialog", "Tolerable Error"))
        self.label_4.setText(_translate("Dialog", "Max Iterations"))
        self.label_5.setText(_translate("Dialog", "Third Point"))
        self.checkBox.setText(_translate("Dialog", "show function plot"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.setWindowTitle("Find Root")
    Dialog.show()
    sys.exit(app.exec_())


