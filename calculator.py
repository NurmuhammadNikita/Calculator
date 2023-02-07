from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
def calculator():
    app=QApplication(sys.argv)
    forma=QWidget()
    forma.setWindowTitle("Calculator")
    forma.resize(500,650)
    forma.move(300,280)
    forma.setFont(QFont("Calibri",20))
    forma.setWindowIcon(QIcon("C:\\Users\\hop\\Downloads\\calc.ico"))
    forma.setStyleSheet("""
    color: rgb(77, 41, 8 );
    background-color: rgb(27, 14, 1 );
    border-width: 3px;
    border-style: solid; 
    """)
   
    doska=QLabel(forma)
    doska.setGeometry(0,0,500,120)
    doska.setFont(QFont("Calibri",40))
    doska.setText("0")
    doska.setAlignment(Qt.AlignRight)
    doska.setStyleSheet("""
    color: rgb(255,255,255);
    background-color: rgb(25, 25, 25 );
    border-color: rgb(0,0,0);
    border-width: 3px;
    border-style: solid; 
    """)

    num1=QPushButton("1",forma)

    num1.setGeometry(20,160,80,80)
    forma.setFont(QFont("Calibri",20))
    num1.setStyleSheet("""
    color: rgb(255,252,250);
    background-color: rgb(234,142,55);
    border-color: rgb(234,142,55);
    border-width: 3px;
    border-radius: 40px;
    border-style: solid; 
    """)

    num4=QPushButton("4",forma)

    num4.setGeometry(20,280,80,80)
    forma.setFont(QFont("Calibri",20))
    num4.setStyleSheet("""
    color: rgb(255,252,250);
    background-color: rgb(234,142,55);
    border-color: rgb(234,142,55);
    border-width: 3px;
    border-radius: 40px;
    border-style: solid; 
    """)

    num7=QPushButton("7",forma)

    num7.setGeometry(20,400,80,80)
    forma.setFont(QFont("Calibri",20))
    num7.setStyleSheet("""
    color: rgb(255,252,250);
    background-color: rgb(234,142,55);
    border-color: rgb(234,142,55);
    border-width: 3px;
    border-radius: 40px;
    border-style: solid; 
    """)

    num2=QPushButton("2",forma)

    num2.setGeometry(140,160,80,80)
    forma.setFont(QFont("Calibri",20))
    num2.setStyleSheet("""
    color: rgb(255,252,250);
    background-color: rgb(234,142,55);
    border-color: rgb(234,142,55);
    border-width: 3px;
    border-radius: 40px;
    border-style: solid; 
    """)

    num5=QPushButton("5",forma)

    num5.setGeometry(140,280,80,80)
    forma.setFont(QFont("Calibri",20))
    num5.setStyleSheet("""
    color: rgb(255,252,250);
    background-color: rgb(234,142,55);
    border-color: rgb(234,142,55);
    border-width: 3px;
    border-radius: 40px;
    border-style: solid; 
    """)

    num8=QPushButton("8",forma)

    num8.setGeometry(140,400,80,80)
    forma.setFont(QFont("Calibri",20))
    num8.setStyleSheet("""
    color: rgb(255,252,250);
    background-color: rgb(234,142,55);
    border-color: rgb(234,142,55);
    border-width: 3px;
    border-radius: 40px;
    border-style: solid; 
    """)


    num3=QPushButton("3",forma)

    num3.setGeometry(260,160,80,80)
    forma.setFont(QFont("Calibri",20))
    num3.setStyleSheet("""
    color: rgb(255,252,250);
    background-color: rgb(234,142,55);
    border-color: rgb(234,142,55);
    border-width: 3px;
    border-radius: 40px;
    border-style: solid; 
    """)

    num6=QPushButton("6",forma)

    num6.setGeometry(260,280,80,80)
    forma.setFont(QFont("Calibri",20))
    num6.setStyleSheet("""
    color: rgb(255,252,250);
    background-color: rgb(234,142,55);
    border-color: rgb(234,142,55);
    border-width: 3px;
    border-radius: 40px;
    border-style: solid; 
    """)

    num9=QPushButton("9",forma)

    num9.setGeometry(260,400,80,80)
    forma.setFont(QFont("Calibri",20))
    num9.setStyleSheet("""
    color: rgb(255,252,250);
    background-color: rgb(234,142,55);
    border-color: rgb(234,142,55);
    border-width: 3px;
    border-radius: 40px;
    border-style: solid; 
    """)
###############################################################################

    action1=QPushButton("<---",forma)

    action1.setGeometry(400,160,80,80)
    forma.setFont(QFont("Calibri",20))
    action1.setStyleSheet("""
    color: rgb(255,252,250);
    background-color: rgb(234,142,55);
    border-color: rgb(234,142,55);
    border-width: 3px;
    border-radius: 40px;
    border-style: solid; 
    """)

    action2=QPushButton("/",forma)

    action2.setGeometry(400,280,80,80)
    forma.setFont(QFont("Calibri",20))
    action2.setStyleSheet("""
    color: rgb(255,252,250);
    background-color: rgb(234,142,55);
    border-color: rgb(234,142,55);
    border-width: 3px;
    border-radius: 40px;
    border-style: solid; 
    """)

    action3=QPushButton("*",forma)

    action3.setGeometry(400,400,80,80)
    forma.setFont(QFont("Calibri",20))
    action3.setStyleSheet("""
    color: rgb(255,252,250);
    background-color: rgb(234,142,55);
    border-color: rgb(234,142,55);
    border-width: 3px;
    border-radius: 40px;
    border-style: solid; 
    """)

    action4=QPushButton("=",forma)
    action4.setGeometry(400,520,80,80)
    forma.setFont(QFont("Calibri",20))
    action4.setStyleSheet("""
    color: rgb(255,252,250);
    background-color: rgb(234,142,55);
    border-color: rgb(234,142,55);
    border-width: 3px;
    border-radius: 40px;
    border-style: solid; 
    """)
    action5=QPushButton("-",forma)

    action5.setGeometry(260,520,80,80)
    forma.setFont(QFont("Calibri",20))
    action5.setStyleSheet("""
    color: rgb(255,252,250);
    background-color: rgb(234,142,55);
    border-color: rgb(234,142,55);
    border-width: 3px;
    border-radius: 40px;
    border-style: solid; 
    """)

    action6=QPushButton("+",forma)

    action6.setGeometry(140,520,80,80)
    forma.setFont(QFont("Calibri",20))
    action6.setStyleSheet("""
    color: rgb(255,252,250);
    background-color: rgb(234,142,55);
    border-color: rgb(234,142,55);
    border-width: 3px;
    border-radius: 40px;
    border-style: solid; 
    """)

    num0=QPushButton("0",forma)

    num0.setGeometry(20,520,80,80)
    num0.setFont(QFont("Calibri",20))
    num0.setStyleSheet("""
    color: rgb(255,252,250);
    background-color: rgb(234,142,55);
    border-color: rgb(234,142,55);
    border-width: 3px;
    border-radius: 40px;
    border-style: solid; 
    """)





    forma.show()
    sys.exit(app.exec_())
calculator()