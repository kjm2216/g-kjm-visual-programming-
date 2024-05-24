import sys 
from PySide6.QtWidgets import(
    QApplication,
    QDialog,
    QDialogButtonBox,
    QLabel,
    QVBoxLayout,
    QMainWindow,
    QWidget,
    QMessageBox,
    QButtonGroup,
    QRadioButton
)

class CustomDlg(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        
        self.setWindowTitle('Hello,QDialog')
        
        buttons = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.button_box = QDialogButtonBox(buttons)
        
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)
        
        message = QLabel("Is something ok?")
        
        self.layout = QVBoxLayout()
        
        self.layout.addWidget(message)
        self.layout.addWidget(self.button_box)
        self.setLayout(self.layout)
        
        
class MW(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QDialog QRadioButton")
        
        l_str = ['Simple QDialog',
                 'Custom Dialog',
                 'QMessageBox.information',
                 'QMessageBox.warning',
                 'QMessageBox.critical',
                 'QMessageBox.about',
                 'QMessageBox.question']
        
        layout = QVBoxLayout()
        self.radio_buttons = []
        
        self.group = QButtonGroup()
        self.group.setExclusive(True)
        
        for idx, i in enumerate(l_str):
            radio_button = QRadioButton(i)
            radio_button.clicked.connect(self.handleRadioButtonClicked)
            self.radio_buttons.append(radio_button)
            self.group.addButton(radio_button)
            layout.addWidget(radio_button)
            
        self.selected_label = QLabel("No selection")
        layout.addWidget(self.selected_label)
        
        a = QWidget()
        a.setLayout(layout)
        self.setCentralWidget(a)
        
    def handleRadioButtonClicked(self):
        sender = self.sender()
        selected_text = sender.text()
        
        self.selected_label.setText(f"Selected: {selected_text}")
        
        if selected_text == 'Simple QDialog':
            dlg = QDialog(self)
            dlg.setWindowTitle("QDialog Title")
            dlg.exec()
            
        elif selected_text == 'Custom Dialog':
            dlg = CustomDlg(self)
            if dlg.exec():
                print('ok')
            else:
                print('cancel')
                
        elif selected_text == 'QMessageBox.information':
            QMessageBox.information(
                self,
                'Message',
                'This is an information message'
            )
        
        elif selected_text == 'QMessageBox.warning':
            QMessageBox.warning(
                self,
                'Message',
                'This is an warning message'
            )
        
        elif selected_text == 'QMessageBox.critical':
            QMessageBox.critical(
                self,
                'Message',
                'This is an critical message'
            )
        
        elif selected_text == 'QMessageBox.about':
            QMessageBox.about(
                self,
                "About This SW",
                """<p>The example of QMessageBox</p> <p>version 0.1</p>"""
            )
            
            
        elif selected_text == "QMessageBox.question":
            ans = QMessageBox.question(
                self,
                'title of question',
                'content of question',
                QMessageBox.StandardButton.No | QMessageBox.StandardButton.Yes,
                QMessageBox.StandardButton.Yes,
            )
            print(f'{ans=},{QMessageBox.StandardButton.Yes=}')
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MW()
    window.show()
    sys.exit(app.exec())
            
            