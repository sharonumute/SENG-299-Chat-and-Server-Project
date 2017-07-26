from MessageUpdater import MessageUpdater
from ClientStateInfo import ClientStateInfo
from ServerWrapper import ServerWrapper
from Credentials import Credentials
from Chat import Chat
import time

username = 'messageUpdaterTest'
password = 'password'
chatroom = 'messageUpChat'
ownerName = 'UpChatOwner'

serverWrapper = ServerWrapper()
userID = serverWrapper.signup(username,password)
ownerID = serverWrapper.signup(ownerName,password)
serverWrapper.create(ownerID,password,chatroom)
clientStateInfo = ClientStateInfo(Credentials(userID,password),'messageUpChat')

messageUpdater = MessageUpdater(serverWrapper,clientStateInfo,Chat)

messageUpdater.run()

for i in xrange(20):
    serverWrapper.send(ownerID,password,chatroom, 'message' + str(i))

serverWrapper.delete(ownerID,password, chatroom)

time.sleep(5)

serverWrapper.create(ownerID,password,chatroom)
clientStateInfo.chatroom = chatroom
time.sleep(5)

serverWrapper.block(ownerID,password,username, chatroom)
time.sleep(5)

messageUpdater.quit()
