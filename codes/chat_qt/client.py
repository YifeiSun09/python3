#coding:utf8
from PyQt5.QtWidgets import QApplication,QWidget,QDesktopWidget,QMessageBox,QTextEdit,QLineEdit,QPushButton
import sys
from PyQt5.QtCore import QEvent,Qt
from PyQt5.QtGui import QFont,QTextCursor
import threading
import socket
import json

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.msg = ''
        self.who = input('请输入你的名称: ')
        sock = self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        try:
            sock.connect(('127.0.0.1',10086))
        except:
            print('服务器连接失败')
            sys.exit(0)
        sock.send(self.make(who=self.who,action='login')) # 发送登录消息
        threading.Thread(target = self.readMsg,args = ()).start()
        self.initUI()

    def readMsg(self):
        try:
            while True:
                data = self.sock.recv(1024)
                if data:
                    datas = self.parse(data)    # 解码
                    if datas['action'] == 'login':
                        self.panel.append(self.say('系统',datas['who']+'上线了!'))
                        self.panel.moveCursor(QTextCursor.End)
                    elif datas['action'] == 'send_msg':
                        self.panel.append(self.say(datas['who'],datas['msg']))
                        self.panel.moveCursor(QTextCursor.End)
        except:
            sys.exit(0)

    def center(self):
        frame = self.frameGeometry() # 当前窗口的帧
        win_center = QDesktopWidget().availableGeometry().center() # 屏幕中心
        frame.moveCenter(win_center)
        self.move(frame.topLeft())

    def say(self,who,msg):
        role = 'me' if who == self.who else 'other' # 当前用户
        color = 'red' if who == self.who else 'green' # 颜色
        return '<div style="line-height:14px;font-size:14px;"><b style="float:right;color:'+color+';display:inline-block;font-size:16px;line-height:14px;padding:0;">%s: </b><p style="padding:0;line-height:14px;">%s</p></div>' % (who,msg)

    # 创建消息协议
    def make(self,**kw):
        return json.dumps(kw).encode('utf8')

    # 解析消息协议
    def parse(self,data):
        data = data.decode('utf8').strip()
        return json.loads(data)

    def sendMsg(self):
        msg = self.line_msg.text()  # 当前信息
        if msg == '':
            return
        format_msg = self.say(self.who,msg)
        self.msg += format_msg
        self.line_msg.setText('')
        self.panel.append(format_msg)
        self.panel.moveCursor(QTextCursor.End)
        self.sock.send(self.make(who=self.who,msg=msg,action='send_msg')) # 发送消息

    def eventFilter(self,source,event):
        if event.type() == QEvent.KeyPress:
            if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return: # 回车
                self.sendMsg()
        return super().eventFilter(source,event)

    def initUI(self):
        self.setWindowTitle('%s聊天窗口' % self.who)
        self.resize(600,400)
        self.panel = panel = QTextEdit(self)
        panel.setGeometry(0,0,600,368)
        panel.setStyleSheet('QTextEdit{background:white;padding:0 14px 14px 14px;color:black;}')
        panel.setFocusPolicy(Qt.NoFocus) # 禁止编辑

        self.line_msg = line_msg = QLineEdit(self)
        line_msg.setGeometry(0,368,600,32)
        line_msg.setStyleSheet('QLineEdit{border:none;line-height:32px;font-size:14px;padding:0 14px;background:#fafafa;color:#333;outline:none;}')
        line_msg.installEventFilter(self)
        line_msg.setPlaceholderText('这里输入需要发送的消息')
        line_msg.setFocus()

        self.btn = btn = QPushButton('发送',self)
        btn.setToolTip('点击发送信息')
        btn.setGeometry(526,368,64,32)
        btn.setStyleSheet('QPushButton{color:black;}')
        btn.resize(btn.sizeHint())
        btn.clicked.connect(self.buttonClicked)

        self.show()

    def buttonClicked(self):
        sender = self.sender()
        self.sendMsg()

    def closeEvent(self,event):
        sel = QMessageBox.question(self,'关闭确认窗口','确认需要关闭吗?',QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
        if sel == QMessageBox.Yes:
            self.sock.send(b'exit')
            self.sock.close() # 关闭连接
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    sys.exit(app.exec_())
