import sys
from tokenize import tabsize
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
import os
import webbrowser


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(
            QUrl('https://search.brave.com/?msclkid=02c63c69b99411ec94fc7c8fe3036486'))
        self.setCentralWidget(self.browser)
        self.showMaximized()
        #----------------------------------------------------#
        self.tabs = QTabWidget()
        self.tabs.addTab(self.browser, 'principal')
        self.setCentralWidget(self.tabs)
        # poder mover los tabs
        self.tabs.setMovable(True)
        #----------------------------------------------------#

        # hacer un menu
        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu('&File')  # submenu
        self.home_action = QAction('Home', self)
        self.home_action.setShortcut('Ctrl+H')
        self.home_action.triggered.connect(self.navigate_home)
        self.file_menu.addAction(self.home_action)
        #----------------------------------------------------#
        # reiniciar el navegador
        self.reload_action = QAction('&Reload', self)
        self.reload_action.setShortcut('Ctrl+R')
        self.reload_action.triggered.connect(self.browser.reload)
        self.file_menu.addAction(self.reload_action)
        #----------------------------------------------------#
        # cerrar el navegador
        self.quit_action = QAction('&Quit', self)
        self.quit_action.setShortcut('Ctrl+Q')
        self.quit_action.triggered.connect(self.close)
        self.file_menu.addAction(self.quit_action)
        #----------------------------------------------------#
        # agregar una pestaña
        self.add_tab_action = QAction('&Add Tab', self)
        self.add_tab_action.setShortcut('Ctrl+T')
        self.add_tab_action.triggered.connect(self.add_tab)
        self.file_menu.addAction(self.add_tab_action)
        #----------------------------------------------------#
        # boton para cerrar la pestaña
        self.close_tab_action = QAction('&Close Tab', self)
        self.close_tab_action.setShortcut('Ctrl+W')
        self.close_tab_action.triggered.connect(self.close_tab)
        self.file_menu.addAction(self.close_tab_action)
        #----------------------------------------------------#

        # agregar otra ventana
        self.view_menu = self.menu.addMenu('&View')

        # crear una nueva ventana
        self.new_window_action = QAction('New Window', self)
        self.new_window_action.triggered.connect(self.new_window)
        self.view_menu.addAction(self.new_window_action)
        #----------------------------------------------------#

        # agregar una pagina a favorito
        self.favorites_menu = self.menu.addMenu('&Favorites')
        self.favorites_menu.addAction(
            'Google', lambda: self.browser.setUrl(QUrl('http://google.com')))
        self.favorites_menu.addAction(
            'Yahoo', lambda: self.browser.setUrl(QUrl('http://yahoo.com')))
        self.favorites_menu.addAction(
            'Bing', lambda: self.browser.setUrl(QUrl('http://bing.com')))
        #----------------------------------------------------#

        # boton para agregar favorito
        self.add_favorite_action = QAction('Add Favorite', self)
        self.add_favorite_action.triggered.connect(self.add_favorite)
        self.view_menu.addAction(self.add_favorite_action)
        #----------------------------------------------------#

        # eliminar favorites_menu
        self.view_menu.addSeparator()
        #----------------------------------------------------#
        # delete to favorites
        self.delete_favorites_action = QAction('Delete Favorites', self)
        self.delete_favorites_action.triggered.connect(
            self.favorites_menu.clear)
        self.view_menu.addAction(self.delete_favorites_action)
        #----------------------------------------------------#

    

        

        
        

        #----------------------------------------------------#
        
        




        # navbar
        navbar = QToolBar()
        self.addToolBar(navbar)
        navbar.setIconSize(QSize(16, 16))

        back_btn = QAction('Back', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn = QAction('Forward', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction('Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(QUrl('http://google.com'))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())

    def add_tab(self):
        self.tabs.addTab(QWebEngineView(), 'Tab {}'.format(self.tabs.count()))
        # ponerle una url
        self.tabs.setCurrentIndex(self.tabs.count()-1)
        self.tabs.currentWidget().setUrl(QUrl('http://google.com'))

    def close_tab(self):
        if self.tabs.count() > 1:
            self.tabs.removeTab(self.tabs.currentIndex())
        else:
            self.close()

    def new_window(self):
        self.w = MainWindow()
        self.w.show()

    def add_favorite(self):
        url, ok = QInputDialog.getText(self, 'Add Favorite', 'URL:')
        if ok:
            self.favorites_menu.addAction(
                url, lambda: self.browser.setUrl(QUrl(url)))

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
    
    
    

    
    
    


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
    


# funcion de el bloqueador de anuncios


app = QApplication(sys.argv)
QApplication.setApplicationName('My Cool Browser')
window = MainWindow()
app.exec_()
