from bson import ObjectId
import DatabaseConfig
def AddChannelLink(Channel_Source, Channel_destination,databaseDest=DatabaseConfig.db.ChannelLink):
  document = {"src":Channel_Source,"dest":Channel_destination}
  return databaseDest.insert_one(document).inserted_id
def DeleteChannelLink_ID(ID,databaseDest=DatabaseConfig.db.ChannelLink):
  DatabaseConfig.db.ChannelLink.delete_one({'_id': ObjectId(str(ID))})
  return f'{str(ID)} Deleted'
def DeleteChannelLink_ChanNum(Channel_Source,Channel_destination):
  tmp_doc = {"src":Channel_Source,"dest":Channel_destination}
  DatabaseConfig.db.ChannelLink.delete_one(tmp_doc)
  return "Deleted Link"
def GetLinkedChannels(client,Channel_Source):
  ret_str = "This Channel Is linked to "
  for doc in DatabaseConfig.db.ChannelLink.find():
    if(doc['src']==int(Channel_Source)):
      ret_str = ret_str + str(client.get_channel(doc['dest']))+ ", "
  return ret_str
def GetLinkedChannelsList(Channel_Source):
  return [
      doc['dest'] for doc in DatabaseConfig.db.ChannelLink.find()
      if (doc['src'] == int(Channel_Source))
  ]
def to_ChannelId(channelName):
  channelName = channelName.replace("<#","")
  channelName = channelName.replace(">","")
  return int(channelName)
#DISCORD.PY
