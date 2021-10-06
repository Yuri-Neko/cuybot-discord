import os
from TikTokAPI import TikTokAPI

cookie = {
  "s_v_web_id": os.getenv('SVWID'),
  "tt_webid": os.getenv('TTWID')
}

api = TikTokAPI(cookie=cookie)
user_obj = api.getUserByName("dea.afrizal")
get_follower = str(user_obj['userInfo']['stats']['followerCount'])
get_likes = str(user_obj['userInfo']['stats']['heart'])
get_total_video = str(user_obj['userInfo']['stats']['videoCount'])
get_url = str(user_obj['seoProps']['metaParams']['canonicalHref'])

def info():
  return(':clap: Info Account Bang Dea :clap:\n\n' + 'Follower saat ini: **' + get_follower + '** orang\n' + 'Jumlah Likes: **' + get_likes + '** suka\n' + 'Total video tayang: **' + get_total_video + '** video\n' + 'Link tiktok: `*' + get_url + '*`' + '\n\n:robot: Thanks cuy udah follow bang dea! :robot:')

def last_follower():
  return('Jumlah follower bang dea saat ini: ' + '**' + get_follower + '** orang')

def last_liked():
  return('Jumlah like bang dea saat ini: ' + '**' + get_likes + '** suka')

def total_video():
  return('Total video bang dea saat ini: ' + '**' + get_total_video + '** video')

def url():
  return('Link tiktok bang dea: ' + '`' + get_url + '`')