import requests
from lxml import html

#search for user
def stats(usernameInput):

    url = 'https://r6.tracker.network/profile/pc/' + usernameInput
    page = requests.get(url)

    if page.status_code == 404:
        return "Profile not found"
        
    tree = html.fromstring(page.content)
   
    #get info from tree
    level = tree.xpath('//div[@class = "trn-defstat__value-stylized"]/text()')[1]
    rank = tree.xpath('//div[@class = "trn-defstat__value"]/text()')[66]
    mmr = tree.xpath('//div[@class = "trn-defstat__value"]/text()')[68]
    seasonalHighestMmr = tree.xpath('//div[@class = "trn-defstat__value"]/text()')[69]
    overallHighestMmr = tree.xpath("//div[.='Personal Record']/following::div[1]/text()")[0]
    overallkd = tree.xpath('//div[@class = "trn-defstat__value"]/text()')[7]
    seasonalkd = tree.xpath('//div[@class = "trn-defstat__value"]/text()')[54]
        

    output = ("Level: " + level.strip() + "\n" + "Rank: " + rank.strip() + "\n"  + "MMR: " + mmr.strip() + "\n" + "Seasonal highest MMR: " + seasonalHighestMmr.strip() + "\n" + "Overall highest MMR: " + overallHighestMmr.split()[0] + "\n"+ "Overall K/D: " + overallkd.strip() + "\n" + "Seasonal Ranked K/D: " + seasonalkd.strip())
    return output

def operators(operatorInput):
    
    url = 'https://r6.tracker.network/profile/pc/' + operatorInput + '/operators?seasonal=1'
    page = requests.get(url)

    if page.status_code == 404:
        return "Profile not found"
    
    tree2 = html.fromstring(page.content)
    
    #get info from tree
    attacker = tree2.xpath('//span[not(@class)]/text()')[5]
    attackerkd = tree2.xpath('//td[@class = "trn-text--right"]/text()')[3]
    defender = tree2.xpath("//th[.='Operator Stat']/following::span[1]/text()")[1]
    defenderkd = tree2.xpath("//th[.='Operator Stat']/following::td[5]/text()")[1]

    output2 = ("Seasonal Attacker: " + attacker + " "*4 + "K/D: " + attackerkd + "\n" + "Seasonal Defender: " + defender + " "*4 + "K/D: " + defenderkd)
    return output2
