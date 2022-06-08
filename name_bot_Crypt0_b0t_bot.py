
def start_prog (user_id,namebot,message_in,status,message_id,name_file_picture,telefon_nome):
    import iz_func
    import iz_game
    import iz_main
    import time
    import iz_telegram
    
    if message_in == '/start': 
        status = '' 
        iz_telegram.save_variable (user_id,namebot,'status','')
        

    if message_in == 'Отмена': 
        status = '' 
        #message_out,menu,answer = iz_telegram.send_message (user_id,namebot,"Отмена",'S',0) 
        iz_telegram.save_variable (user_id,namebot,'status','')

    
    
    if message_in == 'Ознакомлен': 
        message_out,menu,answer = iz_telegram.send_message (user_id,namebot,"После регистрации на бирже",'S',0) 
        
    
    if message_in == 'Подписаться на сигналы': 
        #iz_telegram.save_variable (user_id,namebot,'status','Ввести API KEY')        
        #message_out = 'Вы сделали подписку на сигналы крипты'
        message_out,menu = iz_telegram.get_message (user_id,'Вы сделали подписку на сигналы крипты',namebot)
        markup = ''
        #answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,0)         
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,0)  
        #message_out,menu,answer = iz_telegram.send_message (user_id,namebot,"После регистрации на бирже",'S',0)         
    
    
    if message_in == 'Передать ключи API': 
        iz_telegram.save_variable (user_id,namebot,'status','Введите ID Binance')
        #message_out = 'Укажите как получить ключ'
        markup  = ''
        #answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,message_id)    
        #answer = iz_telegram.bot_send (user_id,namebot,"Введите ID Binance",markup,0)    
        message_out,menu,answer = iz_telegram.send_message (user_id,namebot,"Введите ID Binance",'S',0) 

    if status == 'Введите ID Binance': 
        iz_telegram.save_variable (user_id,namebot,'ID Binance',message_in)
        iz_telegram.save_variable (user_id,namebot,'status','Ввести API key')
        #message_out = 'Введите secret key'
        markup  = ''
        #answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,0)    
        message_out,menu,answer = iz_telegram.send_message (user_id,namebot,"Ввести API key",'S',0) 

    if status == 'Ввести API key': 
        iz_telegram.save_variable (user_id,namebot,'API KEY',message_in)
        iz_telegram.save_variable (user_id,namebot,'status','Ввести SECRET KEY')
        #message_out = 'Введите secret key'
        markup  = ''
        message_out,menu,answer = iz_telegram.send_message (user_id,namebot,"Введите secret key",'S',0)
        #answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,0)    
        
    if status == 'Ввести SECRET KEY':     
        iz_telegram.save_variable (user_id,namebot,'SECRET KEY',message_in)
        iz_telegram.save_variable (user_id,namebot,'status','')
        #message_out = 'Спасибо за регистрацию'
        markup  = ''
        #answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,0)    
        message_out,menu,answer = iz_telegram.send_message (user_id,namebot,"Спасибо за регистрацию",'S',0)
        
        API_KEY      = iz_telegram.load_variable (user_id,namebot,'API KEY')
        SECRET_KEY   = iz_telegram.load_variable (user_id,namebot,'SECRET KEY')
        ID_Binance   = iz_telegram.load_variable (user_id,namebot,'ID Binance')
        
        db,cursor = iz_func.connect ()
        login     = ''  
        project   = ''  
        summ      = ''  
        system    = ''  
        wallet    = ''  
        komment   = ID_Binance  
        
        adress    = API_KEY
        telefon   = SECRET_KEY
        
        sql = "INSERT INTO bot_active_user (language,namebot,user_id,login,project,summ,`system`,wallet,komment,adress,telefon) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format ('ru',namebot,user_id,login,project,summ,system,wallet,komment,adress,telefon)
        cursor.execute(sql)
        db.commit() 
