'''
@author: Techcore-Paul
'''

import httplib  
import sys

(POS_ENG_NAME,
    POS_CHN_NAME,
    POS_OPEN_PRICE,
    POS_CLOSE_PRICE_Y,
    POS_MAX_PRICE,
    POS_MIN_PRICE,
    POS_CLOSE_PRICE,
    POS_UP_DOWN,
    POS_RATIO,
    POS_FIRST_BUY,
    POS_FIRST_SELL,
    POS_VOLUME,
    POS_TURNOVER,
    POS_PE_RATIO,
    POS_UNKNOWN,
    POS_52MAX,
    POS_52MIN,
    POS_DATE,
    POS_TIME) = range(19);
    
def get_date():
    conn.request("GET", "/list=hk00001")  
    r1 = conn.getresponse()  
    if r1.reason == 'OK': 
        dta = r1.read();
        dta = dta.split('"')[1].split(',')[-2];
        dta = dta.replace('/','');
        return dta;
        

def get_http_data(stkId):
    conn.request("GET", "/list=hk"+stkId)  
    r1 = conn.getresponse()  
    if r1.reason == 'OK': 
        return r1.read();
    else:
        return 0;

def get_specific_stock(stkId):
    return get_http_data(stkId);

def save_stock_data():
    allDta = '';
    for i in range(4000):
        stockId = '%d' %(i+1);
        stockId = '0'*(5 - len(stockId)) + stockId;
        stkDta = get_http_data(stockId);
        if stkDta == 0:
            continue;

        stkDta = stkDta.split('"')[1];
        if stkDta == '':
            continue;
        
        stkDta = stkDta.split(',');
        allDta += (stockId+'\n');
        allDta += stkDta[POS_OPEN_PRICE] + '\n';
        allDta += stkDta[POS_CLOSE_PRICE_Y] + '\n';
        allDta += stkDta[POS_MAX_PRICE] + '\n';
        allDta += stkDta[POS_MIN_PRICE] + '\n';
        allDta += stkDta[POS_UP_DOWN] + '\n';
        allDta += stkDta[POS_CLOSE_PRICE] + '\n';
        allDta += stkDta[POS_RATIO] + '\n';
        allDta += stkDta[POS_VOLUME] + '\n';
        allDta += stkDta[POS_TURNOVER] + '\n';
        allDta += stkDta[POS_52MAX] + '\n';
        allDta += stkDta[POS_52MIN] + '\n';

        if i % 10 == 0:
            print i;

    fName = get_date() + '.txt';
    fp = open(fName,'w');
    fp.write(allDta);
    fp.close();
        

if __name__ == '__main__':  
    
    conn = httplib.HTTPConnection("hq.sinajs.cn"); 
    for i in range(1,len(sys.argv)):
        print sys.argv[i];
        if sys.argv[i] == '-a':
            save_stock_data();
        else:
            print get_specific_stock(sys.argv[i]);

    conn.close();