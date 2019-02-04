import tweepy
import networkx as net
import time
import matplotlib.pyplot as plt
import pylab
from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import operator


#1stAcc
#CONSUMER_KEY = ''
#CONSUMER_SECRET = ''
#ACCESS_KEY = ''
#ACCESS_SECRET = ''

##2ndAcc
#CONSUMER_KEY = ''
#CONSUMER_SECRET = ''
#ACCESS_KEY=''
#ACCESS_SECRET=''

#3rdAcc
#CONSUMER_KEY=''
#CONSUMER_SECRET = ''
#ACCESS_KEY=''
#ACCESS_SECRET=''

#4thAcc
#CONSUMER_KEY=''
#CONSUMER_SECRET = ''
#ACCESS_KEY=''
#ACCESS_SECRET=''

#5thAcc
#CONSUMER_KEY=''
#CONSUMER_SECRET = ''
#ACCESS_KEY=''
#ACCESS_SECRET=''

#6thAcc
#CONSUMER_KEY=''
#CONSUMER_SECRET = ''
#ACCESS_KEY=''
#ACCESS_SECRET=''

#7thAcc
#CONSUMER_KEY=''
#CONSUMER_SECRET = ''
#ACCESS_KEY=''
#ACCESS_SECRET=''

#8thAcc
#CONSUMER_KEY=''
#CONSUMER_SECRET = ''
#ACCESS_KEY=''
#ACCESS_SECRET=''


NumCuentas=8

CONSUMER_KEYS=[] #List with Consumer Keys
CONSUMER_SECRETS=[] #List with Consumer Secrets
ACCESS_KEYS=[] #List with Access keys
ACCESS_SECRETS=[] #List with Access Secrets


auth = tweepy.OAuthHandler(CONSUMER_KEYS[0], CONSUMER_SECRETS[0])
auth.set_access_token(ACCESS_KEYS[0], ACCESS_SECRETS[0])
api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True,compression=True)
 
print("Start")
query = '#python'
max_tweets = 60
searched_tweets = [status for status in tweepy.Cursor(api.search, q=query).items(max_tweets)]
#query = api.search("#python",count=17)

listaUsers=[]
cont=0
for result in searched_tweets:
#    print("Tweet: "+ result.text)
#    print("Creation date: " + str(result.created_at))
#    print("Favs count: " + str(result.favorite_count))
#    print("Language: " + result.lang)
#    print("Retweets count: " + str(result.retweet_count))
#    print("Account: " + result.user.screen_name )
#    print("AccID: " + str(result.id))
#    print("\n")
    listaUsers.append(result.user.screen_name)
    cont=cont+1
    print(cont)
    
    
#Check relation between 2 persons
#is_following = api.show_friendship(source_screen_name="1stPersonNick",target_screen_name="2ndPersonNick")
#print(is_following[0].followed_by)


#Resul=6 in case of 30 acc, resul=3 for 60 accs, the maximun of calls without sleep is 180... 180/30 = 6, 180/60 = 3
#For sum up, it would be 180/Number of twitter accounts (or max tweets) = resul
#IMPORTANT, CHANGE resul TO RESULT OF THE PREVIOUS OPERATION: 180/max tweets=resul
resul=3

cont=resul
parameter=0
cuenta=0

print("Cycles of " +str(cont)+ "  times")

Seguidores={}                                                              
for x in listaUsers:                                       
    dicValues=[]
    cuenta=cuenta+1
    print("Acc number "+str(cuenta))                                                                                           
    for y in listaUsers:
        if x==y:                                                          
            pass
        else:
            if cont==resul:
                cont=0
                parameter=(parameter+1)%NumCuentas          
            auth = tweepy.OAuthHandler(CONSUMER_KEYS[parameter], CONSUMER_SECRETS[parameter])
            auth.set_access_token(ACCESS_KEYS[parameter], ACCESS_SECRETS[parameter])
            api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True,compression=True)
            time.sleep(0.2)
            is_following = api.show_friendship(source_screen_name=x,target_screen_name=y)       #Arreglar con el try catch
            if is_following[0].followed_by == True:
                if y in dicValues:
                    pass
                else:
                    dicValues.append(y)
    if x in Seguidores.keys():
        pass
    else:
        Seguidores[x]=dicValues    
    cont=cont+1
print(Seguidores)
G=net.DiGraph()
edges=[]
for x in Seguidores.keys():
    G.add_node(x)
    if len(Seguidores[x])==0:
        pass
    else:
        for y in Seguidores[x]:
            edges.append([y,x])
G.add_edges_from(edges)
posit=net.spring_layout(G)
plt.figure(figsize=(30,30),dpi=10)
net.draw_networkx_labels(G,posit,font_size=11)
net.draw_networkx_edges(G,posit,edgelist=edges,arrows=True,width=0.5)
net.draw_networkx_nodes(G,posit,node_size=20)
plt.savefig("graph.pdf")
plt.savefig("graph.png")
plt.close()

centralidad=net.degree_centrality(G)
centralidad_ordenada= sorted(centralidad.items(),key=operator.itemgetter(1),reverse=True)
print(centralidad_ordenada)





#PDF   

packet = io.BytesIO()
# create a new PDF with Reportlab
can = canvas.Canvas(packet, pagesize=letter)
contpag=680
ancho=50
can.drawString(280, 710,"Centrality")
can.setFontSize(5)
for x in centralidad_ordenada:    
    can.drawString(ancho, contpag, str(x))
    contpag-=10
    if contpag==50:
        contpag=760
        ancho=500
can.save()

packet.seek(0)
new_pdf = PdfFileReader(packet)
existing_pdf = PdfFileReader(open("graph.pdf", "rb"))
output = PdfFileWriter()
page2 = existing_pdf.getPage(0)
page = new_pdf.getPage(0)
page.scaleTo(page2.mediaBox[2],page2.mediaBox[3])
output.addPage(page2)
output.addPage(page)
outputStream = open("graphCentrality.pdf", "wb")
output.write(outputStream)
outputStream.close()


auth = tweepy.OAuthHandler(CONSUMER_KEYS[0], CONSUMER_SECRETS[0])
auth.set_access_token(ACCESS_KEYS[0], ACCESS_SECRETS[0])
api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True,compression=True)

imagepath="graph.png"
status="This is the graph generated for the Centrality for the hashtag "+ query +" for" + str(max_tweets) + " tweets."
api.update_with_media(imagepath,status)


