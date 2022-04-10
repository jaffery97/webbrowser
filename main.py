import sys

#importing Widgtes
from PyQt5.QtWidgets import *

#importing Engine Widgets
from PyQt5.QtWebEngineWidgets import *

#import webbrowser

#importing graphic interface
#from PyQt5.QtGui import *


#importing QtCore to use Qurl
from PyQt5.QtCore import *


#main window class (to create a window)-sub class of QMainWindow class
class Window(QMainWindow):

    #defining constructor function
    def __init__(self):
        #creating connnection with parent class constructor
        super(Window,self).__init__()

        # setting title
        self.setWindowTitle("EDCHAT DASHBOARD")


        #---------------------adding browser-------------------
        self.browser = QWebEngineView()

        #setting url for browser, you can use any other url also
        self.browser.setUrl(QUrl('http://www.edchat.info/'))

        #webbrowser.open("file:/Volumes/Web/Projects/Test/file/index.html")

        #to display google search engine on our browser
        self.setCentralWidget(self.browser)


        #-------------------full screen mode------------------
        #to display browser in full screen mode, you may comment below line if you don't want to open your browser in full screen mode
        self.showMaximized()

        #----------------------navbar-------------------------
        #creating a navigation bar for the browser
        navbar = QToolBar()
        #adding created navbar
        self.addToolBar(navbar)

        #-----------------prev Button-----------------
        #creating prev button
        prevBtn = QAction('<',self)
        #when triggered set connection
        prevBtn.triggered.connect(self.browser.back)
        self.setStyleSheet("border :1px solid yellow")
        # adding prev button to the navbar
        navbar.addAction(prevBtn)

        #-----------------next Button---------------
        nextBtn = QAction('>',self)
        nextBtn.triggered.connect(self.browser.forward)
        navbar.addAction(nextBtn)

        #-----------refresh Button--------------------
        refreshBtn = QAction('Refresh',self)
        refreshBtn.triggered.connect(self.browser.reload)
        navbar.addAction(refreshBtn)

        #-----------home button----------------------
        homeBtn = QAction('Home',self)
        #btn_enter = Tkinter.Button(all_your_args, fg=your_desired_value)
        #when triggered call home method
        homeBtn.triggered.connect(self.home)
        navbar.addAction(homeBtn)

        #-----------Login button----------------------
        loginBtn = QAction('Login',self)
        #when triggered call login method
        loginBtn.triggered.connect(self.login)
        navbar.addAction(loginBtn)

        #-----------Register button----------------------
        registerBtn = QAction('Register', self)
        #when triggered call register method
        registerBtn.triggered.connect(self.register)
        navbar.addAction(registerBtn)

        #-----------Serach button----------------------
        searchBtn = QAction('Search', self)
        #when triggered call register method
        searchBtn.triggered.connect(self.search)
        navbar.addAction(searchBtn)


        #---------------------search bar---------------------------------
        #to maintain a single line
        self.searchBar = QLineEdit()
        #when someone presses return(enter) call loadUrl method
        self.searchBar.returnPressed.connect(self.loadUrl)
        #adding created seach bar to navbar
        #navbar.addWidget(self.searchBar)

        #if url in the searchBar is changed then call updateUrl method
        self.browser.urlChanged.connect(self.updateUrl)

    #method to navigate back to home page
    def home(self):
        self.browser.setUrl(QUrl('http://www.edchat.info/'))

    #method to navigate to login page
    def login(self):
        self.browser.setUrl(QUrl('https://localprayertime.org/login.php'))

    #method to navigate to register page
    def register(self):
        self.browser.setUrl(QUrl('https://localprayertime.org/register1.php'))

    #method to navigate to search page
    def search(self):
        self.browser.setUrl(QUrl('https://localprayertime.org/search1.php'))

    #method to load the required url
    def loadUrl(self):
        #fetching entered url from searchBar
        url = self.searchBar.text()
        #loading url
        self.browser.setUrl(QUrl(url))

    #method to update the url
    def updateUrl(self, url):
        #changing the content(text) of searchBar
        self.searchBar.setText(url.toString())

MyApp = QApplication(sys.argv)

#setting application name
QApplication.setApplicationName('Local Prayer Dashboard')

#creating window
window = Window()
#executing created app
MyApp.exec_()
