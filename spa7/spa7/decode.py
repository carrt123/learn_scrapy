import re
import json

data = """
const players = [
  {
    name: '凯文-杜兰特',
    image: 'durant.png',
    birthday: '1988-09-29',
    height: '208cm',
    weight: '108.9KG'
  }, {
    name: '勒布朗-詹姆斯',
    image: 'james.png',
    birthday: '1984-12-30',
    height: '206cm',
    weight: '113.4KG'
  }, {
    name: '斯蒂芬-库里',
    image: 'curry.png',
    birthday: '1988-03-14',
    height: '191cm',
    weight: '83.9KG'
  }, {
    name: '詹姆斯-哈登',
    image: 'harden.png',
    birthday: '1989-08-26',
    height: '196cm',
    weight: '99.8KG'
  }, {
    name: '扬尼斯-安特托昆博',
    image: 'antetokounmpo.png',
    birthday: '1994-12-06',
    height: '211cm',
    weight: '109.8KG'
  }, {
    name: '拉塞尔-威斯布鲁克',
    image: 'westbrook.png',
    birthday: '1988-11-12',
    height: '191cm',
    weight: '90.7KG'
  }, {
    name: '凯里-欧文',
    image: 'irving.png',
    birthday: '1992-03-23',
    height: '188cm',
    weight: '88.5KG'
  }, {
    name: '安东尼-戴维斯',
    image: 'davis.png',
    birthday: '1993-03-11',
    height: '208cm',
    weight: '114.8KG'
  }, {
    name: '乔尔-恩比德',
    image: 'embiid.png',
    birthday: '1994-03-16',
    height: '213cm',
    weight: '127.0KG'
  }, {
    name: '克雷-汤普森',
    image: 'thompson.png',
    birthday: '1990-02-08',
    height: '198cm',
    weight: '97.5KG'
  }, {
    name: '考瓦伊-莱昂纳德',
    image: 'leonard.png',
    birthday: '1991-06-29',
    height: '201cm',
    weight: '102.1KG'
  }, {
    name: '达米安-利拉德',
    image: 'lillard.png',
    birthday: '1990-07-15',
    height: '188cm',
    weight: '88.5KG'
  }, {
    name: '卡梅罗-安东尼',
    image: 'anthony.png',
    birthday: '1984-05-29',
    height: '203cm',
    weight: '108KG'
  }, {
    name: '尼科拉-约基奇',
    image: 'jokic.png',
    birthday: '1995-02-19',
    height: '213cm',
    weight: '128.8KG'
  }, {
    name: '卡尔-安东尼-唐斯',
    image: 'towns.png',
    birthday: '1995-11-15',
    height: '211cm',
    weight: '112.5KG'
  }, {
    name: '克里斯-保罗',
    image: 'paul.png',
    birthday: '1985-05-06',
    height: '185cm',
    weight: '79.4KG'
  },
]
new Vue({
  el: '#app',
  data: function () {
    return {
      players,
      key: 'fipFfVsZsTda94hJNKJfLoaqyqMZFFimwLt'
    }
  },
  methods: {
    getToken(player) {
      let key = CryptoJS.enc.Utf8.parse(this.key)
      const {name, birthday, height, weight} = player
      let base64Name = CryptoJS.enc.Base64.stringify(CryptoJS.enc.Utf8.parse(name))
      let encrypted = CryptoJS.DES.encrypt(`${base64Name}${birthday}${height}${weight}`, key, {
        mode: CryptoJS.mode.ECB,
        padding: CryptoJS.pad.Pkcs7
      })
      return encrypted.toString()
    }
  }
})
"""

# 使用正则表达式匹配 players 数组
match = re.search(r'players = \[(.*?)\]', data, re.DOTALL)

if match:
    # 获取 players 数组字符串
    players_str = match.group(1)
    data = json.loads(match.group(1))
    print(data)

    print('------------------------')
    # 替换 JavaScript 对象语法为 Python 字典语法
    python_friendly_str = players_str.replace('const', '').replace(';', '').strip() \
        .replace('name:', "'name':") \
        .replace('image:', "'image':") \
        .replace('birthday:', "'birthday':") \
        .replace('height:', "'height':") \
        .replace('weight:', "'weight':")
    # 转换为 Python 字典列表
    players_dict = eval(f"[{python_friendly_str}]")

    # 转换为 JSON 格式字符串
    players_json = json.dumps(players_dict, ensure_ascii=False, indent=2)
    # for player in players_dict:
    #     print(player)
    # print(players_json)
else:
    print("No match found.")