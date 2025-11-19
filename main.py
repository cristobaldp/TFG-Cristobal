from PySide6.QtWidgets import QApplication
from controllers.app_controller import AppController
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = AppController()
    sys.exit(app.exec())
print ("Ejecutando app...") 
print ("Cambios")